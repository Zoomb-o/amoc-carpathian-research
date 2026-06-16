import xarray as xr
import pandas as pd
import numpy as np
from scipy.stats import linregress

def calculate_trend(nc_file):
    ds = xr.open_dataset(nc_file)

    temp = (
        ds["t2m"]
        .mean(dim=["latitude", "longitude"])
        - 273.15
    )

    df = pd.DataFrame({
        "Date": pd.to_datetime(ds["valid_time"].values),
        "Temperature": temp.values
    })

    df["Year"] = df["Date"].dt.year

    annual = (
        df.groupby("Year")["Temperature"]
        .mean()
        .reset_index()
    )

    annual = annual[
        (annual["Year"] >= 2004)
        & (annual["Year"] <= 2024)
    ]

    result = linregress(
        annual["Year"],
        annual["Temperature"]
    )

    return result.slope * 10

carp_trend = calculate_trend(
    "data/carpathian_temperature_1980_2025.nc"
)

west_trend = calculate_trend(
    "data/western_europe_temperature_1980_2025.nc"
)

print()
print("Carpathian trend:")
print(round(carp_trend, 3), "°C per decade")

print()
print("Western Europe trend:")
print(round(west_trend, 3), "°C per decade")

print()
print("Difference:")
print(round(carp_trend - west_trend, 3), "°C per decade")