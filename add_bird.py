#!/usr/bin/env python3
"""
add_bird.py — BirdsBirdBirds workshop helper
================================================
Usage:
    python3 add_bird.py

This script walks you through the entire workshop activity:
  1. Drawing a bird in jspaint.app
  2. Cleaning it up with Google AI Studio
  3. Generating an animation in AI Studio
  4. Adding the bird to this repo
  5. Pushing it with a dummy GitHub account
"""

import sys
import os
import json
import shutil
import subprocess
import urllib.request
import urllib.parse

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_clean(text):
    if not text: return True
    try:
        url = "https://www.purgomalum.com/service/containsprofanity?text=" + urllib.parse.quote(text)
        with urllib.request.urlopen(url, timeout=3) as resp:
            return resp.read().decode('utf-8').strip() == 'false'
    except:
        return True # Fallback if API is down

def print_header():
    print("\033[95m" + "=" * 50)
    print("      🐦  BirdsBirdBirds CLI Guide  🐦")
    print("=" * 50 + "\033[0m\n")

def pause():
    input("\n\033[90mPress ENTER when you're ready to continue...\033[0m")
    clear_screen()
    print_header()

def main():
    clear_screen()
    print_header()

    print("\033[94mSTEP 1: Draw Your Bird\033[0m")
    print("-" * 30)
    print("1. Open your browser and go to: \033[96mhttps://jspaint.app\033[0m")
    print("2. Draw a bird — any bird! Simple, complex, realistic, abstract — all birds welcome.")
    print("3. Download/save that bird to this computer.")
    pause()

    print("\033[94mSTEP 2: Clean Up Your Bird\033[0m")
    print("-" * 30)
    print("1. Go to Google AI Studio (\033[96mhttps://aistudio.google.com\033[0m)")
    print("2. Upload the bird you just downloaded.")
    print("3. Use this prompt to clean it up:\n")
    print("\033[93m\"Please clean up the lines of this bird drawing, keeping the original hand-drawn style exactly as it is.")
    print("OUTPUT THE IMAGE ON A SOLID PURE WHITE BACKGROUND.")
    print("DO NOT attempt to make the background transparent, and DO NOT add a fake checkered background!\"\033[0m\n")
    print("4. Download the cleaned-up bird to this computer.")
    pause()

    print("\033[94mSTEP 3: Animate Your Bird\033[0m")
    print("-" * 30)
    print("1. In AI Studio, start a New Prompt.")
    print("2. Upload your CLEANED-UP bird image.")
    print("3. Paste the prompt below. Feel free to tweak the transform or duration to \"hack\" your bird!\n")
    
    prompt = """\033[93mYou are an animation assistant for a live art installation.
When given an image of a hand-drawn bird, generate a CSS keyframe animation for it flying across a projector screen.

Respond ONLY with a single valid JSON object in this exact format, with no extra text before or after:
{
  "id": "bird_XXXX",
  "animation": {
    "css_keyframes": "@keyframes fly_XXXX { 0% { transform: translate(-20vw, 40vh) rotate(-5deg); } 50% { transform: translate(50vw, 20vh) rotate(3deg); } 100% { transform: translate(120vw, 35vh) rotate(-3deg); } }",
    "animation_name": "fly_XXXX",
    "duration": "18s",
    "timing_function": "ease-in-out"
  }
}

Rules:
- Replace all instances of "XXXX" with a unique 4-letter word.
- SAFETY POLICY: If the uploaded drawing contains offensive, inappropriate, or NSFW content, you must output EXACTLY: {"error": "inappropriate"} and nothing else.
- DO NOT copy the example keyframes! Invent a UNIQUE, highly randomized flight path for this specific bird.
- The animation must start at `transform: translate(-20vw, Y)` and end at `translate(120vw, Y)` where Y is a random height between 10vh and 90vh.
- Create at least 5 different keyframe percentages (e.g. 0%, 20%, 50%, 80%, 100%) with varying heights and rotation angles.
- Choose a flight character (swooping, fluttering, gliding, bouncing) that fits the bird.
- Return ONLY the JSON. No markdown, no explanation.\033[0m"""
    
    print(prompt)
    print("\n4. Click Run, and COPY the JSON it generates.")
    pause()

    print("\033[94mSTEP 4: Add Your Bird to the Flock\033[0m")
    print("-" * 30)
    
    while True:
        img_path = input("📂 Drag and drop your downloaded CLEANED bird image here (or type the path): ").strip()
        # Remove quotes if dragged in macOS/Linux terminal
        if img_path.startswith("'") and img_path.endswith("'"):
            img_path = img_path[1:-1]
        elif img_path.startswith('"') and img_path.endswith('"'):
            img_path = img_path[1:-1]
            
        # Also remove trailing spaces from drag-and-drop
        img_path = img_path.strip()
            
        if os.path.exists(img_path) and os.path.isfile(img_path):
            break
        print(f"❌ Could not find file: {img_path}. Please check the path and try again.")

    while True:
        bird_name = input("\n✏️   What's your name? ").strip() or "Anonymous"
        origin = input("📍  Where are you flying in from? (e.g. Boston, MA): ").strip() or "Parts Unknown"
        print("Checking text for inappropriate content...")
        if is_clean(bird_name) and is_clean(origin):
            break
        print("❌ Please keep it family-friendly! Let's try typing that again.")

    print("\n📋  Paste the JSON from AI Studio below.")
    print("    (The script will automatically continue once it receives valid JSON)\n")

    lines =[]
    raw = ""
    try:
        while True:
            line = input()
            lines.append(line)
            
            raw_text = "\n".join(lines).strip()
            
            # Clean up markdown fences for testing
            if raw_text.startswith("```"):
                parts = raw_text.split("```")
                if len(parts) >= 2:
                    raw_text = parts[1]
                if raw_text.startswith("json"):
                    raw_text = raw_text[4:]
                raw_text = raw_text.strip()
                
            # If it looks like a complete object, try parsing
            if raw_text.startswith("{") and raw_text.endswith("}"):
                try:
                    json.loads(raw_text)
                    # Valid JSON detected, we can break automatically!
                    raw = raw_text
                    break
                except json.JSONDecodeError:
                    pass
                    
            # Fallback: break on 3 consecutive empty lines if they get stuck
            if len(lines) >= 3 and lines[-1] == "" and lines[-2] == "" and lines[-3] == "":
                raw = raw_text
                break
    except EOFError:
        pass

    try:
        entry = json.loads(raw)
        if "error" in entry:
            print("\n❌ AI Safety Filter: Your bird drawing was flagged as inappropriate.")
            print("    Please redraw a family-friendly bird and try again!")
            sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"\n❌  That doesn't look like valid JSON: {e}")
        print("    Please run the script again and make sure you copied the full block from AI Studio.")
        sys.exit(1)

    # Move image to birds/ directory
    os.makedirs("birds", exist_ok=True)
    file_ext = os.path.splitext(img_path)[1]
    if not file_ext:
        file_ext = ".png"
        
    safe_name = "".join(c for c in bird_name if c.isalnum() or c == '_').lower()
    if not safe_name: safe_name = "bird"
    
    dest_img_name = f"{safe_name}_{entry.get('id', 'new')}{file_ext}"
    dest_path = os.path.join("birds", dest_img_name)
    
    try:
        try:
            from PIL import Image
            img = Image.open(img_path).convert("RGBA")
            datas = img.getdata()
            
            newData =[]
            for item in datas:
                # If the pixel is very close to white, make it completely transparent
                if item[0] > 235 and item[1] > 235 and item[2] > 235:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
                    
            img.putdata(newData)
            img.save(dest_path, "PNG")
            print(f"\n✅ Processed image (removed background) and saved to {dest_path}")
        except ImportError:
            print("\n\033[93m⚠️  Python 'Pillow' library not installed! (Install via: pip install Pillow)\033[0m")
            print("   Falling back to standard copy (no automatic background removal).")
            shutil.copy(img_path, dest_path)
            print(f"✅ Copied raw image to {dest_path}")
    except Exception as e:
        print(f"❌ Failed to save image: {e}")
        sys.exit(1)

    # Update entry with image path directly in birds/ folder (web safe)
    web_path = dest_path.replace("\\", "/")
    entry["image"] = web_path
    entry["origin"] = origin
    entry["bird_name"] = bird_name

    print("\n\033[94mSTEP 5: Send It Live\033[0m")
    print("-" * 30)
    print("Executing git commands to push your bird to the repo...")
    
    import time
    import random
    
    manifest_path = "manifest.json"
    max_retries = 5
    
    for attempt in range(max_retries):
        # Always pull latest to avoid manifest.json conflicts
        print(f"> git pull --rebase (Attempt {attempt+1}/{max_retries})")
        
        # If manifest.json was modified on a previous failed loop, reset it so we can pull cleanly
        subprocess.run(['git', 'checkout', '--', manifest_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Print the pull command output so we can see network or auth errors
        print("> git pull origin main --rebase")
        pull_result = subprocess.run(['git', 'pull', 'origin', 'main', '--rebase']).returncode
        if pull_result != 0:
            print("\033[93m⚠️ Warning: Pull failed. Trying to proceed anyway...\033[0m")
        
        # Now read the fresh manifest
        manifest = []
        if os.path.exists(manifest_path):
            with open(manifest_path, "r") as f:
                try:
                    manifest = json.load(f)
                except json.JSONDecodeError:
                    manifest = []
        
        # Remove existing bird with same id
        manifest =[existing for existing in manifest if existing.get("id") != entry.get("id")]
        manifest.append(entry)

        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)
            
        print("✅  Successfully updated manifest.json!")
        
        print("> git add .")
        subprocess.run(['git', 'add', '.'])

        commit_msg = f"Add {bird_name}'s bird 🐦"
        print(f'> git commit -m "{commit_msg}"')
        subprocess.run(['git', 'commit', '-m', commit_msg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print("> git push")
        push_result = subprocess.run(['git', 'push']).returncode
        
        if push_result == 0:
            print("\n\033[92m✨ SUCCESS! ✨\033[0m")
            print("Your bird is now flying to the repo!")
            print("Watch the sky at: https://mpsiebert.github.io/BirdsBirdBirds/")
            break
        else:
            print("\n\033[93m⚠️ Push failed (someone else pushed an update, or authentication failed).\033[0m")
            print("Undoing commit and retrying...")
            # Use a mixed reset (not --hard) so we don't accidentally delete the bird image file!
            subprocess.run(['git', 'reset', 'HEAD~1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(random.uniform(1, 3))
    else:
        print("\n\033[91m⚠️ Hmm, the push failed after multiple retries.\033[0m")
        print("You might need to manually push or check authentication.")

if __name__ == "__main__":
    if not os.path.exists(".git"):
         print("\033[91mError: You are not inside a Git repository.\033
