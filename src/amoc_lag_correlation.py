import pandas as pd
import xarray as xr
import numpy as np
from scipy.stats import pearsonr

# =====================
# AMOC
# =====================

amoc = pd.read_csv(
    "data/amoc/rapid_amoc.txt",
    sep=r"\s+",
    header=None,
    engine="python"
)

amoc = amoc.replace(-99999, np.nan)

amoc["Year"] = amoc[1].astype(int)

annual_amoc = (
    amoc.groupby("Year")[13]
    .mean()
    .reset_index()
)

annual_amoc.columns = ["Year", "AMOC"]

# =====================
# SUMMER TEMPERATURE
# =====================

ds = xr.open_dataset(
    "data/carpathian_temperature_1980_2025.nc"
)

temps = ds["t2m"].mean(
    dim=["latitude", "longitude"]
)

temps = temps - 273.15

temp_df = pd.DataFrame({
    "Date": pd.to_datetime(ds["valid_time"].values),
    "Temperature": temps.values
})

temp_df["Year"] = temp_df["Date"].dt.year
temp_df["Month"] = temp_df["Date"].dt.month

summer = temp_df[
    temp_df["Month"].isin([6, 7, 8])
]

summer = (
    summer.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

# =====================
# TEST LAGS
# =====================

for lag in [0, 1, 2, 3]:

    temp_lag = summer.copy()
    temp_lag["Year"] = temp_lag["Year"] - lag

    merged = annual_amoc.merge(
        temp_lag,
        on="Year"
    )

    merged = merged[
        (merged["Year"] >= 2004) &
        (merged["Year"] <= 2024)
    ]

    r, p = pearsonr(
        merged["AMOC"],
        merged["Temperature"]
    )

    print()
    print(f"Lag {lag} years")
    print("Correlation:", round(r, 3))
    print("P-value:", round(p, 4))
    print("N:", len(merged))