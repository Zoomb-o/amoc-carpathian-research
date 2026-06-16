import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

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

annual_temp = (
    df.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

annual_temp = annual_temp[
    (annual_temp["Year"] >= 2004)
    & (annual_temp["Year"] <= 2024)
]

# =====================
# MERGE
# =====================

merged = annual_amoc.merge(
    annual_temp,
    on="Year"
)

# =====================
# ANOMALIES
# =====================

merged["TempAnomaly"] = (
    merged["Temperature"]
    - merged["Temperature"].mean()
)

merged["AMOCAnomaly"] = (
    merged["AMOC"]
    - merged["AMOC"].mean()
)

# =====================
# PLOT
# =====================

plt.figure(figsize=(10, 6))

plt.plot(
    merged["Year"],
    merged["AMOCAnomaly"],
    label="AMOC Anomaly (Sv)"
)

plt.plot(
    merged["Year"],
    merged["TempAnomaly"],
    label="Temperature Anomaly (°C)"
)

plt.axhline(0, linestyle="--")

plt.xlabel("Year")
plt.ylabel("Anomaly")

plt.title(
    "AMOC and Carpathian Basin Temperature Anomalies (2004–2024)"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/amoc_temperature_timeseries.png",
    dpi=300
)

plt.show()