# ============================================================
# TASK 2: UNEMPLOYMENT ANALYSIS WITH PYTHON
# ============================================================

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_csv("Unemployment in India.csv")

print("=" * 60)
print("UNEMPLOYMENT ANALYSIS")
print("=" * 60)

print("\nOriginal dataset shape:", df.shape)


# ============================================================
# 3. DATA CLEANING
# ============================================================

# Remove completely empty rows
df = df.dropna(how="all")

# Clean column names
df.columns = df.columns.str.strip()

# Clean text columns
for column in ["Region", "Frequency", "Area"]:
    df[column] = df[column].astype(str).str.strip()

# Convert date column
df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

# Convert numerical columns
numeric_columns = [
    "Estimated Unemployment Rate (%)",
    "Estimated Employed",
    "Estimated Labour Participation Rate (%)"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

# Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter cleaning:", df.shape)


# ============================================================
# 4. DATA QUALITY CHECK
# ============================================================

print("\n" + "=" * 60)
print("DATA QUALITY CHECK")
print("=" * 60)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nDate range:")
print(
    df["Date"].min().strftime("%B %Y"),
    "to",
    df["Date"].max().strftime("%B %Y")
)

print("\nNumber of regions:", df["Region"].nunique())

print("\nAreas:")
print(df["Area"].unique())


# ============================================================
# 5. BASIC EXPLORATION
# ============================================================

unemployment = df["Estimated Unemployment Rate (%)"]

print("\n" + "=" * 60)
print("BASIC STATISTICS")
print("=" * 60)

print(f"\nMean:   {unemployment.mean():.2f}%")
print(f"Median: {unemployment.median():.2f}%")
print(f"Minimum: {unemployment.min():.2f}%")
print(f"Maximum: {unemployment.max():.2f}%")
print(f"Std Dev: {unemployment.std():.2f}")


# ============================================================
# 6. MONTHLY AVERAGE UNEMPLOYMENT
# ============================================================

monthly = (
    df.groupby("Date")["Estimated Unemployment Rate (%)"]
    .mean()
    .sort_index()
)

print("\n" + "=" * 60)
print("MONTHLY AVERAGE UNEMPLOYMENT")
print("=" * 60)

for date, value in monthly.items():
    print(f"{date.strftime('%b %Y'):10} : {value:.2f}%")


# ============================================================
# 7. GRAPH 1 — OVERALL UNEMPLOYMENT TREND
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly.index,
    monthly.values,
    marker="o",
    linewidth=2
)

plt.title(
    "Average Unemployment Rate in India",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")

# Show dates as: May 2019, Jun 2019, etc.
plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%b %Y")
)

plt.xlim(
    monthly.index.min(),
    monthly.index.max()
)

plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# ============================================================
# 8. COVID-19 IMPACT ANALYSIS
# ============================================================

# Pre-COVID: May 2019 - February 2020
pre_covid = df[
    df["Date"] < pd.Timestamp("2020-03-01")
]

# COVID-impact period: March 2020 - June 2020
covid = df[
    df["Date"] >= pd.Timestamp("2020-03-01")
]

pre_covid_avg = (
    pre_covid["Estimated Unemployment Rate (%)"].mean()
)

covid_avg = (
    covid["Estimated Unemployment Rate (%)"].mean()
)

difference = covid_avg - pre_covid_avg

percentage_change = (
    difference / pre_covid_avg
) * 100


print("\n" + "=" * 60)
print("COVID-19 IMPACT ANALYSIS")
print("=" * 60)

print(f"\nPre-COVID average: {pre_covid_avg:.2f}%")
print(f"COVID-period average: {covid_avg:.2f}%")
print(f"Increase: {difference:.2f} percentage points")
print(f"Relative increase: {percentage_change:.2f}%")


# ============================================================
# 9. GRAPH 2 — COVID-19 IMPACT
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly.index,
    monthly.values,
    marker="o",
    linewidth=2,
    label="Average unemployment"
)

# Highlight COVID period
plt.axvspan(
    pd.Timestamp("2020-03-01"),
    pd.Timestamp("2020-06-30"),
    alpha=0.15,
    label="COVID-impact period"
)

plt.axvline(
    pd.Timestamp("2020-03-01"),
    linestyle="--",
    linewidth=1.5
)

