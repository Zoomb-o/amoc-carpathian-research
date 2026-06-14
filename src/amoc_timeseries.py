import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/amoc/rapid_amoc.txt",
    sep=r"\s+",
    header=None
)

# Replace missing values
df = df.replace(-99999, pd.NA)

# Create decimal year

df["decimal_year"] = (
    df[1]
    + (df[2] - 1) / 12
)

# Column 13 appears to be AMOC strength
df["amoc"] = df[13]

# Remove missing rows
df = df.dropna(subset=["amoc"])

plt.figure(figsize=(12,6))

plt.plot(
    df["decimal_year"],
    df["amoc"]
)

plt.title(
    "AMOC Strength (RAPID 26.5°N)"
)

plt.xlabel("Year")
plt.ylabel("Transport (Sv)")

plt.tight_layout()

plt.savefig(
    "figures/amoc_timeseries.png",
    dpi=300
)

plt.show()

print()
print("Mean AMOC:")
print(round(df["amoc"].mean(), 2), "Sv")

print()
print("Minimum:")
print(round(df["amoc"].min(), 2), "Sv")

print()
print("Maximum:")
print(round(df["amoc"].max(), 2), "Sv")