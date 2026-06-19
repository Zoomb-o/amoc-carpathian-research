# Enhanced Warming of the Carpathian Basin and Its Relationship with Atlantic Meridional Overturning Circulation Variability

**Author:** Zsombor Sztyehlik

**Date:** June 2026

---

# Abstract

The Carpathian Basin has experienced substantial warming in recent decades, exceeding the average warming observed across Western Europe. This study investigates long-term temperature trends in the Carpathian Basin between 1980 and 2025 and examines their relationship with Atlantic Meridional Overturning Circulation (AMOC) variability during the RAPID observation period (2004–2024).

Annual mean temperatures were derived from ERA5 reanalysis data and compared with a Western European reference region. AMOC strength was obtained from observations of the RAPID monitoring array at 26.5°N in the North Atlantic.

The Carpathian Basin warmed at a rate of 0.557 °C per decade between 1980 and 2025, compared with 0.304 °C per decade in Western Europe. During the RAPID observation period (2004–2024), warming accelerated to 0.895 °C per decade in the Carpathian Basin, while Western Europe warmed at 0.338 °C per decade. Consequently, the Carpathian Basin warmed approximately 2.65 times faster than Western Europe during this period. AMOC strength declined by 0.951 Sv per decade between 2004 and 2024.

A significant negative correlation was identified between AMOC strength and Carpathian Basin summer temperature (r = -0.583, p = 0.0055). A similarly strong relationship was observed between AMOC strength and the temperature difference between the Carpathian Basin and Western Europe (r = -0.587, p = 0.0052). A 10,000-iteration permutation test confirmed the robustness of the observed relationship (p = 0.0069).

These results suggest that AMOC variability may contribute to enhanced warming in the Carpathian Basin relative to Western Europe. However, the observational nature of the analysis does not establish causality, and further investigation of the underlying physical mechanisms is required.


---

# Introduction

Global mean surface temperatures have increased substantially since the late nineteenth century as a result of increasing greenhouse gas concentrations. However, the magnitude of warming is not spatially uniform, and some regions have experienced significantly faster temperature increases than the global average.

Europe is among the fastest-warming continents, with particularly strong warming observed in Central and Eastern Europe. Several studies have identified enhanced summer warming, increasing frequency of heat extremes, and changing precipitation patterns across the region. Understanding the mechanisms responsible for regional warming differences is important for climate adaptation and impact assessment.

The Carpathian Basin represents a geographically distinct region of Central Europe surrounded by the Carpathian mountain system. Its semi-enclosed topography, continental influences, and complex circulation patterns make it particularly sensitive to climatic variability. Previous studies have documented substantial warming across the region, but the extent to which large-scale oceanic circulation changes may contribute to observed trends remains an open question.

One of the most important components of the global climate system is the Atlantic Meridional Overturning Circulation (AMOC). The AMOC transports heat northward through the Atlantic Ocean and influences atmospheric circulation, precipitation patterns, and temperature distributions across Europe and the North Atlantic region. Recent observations from the RAPID monitoring array at 26.5°N indicate substantial interannual variability and a possible long-term weakening trend during the observational period.

Changes in AMOC strength have been linked to climate variability across Europe through modifications of oceanic heat transport and atmospheric circulation. While much attention has focused on impacts in Western Europe and the North Atlantic region, potential relationships between AMOC variability and temperature changes within the Carpathian Basin remain less well understood.

This study investigates long-term temperature trends in the Carpathian Basin using ERA5 reanalysis data for 1980–2025 and compares them with trends in a Western European reference region. In addition, the study examines relationships between observed AMOC variability and regional temperature changes during the RAPID observation period (2004–2024).

The objectives of this study are:

1. Quantify long-term temperature trends in the Carpathian Basin.
2. Compare regional warming rates between the Carpathian Basin and Western Europe.
3. Assess trends in AMOC strength during the RAPID observation period.
4. Evaluate statistical relationships between AMOC variability and regional temperature changes.
5. Determine whether AMOC variability is associated with enhanced warming of the Carpathian Basin relative to Western Europe.


---

# Data and Methods

## Study Region

The primary study region was the Carpathian Basin, represented by ERA5 grid cells spanning approximately 44°N–49°N and 15°E–27°E. A second region representing Western Europe was defined for comparison.

Spatial averages were calculated across all grid cells within each study region to obtain regional mean climate time series.

