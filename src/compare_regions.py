import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def annual_trend(dataset_path):

    ds = xr.open_dataset(dataset_path)

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

    coeffs = np.polyfit(
        annual["Year"],
        annual["Temperature"],
        1
    )

    trend = coeffs[0] * 10

    return annual, trend


carpathian, c_trend = annual_trend(
    "data/carpathian_temperature_1980_2025.nc"
)

western, w_trend = annual_trend(
    "data/western_europe_temperature_1980_2025.nc"
)

print()
print("Carpathian Basin trend:")
print(round(c_trend, 3), "°C/decade")

print()
print("Western Europe trend:")
print(round(w_trend, 3), "°C/decade")

plt.figure(figsize=(12, 6))

plt.plot(
    carpathian["Year"],
    carpathian["Temperature"],
    label="Carpathian Basin"
)

plt.plot(
    western["Year"],
    western["Temperature"],
    label="Western Europe"
)

plt.title(
    "Annual Mean Temperature Comparison"
)

plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/carpathian_vs_western_europe.png",
    dpi=300
)

plt.show()