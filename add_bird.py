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
import os
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("\033[95m" + "=" * 50)
    print("      🐦  BirdsBirdBirds CLI Guide  🐦")
    print("=" * 50 + "\033[0m\n")

def main():
    if not os.path.exists(".git"):
        print("\033[91mError: You are not inside a Git repository.\033[0m")
        print("Please run this script from inside your cloned 'BirdsBirdBirds' folder.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python3 add_bird.py birds/your_bird.png")
        sys.exit(1)
        
    image_path = sys.argv[1]
    
    if not os.path.exists(image_path):
        print(f"\n❌  Could not find image: {image_path}")
        print("    Make sure it's inside the birds/ folder.")
        sys.exit(1)

    clear_screen()
    print_header()

    # 1. Ask for name & origin
    print("\033[94mSTEP 1: Tell us about your bird\033[0m")
    print("-" * 30)
    bird_name = input("✏️   What's your name? ").strip()
    if not bird_name:
        bird_name = "Anonymous"
    origin = input("📍  Where are you flying in from? (e.g. Boston, MA): ").strip()
    if not origin:
        origin = "Parts Unknown"

    # 2. Get JSON from AI Studio
    print()
    print("\033[94mSTEP 2: Add AI Studio Animation\033[0m")
    print("-" * 30)
    print("📋  Paste the JSON from AI Studio below.")
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

    # Strip markdown code fences if AI Studio added them
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    # 3. Parse & validate
    try:
        entry = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"\n❌  That doesn't look like valid JSON: {e}")
        print("    Make sure you copied the full block from AI Studio.")
        sys.exit(1)

    required_keys = {"id", "animation"}
    anim_keys = {"css_keyframes", "animation_name", "duration", "timing_function"}

    if not required_keys.issubset(entry.keys()):
        print(f"\n❌  JSON is missing required keys: {required_keys - set(entry.keys())}")
        sys.exit(1)

    if not anim_keys.issubset(entry["animation"].keys()):
        print(f"\n❌  animation object is missing keys: {anim_keys - set(entry['animation'].keys())}")
        sys.exit(1)

    # Overwrite/set fields
    entry["image"] = image_path
    entry["origin"] = origin

    if bird_name:
        entry["bird_name"] = bird_name
    elif "bird_name" not in entry:
        entry["bird_name"] = "Unknown Bird"

    # 4. Load & update manifest.json
    print("\n\033[94mSTEP 3: Saving to manifest\033[0m")
    print("-" * 30)
    manifest_path = "manifest.json"
    manifest = []
    if os.path.exists(manifest_path):
        with open(manifest_path, "r") as f:
            try:
                manifest = json.load(f)
            except json.JSONDecodeError:
                manifest = []
    
    # Check if id already exists
    for existing in manifest:
        if existing.get("id") == entry["id"]:
            print(f"⚠️  Bird with id '{entry['id']}' already exists in manifest!")
            print("   We will replace it.")
            manifest.remove(existing)
            break

    manifest.append(entry)

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"✅  Successfully added {bird_name}'s bird to manifest.json!")

    # 5. Print the git commands to send it live
    print("\n\033[92m✨ SUCCESS! ✨\033[0m")
    print("=" * 50)
    print("🚀  Ready for takeoff! Run these commands:")
    print("=" * 50)
    print("git add .")
    print(f'git commit -m "Add my bird 🐦"')
    print("git push")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting... Bye! 🐦")
        sys.exit()
