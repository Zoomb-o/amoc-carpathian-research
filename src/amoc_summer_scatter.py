import pandas as pd
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# RAPID AMOC
amoc = pd.read_csv(
    "data/amoc/rapid_amoc.txt",
    sep=r"\s+",
    header=None,
    engine="python"
)

amoc = amoc.replace(-99999, np.nan)

amoc["Year"] = amoc[1].astype(int)

annual_amoc = (
    amoc.groupby("Year")[13]
    .mean()
    .reset_index()
)

annual_amoc.columns = ["Year", "AMOC"]

# Temperature
ds = xr.open_dataset(
    "data/carpathian_temperature_1980_2025.nc"
)

temps = ds["t2m"].mean(
    dim=["latitude", "longitude"]
)

temps = temps - 273.15

df = pd.DataFrame({
    "Date": pd.to_datetime(ds["valid_time"].values),
    "Temperature": temps.values
})

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

summer = df[
    df["Month"].isin([6,7,8])
]

summer = (
    summer.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

merged = annual_amoc.merge(
    summer,
    on="Year"
)

merged = merged[
    (merged["Year"] >= 2004) &
    (merged["Year"] <= 2024)
]

corr = merged["AMOC"].corr(
    merged["Temperature"]
)

print()
print("Correlation:")
print(round(corr, 3))

print()
print("Number of years:")
print(len(merged))

print()
print("AMOC range:")
print(
    round(merged["AMOC"].min(), 2),
    "to",
    round(merged["AMOC"].max(), 2)
)

print()
print("Summer temperature range:")
print(
    round(merged["Temperature"].min(), 2),
    "to",
    round(merged["Temperature"].max(), 2)
)

plt.figure(figsize=(8,6))

plt.scatter(
    merged["AMOC"],
    merged["Temperature"]
)

slope, intercept = np.polyfit(
    merged["AMOC"],
    merged["Temperature"],
    1
)

x = np.linspace(
    merged["AMOC"].min(),
    merged["AMOC"].max(),
    100
)

plt.plot(
    x,
    slope*x + intercept
)

plt.xlabel("AMOC Strength (Sv)")
plt.ylabel("Summer Temperature (°C)")

plt.title(
    f"AMOC vs Carpathian Basin Summer Temperature\nr = {corr:.2f}"
)

plt.tight_layout()

plt.savefig(
    "figures/amoc_summer_correlation.png",
    dpi=300
)

plt.show()