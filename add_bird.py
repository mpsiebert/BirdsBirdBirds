#!/usr/bin/env python3
import os
import sys
import subprocess
import webbrowser
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("\033[95m" + "=" * 50)
    print("      🐦  BirdsBirdBirds CLI Guide  🐦")
    print("=" * 50 + "\033[0m\n")

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
        print("\nOpening browser... Press Enter when you're done drawing.")
        input()
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
    print("\033[94mSTEP 2: Save Your Bird 💾\033[0m")
    print("-" * 30)
    print("1. In jspaint.app, go to File > Save.")
    print("2. Save the PNG directly into the 'birds/' folder in this repo.")
    print("3. Give it a unique name (e.g., 'yourname_bird.png').")
    
    print("\nChecking 'birds/' folder for new files...")
    files = [f for f in os.listdir("birds") if f != ".gitkeep"]
    if files:
        print(f"\n✅ Found {len(files)} bird(s): {', '.join(files)}")
        print("\n[P] Push to the sky! 🚀")
    else:
        print("\n❌ No birds found in 'birds/' folder yet.")
        print("[R] Refresh / Re-check")
    
    print("[B] Back")
    print("[Q] Quit")
    
    choice = input("\n> ").lower()
    if choice == 'p':
        push_to_github()
    elif choice == 'r':
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
        subprocess.run(["git", "commit", "-m", "Manual bird submission via CLI"], check=True)
        
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
        step_one()
    except KeyboardInterrupt:
        print("\n\nExiting... Bye! 🐦")
        sys.exit()
