# 🐦 BirdsBirdBirds — Workshop Instructions

## What you'll do
Draw a bird → have AI animate it → push it to GitHub → watch it fly on the big screen!

---

## Before You Start — Prerequisites ✅

Make sure you have these on your laptop:

- [ ] **A GitHub account** → sign up free at [github.com](https://github.com)
- [ ] **Git installed** → check by typing `git --version` in your terminal
  - Mac: comes pre-installed, or install via `xcode-select --install`
  - Windows: download from [git-scm.com](https://git-scm.com)
- [ ] **Python 3 installed** → check by typing `python3 --version` in your terminal
  - Mac: comes pre-installed
  - Windows: download from [python.org](https://python.org)
- [ ] **A GitHub Personal Access Token** → you'll need this to push code
  - Go to [github.com/settings/tokens](https://github.com/settings/tokens) → Generate new token (classic) → check `repo` → Generate → **copy and save it!**

> **First-time git setup** (only do this once, ever):
> ```
> git config --global user.name "Your Name"
> git config --global user.email "you@email.com"
> ```

---

## Step 1 — Draw Your Bird 🎨
1. Open **MS Paint** (or any drawing tool on your laptop)
2. Draw a bird — any bird! Simple, complex, realistic, abstract — all birds welcome
3. Save it as a **PNG file** somewhere you can find it (e.g. your Desktop)

---

## Step 2 — Animate it with AI Studio 🤖
1. Go to: **https://aistudio.google.com** (sign in with your Google account)
2. Start a **new prompt** → select **Gemini 1.5 Flash**
3. Click the **📎 attachment button** and upload your bird image
4. Paste the following prompt and click **Run**:

```
I drew this bird. Generate a dramatic, unique CSS keyframe animation for it flying across a wide projector screen.

Return ONLY a valid JSON object in this exact format, no extra text:
{
  "id": "bird_XXXX",
  "image": "birds/bird_XXXX.png",
  "animation": {
    "css_keyframes": "YOUR KEYFRAMES HERE",
    "animation_name": "fly_XXXX",
    "duration": "18s",
    "timing_function": "ease-in-out"
  }
}

Rules for XXXX: Replace all instances with a unique 4-letter word matching the bird's vibe.

Rules for the keyframes:
- Use at LEAST 6 waypoints (0%, 15%, 35%, 55%, 75%, 100%) to create complex, organic flight
- MUST start at translate(-20vw, ...) and end at translate(120vw, ...) to cross the full screen
- Vertical position should vary dramatically — include swoops, dives, and climbs between 10vh and 80vh
- Add rotation changes (-15deg to 15deg) to simulate banking turns
- Add subtle scale changes (0.85 to 1.15) to create depth — bird appears closer or farther
- Pick ONE of these flight personalities based on the bird's appearance:
  * Majestic glider: slow, wide swoops with gentle banking
  * Frantic flutterer: rapid up-down zigzags, lots of rotation
  * Dive bomber: climbs high then dramatically dives low, repeat
  * Lazy drifter: mostly level with occasional gentle bobs
  * Show-off: loops, dramatic climbs, sudden direction changes
- Duration between 14s and 28s (bigger/heavier birds = slower)
- Return ONLY the JSON. No markdown, no explanation.
```

5. **Copy the entire JSON** that Gemini gives you — you'll paste it later

---

## Step 3 — Clone the Repo 💻

Open a **terminal** on your laptop:
- **Mac:** open the Terminal app (search "Terminal" in Spotlight)
- **Windows:** open Git Bash or Command Prompt

Run this to download the project:

```
git clone https://github.com/mpsiebert/BirdsBirdBirds
```

Then move into the project folder:

```
cd BirdsBirdBirds
```

> ⚠️ **IMPORTANT:** You must be inside the `BirdsBirdBirds` folder for ALL the commands below to work! If you get "file not found" errors, you're probably in the wrong folder.

---

## Step 4 — Copy Your Bird Image 🖼️

Copy your bird image into the `birds/` folder.

**Mac:**
```
cp ~/Desktop/mybird.png birds/
```

**Windows:**
```
copy C:\Users\YourName\Desktop\mybird.png birds\
```

> Replace `mybird.png` with whatever you named your file.

---

## Step 5 — Run the Helper Script 🐦

```
python3 add_bird.py birds/mybird.png
```

> **Windows users:** if `python3` doesn't work, try `python` instead.

It will ask you three things:
1. **What's your name?** → type your name
2. **Where are you flying in from?** → type your city (e.g. `Kansas City`)
3. **Paste the JSON** → paste the output from AI Studio, then type **END** on a new line and press **Enter**

---

## Step 6 — Push to GitHub 🚀

Run these three commands one at a time:

```
git add .
```

```
git commit -m "Add my bird"
```

```
git push
```

> When asked for your password, use your **Personal Access Token** (from the prerequisites), NOT your GitHub password.

---

## Step 7 — Watch the Sky! 👀

Look at the projector screen at:
**https://mpsiebert.github.io/BirdsBirdBirds/**

Your bird should appear within **~30 seconds**! 🎉

---

## Troubleshooting 🔧

| Problem | Solution |
|---|---|
| `file not found` or `no such directory` | Make sure you ran `cd BirdsBirdBirds` first |
| `python3: command not found` | Try `python` instead (Windows) |
| `git push` rejected | Run `git pull` first, then try pushing again |
| `authentication failed` | Use your Personal Access Token, not your password |

---

*made with ♥ by the MLH AI Roadshow Team*
