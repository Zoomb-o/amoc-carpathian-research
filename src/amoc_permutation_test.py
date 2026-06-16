import pandas as pd
import numpy as np
import xarray as xr
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
# CARPATHIAN SUMMER
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
df["Month"] = df["Date"].dt.month

summer = df[df["Month"].isin([6, 7, 8])]

summer_annual = (
    summer.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

# =====================
# MERGE
# =====================

merged = annual_amoc.merge(
    summer_annual,
    on="Year"
)

merged = merged[
    (merged["Year"] >= 2004)
    & (merged["Year"] <= 2024)
]

x = merged["AMOC"].values
y = merged["Temperature"].values

observed_r, _ = pearsonr(x, y)

# =====================
# PERMUTATION TEST
# =====================

n_iter = 10000

count = 0

for _ in range(n_iter):

    shuffled = np.random.permutation(y)

    r, _ = pearsonr(x, shuffled)

    if abs(r) >= abs(observed_r):
        count += 1

perm_p = count / n_iter

print()
print("Observed correlation:")
print(round(observed_r, 3))

print()
print("Permutation p-value:")
print(round(perm_p, 4))

print()
print("Iterations:")
print(n_iter)