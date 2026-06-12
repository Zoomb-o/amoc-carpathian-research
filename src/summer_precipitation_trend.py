import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
ds = xr.open_dataset(
    "data/carpathian_precipitation_1980_2025.nc"
)

# Spatial average
precip = ds["tp"].mean(
    dim=["latitude", "longitude"]
)

# Convert meters -> millimeters
precip = precip * 1000

# Create dataframe
df = pd.DataFrame({
    "Date": pd.to_datetime(ds["valid_time"].values),
    "Precipitation_mm": precip.values
})

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# Summer months (June, July, August)
summer = df[df["Month"].isin([6, 7, 8])]

# Summer total precipitation per year
summer_annual = (
    summer.groupby("Year")["Precipitation_mm"]
    .sum()
    .reset_index()
)

# Trend line
coeffs = np.polyfit(
    summer_annual["Year"],
    summer_annual["Precipitation_mm"],
    1
)

trend = coeffs[0] * 10

print()
print("Summer precipitation trend:")
print(round(trend, 2), "mm per decade")

# Plot
plt.figure(figsize=(12, 6))

plt.plot(
    summer_annual["Year"],
    summer_annual["Precipitation_mm"],
    label="Summer Precipitation"
)

plt.plot(
    summer_annual["Year"],
    np.poly1d(coeffs)(summer_annual["Year"]),
    label="Linear Trend"
)

plt.title(
    "Carpathian Basin Summer Precipitation (JJA, 1980–2025)"
)

plt.xlabel("Year")
plt.ylabel("Summer Precipitation (mm)")
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/summer_precipitation_trend.png",
    dpi=300
)

plt.show()