import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/amoc/rapid_amoc.txt",
    sep=r"\s+",
    header=None
)

df = df.replace(-99999, np.nan)

df["decimal_year"] = (
    df[1]
    + (df[2] - 1) / 12
)

amoc = df[[13, "decimal_year"]].dropna()

slope, intercept = np.polyfit(
    amoc["decimal_year"],
    amoc[13],
    1
)

print()
print("AMOC trend:")
print(round(slope * 10, 3), "Sv per decade")