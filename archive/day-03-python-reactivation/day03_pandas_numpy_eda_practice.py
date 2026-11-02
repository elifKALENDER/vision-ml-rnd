"""
Industrial AI / ML Prep
Day 3 — NumPy + Pandas + EDA Practice

DATA
----
Use the existing:
    machine_sensor_dirty.csv

SOURCE
------
Built from the MIUUL data_analysis_with_python.py topics:
NumPy, Pandas, selection, aggregation/grouping, apply/lambda,
Matplotlib/Seaborn, categorical/numerical analysis and correlation.

RULE
----
Today is about understanding and analyzing the data, not ML yet.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DATA_PATH = Path("machine_sensor_dirty.csv")


# ============================================================
# BLOCK A — NUMPY
# ============================================================

# EXERCISE 1 — Sensor Array
"""
A machine produced these temperature readings:
[65, 91, 72, 88, 69, 76, 95, 84, 79, 102]

Convert to a NumPy array and inspect:
- type
- ndim
- shape
- size
- dtype
"""
temperature_readings = [65, 91, 72, 88, 69, 76, 95, 84, 79, 102]
# TODO
arr=np.array(temperature_readings)

print(f"""
type    : {type(arr)}
ndim    : {arr.ndim}
shape   : {arr.shape}
size    : {arr.size}
dtype   : {arr.dtype}
""")


# EXERCISE 2 — NumPy Conditions
"""
Using the array:
A) first 5 readings
B) last 3 readings
C) readings > 80
D) readings between 70 and 90
"""
# TODO
print(f"""
{arr[:5]} 
{arr[-3:]} 
{arr[arr>80]}
{arr[(70<arr)&(arr<80)]}
""")

# EXERCISE 3 — NumPy Statistics
"""
Calculate:
- mean
- min
- max
- variance
- standard deviation
- sum
"""
# TODO


# EXERCISE 4 — Sensor Matrix
"""
Rows are machines.
Columns are [temperature, vibration, pressure].

Build:
[
    [65, 1.2, 42],
    [91, 2.8, 55],
    [72, 1.1, 39],
    [88, 3.0, 61],
]

Inspect shape and practice row/column indexing.
"""
# TODO


# ============================================================
# BLOCK B — PANDAS FOUNDATIONS
# ============================================================

# EXERCISE 5 — Load and Inspect
"""
Read machine_sensor_dirty.csv into df.

Inspect:
- head()
- shape
- columns
- dtypes
- info()
"""
# TODO


# EXERCISE 6 — Series vs DataFrame
"""
Compare:
df["temperature"]
df[["temperature"]]

Print their values and types.
Explain the difference in one comment.
"""
# TODO


# EXERCISE 7 — Column Selection
"""
Create:
A) machine_id + temperature + vibration
B) machine_id + status
"""
# TODO


# EXERCISE 8 — Row Selection
"""
Use loc and iloc:
A) first row
B) first three rows
C) row with index 1
D) first two rows + selected columns
"""
# TODO


# EXERCISE 9 — Filtering
"""
Answer:
A) temperature > 80
B) vibration > 2.5
C) pressure > 50
D) temperature > 85 OR vibration > 2.5
"""
# TODO


# ============================================================
# BLOCK C — DATA QUALITY
# ============================================================

# EXERCISE 10 — Missing Values
"""
Count missing values per column.
Display rows missing temperature, vibration or pressure.
Do not clean yet.
"""
# TODO


# EXERCISE 11 — Duplicates
"""
Count duplicates, display them, create df_clean, remove duplicates,
and compare before/after shape.
"""
# TODO


# EXERCISE 12 — Descriptive Statistics
"""
For temperature, vibration and pressure calculate:
count, mean, median, std, min, max, 25%, 50%, 75%.
Compare with df_clean.describe().
"""
# TODO


# EXERCISE 13 — Mean vs Median Decision
"""
For each numeric sensor:
- inspect describe()
- compare mean and median
- inspect histogram
- inspect boxplot

Decide which imputation approach is more sensible and explain why.
Do not fill yet.
"""
# TODO


# ============================================================
# BLOCK D — CATEGORICAL + VISUAL ANALYSIS
# ============================================================

# EXERCISE 14 — Normalize Status
"""
strip + lowercase
Then print unique values.
"""
# TODO


# EXERCISE 15 — Status Counts + Ratios
"""
Use value_counts().
Create a summary DataFrame:
status | count | ratio
"""
# TODO


# EXERCISE 16 — Status Plot
"""
Create a Seaborn/Matplotlib count plot with title and labels.
"""
# TODO


# EXERCISE 17 — Temperature Distribution
"""
Create:
- temperature histogram
- temperature boxplot

Write one observation for each.
"""
# TODO


# EXERCISE 18 — Vibration + Pressure
"""
Create histogram and boxplot for vibration and pressure.
Be cautious with conclusions because the dataset is small.
"""
# TODO


# EXERCISE 19 — Correlation
"""
Calculate the correlation matrix for:
temperature, vibration, pressure

Visualize it with a Seaborn heatmap.

Answer:
- strongest positive pair?
- weakest pair?
- does correlation prove causation?
"""
# TODO


# ============================================================
# BLOCK E — GROUPBY / APPLY
# ============================================================

# EXERCISE 20 — Status Group Analysis
"""
Group by status and calculate:
- count
- mean temperature
- mean vibration
- mean pressure
"""
# TODO


# EXERCISE 21 — Highest Mean Temperature Group
"""
From the grouped result, identify the status with highest mean temperature.
Use sorting/selection, not manual reading.
"""
# TODO


# EXERCISE 22 — Multi-Aggregation
"""
Create a compact summary:
temperature -> mean, median, max
vibration   -> mean, max
pressure    -> mean, min, max
"""
# TODO


# EXERCISE 23 — Apply/Lambda
"""
Create temperature_label:
temperature > 85 -> "critical"
otherwise -> "normal"

Use apply + lambda once.
Then compare with a vectorized Pandas expression.
"""
# TODO


# EXERCISE 24 — Severity Score
"""
Learning-only:
+1 temperature > 80
+1 vibration > 2.0
+1 pressure > 55

Create risk/severity score and sort descending.
Explain why this is not a production ML model.
"""
# TODO


# ============================================================
# BLOCK F — MINI EDA REPORT
# ============================================================

# EXERCISE 25 — Five Questions
"""
Answer with code:
1. row count after cleaning
2. column with most missing values before cleaning
3. hottest machine
4. highest-vibration machine
5. anomaly percentage under our learning rule
"""
# TODO


# EXERCISE 26 — Three Useful Charts
"""
Choose three charts that answer meaningful questions.
For each: title + labels + one-sentence interpretation.
"""
# TODO


# EXERCISE 27 — Reusable EDA Function
"""
Write basic_eda_report(df) returning/printing:
- observations
- variables
- missing values
- duplicates
- numeric columns
- categorical columns
"""
def basic_eda_report(df):
    # TODO
    pass


# ============================================================
# FINAL CHALLENGE — AI-FREE MINI EDA
# ============================================================
"""
In a NEW blank file, use machine_sensor_dirty.csv.

Without looking at this solution:
1. load
2. inspect
3. clean obvious problems
4. decide imputation
5. descriptive statistics
6. categorical analysis
7. numeric analysis
8. correlation
9. 3 useful charts
10. write a short EDA conclusion

Separate:
- what the data shows
- what is only a possible pattern
- what cannot be concluded due to the tiny dataset
"""

if __name__ == "__main__":
    pass
