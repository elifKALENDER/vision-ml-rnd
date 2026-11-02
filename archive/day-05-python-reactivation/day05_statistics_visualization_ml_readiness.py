"""
Industrial AI / ML Prep
Day 5 — Statistics + Visualization + ML Readiness

Goal:
Finish the data-analysis stage and become ready to start scikit-learn
on Day 6.

Use the same industrial sensor CSV.
No complex model today.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("machine_sensor_dirty.csv")


# ============================================================
# EXERCISE 1 — Rebuild the Clean Dataset from Blank
# ============================================================
"""
Without copying your Day 4 solution:
- load
- inspect
- clean
- normalize
- convert numeric fields
- handle missing values
- remove duplicates

Create df_clean.
"""
# TODO


# EXERCISE 2 — Descriptive Statistics Review
"""
For all numeric columns:
- describe()
- mean
- median
- std
- min
- max
- Q1/Q3

Identify one possible outlier or unusual value.
"""
# TODO


# EXERCISE 3 — Distribution Comparison
"""
For temperature, vibration and pressure:
- histogram
- boxplot

Write one sentence per variable:
"What does this distribution suggest?"
"""
# TODO


# EXERCISE 4 — Pairwise Relationships
"""
Create scatter plots for:
- temperature vs vibration
- temperature vs pressure
- vibration vs pressure

Then inspect correlation numerically.

Reminder:
correlation != causation.
"""
# TODO


# EXERCISE 5 — Correlation Heatmap
"""
Create a clean heatmap for numeric sensor columns.

Answer:
Which variables are most strongly related in this tiny sample?
"""
# TODO


# EXERCISE 6 — Status vs Sensor Behavior
"""
Compare each status group's:
- count
- mean temperature
- mean vibration
- mean pressure

Visualize one useful comparison.
"""
# TODO


# ============================================================
# TARGET / ANOMALY ANALYSIS
# ============================================================

# EXERCISE 7 — Define the Learning Target
"""
Create:
anomaly

Rule:
temperature > 85 OR vibration > 2.5

Then calculate:
- class counts
- class percentages
"""
# TODO


# EXERCISE 8 — Compare Sensor Distributions by Target
"""
For anomaly=False and anomaly=True, compare:
- temperature
- vibration
- pressure

Use groupby and/or boxplots.

Write:
Which sensor appears most different between the groups?
"""
# TODO


# EXERCISE 9 — Feature Matrix
"""
Create:
X = [["temperature", "vibration", "pressure"]]
y = anomaly

Check:
- X shape
- y shape
- missing values
- dtypes
"""
# TODO


# EXERCISE 10 — Leakage Thought Experiment
"""
Write comments answering:

Could any of the following accidentally leak the answer?
- anomaly column itself
- risk_score built directly from the anomaly rule
- machine_id
- status

Which columns should NOT be used as model features if they directly encode
the target or information unavailable at prediction time?
"""
# TODO


# ============================================================
# BASIC STATISTICS FOR ML THINKING
# ============================================================

# EXERCISE 11 — Standard Deviation
"""
Calculate standard deviation for each sensor.

Explain:
What does a high std mean?
What does a low std mean?
"""
# TODO


# EXERCISE 12 — Z-score Thinking
"""
Without using an ML model, calculate a z-score for temperature:

z = (value - mean) / std

Create a temperature_z column.

Then find records with abs(z) > 2.

This is only an exploratory outlier technique.
"""
# TODO


# EXERCISE 13 — IQR Thinking
"""
Calculate Q1 and Q3 for temperature.

IQR = Q3 - Q1

Calculate:
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

Find temperature outliers.

Compare this with the z-score method.
"""
# TODO


# ============================================================
# VISUAL COMMUNICATION
# ============================================================

# EXERCISE 14 — Build an Engineer-Friendly Figure Set
"""
Choose four useful visuals for a one-page maintenance summary:

1. status distribution
2. temperature distribution
3. sensor relationship
4. anomaly comparison

Every plot must have:
- clear title
- useful axis labels
- no decorative charting for its own sake

Write one sentence under each in comments.
"""
# TODO


# EXERCISE 15 — One-Page EDA Conclusions
"""
Write 8–12 lines covering:
- data quality
- distributions
- sensor relationships
- anomaly prevalence
- possible useful features
- limitations of the dataset

Be careful:
this dataset is tiny, so do not claim general industrial behavior.
"""
# TODO


# ============================================================
# FINAL DAY 5 — 60 MIN AI-FREE DATA SCIENCE CHECK
# ============================================================
"""
Start a blank script/notebook.

Using machine_sensor_dirty.csv:

1. load
2. inspect
3. clean
4. create anomaly
5. summarize
6. visualize
7. calculate correlation
8. create X and y
9. check class balance
10. identify at least one potential leakage problem
11. prepare ML-ready data
12. write a short conclusion

NO AI during first 60 minutes.

You should finish today knowing:
- what your data means
- what the target is
- what the features are
- what data problems remain
- what you would give to a model tomorrow
"""

if __name__ == "__main__":
    pass
