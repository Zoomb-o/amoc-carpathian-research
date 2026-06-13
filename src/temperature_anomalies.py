import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

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

annual["Anomaly"] = (
    annual["Temperature"] - baseline
)

plt.figure(figsize=(12,6))

plt.bar(
    annual["Year"],
    annual["Anomaly"]
)

plt.axhline(
    0,
    linestyle="--"
)

plt.title(
    "Carpathian Basin Temperature Anomalies\n(1980–2000 Baseline)"
)

plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")

plt.tight_layout()

plt.savefig(
    "figures/temperature_anomalies.png",
    dpi=300
)

plt.show()