import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
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

# Seasons
winter = df[df["Month"].isin([12, 1, 2])]
summer = df[df["Month"].isin([6, 7, 8])]

winter_annual = (
    winter.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

summer_annual = (
    summer.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

# Trends
winter_fit = np.polyfit(
    winter_annual["Year"],
    winter_annual["Temperature"],
    1
)

summer_fit = np.polyfit(
    summer_annual["Year"],
    summer_annual["Temperature"],
    1
)

print()
print("Winter trend:")
print(round(winter_fit[0] * 10, 3), "°C per decade")

print()
print("Summer trend:")
print(round(summer_fit[0] * 10, 3), "°C per decade")

# Plot
plt.figure(figsize=(12,6))

plt.plot(
    winter_annual["Year"],
    winter_annual["Temperature"],
    label="Winter (DJF)"
)

plt.plot(
    summer_annual["Year"],
    summer_annual["Temperature"],
    label="Summer (JJA)"
)

plt.title(
    "Seasonal Temperatures in the Carpathian Basin"
)

plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/seasonal_temperatures.png",
    dpi=300
)

plt.show()