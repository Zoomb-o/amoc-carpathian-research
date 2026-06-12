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

summer = (
    df[df["Month"].isin([6, 7, 8])]
    .groupby("Year")["Temperature"]
    .mean()
)

winter = (
    df[df["Month"].isin([12, 1, 2])]
    .groupby("Year")["Temperature"]
    .mean()
)

continentality = pd.DataFrame({
    "Year": summer.index,
    "Summer": summer.values,
    "Winter": winter.values
})

continentality["Range"] = (
    continentality["Summer"]
    - continentality["Winter"]
)

fit = np.polyfit(
    continentality["Year"],
    continentality["Range"],
    1
)

trend = fit[0] * 10

print()
print("Continentality trend:")
print(round(trend, 3), "°C per decade")

plt.figure(figsize=(12,6))

plt.plot(
    continentality["Year"],
    continentality["Range"]
)

plt.title(
    "Carpathian Basin Annual Temperature Range"
)

plt.xlabel("Year")
plt.ylabel("Summer - Winter (°C)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "figures/continentality_trend.png",
    dpi=300
)

plt.show()