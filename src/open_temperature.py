import xarray as xr

ds = xr.open_dataset(
    "data/carpathian_temperature_2000_2005.nc"
)

print(ds)