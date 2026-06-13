import pandas as pd

df = pd.read_csv(
    "data/amoc/rapid_amoc.txt",
    sep=r"\s+",
    header=None,
    engine="python"
)

# Replace missing values
df = df.replace(-99999, pd.NA)

for col in range(5, 14):

    series = pd.to_numeric(
        df[col],
        errors="coerce"
    )

    print()
    print(f"Column {col}")
    print("Count:", series.count())
    print("Min:", round(series.min(), 2))
    print("Max:", round(series.max(), 2))
    print("Mean:", round(series.mean(), 2))