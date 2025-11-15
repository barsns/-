#!/usr/bin/env python3
import subprocess
import time
import os

while True:
    log = subprocess.getoutput("tinyalsa-mixer -D 0 list")
    filename = f"audio_log_{time.strftime('%H%M')}.txt"
    with open(filename, "w") as f:
        f.write(f"# {time.strftime('%Y-%m-%d %H:%M')}\n{log}")
    print(f"Лог сохранён: {filename}")
    time.sleep(600)  # 10 минут