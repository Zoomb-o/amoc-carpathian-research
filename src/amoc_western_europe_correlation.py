import pandas as pd
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# =====================
# AMOC
# =====================

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

# =====================
# CARPATHIAN BASIN TEMPERATURE
# =====================

ds = xr.open_dataset(
    "data/western_europe_temperature_1980_2025.nc"
)

temps = ds["t2m"].mean(
    dim=["latitude", "longitude"]
)

temps = temps - 273.15

df_temp = pd.DataFrame({
    "Date": pd.to_datetime(ds["valid_time"].values),
    "Temperature": temps.values
})

df_temp["Year"] = df_temp["Date"].dt.year

annual_temp = (
    df_temp.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

annual_temp.columns = ["Year", "WesternEuropeTemperature"]

# =====================
# MERGE
# =====================

df = annual_amoc.merge(
    annual_temp,
    on="Year"
)

df = df[
    (df["Year"] >= 2004) &
    (df["Year"] <= 2024)
]

# =====================
# CORRELATION
# =====================

corr = df["AMOC"].corr(
    df["WesternEuropeTemperature"]
)

print()
print("Correlation:")
print(round(corr, 3))

# =====================
# SCATTER PLOT
# =====================

plt.figure(figsize=(8,6))

plt.scatter(
    df["AMOC"],
    df["WesternEuropeTemperature"]
)

slope, intercept = np.polyfit(
    df["AMOC"],
    df["WesternEuropeTemperature"],
    1
)

x = np.linspace(
    df["AMOC"].min(),
    df["AMOC"].max(),
    100
)

plt.plot(
    x,
    slope*x + intercept
)

plt.xlabel("AMOC Strength (Sv)")
plt.ylabel("Western Europe Temperature (°C)")

plt.title(
    f"AMOC vs Carpathian Basin Temperature\nr = {corr:.2f}"
)

plt.tight_layout()

plt.savefig(
    "figures/amoc_temperature_correlation.png",
    dpi=300
)

plt.show()