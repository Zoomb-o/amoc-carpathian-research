from pathlib import Path

for file in Path("data/amoc").iterdir():
    print(file.name)