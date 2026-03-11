#!/usr/bin/env python3
import os
import sys
import subprocess
import webbrowser
import time
import json
import shutil
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("\033[95m" + "=" * 50)
    print("      🐦  BirdsBirdBirds CLI Guide  🐦")
    print("=" * 50 + "\033[0m\n")

def scan_downloads():
    """Scans the ~/Downloads folder for recent PNG files."""
    downloads_path = os.path.expanduser("~/Downloads")
    if not os.path.exists(downloads_path):
        return []
    
    now = time.time()
    recent_files = []
    
    try:
        for f in os.listdir(downloads_path):
            if f.lower().endswith('.png') and not f.startswith('.'):
                full_path = os.path.join(downloads_path, f)
                # Check if file was created/modified in the last 15 minutes
                if now - os.path.getmtime(full_path) < 900:
                    recent_files.append(f)
    except Exception as e:
        print(f"Error scanning Downloads: {e}")
        
    return recent_files

def step_one():
    clear_screen()
    print_header()
    print("\033[94mSTEP 1: Draw Your Bird 🎨\033[0m")
    print("-" * 30)
    print("Go to jspaint.app to create your masterpiece.")
    print("Draw anything you like - just make sure it's a bird!")
    print("\n[O] Open jspaint.app in browser")
    print("[N] Next Step (if already drawn)")
    print("[Q] Quit")
    
    choice = input("\n> ").lower()
    if choice == 'o':
        webbrowser.open("https://jspaint.app")
        print("\nOpening browser... Just click 'File > Save' in jspaint when you're done.")
        print("I'll automatically find it in your Downloads folder!")
        input("\nPress Enter to continue once you've saved your bird...")
        step_two()
    elif choice == 'n':
        step_two()
    elif choice == 'q':
        sys.exit()
    else:
        step_one()

def step_two():
    clear_screen()
    print_header()
    print("\033[94mSTEP 2: Save & Sync Your Bird 💾\033[0m")
    print("-" * 30)
    
    # Ensure birds directory exists
    if not os.path.exists("birds"):
        os.makedirs("birds")
        
    # Check Downloads folder
    print("Checking your Downloads folder for new drawings...")
    recent_downloads = scan_downloads()
    if recent_downloads:
        print(f"\n✨ I found {len(recent_downloads)} recent drawing(s) in your Downloads!")
        for f in recent_downloads:
            print(f"   - {f}")
        move_choice = input("\nMove them to the 'birds/' folder automatically? [Y/n] ").lower()
        if move_choice != 'n':
            for f in recent_downloads:
                src = os.path.expanduser(f"~/Downloads/{f}")
                dest = os.path.join("birds", f)
                # Avoid overwriting or conflicts
                if os.path.exists(dest):
                    dest = os.path.join("birds", f"{int(time.time())}_{f}")
                shutil.move(src, dest)
            print("✅ Moved to 'birds/' folder!")
            time.sleep(1)

    # Load manifest to see what's already live
    manifest_birds = set()
    if os.path.exists("manifest.json"):
        try:
            with open("manifest.json", "r") as f:
                manifest = json.load(f)
                manifest_birds = {b.get("image", "").replace("birds/", "") for b in manifest}
        except:
            pass

    print("\nChecking 'birds/' folder for new files...")
    all_files = [f for f in os.listdir("birds") if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) and not f.startswith('.')]
    
    # Only care about files NOT in the manifest
    files = [f for f in all_files if f not in manifest_birds]
    
    if files:
        print(f"\n✅ Found {len(files)} new bird(s): {', '.join(files)}")
        print("\n\033[94mWait! We need a little info first...\033[0m")
        
        # Collect metadata for each new file if not already collected
        for filename in files:
            meta_path = os.path.join("birds", f"{filename}.meta.json")
            if not os.path.exists(meta_path):
                print(f"\n--- Info for {filename} ---")
                name = input("✏️  What's your name? ").strip() or "Anonymous"
                origin = input("📍 Where are you flying in from? (e.g. London) ").strip() or "The Sky"
                
                with open(meta_path, "w") as f:
                    json.dump({"bird_name": name, "origin": origin}, f)
                print(f"✅ Metadata saved for {filename}")

        print("\n[P] Push to the sky! 🚀")
    else:
        print("\n❌ No new birds found yet.")
        print("[R] Refresh / Re-scan Downloads")
    
    print("[B] Back")
    print("[Q] Quit")
    
    choice = input("\n> ").lower()
    if choice == 'p':
        push_to_github()
    elif choice == 'r' or choice == '':
        step_two()
    elif choice == 'b':
        step_one()
    elif choice == 'q':
        sys.exit()
    else:
        step_two()

def push_to_github():
    clear_screen()
    print_header()
    print("\033[94mSTEP 3: Sending to the Sky 🚀\033[0m")
    print("-" * 30)
    print("I'll now run the Git commands to upload your bird.")
    
    try:
        print("\nAdding files...")
        subprocess.run(["git", "add", "."], check=True)
        
        print("Committing changes...")
        subprocess.run(["git", "commit", "-m", "New bird submission with metadata"], check=True)
        
        print("Pushing to GitHub...")
        subprocess.run(["git", "push"], check=True)
        
        print("\n\033[92m✨ SUCCESS! ✨\033[0m")
        print("Your bird is on its way to the big screen.")
        print("It should appear at https://mpsiebert.github.io/BirdsBirdBirds/ in ~1 minute.")
        input("\nPress Enter to finish...")
    except subprocess.CalledProcessError as e:
        print(f"\n\033[91mError during Git commands:\033[0m {e}")
        print("Make sure you have permissions and your remote is set up correctly.")
        input("\nPress Enter to return...")
        step_two()

if __name__ == "__main__":
    try:
        # Check if we are in a git repo
        if not os.path.exists(".git"):
            print("\033[91mError: You are not inside a Git repository.\033[0m")
            print("Please run this script from inside your cloned 'BirdsBirdBirds' folder.")
            sys.exit(1)
        step_one()
    except KeyboardInterrupt:
        print("\n\nExiting... Bye! 🐦")
        sys.exit()
