import cdsapi

client = cdsapi.Client()

client.retrieve(
    "reanalysis-era5-single-levels-monthly-means",
    {
        "product_type": "monthly_averaged_reanalysis",
        "variable": "2m_temperature",
        "year": [
            "2000",
            "2001",
            "2002",
            "2003",
            "2004",
            "2005"
        ],
        "month": [
            "01","02","03","04","05","06",
            "07","08","09","10","11","12"
        ],
        "time": "00:00",
        "format": "netcdf",
        "area": [
            49,
            15,
            44,
            27
        ]
    },
    "data/carpathian_temperature_2000_2005.nc"
)

print("Download complete!")