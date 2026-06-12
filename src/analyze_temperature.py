import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

ds = xr.open_dataset(
    "data/carpathian_temperature_2000_2005.nc"
)

temps = ds["t2m"].mean(
    dim=["latitude", "longitude"]
)

temps = temps - 273.15

df = pd.DataFrame({
    "Date": ds["valid_time"].values,
    "Temperature_C": temps.values
})

plt.figure(figsize=(12, 5))

plt.plot(
    df["Date"],
    df["Temperature_C"]
)

plt.title(
    "Average Monthly Temperature of the Carpathian Basin (2000–2005)"
)

plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "figures/carpathian_temperature_2000_2005.png",
    dpi=300
)

plt.show()