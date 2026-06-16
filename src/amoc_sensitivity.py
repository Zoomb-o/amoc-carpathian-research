import pandas as pd
import numpy as np
from scipy.stats import linregress

df = pd.read_csv(
    "data/amoc_summer_temperature.csv"
)

result = linregress(
    df["AMOC"],
    df["SummerTemperature"]
)

print()
print("Slope:")
print(round(result.slope, 3), "°C per Sv")

print()
print("Intercept:")
print(round(result.intercept, 3))

print()
print("R-squared:")
print(round(result.rvalue**2, 3))