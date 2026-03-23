# 🐦 BirdsBirdBirds — Workshop Instructions

## What you'll do
Clone the repo → Draw a bird in jspaint.app → Push it to GitHub → Watch it fly on the big screen!

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
- DO NOT copy the example keyframes! Invent a UNIQUE, highly randomized flight path for this specific bird.
- The animation must start at `transform: translate(-20vw, Y)` and end at `translate(120vw, Y)` where Y is a random height between 10vh and 90vh.
- Create at least 5 different keyframe percentages (e.g. 0%, 20%, 50%, 80%, 100%) with varying heights and rotation angles.
- Choose a flight character (swooping, fluttering, gliding, bouncing) that fits the bird.
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

---

## Step 1 — Clone the Repo 💻

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

> ⚠️ **IMPORTANT:** You must be inside the `BirdsBirdBirds` folder for all subsequent steps!

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

3. Paste your JSON, then press **Enter twice**

---

## Step 3 — Push to GitHub 🚀

Back in your **terminal**, run these three commands one at a time:

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

## Step 4 — Watch the Sky! 👀

Look at the projector screen at:
**https://mpsiebert.github.io/BirdsBirdBirds/**

Our GitHub Action will automatically pick up your image, remove the background, and have AI generate a unique flight animation for it. It should appear within **~1 minute**! 🎉

---

## Troubleshooting 🔧

| Problem | Solution |
|---|---|
| `file not found` or `no such directory` | Make sure you ran `cd BirdsBirdBirds` first |
| `git push` rejected | Run `git pull` first, then try pushing again |
| `authentication failed` | Use your Personal Access Token, not your password |

---

*made with ♥ by the MLH AI Roadshow Team*
