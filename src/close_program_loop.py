import subprocess
import time
import time_settings

KILL_TASK="steam.exe"
sleep_minutes = 5

while True:
    if time_settings.is_program_locked():
        print("Killing program...")
        subprocess.call(f"TASKKILL /F /IM {KILL_TASK}", shell=True)
    print("Going to sleep...")
    time.sleep(sleep_minutes*60)