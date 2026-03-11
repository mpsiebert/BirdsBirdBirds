# 🐦 BirdsBirdBirds

An interactive art installation for the **MLH AI Roadshow** — draw a bird, save it to the `birds/` folder, push it to GitHub, and watch it fly across the big screen!

**Live Display:** [https://mpsiebert.github.io/BirdsBirdBirds/](https://mpsiebert.github.io/BirdsBirdBirds/)

---

## How it works
1. Clone this repository to your laptop.
2. Run `python3 add_bird.py` in your terminal — it will guide you through the whole process!
3. Draw your bird in jspaint, save it to `birds/`, and the tool will help you push it to the sky.

## Workshop Instructions
See **[INSTRUCTIONS.md](INSTRUCTIONS.md)** for the full step-by-step guide.

## Repo structure
```
BirdsBirdBirds/
├── index.html        ← Live projector display (GitHub Pages)
├── manifest.json     ← Queue of all submitted birds + animation data
├── process_birds.py  ← Automation script (runs via GitHub Actions)
├── INSTRUCTIONS.md   ← Step-by-step attendee guide
└── birds/            ← Submitted bird images
```

*made with ♥ by the MLH AI Roadshow Team*
