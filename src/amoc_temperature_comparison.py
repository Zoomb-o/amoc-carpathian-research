import pandas as pd
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

amoc = amoc.replace(-99999, pd.NA)

amoc["Year"] = amoc[1]

annual_amoc = (
    amoc.groupby("Year")[13]
    .mean()
    .reset_index()
)

annual_amoc.columns = ["Year", "AMOC"]

# =====================
# CARPATHIAN BASIN
# =====================

ds_cb = xr.open_dataset(
    "data/carpathian_temperature_1980_2025.nc"
)

cb = ds_cb["t2m"].mean(
    dim=["latitude", "longitude"]
)

cb = cb - 273.15

df_cb = pd.DataFrame({
    "Date": pd.to_datetime(ds_cb["valid_time"].values),
    "Temperature": cb.values
})

df_cb["Year"] = df_cb["Date"].dt.year

annual_cb = (
    df_cb.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

annual_cb.columns = ["Year", "Carpathian"]

# =====================
# WESTERN EUROPE
# =====================

ds_we = xr.open_dataset(
    "data/western_europe_temperature_1980_2025.nc"
)

we = ds_we["t2m"].mean(
    dim=["latitude", "longitude"]
)

we = we - 273.15

df_we = pd.DataFrame({
    "Date": pd.to_datetime(ds_we["valid_time"].values),
    "Temperature": we.values
})

df_we["Year"] = df_we["Date"].dt.year

annual_we = (
    df_we.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

annual_we.columns = ["Year", "WesternEurope"]

# =====================
# MERGE
# =====================

df = annual_amoc.merge(
    annual_cb,
    on="Year"
)

df = df.merge(
    annual_we,
    on="Year"
)

df = df[
    (df["Year"] >= 2004) &
    (df["Year"] <= 2024)
]

# =====================
# STANDARDIZE
# =====================

for col in [
    "AMOC",
    "Carpathian",
    "WesternEurope"
]:
    df[col] = (
        df[col] - df[col].mean()
    ) / df[col].std()

# =====================
# PLOT
# =====================

plt.figure(figsize=(12,6))

plt.plot(
    df["Year"],
    df["AMOC"],
    label="AMOC"
)

plt.plot(
    df["Year"],
    df["Carpathian"],
    label="Carpathian Basin"
)

plt.plot(
    df["Year"],
    df["WesternEurope"],
    label="Western Europe"
)

plt.axhline(
    0,
    linestyle="--"
)

plt.title(
    "Standardized AMOC and Temperature Variability (2004–2024)"
)

plt.xlabel("Year")
plt.ylabel("Standardized Anomaly")

plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/amoc_temperature_comparison.png",
    dpi=300
)

plt.show()