import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = np.arange(1950, 2025)

# Example climate trend
temperature = (
    10
    + 0.03 * (years - 1950)
    + np.random.normal(0, 0.3, len(years))
)

df = pd.DataFrame({
    "Year": years,
    "Temperature": temperature
})

print(df.head())

plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Temperature"])
plt.title("Example Climate Trend")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()