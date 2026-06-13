import xarray as xr
import pandas as pd

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

period1 = df[
    (df["Year"] >= 1980) &
    (df["Year"] <= 2000)
]

period2 = df[
    (df["Year"] >= 2001) &
    (df["Year"] <= 2025)
]

print()
print("1980-2000 mean:")
print(round(period1["Temperature"].mean(), 2), "°C")

print()
print("2001-2025 mean:")
print(round(period2["Temperature"].mean(), 2), "°C")

print()
print("Difference:")
print(
    round(
        period2["Temperature"].mean()
        - period1["Temperature"].mean(),
        2
    ),
    "°C"
)