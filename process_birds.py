#!/usr/bin/env python3
import os
import json
import re
import sys
import uuid
from io import BytesIO
from PIL import Image
import google.generativeai as genai

# Configuration
BIRDS_DIR = "birds"
MANIFEST_PATH = "manifest.json"
GEMINI_API_KEY = os.environ.get("GOOGLE_GEMINI_API_KEY")

def setup_gemini():
    if not GEMINI_API_KEY:
        print("Error: GOOGLE_GEMINI_API_KEY environment variable not set.")
        sys.exit(1)
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel('gemini-1.5-flash-latest')

def process_image(img_path):
    """Removes white background and crops the image."""
    try:
        img = Image.open(img_path).convert("RGBA")
        datas = img.getdata()
        
        new_data = []
        for item in datas:
            # Turn white or near-white into transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
                
        img.putdata(new_data)
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
        
        img.save(img_path, "PNG")
        print(f"Processed image: {img_path}")
        return True
    except Exception as e:
        print(f"Error processing image {img_path}: {e}")
        return False

def get_bird_data(model, img_path, bird_id):
    """Calls Gemini to moderate the image and generate flight animation CSS."""
    try:
        img = Image.open(img_path)
        prompt = f"""
        You are a content moderator and animator for a family-friendly event run by Major League Hacking (MLH).
        
        PART 1: MODERATION
        Review this image and determine if it complies with the MLH Code of Conduct.
        It must NOT contain: Nudity, sexual content, hate symbols, slurs, violence, drugs/alcohol, or harassment.
        It should also be a drawing of a bird (or a creative interpretation of one).

        PART 2: ANIMATION
        If approved, generate CSS keyframes for this bird flying across a screen.
        Ensure it starts off-screen left (-20vw) and ends off-screen right (120vw).

        Return ONLY a valid JSON object with the following structure:
        {{
            "status": "APPROVED" or "REJECTED",
            "reason": "Reason for rejection (if applicable)",
            "animation": {{
                "css_keyframes": "@keyframes fly_{bird_id} {{ ... }}",
                "animation_name": "fly_{bird_id}",
                "duration": "18s",
                "timing_function": "ease-in-out"
            }}
        }}
        """
        response = model.generate_content([prompt, img])
        text = response.text
        match = re.search(r'```(?:json)?(.*?)```', text, re.DOTALL)
        if match:
            text = match.group(1).strip()
        
        return json.loads(text)
    except Exception as e:
        print(f"Error getting bird data for {img_path}: {e}")
        return None

def main():
    if not os.path.exists(BIRDS_DIR):
        print(f"No {BIRDS_DIR} directory found.")
        return

    # Load manifest
    if os.path.exists(MANIFEST_PATH):
        try:
            with open(MANIFEST_PATH, "r") as f:
                manifest = json.load(f)
        except json.JSONDecodeError:
            manifest = []
    else:
        manifest = []

    existing_images = {b["image"] for b in manifest}
    new_birds_added = False
    
    model = setup_gemini()

    # Scan for new images
    for filename in os.listdir(BIRDS_DIR):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")) and filename != ".gitkeep":
            img_path = os.path.join(BIRDS_DIR, filename)
            
            if img_path not in existing_images:
                print(f"New bird detected: {filename}")
                
                 # Check for metadata sidecar file
                meta_path = f"{img_path}.meta.json"
                bird_name = "Anonymous"
                origin = "GitHub"
                
                if os.path.exists(meta_path):
                    try:
                        with open(meta_path, "r") as f:
                            meta = json.load(f)
                            bird_name = meta.get("bird_name", "Anonymous")
                            origin = meta.get("origin", "GitHub")
                    except Exception as e:
                        print(f"Error reading metadata for {filename}: {e}")

                # 1. Process image
                if not process_image(img_path):
                    continue
                
                # 2. Get Moderation and Animation Data
                bird_id = f"bird_{uuid.uuid4().hex[:8]}"
                bird_data = get_bird_data(model, img_path, bird_id)
                
                if bird_data and bird_data.get("status") == "APPROVED":
                    # 3. Add to manifest
                    entry = {
                        "id": bird_id,
                        "image": img_path,
                        "bird_name": bird_name,
                        "origin": origin,
                        "animation": bird_data["animation"]
                    }
                    if not isinstance(manifest, list):
                        manifest = []
                    manifest.append(entry)
                    new_birds_added = True
                    print(f"✅ Approved and added: {bird_name}")
                    
                    # Cleanup metadata file
                    if os.path.exists(meta_path):
                        os.remove(meta_path)
                elif bird_data:
                    print(f"🚫 Rejected {filename}: {bird_data.get('reason', 'No reason provided')}")
                    # Even if rejected, we might want to cleanup the meta file
                    if os.path.exists(meta_path):
                        os.remove(meta_path)

    if new_birds_added:
        with open(MANIFEST_PATH, "w") as f:
            json.dump(manifest, f, indent=2)
        print("Updated manifest.json")
    else:
        print("No new birds found.")

if __name__ == "__main__":
    main()
