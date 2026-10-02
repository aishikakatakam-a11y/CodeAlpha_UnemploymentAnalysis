# Unemployment Analysis with Python

> **CodeAlpha Internship — Data Science / Data Analytics Project**

An exploratory data analysis project that examines unemployment trends in India, with a focus on the COVID-19 period, Rural–Urban differences, regional variation, and monthly patterns.

---

##  Project Overview

Unemployment is an important indicator of economic and social conditions. Understanding how unemployment changes over time and across different regions can provide useful information for analyzing labour-market conditions.

This project uses **Python** to clean, explore, analyze, and visualize unemployment data from India. The analysis focuses on identifying major unemployment trends, examining changes during the COVID-19 period, comparing Rural and Urban areas, and studying regional and monthly variations.

The project also translates the analytical findings into **economic and social policy insights**, while considering the limitations of the available dataset.

---

##  Objectives

-  Clean and prepare the unemployment dataset
-  Perform exploratory data analysis
-  Analyze unemployment trends over time
-  Investigate changes during the COVID-19 period
-  Compare Rural and Urban unemployment
-  Analyze regional unemployment variation
-  Examine monthly unemployment patterns
-  Create meaningful data visualizations
-  Identify insights relevant to economic and social policy planning

---

##  Dataset

The project uses the **Unemployment in India** dataset.

**| Feature | Details |**
|  Time Period | May 2019 – June 2020 |
|  Regions | 28 |
|  Areas | Rural & Urban |
|  Frequency | Monthly |
|  Observations after cleaning | 740 |

### Main Variables

**| Column | Description |**
| `Region` | Region represented in the observation |
| `Date` | Month and year of observation |
| `Frequency` | Frequency of the data |
| `Estimated Unemployment Rate (%)` | Estimated unemployment rate |
| `Estimated Employed` | Estimated number of employed people |
| `Estimated Labour Participation Rate (%)` | Estimated labour participation rate |
| `Area` | Rural or Urban |

---

##  Technologies Used

**Language**

- Python

**Libraries**

-  Pandas — data manipulation and analysis
-  NumPy — numerical operations
-  Matplotlib — data visualization
-  Seaborn — statistical visualization

**Development Environment**

- Jupyter Notebook
- VS Code

**Version Control**

- GitHub

---

##  Data Preparation

The dataset was prepared before analysis using the following steps:

1. Removed completely empty rows.
2. Cleaned column names and text values.
3. Converted the `Date` column into datetime format.
4. Converted numerical columns into numeric data types.
5. Removed duplicate records.
6. Checked missing values.
7. Verified the date range and number of regions.
8. Prepared the cleaned dataset for analysis.

After cleaning:

**768 → 740 valid observations**

---

##  Exploratory Data Analysis

The analysis examined:

- Dataset structure and dimensions
- Missing values
- Duplicate records
- Date range
- Number of regions
- Rural and Urban categories
- Mean unemployment rate
- Median unemployment rate
- Minimum and maximum unemployment rates
- Standard deviation

### Overall Statistics

**| Statistic | Value |**
| Mean | **11.79%** |
| Median | **8.35%** |
| Minimum | **0.00%** |
| Maximum | **76.74%** |
| Standard Deviation | **10.72%** |

---

##  Unemployment Trend

Monthly average unemployment rates were calculated and visualized to understand how unemployment changed throughout the available period.

The analysis shows relatively lower unemployment levels during much of 2019 and early 2020, followed by a substantial increase during the COVID-impact period.

**Highest monthly average:**

> **May 2020 — 24.88%**

---

##  COVID-19 Impact Analysis

To examine the change during the COVID-impact period, the data was divided into two periods:

**| Period | Average Unemployment |**
| Pre-COVID | **9.51%** |
| COVID-impact period | **17.77%** |
| Difference | **+8.26 percentage points** |
| Relative increase | **~86.9%** |

The largest month-to-month increase occurred between **March and April 2020**.

The analysis identifies a strong temporal association between the COVID-impact period and increased unemployment in the dataset. However, this analysis alone does not establish a causal relationship.

---

##  Rural vs Urban

Average unemployment rates were compared between Rural and Urban areas.

**| Area | Average Unemployment |**
| Rural | **10.32%** |
| Urban | **13.17%** |

The results show differences in unemployment conditions between Rural and Urban areas during the period covered by the dataset.

---

##  Regional Analysis

Average unemployment rates were calculated for each region.

The analysis shows **considerable variation across regions**, demonstrating that a national average may not fully represent labor-market conditions in every region.

A horizontal bar chart is used to make regional differences easier to compare.

---

##  Monthly Pattern

The project also examines unemployment by calendar month.

Monthly variation is visible in the available data. However, the dataset covers only **May 2019 to June 2020**, so there is insufficient repeated yearly data to establish reliable recurring seasonal patterns.

A longer multi-year dataset would be required for a proper seasonal analysis.

---

##  Visualizations

The project includes the following visualizations:

| Visualization | Purpose |
|---|---|
|  Overall Unemployment Trend | Shows unemployment over time |
|  COVID-19 Impact | Highlights the COVID-impact period |
|  Month-to-Month Change | Shows monthly increases and decreases |
|  Rural vs Urban | Compares area-level unemployment |
|  Regional Analysis | Shows regional variation |
|  Monthly Pattern | Examines monthly variation |
|  Distribution | Shows the distribution of unemployment rates |

---

##  Key Findings

- The overall average unemployment rate was approximately **11.79%**.
- The pre-COVID average was approximately **9.51%**.
- The COVID-impact period average increased to approximately **17.77%**.
- The difference between the two periods was approximately **8.26 percentage points**.
- **May 2020** recorded the highest monthly average unemployment rate at approximately **24.88%**.
- Rural and Urban areas showed different average unemployment rates.
- Considerable variation was observed across regions.
- Monthly variation is visible, but recurring seasonal patterns cannot be established reliably from this dataset.

---

##  Economic & Social Policy Insights

The findings provide several areas that can be considered when planning employment and social policies:

### 1. Crisis Employment Support
The sharp increase in unemployment during the COVID-impact period highlights the importance of rapid employment and income-support mechanisms during major economic disruptions.

### 2. Rural–Urban Monitoring
Differences between Rural and Urban unemployment rates suggest that labor-market conditions can be monitored separately across different areas.

### 3. Regional Employment Planning
Regional variation indicates that region-level unemployment information can provide useful context for employment and skill-development planning.

### 4. Timely Labour-Market Monitoring
Large month-to-month changes demonstrate the value of timely unemployment data for identifying sudden labor-market disruptions.

### 5. Long-Term Data Collection
Multi-year unemployment data would allow more reliable analysis of seasonal patterns, long-term trends, and changes beyond the period covered by this project.

---

## Limitations

- The dataset covers only **May 2019 to June 2020**.
- There is insufficient repeated yearly data to establish recurring seasonal patterns.
- The analysis identifies trends and associations but does not establish causal relationships.
- The dataset ends in June 2020, so long-term post-COVID recovery cannot be evaluated.
- Regional averages represent the period covered by this dataset and should not be interpreted as current regional unemployment rankings.

---
