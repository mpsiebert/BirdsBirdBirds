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
You are an animation assistant for a live art installation.
When given an image of a hand-drawn bird, generate a CSS keyframe animation for it flying across a projector screen.

Respond ONLY with a single valid JSON object in this exact format, with no extra text before or after:
{
  "id": "bird_XXXX",
  "image": "birds/bird_XXXX.png",
  "animation": {
    "css_keyframes": "@keyframes fly_XXXX { 0% { transform: translate(-20vw, 40vh) rotate(-5deg); } 50% { transform: translate(50vw, 20vh) rotate(3deg); } 100% { transform: translate(120vw, 35vh) rotate(-3deg); } }",
    "animation_name": "fly_XXXX",
    "duration": "18s",
    "timing_function": "ease-in-out"
  }
}

Rules:
- Replace all instances of "XXXX" with a unique 4-letter word (e.g. "swift", "wren", "dove").
- The animation must start at transform: translate(-20vw, ...) and end at translate(120vw, ...) so it crosses the full screen.
- Choose a vertical path and flight character (swooping, fluttering, gliding) that fits the bird's personality.
- The duration should be between 10s and 25s.
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

Clone the repo (download it to your computer) and install Pillow (this automatically removes the white background from your drawings!):
```bash
git clone https://github.com/mpsiebert/BirdsBirdBirds
cd BirdsBirdBirds
pip install Pillow
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
