# 🐦 BirdsBirdBirds

An interactive art installation for the **MLH AI Roadshow** — draw a bird, animate it with AI, push it to GitHub, and watch it fly across the big screen!

**Live Display:** https://mpsiebert.github.io/BirdsBirdBirds/

---

## How it works
1. Attendees draw a bird in MS Paint
2. Use [AI Studio](https://aistudio.google.com) + a provided prompt to generate a CSS flight animation
3. Run `python3 add_bird.py birds/your_bird.png`, paste the JSON, then `git push`
4. Their bird appears on the projected display within ~30 seconds

## Workshop Instructions
See **[INSTRUCTIONS.md](INSTRUCTIONS.md)** for the full step-by-step guide.

## Repo structure
```
BirdsBirdBirds/
├── index.html        ← Live projector display (GitHub Pages)
├── manifest.json     ← Queue of all submitted birds + animation data
├── add_bird.py       ← Workshop helper script
├── INSTRUCTIONS.md   ← Step-by-step attendee guide
└── birds/            ← Submitted bird images
```

*made with ♥ by the MLH AI Roadshow Team*
