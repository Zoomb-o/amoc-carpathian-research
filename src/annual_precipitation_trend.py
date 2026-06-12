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

# DataFrame
df = pd.DataFrame({
    "Date": pd.to_datetime(ds["valid_time"].values),
    "Precipitation_mm": precip.values
})

df["Year"] = df["Date"].dt.year

# Annual total precipitation
annual = (
    df.groupby("Year")["Precipitation_mm"]
    .sum()
    .reset_index()
)

# Trend
coeffs = np.polyfit(
    annual["Year"],
    annual["Precipitation_mm"],
    1
)

trend = coeffs[0] * 10

print()
print("Annual precipitation trend:")
print(round(trend, 2), "mm per decade")

# Plot
plt.figure(figsize=(12,6))

plt.plot(
    annual["Year"],
    annual["Precipitation_mm"]
)

plt.title(
    "Carpathian Basin Annual Precipitation (1980–2025)"
)

plt.xlabel("Year")
plt.ylabel("Precipitation (mm)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "figures/annual_precipitation_trend.png",
    dpi=300
)

plt.show()