## Temperature Data

Monthly mean 2-metre air temperature data were obtained from the ERA5 reanalysis dataset for the period January 1980 to December 2025.

Temperatures were converted from Kelvin to degrees Celsius prior to analysis. Annual mean temperatures were calculated by averaging monthly values within each calendar year.

Seasonal temperatures were also calculated. Summer temperature was defined as the average of June, July, and August (JJA), while winter temperature was defined as the average of December, January, and February (DJF).

## Precipitation Data

Monthly total precipitation data were obtained from ERA5 for the period 1980–2025.

Annual precipitation totals were calculated by summing monthly values within each year. Summer precipitation totals were calculated using June–August values.

## Mean Sea Level Pressure

Monthly mean sea level pressure (MSLP) data were obtained from ERA5 for 1980–2025.

Pressure values were converted from Pascals (Pa) to hectopascals (hPa). Annual and summer mean pressure series were calculated for trend analysis and correlation testing.

## AMOC Data

AMOC observations were obtained from the RAPID monitoring array at 26.5°N in the North Atlantic Ocean.

The RAPID dataset covers the period from April 2004 to March 2024 and includes estimates of total AMOC transport and its individual transport components.

Annual mean AMOC strength was calculated from the reported overturning transport values.

AMOC strength is expressed in Sverdrups (Sv), where:

1 Sv = 10⁶ m³ s⁻¹

## Trend Analysis

Linear trends were estimated using ordinary least-squares (OLS) regression.

Trend magnitudes were converted to units per decade for reporting. Separate trend analyses were performed for:

* Carpathian Basin temperature
* Western European temperature
* Precipitation
* Mean sea level pressure
* AMOC strength
* Continentality indices

## Correlation Analysis

Pearson correlation coefficients were calculated to assess relationships between AMOC variability and regional climate variables.

The following relationships were examined:

* AMOC strength and Carpathian Basin summer temperature
* AMOC strength and winter temperature
* AMOC strength and the Carpathian Basin–Western Europe temperature difference
* Mean sea level pressure and temperature

Statistical significance was evaluated using two-sided p-values.

## Detrended Analysis

To assess whether correlations were driven primarily by shared long-term trends, detrended temperature and AMOC series were generated by removing linear trends from each dataset prior to correlation analysis.

## Lag Analysis

Lagged correlations were calculated to investigate whether AMOC variability preceded regional temperature changes. Correlations were evaluated for lags of up to three years.

## Permutation Testing

A Monte Carlo permutation test was performed using 10,000 random shuffles of the temperature series.

For each iteration, the correlation between the randomized temperature series and the observed AMOC series was calculated.

The permutation p-value was defined as the fraction of randomized correlations with an absolute magnitude equal to or greater than the observed correlation.

## Software

All analyses were performed in Python using the pandas, NumPy, SciPy, xarray, and Matplotlib libraries. Version-controlled workflows were maintained using Git and GitHub.


---

# Results

## 1. Temperature Trends

The Carpathian Basin warmed at a rate of 0.557 °C per decade between 1980 and 2025, compared with 0.304 °C per decade in Western Europe. The resulting difference trend of 0.252 °C per decade indicates substantially faster warming in the Carpathian Basin.

During the RAPID AMOC observation period (2004–2024), warming accelerated in both regions but remained considerably stronger in the Carpathian Basin. The Carpathian Basin warmed at 0.895 °C per decade, while Western Europe warmed at 0.338 °C per decade. The resulting warming contrast of 0.557 °C per decade was more than twice as large as the contrast observed over the full 1980–2025 period.

### Warming Amplification

During 2004–2024, the warming rate in the Carpathian Basin was approximately 2.65 times greater than that observed in Western Europe, indicating substantial regional amplification of warming.

## 2. Precipitation Trends

Annual precipitation in the Carpathian Basin exhibited a weak negative trend of -0.1 mm per decade, while summer precipitation declined by -0.3 mm per decade. In contrast, Western Europe experienced a positive precipitation trend of 0.35 mm per decade.

## 3. Continentality

The continentality index showed a slight negative trend of -0.049 °C per decade over the study period, indicating only minor long-term changes in seasonal temperature contrast.

## 4. AMOC Trends

The mean AMOC strength during the RAPID observation period was 16.98 Sv. A negative trend of -0.951 Sv per decade was identified between 2004 and 2024, indicating a weakening of the overturning circulation during the observational record.

