import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
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
# CARPATHIAN
# =====================

carp = xr.open_dataset(
    "data/carpathian_temperature_1980_2025.nc"
)

carp_temp = (
    carp["t2m"]
    .mean(dim=["latitude", "longitude"])
    - 273.15
)

carp_df = pd.DataFrame({
    "Date": pd.to_datetime(carp["valid_time"].values),
    "Temperature": carp_temp.values
})

carp_df["Year"] = carp_df["Date"].dt.year

carp_annual = (
    carp_df.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

# =====================
# WESTERN EUROPE
# =====================

west = xr.open_dataset(
    "data/western_europe_temperature_1980_2025.nc"
)

west_temp = (
    west["t2m"]
    .mean(dim=["latitude", "longitude"])
    - 273.15
)

west_df = pd.DataFrame({
    "Date": pd.to_datetime(west["valid_time"].values),
    "Temperature": west_temp.values
})

west_df["Year"] = west_df["Date"].dt.year

west_annual = (
    west_df.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

# =====================
# MERGE
# =====================

merged = carp_annual.merge(
    west_annual,
    on="Year",
    suffixes=("_carp", "_west")
)

merged["Difference"] = (
    merged["Temperature_carp"]
    - merged["Temperature_west"]
)

merged = merged.merge(
    annual_amoc,
    on="Year"
)

merged = merged[
    (merged["Year"] >= 2004)
    & (merged["Year"] <= 2024)
]

# =====================
# STATS
# =====================

r, p = pearsonr(
    merged["AMOC"],
    merged["Difference"]
)

# =====================
# PLOT
# =====================

plt.figure(figsize=(8, 6))

plt.scatter(
    merged["AMOC"],
    merged["Difference"]
)

m, b = np.polyfit(
    merged["AMOC"],
    merged["Difference"],
    1
)

x = np.linspace(
    merged["AMOC"].min(),
    merged["AMOC"].max(),
    100
)

plt.plot(
    x,
    m * x + b
)

plt.xlabel("AMOC Strength (Sv)")
plt.ylabel(
    "Carpathian - Western Europe Temperature Difference (°C)"
)

plt.title(
    f"AMOC vs Temperature Difference\nr={r:.3f}, p={p:.4f}"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "figures/amoc_temperature_difference_scatter.png",
    dpi=300
)

plt.show()