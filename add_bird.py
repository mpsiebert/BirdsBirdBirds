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
    print('    git commit -m "Add my bird 🐦"')
    print("    git push")
    print()
    print("Then watch the projector screen... 👀🐦")
    print()

if __name__ == "__main__":
    main()
