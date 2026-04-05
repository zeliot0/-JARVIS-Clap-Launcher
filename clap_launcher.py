import pyaudio
import numpy as np
import subprocess
import time
import webbrowser

# --- CONFIG ---
THRESHOLD = 300
COOLDOWN = 3.0

# --- APP PATHS ---
INTELLIJ_PATH = r"D:\IntelliJ IDEA 2026.1\bin\idea64.exe"
SPOTIFY_PATH = r"C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\Spotify.exe"
YOUTUBE_URL = "https://www.youtube.com/watch?v=rrim6_9VSeM&list=RDrrim6_9VSeM&start_radio=1"

# --- AUDIO SETUP ---
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Listening for a clap... (Ctrl+C to stop)")

last_launch = 0

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio = np.frombuffer(data, dtype=np.int16)
        volume = np.abs(audio).mean()
        now = time.time()

        if volume > THRESHOLD:
            if now - last_launch > COOLDOWN:
                print("Clap detected! Launching everything like JARVIS...")
                subprocess.Popen([INTELLIJ_PATH])
                subprocess.Popen([SPOTIFY_PATH])
                webbrowser.open(YOUTUBE_URL)
                # Open Neuroclaw in its own tab
                subprocess.Popen(
                    ["wt", "-w", "0", "new-tab", "--title", "NEUROCLAW", "powershell", "-NoExit", "-Command", "neuro"]
                )
                # Open Gemini in its own tab
                subprocess.Popen(
                    ["wt", "-w", "0", "new-tab", "--title", "GEMINI", "powershell", "-NoExit", "-Command", "gemini"]
                )
                # Open Claude in its own tab
                subprocess.Popen(
                    ["wt", "-w", "0", "new-tab", "--title", "CLAUDE", "powershell", "-NoExit", "-Command", "claude"]
                )
                last_launch = now

except KeyboardInterrupt:
    print("Stopped.")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()