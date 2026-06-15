import xarray as xr
import pandas as pd
import numpy as np

ds = xr.open_dataset(
    "data/carpathian_mslp_1980_2025.nc"
)

pressure = ds["msl"].mean(
    dim=["latitude", "longitude"]
)

pressure = pressure / 100

df = pd.DataFrame({
    "Date": pd.to_datetime(ds["valid_time"].values),
    "Pressure": pressure.values
})

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

summer = df[
    df["Month"].isin([6, 7, 8])
]

summer = (
    summer.groupby("Year")["Pressure"]
    .mean()
    .reset_index()
)

slope, intercept = np.polyfit(
    summer["Year"],
    summer["Pressure"],
    1
)

print()
print("Summer pressure trend:")
print(round(slope * 10, 3), "hPa per decade")