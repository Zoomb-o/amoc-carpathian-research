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
# SUMMER TEMPERATURE
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

summer = df[
    df["Month"].isin([6, 7, 8])
]

summer = (
    summer.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

merged = annual_amoc.merge(
    summer,
    on="Year"
)

merged = merged[
    (merged["Year"] >= 2004) &
    (merged["Year"] <= 2024)
]

# =====================
# DETREND AMOC
# =====================

amoc_fit = np.polyfit(
    merged["Year"],
    merged["AMOC"],
    1
)

amoc_trend = np.polyval(
    amoc_fit,
    merged["Year"]
)

merged["AMOC_detrended"] = (
    merged["AMOC"] - amoc_trend
)

# =====================
# DETREND TEMPERATURE
# =====================

temp_fit = np.polyfit(
    merged["Year"],
    merged["Temperature"],
    1
)

temp_trend = np.polyval(
    temp_fit,
    merged["Year"]
)

merged["Temp_detrended"] = (
    merged["Temperature"] - temp_trend
)

# =====================
# CORRELATION
# =====================

corr = merged["AMOC_detrended"].corr(
    merged["Temp_detrended"]
)

print()
print("Detrended correlation:")
print(round(corr, 3))