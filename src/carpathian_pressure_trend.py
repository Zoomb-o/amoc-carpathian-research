import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds = xr.open_dataset(
    "data/carpathian_mslp_1980_2025.nc"
)

pressure = ds["msl"].mean(
    dim=["latitude", "longitude"]
)

# Convert Pa -> hPa
pressure = pressure / 100

df = pd.DataFrame({
    "Date": pd.to_datetime(ds["valid_time"].values),
    "Pressure": pressure.values
})

df["Year"] = df["Date"].dt.year

annual = (
    df.groupby("Year")["Pressure"]
    .mean()
    .reset_index()
)

slope, intercept = np.polyfit(
    annual["Year"],
    annual["Pressure"],
    1
)

print()
print("Pressure trend:")
print(round(slope * 10, 3), "hPa per decade")

plt.figure(figsize=(10, 6))

plt.plot(
    annual["Year"],
    annual["Pressure"]
)

plt.title(
    "Carpathian Basin Mean Sea Level Pressure"
)

plt.xlabel("Year")
plt.ylabel("Pressure (hPa)")

plt.tight_layout()

plt.savefig(
    "figures/carpathian_pressure_trend.png",
    dpi=300
)

plt.show()