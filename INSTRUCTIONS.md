# 🐦 BirdsBirdBirds — Workshop Instructions

## What you'll do
Clone the repo → Draw a bird in jspaint.app → Push it to GitHub → Watch it fly on the big screen!

---

## Before You Start — Prerequisites ✅

Make sure you have these on your laptop:

- [ ] **A GitHub account** → sign up free at [github.com](https://github.com)
- [ ] **Git installed** → check by typing `git --version` in your terminal
  - Mac: comes pre-installed, or install via `xcode-select --install`
  - Windows: download from [git-scm.com](https://git-scm.com)
- [ ] **A GitHub Personal Access Token** → you'll need this to push code
  - Go to [github.com/settings/tokens](https://github.com/settings/tokens) → Generate new token (classic) → check `repo` → Generate → **copy and save it!**

> **First-time git setup** (only do this once, ever):
> ```
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

## Step 2 — Draw Your Bird 🎨

1. Go to **[jspaint.app](https://jspaint.app)** in your browser.
2. Draw a bird! Simple, complex, realistic, abstract — all birds welcome.
3. Go to **File > Save...** (or press `Ctrl+S`).
4. Save the file directly into the `birds/` folder inside the `BirdsBirdBirds` directory you just cloned.
   - Give your file a name like `my_bird.png`.

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
