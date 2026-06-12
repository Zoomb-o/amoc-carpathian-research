import cdsapi

client = cdsapi.Client()

years = [str(y) for y in range(1980, 2026)]

client.retrieve(
    "reanalysis-era5-single-levels-monthly-means",
    {
        "product_type": "monthly_averaged_reanalysis",
        "variable": "2m_temperature",
        "year": years,
        "month": [
            "01","02","03","04","05","06",
            "07","08","09","10","11","12"
        ],
        "time": "00:00",
        "format": "netcdf",
        "area": [
            60,
            -10,
            45,
            5
        ]
    },
    "data/western_europe_temperature_1980_2025.nc"
)

print("Download complete!")