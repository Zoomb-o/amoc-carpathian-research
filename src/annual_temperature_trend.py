import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
ds = xr.open_dataset(
    "data/carpathian_temperature_1980_2025.nc"
)

# Spatial average
temps = ds["t2m"].mean(
    dim=["latitude", "longitude"]
)

# Kelvin -> Celsius
temps = temps - 273.15

# Create dataframe
df = pd.DataFrame({
    "Date": pd.to_datetime(ds["valid_time"].values),
    "Temperature": temps.values
})

# Extract year
df["Year"] = df["Date"].dt.year

# Annual means
annual = (
    df.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

# Trend line
coeffs = np.polyfit(
    annual["Year"],
    annual["Temperature"],
    1
)

trend = np.poly1d(coeffs)

annual["Trend"] = trend(
    annual["Year"]
)

# Total warming
warming = (
    annual["Temperature"].iloc[-1]
    - annual["Temperature"].iloc[0]
)

print()
print("Total warming:")
print(round(warming, 2), "°C")
print()

print("Trend:")
print(round(coeffs[0] * 10, 3),
      "°C per decade")

# Plot
plt.figure(figsize=(12,6))

plt.plot(
    annual["Year"],
    annual["Temperature"],
    label="Annual Mean"
)

plt.plot(
    annual["Year"],
    annual["Trend"],
    label="Linear Trend"
)

plt.title(
    "Carpathian Basin Annual Mean Temperature (1980-2025)"
)

plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/annual_temperature_trend.png",
    dpi=300
)

plt.show()