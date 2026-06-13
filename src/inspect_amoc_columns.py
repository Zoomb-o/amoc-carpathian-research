import pandas as pd

df = pd.read_csv(
    "data/amoc/rapid_amoc.txt",
    sep=r"\s+",
    header=None,
    engine="python"
)

print(df.head())

print()
print("Shape:", df.shape)

print()
print("Columns:")
for i in df.columns:
    print(i)