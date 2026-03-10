# 🐦 BirdsBirdBirds — Workshop Instructions

## What you'll do
Draw a bird → have AI animate it → push it to GitHub → watch it fly on the big screen!

---

## Step 1 — Draw Your Bird 🎨
1. Open **MS Paint** (or any drawing tool)
2. Draw a bird — any bird! Simple, complex, realistic, abstract — all birds welcome
3. Save it as a **PNG file** with a name like: `bird_yourname.png`

---

## Step 2 — Animate it with AI Studio 🤖
1. Go to: **https://aistudio.google.com**
2. Click **"New prompt"** → select **Gemini 1.5 Flash**
3. Paste in the following **System Instructions** (the text in the box below):

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

4. Upload your bird image using the **📎 attachment button**
5. Click **Run** and wait a moment
6. **Copy all the JSON** that Gemini returns

---

## Step 3 — Set Up GitHub 💻

> **If this is your first time with git**, run these one-time setup commands:
> ```bash
> git config --global user.name "Your Name"
> git config --global user.email "you@email.com"
> ```

Clone the repo (download it to your computer) and install dependencies:
```bash
git clone https://github.com/mpsiebert/BirdsBirdBirds
cd BirdsBirdBirds
pip install Pillow google-generativeai
```

Set up your Gemini API key (ask a workshop mentor for the key!):
```bash
export GOOGLE_GEMINI_API_KEY="your_key_here"
```

---

## Step 4 — Add Your Bird 🐦

1. Copy your bird image into the `birds/` folder:
```bash
# Mac/Linux:
cp ~/Desktop/bird_yourname.png birds/

# Windows:
copy C:\Users\YourName\Desktop\bird_yourname.png birds\
```

2. Run the helper script and paste your AI Studio JSON when prompted:
```bash
python3 add_bird.py birds/bird_yourname.png
```

3. Paste your JSON, then type **END** on a new line and press **Enter**

---

## Step 5 — Push to GitHub 🚀

```bash
git add .
git commit -m "Add my bird"
git push
```

> You may be asked for your GitHub username and a **Personal Access Token** (not your password).
> Get one at: https://github.com/settings/tokens → Classic token → check `repo`

---

## Step 6 — Watch the Sky! 👀

Look at the projector screen at:
**https://mpsiebert.github.io/BirdsBirdBirds/**

Your bird should appear within **~30 seconds**! 🎉

---

*made with ♥ by the MLH AI Roadshow Team*
