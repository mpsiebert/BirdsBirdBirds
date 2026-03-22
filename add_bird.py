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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    print("\033[93m\"Please remove the background of this image, making it completely transparent.")
    print("Clean up the edges of the bird but keep the original hand-drawn style exactly as it is.")
    print("Output ONLY the clean transparent image.\"\033[0m\n")
    print("4. Download the cleaned-up transparent bird to this computer.")
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
- The animation must start at transform: translate(-20vw, ...) and end at translate(120vw, ...).
- Choose a flight character (swooping, fluttering, gliding) that fits the bird.
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

    bird_name = input("\n✏️   What's your name? ").strip() or "Anonymous"
    origin = input("📍  Where are you flying in from? (e.g. Boston, MA): ").strip() or "Parts Unknown"

    print("\n📋  Paste the JSON from AI Studio below.")
    print("    (Paste it, then press Enter twice to continue)\n")

    lines = []
    try:
        while True:
            line = input()
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)
    except EOFError:
        pass

    raw = "\n".join(lines).strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    try:
        entry = json.loads(raw)
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
        shutil.copy(img_path, dest_path)
        print(f"\n✅ Copied image to {dest_path}")
    except Exception as e:
        print(f"❌ Failed to copy image: {e}")
        sys.exit(1)

    # Update entry with image path directly in birds/ folder (web safe)
    web_path = dest_path.replace("\\", "/")
    entry["image"] = web_path
    entry["origin"] = origin
    entry["bird_name"] = bird_name

    manifest_path = "manifest.json"
    manifest = []
    if os.path.exists(manifest_path):
        with open(manifest_path, "r") as f:
            try:
                manifest = json.load(f)
            except json.JSONDecodeError:
                manifest = []
    
    # Remove existing bird with same id
    manifest = [existing for existing in manifest if existing.get("id") != entry.get("id")]
    manifest.append(entry)

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print("✅  Successfully added to manifest.json!")

    print("\n\033[94mSTEP 5: Send It Live\033[0m")
    print("-" * 30)
    
    print("Executing git commands to push your bird to the repo...")
    print("> git add .")
    os.system('git add .')
    
    commit_msg = f"Add {bird_name}'s bird 🐦"
    print(f'> git commit -m "{commit_msg}"')
    os.system(f'git commit -m "{commit_msg}"')
    
    print("> git push")
    push_result = os.system('git push')
    
    if push_result == 0:
        print("\n\033[92m✨ SUCCESS! ✨\033[0m")
        print("Your bird is now flying to the repo!")
        print("Watch the sky at: https://mpsiebert.github.io/BirdsBirdBirds/")
    else:
        print("\n\033[91m⚠️ Hmm, the push failed.\033[0m")
        print("You might need to manually push or check authentication.")

if __name__ == "__main__":
    if not os.path.exists(".git"):
         print("\033[91mError: You are not inside a Git repository.\033[0m")
         print("Please run this script from inside your cloned 'BirdsBirdBirds' folder.")
         sys.exit(1)
         
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting... Bye! 🐦")
        sys.exit()
