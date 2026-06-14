import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================
# CARPATHIAN BASIN
# =====================

ds_cb = xr.open_dataset(
    "data/carpathian_temperature_1980_2025.nc"
)

cb = ds_cb["t2m"].mean(
    dim=["latitude", "longitude"]
)

cb = cb - 273.15

df_cb = pd.DataFrame({
    "Date": pd.to_datetime(ds_cb["valid_time"].values),
    "Temp": cb.values
})

df_cb["Year"] = df_cb["Date"].dt.year

annual_cb = (
    df_cb.groupby("Year")["Temp"]
    .mean()
    .reset_index()
)

# =====================
# WESTERN EUROPE
# =====================

ds_we = xr.open_dataset(
    "data/western_europe_temperature_1980_2025.nc"
)

we = ds_we["t2m"].mean(
    dim=["latitude", "longitude"]
)

we = we - 273.15

df_we = pd.DataFrame({
    "Date": pd.to_datetime(ds_we["valid_time"].values),
    "Temp": we.values
})

df_we["Year"] = df_we["Date"].dt.year

annual_we = (
    df_we.groupby("Year")["Temp"]
    .mean()
    .reset_index()
)

# =====================
# MERGE
# =====================

df = annual_cb.merge(
    annual_we,
    on="Year",
    suffixes=("_CB", "_WE")
)

df["Difference"] = (
    df["Temp_CB"] -
    df["Temp_WE"]
)

# Trend
slope, intercept = np.polyfit(
    df["Year"],
    df["Difference"],
    1
)

print()
print("Difference trend:")
print(round(slope * 10, 3), "°C per decade")

# Plot
plt.figure(figsize=(10,6))

plt.plot(
    df["Year"],
    df["Difference"]
)

plt.axhline(
    0,
    linestyle="--"
)

plt.title(
    "Carpathian Basin Temperature Minus Western Europe"
)

plt.ylabel("Temperature Difference (°C)")
plt.xlabel("Year")

plt.tight_layout()

plt.savefig(
    "figures/carpathian_minus_western.png",
    dpi=300
)

plt.show()