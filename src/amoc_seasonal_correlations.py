import pandas as pd
import xarray as xr
import numpy as np

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
# TEMPERATURE
# =====================

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
df["Month"] = df["Date"].dt.month

# Winter
winter = df[
    df["Month"].isin([12, 1, 2])
]

winter = (
    winter.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

# Summer
summer = df[
    df["Month"].isin([6, 7, 8])
]

summer = (
    summer.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

# =====================
# CORRELATIONS
# =====================

winter_df = annual_amoc.merge(
    winter,
    on="Year"
)

summer_df = annual_amoc.merge(
    summer,
    on="Year"
)

winter_df = winter_df[
    (winter_df["Year"] >= 2004) &
    (winter_df["Year"] <= 2024)
]

summer_df = summer_df[
    (summer_df["Year"] >= 2004) &
    (summer_df["Year"] <= 2024)
]

winter_corr = winter_df["AMOC"].corr(
    winter_df["Temperature"]
)

summer_corr = summer_df["AMOC"].corr(
    summer_df["Temperature"]
)

print()
print("Winter correlation:")
print(round(winter_corr, 3))

print()
print("Summer correlation:")
print(round(summer_corr, 3))