plt.title(
    "Impact of COVID-19 on Unemployment",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%b %Y")
)

plt.xlim(
    monthly.index.min(),
    monthly.index.max()
)

plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# ============================================================
# 10. COVID MONTH-BY-MONTH ANALYSIS
# ============================================================

covid_monthly = monthly[
    monthly.index >= pd.Timestamp("2020-03-01")
]

print("\n" + "=" * 60)
print("COVID-PERIOD MONTHLY CHANGES")
print("=" * 60)

for date, value in covid_monthly.items():
    print(f"{date.strftime('%b %Y'):10} : {value:.2f}%")


# Find highest COVID month
highest_covid_date = covid_monthly.idxmax()
highest_covid_value = covid_monthly.max()

print(
    f"\nHighest COVID-period unemployment: "
    f"{highest_covid_date.strftime('%B %Y')} "
    f"({highest_covid_value:.2f}%)"
)


# ============================================================
# 11. MONTH-TO-MONTH CHANGE
# ============================================================

monthly_change = monthly.diff()

largest_increase_date = monthly_change.idxmax()
largest_increase = monthly_change.max()

largest_decrease_date = monthly_change.idxmin()
largest_decrease = monthly_change.min()

print("\n" + "=" * 60)
print("LARGEST MONTH-TO-MONTH CHANGES")
print("=" * 60)

print(
    f"\nLargest increase: "
    f"{largest_increase:.2f} percentage points "
    f"in {largest_increase_date.strftime('%B %Y')}"
)

print(
    f"Largest decrease: "
    f"{abs(largest_decrease):.2f} percentage points "
    f"in {largest_decrease_date.strftime('%B %Y')}"
)


# ============================================================
# 12. GRAPH 3 — MONTH-TO-MONTH CHANGE
# ============================================================

plt.figure(figsize=(12, 6))

plt.bar(
    monthly_change.index,
    monthly_change.values
)

plt.axhline(
    0,
    linewidth=1
)

plt.title(
    "Month-to-Month Change in Unemployment Rate",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Change in Unemployment Rate (Percentage Points)")

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%b %Y")
)

plt.xlim(
    monthly_change.index.min(),
    monthly_change.index.max()
)

plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()


# ============================================================
# 13. RURAL VS URBAN ANALYSIS
# ============================================================

area_average = (
    df.groupby("Area")["Estimated Unemployment Rate (%)"]
    .mean()
    .sort_values(ascending=False)
)

print("\n" + "=" * 60)
print("RURAL VS URBAN ANALYSIS")
print("=" * 60)

for area, value in area_average.items():
    print(f"{area:10} : {value:.2f}%")


# ============================================================
# 14. GRAPH 4 — RURAL VS URBAN
# ============================================================

plt.figure(figsize=(8, 5))

sns.barplot(
    x=area_average.index,
    y=area_average.values
)

plt.title(
    "Average Unemployment Rate: Rural vs Urban",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Area")
plt.ylabel("Average Unemployment Rate (%)")

plt.tight_layout()
plt.show()


# ============================================================
# 15. REGIONAL ANALYSIS
# ============================================================

region_average = (
    df.groupby("Region")["Estimated Unemployment Rate (%)"]
    .mean()
    .sort_values(ascending=True)
)

print("\n" + "=" * 60)
print("REGIONAL ANALYSIS")
print("=" * 60)

print(region_average.round(2))


# ============================================================
# 16. GRAPH 5 — REGIONAL UNEMPLOYMENT
# ============================================================

plt.figure(figsize=(12, 9))

plt.barh(
    region_average.index,
    region_average.values
)

plt.title(
    "Average Unemployment Rate by Region",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Average Unemployment Rate (%)")
plt.ylabel("Region")

plt.grid(axis="x", alpha=0.3)

plt.tight_layout()
plt.show()


# ============================================================
# 17. MONTHLY PATTERN / SEASONAL ANALYSIS
# ============================================================

df["Month"] = df["Date"].dt.month

monthly_pattern = (
    df.groupby("Month")["Estimated Unemployment Rate (%)"]
    .mean()
)

month_names = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]

print("\n" + "=" * 60)
print("MONTHLY PATTERN")
print("=" * 60)

for month_number, value in monthly_pattern.items():
    print(
        f"{month_names[month_number - 1]:5} : "
        f"{value:.2f}%"
    )


# ============================================================
# 18. GRAPH 6 — MONTHLY PATTERN
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_pattern.index,
    monthly_pattern.values,
    marker="o",
    linewidth=2
)

