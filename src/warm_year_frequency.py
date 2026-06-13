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

annual = (
    df.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

baseline = annual[
    (annual["Year"] >= 1980) &
    (annual["Year"] <= 2000)
]["Temperature"].mean()

warm_years = (
    annual["Temperature"] > baseline
).sum()

cold_years = (
    annual["Temperature"] <= baseline
).sum()

print()
print("Baseline (1980-2000):")
print(round(baseline, 2), "°C")

print()
print("Warmer years:")
print(warm_years)

print()
print("Cooler years:")
print(cold_years)