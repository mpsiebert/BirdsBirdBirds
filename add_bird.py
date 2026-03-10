#!/usr/bin/env python3
"""
add_bird.py  —  BirdsBirdBirds workshop helper
================================================
Usage:
    python3 add_bird.py birds/your_bird.png

This script will:
  1. Ask for your bird's name and where it's flying in from
  2. Ask you to paste the JSON from AI Studio
  3. Validate it looks correct
  4. Add your bird to manifest.json
  5. Print the git commands to send it live

Then you just run:
    git add .
    git commit -m "Add my bird 🐦"
    git push
"""

import sys
import json
import os
import shutil

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

GEMINI_API_KEY = os.environ.get("GOOGLE_GEMINI_API_KEY", "")

def process_image(img_path):
    if not HAS_PIL:
        print("\n⚠️   Tip: Install Pillow ('pip install Pillow') to automatically remove the white background from your MS Paint bird!")
        return

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
        print("\n✨   Automatically removed white background and cropped the image!")
    except Exception as e:
        print(f"\n⚠️   Could not process image background: {e}")

def moderate_image(img_path):
    """Use Gemini to check the image is appropriate per MLH Code of Conduct."""
    if not HAS_GENAI or not GEMINI_API_KEY:
        print("\n⚠️   Content moderation skipped (google-generativeai not installed or API key not set).")
        return True

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')

        img = Image.open(img_path) if HAS_PIL else None
        if img is None:
            return True

        prompt = """You are a content moderator for a family-friendly event run by Major League Hacking (MLH).

Review this image and determine:
1. Is this a drawing of a bird (or a reasonable creative interpretation of one)?
2. Does this image comply with the MLH Code of Conduct? It must NOT contain:
   - Nudity, sexual content, or suggestive imagery
   - Hate symbols, slurs, or discriminatory content
   - Violent or gory imagery
   - Harassment, bullying, or threatening content
   - Drug or alcohol references
   - Any content that would make attendees feel unsafe or unwelcome

Respond with ONLY one word: APPROVED or REJECTED
If rejected, add a brief reason after a pipe character, like: REJECTED|reason here"""

        response = model.generate_content([prompt, img])
        result = response.text.strip()

        if result.startswith("APPROVED"):
            print("\n✅  Content check passed!")
            return True
        else:
            reason = result.split("|", 1)[1].strip() if "|" in result else "Image did not pass content review."
            print(f"\n🚫  Your image was not approved: {reason}")
            print("    Please make sure your drawing is a bird and is appropriate for all attendees.")
            print("    See the MLH Code of Conduct: https://mlh.io/code-of-conduct")
            return False
    except Exception as e:
        print(f"\n⚠️   Content moderation error: {e}")
        # Fail open for workshop — don't block on API errors
        return True

def main():
    print()
    print("🐦  BirdsBirdBirds – Bird Submission Helper")
    print("=" * 45)

    # ── 1. Get the image path ──────────────────────────────────
    if len(sys.argv) < 2:
        print("\n❌  Please provide the path to your bird image.")
        print("    Usage: python3 add_bird.py birds/your_bird.png")
        sys.exit(1)

    image_path = sys.argv[1]

    # If they gave an absolute or desktop path, copy it into birds/
    if not image_path.startswith("birds/"):
        filename  = os.path.basename(image_path)
        dest_path = os.path.join("birds", filename)
        if not os.path.exists(image_path):
            print(f"\n❌  Could not find image: {image_path}")
            sys.exit(1)
        os.makedirs("birds", exist_ok=True)
        shutil.copy2(image_path, dest_path)
        print(f"\n✅  Copied {filename} → {dest_path}")
        image_path = dest_path
    else:
        if not os.path.exists(image_path):
            print(f"\n❌  Could not find image: {image_path}")
            print("    Make sure it's inside the birds/ folder.")
            sys.exit(1)

    # Process the background to make white transparent
    process_image(image_path)

    # Content moderation check
    if not moderate_image(image_path):
        sys.exit(1)

    # ── 2. Ask for name & origin ───────────────────────────────
    print()
    bird_name = input("✏️   What's your name? ").strip()
    if not bird_name:
        bird_name = "Anonymous"
    origin    = input("📍  Where are you flying in from? (e.g. Boston, MA): ").strip()
    if not origin:
        origin = "Parts Unknown"

    # ── 3. Get JSON from AI Studio ─────────────────────────────
    print()
    print("📋  Paste the JSON from AI Studio below.")
    print("    When done, type END on a new line and press Enter.\n")

    lines = []
    try:
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
    except EOFError:
        pass

    raw = "\n".join(lines).strip()

    # Strip markdown code fences if AI Studio added them
    if "```" in raw:
        raw = raw.split("```")[1]
        raw = raw.lstrip("json").strip()

    # ── 4. Parse & validate ────────────────────────────────────
    try:
        entry = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"\n❌  That doesn't look like valid JSON: {e}")
        print("    Make sure you copied the full block from AI Studio.")
        sys.exit(1)

    required_keys = {"id", "animation"}
    anim_keys     = {"css_keyframes", "animation_name", "duration", "timing_function"}

    if not required_keys.issubset(entry.keys()):
        print(f"\n❌  JSON is missing required keys: {required_keys - set(entry.keys())}")
        sys.exit(1)

    if not anim_keys.issubset(entry["animation"].keys()):
        print(f"\n❌  animation object is missing keys: {anim_keys - set(entry['animation'].keys())}")
        sys.exit(1)

    # Overwrite/set fields
    entry["image"]  = image_path
    entry["origin"] = origin

    # Use attendee-provided name over AI suggestion, or fall back to AI's
    if bird_name:
        entry["bird_name"] = bird_name
    elif "bird_name" not in entry:
        entry["bird_name"] = "Unknown Bird"

    # ── 5. Load & update manifest.json ────────────────────────
    manifest_path = "manifest.json"
    if os.path.exists(manifest_path):
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
    else:
        manifest = []

    # Avoid duplicates
    existing_ids = {b["id"] for b in manifest}
    if entry["id"] in existing_ids:
        print(f"\n⚠️   A bird with id '{entry['id']}' already exists.")
        print("    Try changing the id in your JSON to something unique.")
        sys.exit(1)

    manifest.append(entry)

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    # ── 6. Success! ────────────────────────────────────────────
    print()
    print("=" * 45)
    print(f"✅  '{entry['bird_name']}' from {origin} is ready to fly!")
    print()
    print("Run these commands to send your bird to the sky:")
    print()
    print("    git add .")
    print('    git commit -m "Add my bird"')
    print("    git push")
    print()
    print("Then watch the projector screen... 👀🐦")
    print()

if __name__ == "__main__":
    main()