plt.title(
    "Monthly Pattern of Unemployment",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Average Unemployment Rate (%)")

plt.xticks(
    range(1, 13),
    month_names
)

plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# ============================================================
# 19. DISTRIBUTION OF UNEMPLOYMENT
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    unemployment,
    bins=30,
    kde=True
)

plt.title(
    "Distribution of Unemployment Rates",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Number of Observations")

plt.tight_layout()
plt.show()


# ============================================================
# 20. KEY FINDINGS
# ============================================================

highest_month = monthly.idxmax()
highest_value = monthly.max()

lowest_month = monthly.idxmin()
lowest_value = monthly.min()


print("\n")
print("=" * 60)
print("KEY FINDINGS")
print("=" * 60)

print(
    f"""
1. OVERALL TREND
   The overall average unemployment rate in the dataset was
   {unemployment.mean():.2f}%.

2. COVID-19 IMPACT
   Pre-COVID average: {pre_covid_avg:.2f}%
   COVID-period average: {covid_avg:.2f}%
   Difference: {difference:.2f} percentage points.

3. COVID-19 PEAK
   The highest monthly average occurred in
   {highest_covid_date.strftime('%B %Y')} at
   {highest_covid_value:.2f}%.

4. LARGEST MONTHLY INCREASE
   The largest month-to-month increase was
   {largest_increase:.2f} percentage points in
   {largest_increase_date.strftime('%B %Y')}.

5. LARGEST MONTHLY DECREASE
   The largest month-to-month decrease was
   {abs(largest_decrease):.2f} percentage points in
   {largest_decrease_date.strftime('%B %Y')}.

6. RURAL VS URBAN
   Rural average: {area_average.get('Rural', np.nan):.2f}%
   Urban average: {area_average.get('Urban', np.nan):.2f}%.

7. MONTHLY PATTERN
   Monthly variation is visible, but the dataset covers only
   May 2019 to June 2020. Therefore, recurring seasonal
   patterns cannot be established reliably.

8. DATA LIMITATION
   The dataset ends in June 2020. Therefore, this analysis
   cannot determine the long-term post-COVID recovery.
"""
)


# ============================================================
# 21. POLICY-RELEVANT INSIGHTS
# ============================================================

print("=" * 60)
print("POLICY-RELEVANT INSIGHTS")
print("=" * 60)

print(
"""
1. CRISIS EMPLOYMENT SUPPORT
   The sharp increase in unemployment during the COVID-impact
   period shows the importance of rapid employment and income
   support mechanisms during major economic disruptions.

2. REGIONAL LABOUR-MARKET MONITORING
   Large differences between regions indicate that national
   unemployment averages can hide important regional variation.
   Region-level monitoring can therefore provide more detailed
   information for employment planning.

3. RURAL AND URBAN DIFFERENCES
   The difference between Rural and Urban unemployment rates
   suggests that labour-market conditions can be examined
   separately across different areas.

4. TIMELY MONITORING
   The rapid increase and subsequent decline during 2020
   demonstrate the value of timely unemployment data for
   identifying major labour-market changes.

5. SEASONAL ANALYSIS
   A longer multi-year dataset would be required to identify
   reliable recurring seasonal unemployment patterns. Such
   information could be useful for workforce and employment
   planning.
"""
)


# ============================================================
# 22. FINAL CONCLUSION
# ============================================================

print("=" * 60)
print("CONCLUSION")
print("=" * 60)

print(
"""
The unemployment dataset was cleaned and analyzed using Python
to examine overall trends, the COVID-19 impact, Rural-Urban
differences, regional variation, and monthly patterns.

The analysis shows a substantial increase in unemployment during
the COVID-impact period, with the strongest increase occurring
around April and May 2020. The data also shows differences
between Rural and Urban areas and considerable variation across
regions.

Monthly variations are visible, but the dataset covers only
May 2019 to June 2020, so it is not sufficient to establish
recurring seasonal unemployment patterns or long-term
post-COVID recovery.

The results demonstrate how data analysis can help identify
major labour-market changes and provide evidence that can be
considered in economic and social-policy planning.
"""
)

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)