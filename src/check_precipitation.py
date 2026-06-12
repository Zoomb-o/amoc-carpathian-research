import xarray as xr

ds = xr.open_dataset(
    "data/carpathian_precipitation_1980_2025.nc"
)

print(ds)

print()
print("Time steps:", len(ds.valid_time))
print("First:", ds.valid_time.values[0])
print("Last:", ds.valid_time.values[-1])