## 5. AMOC–Temperature Relationships

A statistically significant negative relationship was identified between AMOC strength and Carpathian Basin summer temperature (r = -0.583, p = 0.0055). Weaker AMOC conditions were associated with warmer summers in the Carpathian Basin.

A similarly strong negative relationship was observed between AMOC strength and the temperature difference between the Carpathian Basin and Western Europe (r = -0.587, p = 0.0052), suggesting that AMOC variability may be linked to enhanced relative warming within the Carpathian Basin.

The detrended correlation remained negative (r = -0.347), although its magnitude was reduced after removal of long-term trends.

To assess statistical robustness, a permutation test with 10,000 random shuffles was performed. The resulting permutation p-value of 0.0069 confirmed that the observed relationship is unlikely to have arisen by chance.

## 6. Pressure Analysis

Mean sea level pressure exhibited a weak negative trend of -0.013 hPa per decade, while summer pressure declined by -0.005 hPa per decade. The correlation between summer pressure and temperature was negligible (r = 0.004), suggesting that long-term temperature changes were not strongly related to regional mean sea level pressure variations.

---

# Discussion

## Enhanced Warming of the Carpathian Basin

The strongest warming occurred during the 2004–2024 RAPID AMOC observation period. The Carpathian Basin warmed at 0.895 °C per decade, while Western Europe warmed at 0.338 °C per decade. Consequently, the Carpathian Basin warmed approximately 2.65 times faster than Western Europe during this period.

The resulting warming contrast of 0.557 °C per decade exceeds the long-term 1980–2025 contrast of 0.252 °C per decade. This indicates that the relative warming of the Carpathian Basin intensified during the period in which direct AMOC observations are available.

Several factors may contribute to this enhanced regional warming, including continental influences, land-atmosphere feedbacks, and changes in large-scale atmospheric circulation. However, the results of this study suggest that variability in North Atlantic circulation may also play a role.

## Potential Role of AMOC Variability

The strongest relationship identified in this study was between RAPID AMOC strength and Carpathian Basin summer temperature during 2004–2024.

A statistically significant negative correlation was found (r = -0.583, p = 0.0055). A permutation test using 10,000 random shuffles produced a similar significance level (p = 0.0069), indicating that the relationship is unlikely to arise from random variability.

Weaker AMOC conditions were associated with warmer summers in the Carpathian Basin. A similarly strong relationship was observed between AMOC strength and the temperature difference between the Carpathian Basin and Western Europe (r = -0.587, p = 0.0052), suggesting that AMOC variability may be linked specifically to enhanced warming within the Carpathian Basin relative to Western Europe.

The observed relationship is consistent with previous studies that have suggested European climate can be influenced by changes in North Atlantic ocean circulation through modifications of heat transport and atmospheric circulation patterns.

## Comparison with Western Europe

Although both study regions experienced substantial warming, the warming rate was consistently greater in the Carpathian Basin. This suggests that regional amplification mechanisms are operating in addition to the broader warming trend affecting Europe as a whole.

The stronger relationship between AMOC variability and the Carpathian Basin–Western Europe temperature difference is particularly notable because it indicates that AMOC variability may influence not only absolute temperatures but also regional climate contrasts within Europe.


## Strengths of the Study

This study combines direct AMOC observations from the RAPID monitoring array with high-resolution ERA5 reanalysis data for Central Europe.

Multiple statistical approaches were used to evaluate the robustness of the observed relationships, including correlation analysis, lag analysis, detrended analysis, and permutation testing.

The consistency of results across these methods increases confidence that the identified associations are not solely the result of random variability.

## Limitations

Several limitations should be considered when interpreting these results.

First, the RAPID observational record covers only 21 years, which limits the ability to assess long-term relationships and increases sensitivity to interannual variability.

The relatively short duration of the RAPID observational record limits the ability to distinguish multi-decadal variability from long-term climate trends. Consequently, the results should be interpreted as evidence of statistically significant associations rather than definitive proof of a causal mechanism.

Second, the analysis is observational and therefore cannot establish causality. Although statistically significant relationships were identified, additional modelling studies would be required to determine the physical mechanisms responsible for the observed associations.

Third, only a limited set of climate variables was examined. Other factors, including atmospheric circulation indices, soil moisture feedbacks, and large-scale teleconnection patterns, may also contribute to regional temperature variability.

