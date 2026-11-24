import os
LINE = "Our standup ran so long HR classified it as a second job."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
