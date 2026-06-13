from pathlib import Path

file = Path("data/amoc/rapid_amoc.txt")

with open(file, "r", encoding="utf-8", errors="ignore") as f:
    for i in range(20):
        print(f.readline().rstrip())