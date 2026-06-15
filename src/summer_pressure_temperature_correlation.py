import xarray as xr
import pandas as pd

# =====================
# TEMPERATURE
# =====================

temp_ds = xr.open_dataset(
    "data/carpathian_temperature_1980_2025.nc"
)

temp = temp_ds["t2m"].mean(
    dim=["latitude", "longitude"]
)

temp = temp - 273.15

temp_df = pd.DataFrame({
    "Date": pd.to_datetime(
        temp_ds["valid_time"].values
    ),
    "Temperature": temp.values
})

temp_df["Year"] = temp_df["Date"].dt.year
temp_df["Month"] = temp_df["Date"].dt.month

temp_df = temp_df[
    temp_df["Month"].isin([6, 7, 8])
]

summer_temp = (
    temp_df.groupby("Year")["Temperature"]
    .mean()
    .reset_index()
)

# =====================
# PRESSURE
# =====================

mslp_ds = xr.open_dataset(
    "data/carpathian_mslp_1980_2025.nc"
)

pressure = mslp_ds["msl"].mean(
    dim=["latitude", "longitude"]
)

pressure = pressure / 100

pressure_df = pd.DataFrame({
    "Date": pd.to_datetime(
        mslp_ds["valid_time"].values
    ),
    "Pressure": pressure.values
})

pressure_df["Year"] = pressure_df["Date"].dt.year
pressure_df["Month"] = pressure_df["Date"].dt.month

pressure_df = pressure_df[
    pressure_df["Month"].isin([6, 7, 8])
]

summer_pressure = (
    pressure_df.groupby("Year")["Pressure"]
    .mean()
    .reset_index()
)

# =====================
# MERGE
# =====================

merged = summer_temp.merge(
    summer_pressure,
    on="Year"
)

corr = merged["Temperature"].corr(
    merged["Pressure"]
)

print()
print("Summer pressure-temperature correlation:")
print(round(corr, 3))