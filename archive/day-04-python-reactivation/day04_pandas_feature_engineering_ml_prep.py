"""
Industrial AI / ML Prep
Day 4 — Pandas Analysis + Feature Engineering + Data Preparation

DATA
----
Continue using machine_sensor_dirty.csv.

Goal:
Move from "I can inspect a DataFrame" to
"I can transform data into something an ML workflow can consume."

No ML model yet.
"""

import pandas as pd
import numpy as np
from pathlib import Path

DATA_PATH = Path("machine_sensor_dirty.csv")


# ============================================================
# EXERCISE 1 — Build a Clean Analysis DataFrame
# ============================================================
"""
Load the CSV and create df_clean.

Perform only the cleaning decisions you made on Day 3:
- duplicate removal
- status normalization
- numeric conversion
- missing-value strategy

Check shape and dtypes afterwards.
"""
# TODO


# EXERCISE 2 — Rename Columns
"""
Create clean, consistent column names.

Target style:
machine_id, temperature, vibration, pressure, status

Do not rename columns one by one with repeated assignments.
"""
# TODO


# EXERCISE 3 — Create Rule-Based Features
"""
Create:
- high_temperature
- high_vibration
- high_pressure

Use boolean expressions.

Then create:
- anomaly

Rule:
temperature > 85 OR vibration > 2.5
"""
# TODO


# EXERCISE 4 — Create a Simple Risk Score
"""
Use:
+1 temperature > 80
+1 vibration > 2.0
+1 pressure > 55

Create risk_score.
Sort descending.
Display the riskiest machines.
"""
# TODO


# EXERCISE 5 — Feature Summary
"""
For each numeric feature:
- mean
- median
- std
- min
- max

Create one compact summary DataFrame.
"""
# TODO


# EXERCISE 6 — Grouped Operational Summary
"""
Group by status and calculate:
- count
- mean temperature
- mean vibration
- mean pressure
- mean risk_score

Sort by mean risk_score descending.
"""
# TODO


# EXERCISE 7 — Conditional Machine Lists
"""
Create:
- critical_machines
- normal_machines

as Python lists of machine IDs.

Then create the same results as DataFrames.
"""
# TODO


# EXERCISE 8 — loc / iloc Practice
"""
Using loc and iloc:
- select anomaly=True records
- select first 3 rows
- select machine_id + risk_score
- update one known field safely
"""
# TODO


# EXERCISE 9 — Sorting and Ranking
"""
Produce:
1. top 5 by temperature
2. top 5 by vibration
3. top 5 by risk_score

Compare whether the same machines appear repeatedly.
"""
# TODO


# EXERCISE 10 — Correlation-Based Feature Discussion
"""
Calculate:
temperature/vibration/pressure correlation matrix.

Identify:
- strongest pair
- weakest pair

Then explain:
Why would highly correlated input features sometimes matter to ML?

Do not drop features automatically.
This is an analysis decision.
"""
# TODO


# ============================================================
# TRANSFORMATION / APPLY / MERGE
# ============================================================

# EXERCISE 11 — Status Mapping
"""
Create a numeric status_code mapping:
running -> 0
warning -> 1
critical -> 2
stopped -> 3
unknown -> -1

Use map() or replace().
"""
# TODO


# EXERCISE 12 — Apply a Custom Classification
"""
Write a function classify_risk(score):
0 -> low
1 -> medium
2 -> high
3 -> severe

Apply it to risk_score.
"""
# TODO


# EXERCISE 13 — Build a Second Table
"""
Create a small DataFrame named machine_owners:

machine_id | team
M01        | A
M02        | B
M03        | A
...

Include every machine_id in the cleaned dataset.

Then merge it with df_clean.
"""
# TODO


# EXERCISE 14 — Merge Reasoning
"""
After the merge, answer:
- What happens if an ID exists in df_clean but not machine_owners?
- What happens if an ID exists in machine_owners but not df_clean?

Experiment with:
- inner
- left
- right
"""
# TODO


# ============================================================
# ML-READY DATA
# ============================================================

# EXERCISE 15 — Define Features and Target
"""
Create:

X = machine sensor features
y = anomaly target

For this learning dataset, use:
X = temperature, vibration, pressure
y = anomaly

Do NOT train a model yet.
Just inspect:
X.shape
y.shape
X.dtypes
y.value_counts()
"""
# TODO


# EXERCISE 16 — Check Class Balance
"""
Calculate:
- anomaly count
- normal count
- anomaly percentage

Explain why class balance matters when choosing metrics.
"""
# TODO


# EXERCISE 17 — Prepare a Single Input
"""
Create one Python dictionary representing a new machine reading:

machine_id
temperature
vibration
pressure

Then convert only the feature values into the structure expected by an
ML model.

Do not train anything.
"""
# TODO


# EXERCISE 18 — Save Prepared Data
"""
Save:
- cleaned feature dataset -> cleaned_sensor_data.csv
- small summary -> sensor_summary.json

Then read both files back and verify them.
"""
# TODO


# ============================================================
# FINAL CHALLENGE — DATA PREPARATION
# ============================================================
"""
From a blank file:

1. Load machine_sensor_dirty.csv
2. Clean it
3. Create anomaly
4. Create risk_score
5. Create X and y
6. Inspect class balance
7. Save an ML-ready CSV
8. Explain every transformation

No sklearn yet.

Your final output should be:
- one cleaned CSV
- one summary dictionary
- one short written explanation
"""

if __name__ == "__main__":
    pass
