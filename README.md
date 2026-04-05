# 👏 JARVIS Clap Launcher

> **One clap. Everything opens. Like a boss.**

A Python script that listens to your microphone and launches your entire dev environment with a single clap — IntelliJ, Spotify, YouTube, and your AI agents (Neuroclaw, Gemini, Claude) all at once.

---

## 🚀 What It Opens

| App | How |
|-----|-----|
| 🧠 IntelliJ IDEA | Desktop app |
| 🎵 Spotify | Desktop app |
| 📺 YouTube | Browser (your playlist) |
| 🤖 Neuroclaw | New terminal tab |
| 💎 Gemini CLI | New terminal tab |
| 🔵 Claude CLI | New terminal tab |

---

## 📋 Requirements

- Windows 10/11
- Python 3.x
- A microphone
- Windows Terminal installed
- IntelliJ IDEA, Spotify, Neuroclaw, Gemini CLI, Claude CLI installed

### Install Python dependencies

```bash
pip install pyaudio numpy
```

> On some systems you may also need:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## ⚙️ Setup

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/jarvis-clap-launcher.git
cd jarvis-clap-launcher
```

**2. Edit the paths in `clap_launcher.py`** to match your machine:

```python
INTELLIJ_PATH = r"D:\IntelliJ IDEA 2026.1\bin\idea64.exe"
SPOTIFY_PATH  = r"C:\Users\YourName\AppData\Local\Microsoft\WindowsApps\Spotify.exe"
YOUTUBE_URL   = "https://www.youtube.com/watch?v=..."
```

**3. Find your app paths** if you're unsure:
```powershell
# IntelliJ
Get-ChildItem -Path "C:\Program Files\JetBrains" -Recurse -Filter "idea64.exe"

# VS Code (if you use it)
Get-ChildItem -Path "$env:LOCALAPPDATA\Programs" -Recurse -Filter "Code.exe"

# Spotify
Get-ChildItem -Path "$env:LOCALAPPDATA\Microsoft\WindowsApps" -Filter "Spotify.exe"
```

---

## ▶️ Run

```bash
cd C:\Users\YourName\Desktop
python clap_launcher.py
```

Then **clap once** — everything launches instantly. 🎉

---

## 🎚️ Tuning the Sensitivity

If claps aren't detected or it triggers too easily, adjust the `THRESHOLD` value:

```python
THRESHOLD = 300  # increase if too sensitive, decrease if not detecting
```

To find the right value for your mic, run the test script:

```python
# test_mic.py — shows your mic volume in real time
import pyaudio, numpy as np

CHUNK, RATE = 1024, 44100
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Clap and watch the numbers...")
try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        volume = int(np.abs(np.frombuffer(data, dtype=np.int16)).mean())
        if volume > 100:
            print(f"Volume: {volume}")
except KeyboardInterrupt:
    pass
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
```

Set `THRESHOLD` to about **70% of your clap volume**.

---

## 🛠️ Configuration Reference

| Variable | Description | Default |
|----------|-------------|---------|
| `THRESHOLD` | Minimum volume to detect a clap | `300` |
| `COOLDOWN` | Seconds before next trigger | `3.0` |
| `INTELLIJ_PATH` | Full path to IntelliJ executable | — |
| `SPOTIFY_PATH` | Full path to Spotify executable | — |
| `YOUTUBE_URL` | URL to open in browser | — |

---

## ➕ Adding More Apps

To add any new app, just add a line inside the `if` block:

```python
# Another desktop app
subprocess.Popen([r"C:\Path\To\App.exe"])

# Another CLI tool in a new terminal tab
subprocess.Popen(
    ["wt", "-w", "0", "new-tab", "--title", "MYTOOL", "powershell", "-NoExit", "-Command", "mytool"]
)

# Another URL
webbrowser.open("https://example.com")
```

---

## 📁 Project Structure

```
jarvis-clap-launcher/
│
├── clap_launcher.py   # main script
├── test_mic.py        # mic volume tester
└── README.md
```

---

## 🤖 How It Works

```
Microphone → Volume spike detected → Above threshold?
    → Yes → Cooldown passed? → Yes → Launch all apps
    → No  → Keep listening
```

The script reads raw audio chunks from your microphone 44,100 times per second, calculates the average volume of each chunk, and fires when it exceeds your threshold — all with zero delay.

---

## 📄 License

MIT — do whatever you want with it.

---

> Built because clicking icons is for people who don't clap. 👏
