# 🛠️ Pre-Workshop Computer Setup

Since attendees will be using provided public computers, you need to set up the dummy GitHub accounts and cache their credentials beforehand. This ensures the `python3 add_bird.py` script runs smoothly without prompting users for a password on stage.

*Note: These instructions are geared toward Windows/Linux machines.*

## 1. Prerequisites
On each computer, ensure you have installed:
- **Git** (Git for Windows or via `apt` on Linux)
- **Python 3**
- A web browser (for jspaint.app and Google AI Studio)

## 2. Clone the Repository
Open a terminal and clone the repository:
```bash
git clone https://github.com/mpsiebert/BirdsBirdBirds
cd BirdsBirdBirds
```

## 3. Configure the Dummy Git Identity
For each individual computer, set a dummy name and email so the commits don't bounce:
```bash
git config --global user.name "Workshop User 1"
git config --global user.email "workshop1@example.com"
```
*(You can increment the number for each computer so you know which computer pushed which bird).*

## 4. Cache Credentials (No Password Prompts!)
To let users push their birds automatically, you must authenticate once and let Git remember the dummy account's Personal Access Token.

### On Windows (Git Credential Manager)
Git for Windows usually installs the Git Credential Manager by default.
1. Run:
   ```bash
   git config --global credential.helper manager
   ```
2. Do a test push to trigger the prompt:
   ```bash
   touch test.txt
   git add test.txt
   git commit -m "Test auth"
   git push
   ```
3. A Windows prompt will pop up. Enter the **Dummy GitHub Username** and the **Personal Access Token** as the password.
4. Git Credential Manager will securely save this login in the Windows Credential Manager forever.

### On Linux (Cache in Memory)
You can instruct Git to securely cache credentials in memory for a specified duration (e.g., 10 hours for a full-day workshop).
1. Run:
   ```bash
   # 36000 seconds = 10 hours
   git config --global credential.helper "cache --timeout=36000"
   ```
2. Do a test push to trigger the prompt:
   ```bash
   touch test.txt
   git add test.txt
   git commit -m "Test auth"
   git push
   ```
3. Enter the Dummy Username and Personal Access Token in the terminal. The credentials are now cached for the next 10 hours.

*(If you restart the Linux machine, you will need to do one manual push to re-cache the password).*

## 5. Ready for Attendees!
Once this setup is finished, attendees can simply sit down, draw their bird, and run `python3 add_bird.py`. The script will seamlessly execute the `git add`, `commit`, and `push` commands automatically in the background!