## Future Work

Future work could investigate:

* Atmospheric circulation mechanisms linking AMOC variability to Central European climate.
* Seasonal responses beyond summer.
* Comparison with CMIP climate model simulations.
* Extension of the analysis using longer AMOC proxy reconstructions.
* Examination of additional climate variables, including drought indicators and extreme temperature events.

## Conclusions

Overall, the results suggest that the Carpathian Basin has experienced substantially stronger warming than Western Europe during recent decades and that AMOC variability may contribute to this enhanced warming. While further investigation is required to establish causal mechanisms, the statistically significant relationships identified in this study indicate that North Atlantic circulation variability may be an important factor influencing regional climate change in Central Europe.


---

# Conclusion

## Main Findings

This study investigated temperature trends in the Carpathian Basin and their potential relationship with Atlantic Meridional Overturning Circulation (AMOC) variability.

The Carpathian Basin warmed at a rate of 0.557 °C per decade during 1980–2025, compared with 0.304 °C per decade in Western Europe.

During the RAPID observation period (2004–2024), warming accelerated to 0.895 °C per decade in the Carpathian Basin, while Western Europe warmed at 0.338 °C per decade. Consequently, the Carpathian Basin warmed approximately 2.65 times faster than Western Europe during this period.

AMOC strength declined at a rate of 0.951 Sv per decade between 2004 and 2024.

A statistically significant negative relationship was identified between AMOC strength and Carpathian Basin summer temperature (r = -0.583, p = 0.0055). A similarly strong relationship was found between AMOC strength and the Carpathian Basin–Western Europe temperature difference (r = -0.587, p = 0.0052). A 10,000-iteration permutation test confirmed the robustness of these relationships (p = 0.0069).

## Implications

The results suggest that AMOC variability may contribute to the enhanced warming observed in the Carpathian Basin relative to Western Europe. Although correlation does not establish causation, the consistency between AMOC weakening, increasing regional temperature differences, and statistically significant correlations is consistent with a potential physical connection between North Atlantic circulation variability and regional climate change in Central Europe.

## Future Research

Future work could investigate:

* Atmospheric circulation mechanisms linking AMOC variability to Central European climate.
* Seasonal responses beyond summer.
* Comparison with CMIP climate model simulations.
* Extension of the analysis using longer AMOC proxy reconstructions.
* Examination of additional climate variables, including drought indicators and extreme temperature events.


---

# References

Caesar, L., Rahmstorf, S., Robinson, A., Feulner, G., & Saba, V. (2018). Observed fingerprint of a weakening Atlantic Ocean overturning circulation. Nature, 556, 191–196.

Copernicus Climate Change Service (C3S). ERA5 Monthly Averaged Reanalysis Data. European Centre for Medium-Range Weather Forecasts (ECMWF).

European Environment Agency. (2024). European Climate Risk Assessment.

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Muñoz-Sabater, J., Nicolas, J., Peubey, C., Radu, R., Schepers, D., Simmons, A., Soci, C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, G., Bidlot, J., Bonavita, M., ... Thépaut, J. N. (2020). The ERA5 global reanalysis. Bulletin of the American Meteorological Society, 101(12), E1999–E2049.

IPCC. (2021). Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change. Cambridge University Press.

RAPID-MOCHA-WBTS Programme. RAPID 26.5°N Atlantic Meridional Overturning Circulation Monitoring Array Data.

Smeed, D. A., McCarthy, G. D., Rayner, D., Moat, B. I., Johns, W. E., Baringer, M. O., Meinen, C. S., Collins, J., & Frajka-Williams, E. (2018). The North Atlantic Ocean is in a state of reduced overturning. Geophysical Research Letters, 45(3), 1527–1533.

Trenberth, K. E., Fasullo, J. T., & Shepherd, T. G. (2015). Attribution of climate extreme events. Nature Climate Change, 5, 725–730.

van Oldenborgh, G. J., Doblas-Reyes, F., Wouters, B., Hazeleger, W., & others. (2021). Europe warms faster than the global average. Communications Earth & Environment.

Woollings, T., Hannachi, A., Hoskins, B., & Turner, A. (2010). A regime view of the North Atlantic Oscillation and its response to anthropogenic forcing. Journal of Climate, 23, 1291–1307.

