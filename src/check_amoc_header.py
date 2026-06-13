file = "data/amoc/rapid_amoc.txt"

with open(file, "r", encoding="utf-8", errors="ignore") as f:
    for i in range(50):
        line = f.readline()
        print(repr(line))