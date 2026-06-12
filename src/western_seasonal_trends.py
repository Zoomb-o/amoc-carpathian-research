import xarray as xr
import pandas as pd
import numpy as np

# Load dataset
ds = xr.open_dataset(
    "data/western_europe_temperature_1980_2025.nc"
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
print("Western Europe winter trend:")
print(round(winter_fit[0] * 10, 3),
      "°C per decade")

print()
print("Western Europe summer trend:")
print(round(summer_fit[0] * 10, 3),
      "°C per decade")