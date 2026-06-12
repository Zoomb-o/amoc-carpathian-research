import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def precipitation_trend(path):

    ds = xr.open_dataset(path)

    precip = ds["tp"].mean(
        dim=["latitude", "longitude"]
    )

    precip = precip * 1000

    df = pd.DataFrame({
        "Date": pd.to_datetime(ds["valid_time"].values),
        "Precipitation": precip.values
    })

    df["Year"] = df["Date"].dt.year

    annual = (
        df.groupby("Year")["Precipitation"]
        .sum()
        .reset_index()
    )

    coeffs = np.polyfit(
        annual["Year"],
        annual["Precipitation"],
        1
    )

    trend = coeffs[0] * 10

    return annual, trend


carpathian, c_trend = precipitation_trend(
    "data/carpathian_precipitation_1980_2025.nc"
)

western, w_trend = precipitation_trend(
    "data/western_europe_precipitation_1980_2025.nc"
)

print()
print("Carpathian Basin precipitation trend:")
print(round(c_trend, 2), "mm per decade")

print()
print("Western Europe precipitation trend:")
print(round(w_trend, 2), "mm per decade")

plt.figure(figsize=(12,6))

plt.plot(
    carpathian["Year"],
    carpathian["Precipitation"],
    label="Carpathian Basin"
)

plt.plot(
    western["Year"],
    western["Precipitation"],
    label="Western Europe"
)

plt.title(
    "Annual Precipitation Comparison"
)

plt.xlabel("Year")
plt.ylabel("Annual Precipitation (mm)")
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/precipitation_comparison.png",
    dpi=300
)

plt.show()