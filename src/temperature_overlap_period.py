import xarray as xr
import pandas as pd
import numpy as np

# Load Carpathian Basin temperature data
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

# Annual means
annual = (
    df.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

# RAPID overlap period
overlap = annual[
    (annual["Year"] >= 2004) &
    (annual["Year"] <= 2024)
]

# Linear trend
slope, intercept = np.polyfit(
    overlap["Year"],
    overlap["Temperature"],
    1
)

print()
print("Carpathian Basin trend (2004-2024):")
print(round(slope * 10, 3), "°C per decade")

print()
print("2004 mean:")
print(round(overlap.iloc[0]["Temperature"], 2), "°C")

print()
print("2024 mean:")
print(round(overlap.iloc[-1]["Temperature"], 2), "°C")

print()
print("Difference:")
print(
    round(
        overlap.iloc[-1]["Temperature"]
        - overlap.iloc[0]["Temperature"],
        2
    ),
    "°C"
)