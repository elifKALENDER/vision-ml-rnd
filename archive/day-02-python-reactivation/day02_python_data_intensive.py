"""
Industrial AI / ML Prep
Day 2 — Intensive Python + CSV + Pandas Practice

DATASET USED THROUGHOUT THE DAY
--------------------------------
machine_sensor_dirty.csv

The CSV represents machine sensor records from a small production line.

Columns:
- machine_id   : machine identifier
- temperature  : machine temperature reading
- vibration    : machine vibration reading
- pressure     : machine pressure reading
- status       : machine operating status

IMPORTANT
---------
Block A still practices CORE PYTHON, so it uses small Python lists/dictionaries
taken from the same machine-sensor scenario instead of using Pandas immediately.

From Block B onward, you will work directly on machine_sensor_dirty.csv.

Learning direction:
real machine problem
-> solve it
-> understand the Python pattern
-> later make the same logic reusable

Protocol
--------
1. Read what the data represents.
2. Write the steps in plain language first.
3. Try 10–15 minutes without AI.
4. Ask for hint -> syntax -> minimum correction -> full solution only last.
5. Test reusable functions with pytest.
6. Rewrite two exercises from a blank file at the end of the day.
"""

from pathlib import Path
import json
import pandas as pd
from seaborn.utils import axis_ticklabels_overlap
from unicodedata import numeric

DATA_PATH = Path("machine_sensor_dirty.csv")


# ============================================================
# BLOCK A — PYTHON FLUENCY
# Same industrial sensor scenario, but WITHOUT Pandas.
# ============================================================


# EXERCISE 1 — Temperature Classifier
"""
REAL MEANING
------------
A machine sends one temperature reading.
You want to classify that reading for a simple maintenance screen.

Write:
    classify_temperature(value)

Rules:
value < 70        -> "Normal"
70 <= value <= 85 -> "Warning"
value > 85        -> "Critical"

Examples from the sensor domain:
69 -> Normal
70 -> Warning
85 -> Warning
86 -> Critical

Return the result.
Do not print inside the function.

GENERAL PYTHON PATTERN
----------------------
one numeric value -> if/elif/else -> return a label
"""

def classify_temperature(value):
    if value < 70:
        return "Normal"
    elif 70 <= value <= 85:
        return "Warning"
    else:
        return "Critical"


print(classify_temperature(69))
print(classify_temperature(70))
print(classify_temperature(85))
print(classify_temperature(86))


# EXERCISE 2 — Filter High Temperature Readings
"""
REAL MEANING
------------
These are valid temperature readings taken from the SAME machine-sensor dataset:

temperature_readings = [65, 91, 72, 88, 69, 76, 95, 84, 79, 102]

The maintenance question is:

"Which temperature readings are above the selected threshold?"

Example:
threshold = 80

Write:
    filter_high_readings(values, threshold)

Version A:
- normal for loop
- if
- append
- return a NEW list

Version B:
- list comprehension

GENERAL PYTHON PATTERN
----------------------
list of measurements -> compare each value with a threshold -> filtered list

NOTE ABOUT YOUR CURRENT ATTEMPT
-------------------------------
Your original Version A still needs review:
- the result list should belong to the function
- append() changes the list; append() itself is not the list you want to return
- returning inside the loop stops the loop early
"""

temperature_readings = [65, 91, 72, 88, 69, 76, 95, 84, 79, 102]

# YOUR CURRENT ATTEMPT — review/fix this yourself first.
high_readings_values = []

def filter_high_readings(values, threshold):
    for v in values:
        if v > threshold:
            high_readings_values.append(v)
        else:
            continue
    return high_readings_values

print(f"temperature_readings: {filter_high_readings(temperature_readings, 80)}")


def filter_high_readings_comprehension(values, threshold):
    return [v for v in values if v > threshold]

print(f"temperature_readings: {filter_high_readings_comprehension(temperature_readings, 80)}")


# Suggested manual test after you repair Version A:
# print(filter_high_readings(temperature_readings, 80))
# print(filter_high_readings_comprehension(temperature_readings, 80))


# EXERCISE 3 — Safe Average Vibration
"""
REAL MEANING
------------
These are vibration readings from machine records in the sensor dataset:

vibration_readings = [1.2, 2.8, 3.0, 1.5, 2.1, 1.7, 3.4, 1.3, 2.6, 2.0, 4.1]

Question:
"What is the average vibration reading?"

Write:
    calculate_average(values)

Requirements:
- compute arithmetic mean without Pandas
- first version should use a loop + accumulator
- optional second version may use sum()

IMPORTANT EDGE CASE
-------------------
What should happen if:
    values = []

Your current function works for a non-empty list,
but you still need to decide and implement the empty-list behavior.

GENERAL PYTHON PATTERN
----------------------
list of numeric measurements -> accumulate -> divide by count -> return aggregate
"""

vibration_readings = [1.2, 2.8, 3.0, 1.5, 2.1, 1.7, 3.4, 1.3, 2.6, 2.0, 4.1]


def calculate_average(values):
    total = 0
    count=0
    if len(values)==0: # the list may be empty
        return None
    for v in values:
        if v != None : # it can be "if v is not None"
            total += v
            count +=1
    if count==0: # if list have any None value we can check it in this way
        return  None
    average = total / count
    return average

print(f"{calculate_average(vibration_readings):.2f}")

def calculate_average1(values):
    notNoneValues = []
    if len(values) ==0:
        return None
    for v in values:
        if v== None:
            continue
        else:
            notNoneValues.append(v)

    if len(notNoneValues) == 0:
        return None

    average = sum(notNoneValues) / len(notNoneValues)
    return average
print(f"{calculate_average1(vibration_readings):.2f}") # it writes just 2 digit after the comma

# TODO:
# Decide what calculate_average([]) should do and make both versions safe.
#I've done it before this part


# EXERCISE 4 — Find Machine
"""
REAL MEANING
------------
A small part of the machine registry is represented as a list of dictionaries.

Each dictionary is one machine record.

machine_records = [
    {"id": "M01", "temperature": 65, "vibration": 1.2},
    {"id": "M02", "temperature": 91, "vibration": 2.8},
    {"id": "M04", "temperature": 88, "vibration": 3.0},
]

Question:
"If I ask for M02, give me the FULL dictionary for M02."

Write:
    find_machine(machines, machine_id)

If the ID does not exist:
return None.

GENERAL PYTHON PATTERN
----------------------
list of dictionaries -> loop -> compare dictionary key -> return matching record
"""

machine_records = [
    {"id": "M01", "temperature": 65, "vibration": 1.2},
    {"id": "M02", "temperature": 91, "vibration": 2.8},
    {"id": "M04", "temperature": 88, "vibration": 3.0},
]


def find_machine(machines, machine_id):
    for m in machines:# m is a dict type, it has own keys and values. Type of "machines" is list
        if m["id"] == machine_id:
            return m
    return None
print(f"{find_machine(machine_records,"M02")}")


# Suggested tests:
# print(find_machine(machine_records, "M02"))
# print(find_machine(machine_records, "M99"))


# EXERCISE 5 — Anomaly Report
"""
REAL MEANING
------------
Now combine multiple machine records.

Use this small clean subset from the SAME sensor scenario:

sensor_rows = [
    {"machine": "M01", "temperature": 65, "vibration": 1.2},
    {"machine": "M02", "temperature": 91, "vibration": 2.8},
    {"machine": "M04", "temperature": 88, "vibration": 3.0},
    {"machine": "M05", "temperature": 69, "vibration": 1.5},
    {"machine": "M08", "temperature": 95, "vibration": 3.4},
]

For THIS LEARNING EXERCISE only:

A record is called anomalous when:
temperature > 85 OR vibration > 2.5

TASK
----
Write:
    build_anomaly_report(sensor_rows)

Return:
{
    "total": ...,
    "anomaly_count": ...,
    "normal_count": ...,
    "anomaly_rate": ...,
    "anomaly_machines": [...]
}

Example meaning:
- total            = number of machine records
- anomaly_count    = how many satisfy the rule--> t>85 ot v>2.5 
- normal_count     = how many do not
- anomaly_rate     = anomaly_count / total
- anomaly_machines = IDs/names of anomalous machines

DO NOT use Pandas here.

GENERAL PYTHON PATTERNS
-----------------------
- loop over list of dictionaries
- OR condition
- counter
- append
- summary dictionary
"""

sensor_rows = [
    {"machine": "M01", "temperature": 65, "vibration": 1.2},
    {"machine": "M02", "temperature": 91, "vibration": 2.8},
    {"machine": "M04", "temperature": 88, "vibration": 3.0},
    {"machine": "M05", "temperature": 69, "vibration": 1.5},
    {"machine": "M08", "temperature": 95, "vibration": 3.4},
]




def build_anomaly_report(sensor_rows):

    machines = []
    count=0
    for m in sensor_rows:
        if( m["temperature"]>85 or m["vibration"]>2.5): # "|" this used for pandas,"or" used for python
            count += 1
            machines.append(m["machine"])
    total = len(sensor_rows)
    anomaly_txt={
        "Total": total,
        "Anomaly_count": count,
        "normal_count": total - count,
        "anomaly_rate": count / total,
        "anomaly_machines": machines
    }
    return anomaly_txt

#build_anomaly_report(sensor_rows)
#print(build_anomaly_report(sensor_rows))
report = build_anomaly_report(sensor_rows)

print(f"Toplam makine: {report['Total']}")
print(f"Anomaly sayısı: {report['Anomaly_count']}")
print(f"Normal makine sayısı: {report['normal_count']}")
print(f"Anomaly rate: {report['anomaly_rate']:.2%}")#it gives persentage info
print(f"Anomaly makineleri: {report['anomaly_machines']}")


# ============================================================
# BLOCK B — CSV / DATA CLEANING
# NOW USE machine_sensor_dirty.csv DIRECTLY.
# ============================================================


# EXERCISE 6 — Initial Inspection
"""
REAL SITUATION
--------------
You received machine_sensor_dirty.csv from the production line.

Before changing anything, inspect the raw export.

Read:
    DATA_PATH

Store it as:
    df_raw

Inspect:
- head()
- shape
- columns
- dtypes
- info()

Write comments answering:
1. How many rows?
2. How many columns?
3. Which column has a suspicious dtype?
4. Why is that dtype suspicious?

Do NOT clean yet.
"""

# TODO
# df_raw = ...
df_raw= pd.read_csv(DATA_PATH)
print(f"Head:\n {df_raw.head(13)}")
print(f"Shape:\n{df_raw.shape}")
print(f"Columns:\n{df_raw.columns}")
print(f"Dtypes:\n{df_raw.dtypes}")
print("Info:\n")
df_raw.info()

#How many rows? 13
#How many columns? 5
#Which column has a suspicious dtype?1 ,temprature is str type,it's suspicious
#Why is that dtype suspicious? Because temperature has to be int data type



# EXERCISE 7 — Missing Values
"""
REAL QUESTION
-------------
"Did every machine record contain every sensor measurement?"

Using df_raw:

Find the number of missing values in EVERY column.

Do not clean yet.

Write one short comment:
Which columns contain missing data?
"""

# TODO
df_raw.info()
print(df_raw.isna().sum())

# EXERCISE 8 — Duplicates
"""
REAL QUESTION
-------------
"Did the export accidentally save the same record twice?"

Using df_raw:

1. Count fully duplicated rows.
2. Display the duplicate row(s).
3. Create:
       df_clean = df_raw.copy()
4. Remove duplicates from df_clean.
5. Compare shape before and after.

Keep df_raw unchanged.
"""

# TODO
df_clean=df_raw.copy()
print(df_clean.duplicated().sum() )#Count fully duplicated rows
print(df_clean[df_clean.duplicated()]) # it shows dublicated row ,df.duplicated() executes bool type DataFrame df.duplicated().sum() executes total duplicated rows
df_clean=df_clean.drop_duplicates()
print(f"Before: {df_raw.shape}")
print(f"After: {df_clean.shape}")
print(df_raw)
print(df_clean)


# EXERCISE 9 — Numeric Conversion
"""
REAL PROBLEM
------------
The temperature column contains an invalid text value:
"not_available"

Because of this, Pandas may not treat the whole temperature column as numeric.

TASK
----
On df_clean:

Convert temperature to numeric.

Invalid text should become NaN instead of crashing.

Hint:
pd.to_numeric(...)

After conversion:
1. inspect temperature dtype
2. count missing temperature values
3. display the row(s) whose temperature is missing

Do not decide how to fill/drop them yet.
"""

# inspect temperature dtype
print(df_clean["temperature"])
#change temperature dtype to numeric from string
df_clean["temperature"] = pd.to_numeric(df_clean["temperature"],errors="coerce")
print(df_clean["temperature"])
#count missing temperature values
print(df_clean["temperature"].isna().sum())
#display the row(s) whose temperature is missing
print(df_clean[df_clean["temperature"].isna()])


# ternary/conditional expression: ")value_if_true" if "condition" else "value_if_false"

# EXERCISE 10 — String Cleaning
"""
REAL PROBLEM
------------
The same machine status appears in inconsistent forms:

"running"
" Running "
"RUNNING"
"WARNING"
"warning"

If you group these directly, logically identical values can become separate groups.

TASK
----
On df_clean, normalize status:

- remove surrounding whitespace
- convert text to lowercase

Then display the unique status values.
"""

# TODO
df_clean["status"]=df_clean["status"].str.strip().str.lower()
print(df_clean["status"])

# EXERCISE 11 — Missing-Value Strategy
"""
REAL DECISION
-------------
After numeric conversion, inspect missing values in:

- temperature
- vibration
- pressure

For EACH sensor column decide separately:

- drop affected row
- fill with mean
- fill with median
- keep NaN

BEFORE implementing:
write a short comment explaining WHY you chose that strategy.

There is no single universal answer.
The purpose is to practice data-cleaning reasoning.
"""

# TODO
import seaborn as sns
import matplotlib.pyplot as plt
df=df_clean
print(df)
print(df[df["temperature"].isna()])
print(df[df["vibration"].isna()])
print(df[df["pressure"].isna()])
# I inspect all values and desided to fill them with their mean values because their mean and median values have not any big differences.


print(df[["temperature","vibration","pressure"]].corr())

print(df["temperature"].describe())
df["temperature"]=df["temperature"].fillna(df["temperature"].mean())

print(df["vibration"].describe())
df["vibration"]=df["vibration"].fillna(df["vibration"].mean())

print(df["pressure"].describe())
df["pressure"]=df["pressure"].fillna(df["pressure"].mean())

print(df)
#sns.histplot(data=df_clean, x="temperature")
#plt.show()

# EXERCISE 12 — Validation
"""
REAL QUESTION
-------------
"After cleaning, is the dataset actually cleaner?"

On df_clean verify:

- row count
- duplicate count
- missing-value counts
- numeric dtypes
- unique status values

Print a compact validation summary.

Then add 2–3 comments:
- what problems were fixed?
- what assumptions did you make?
- what uncertainty remains?
"""

# TODO
print(df.shape)
print(df.duplicated().sum())
print(df.isna().sum())
print(df.dtypes)
print(df["status"])
# ============================================================
# BLOCK C — PANDAS ANALYSIS
# Continue using the cleaned version of THE SAME CSV.
# ============================================================


# EXERCISE 13 — Filtering
"""
MAINTENANCE QUESTIONS
---------------------
Using df_clean, answer:

A) Which records have temperature > 80?
B) Which records have vibration > 2.5?
C) Which records have pressure > 50?
D) Which records have temperature > 85 OR vibration > 2.5?

Display only useful columns such as:
machine_id + relevant sensor values + status

GENERAL PANDAS PATTERN
----------------------
DataFrame -> boolean condition -> filtered DataFrame
"""

# TODO
#df_CSV=pd.read_csv(DATA_PATH)
df=df_clean
"""df["temperature"]=pd.to_numeric(df["temperature"],errors="coerce")
df["temperature"]=df["temperature"].fillna(df["temperature"].mean())
df["vibration"]=df["vibration"].fillna(df["vibration"].mean())
df["pressure"]=df["pressure"].fillna(df["pressure"].mean())
df=df.drop_duplicates()"""


print(df.loc[df["temperature"]>80,
    ["machine_id","temperature","status"]])

print(df.loc[df["vibration"]>2.5,["machine_id","vibration","status"]])

print(df.loc[df["pressure"]>50,["machine_id","pressure","status"]])

print(df.loc[((df["temperature"]>85 )| (df["vibration"]>2.5)),["machine_id","temperature","vibration","status"]])#.loc[ rows , columns ]


# EXERCISE 14 — Anomaly Column
"""
REAL PURPOSE
------------
Instead of repeating the anomaly filter each time,
store the result directly on every machine record.

For THIS LEARNING EXERCISE:

anomaly =
temperature > 85 OR vibration > 2.5

Add boolean column:
    anomaly

Display:
machine_id, temperature, vibration, anomaly

Then count how many anomaly=True records exist.
"""

# TODO
df_anomaly=df.copy()
df_anomaly["anomaly"]=(df["temperature"] > 85) | (df["vibration"] > 2.5)
df_a=df_anomaly.loc[:,["machine_id", "temperature", "vibration", "anomaly"]]
print(df_a)

anomaly_count=df_anomaly["anomaly"].sum()# it just counts True values "(~df_anomaly["anomaly"]).sum()" it gives False values so its normal values
print(f"Anomaly count: {anomaly_count}")

# EXERCISE 15 — Summary Statistics
"""
REAL QUESTION
-------------
"What does this shift look like numerically?"

Using df_clean calculate:

- mean temperature
- median temperature
- max vibration
- min pressure
- anomaly count
- anomaly rate

Write 2–3 lines of interpretation in comments.

Do not only print numbers.
Explain what the numbers tell you about this small dataset.
"""

# TODO
df_stat=df_clean.describe()
print(df_stat)
print(f"{df_stat.loc[["mean","50%"],["temperature"]]}\n "
      f"The mean and median temperatures are close," 
    f"which suggests limited skewness in this small sample.")# loc[row,column]
print(f"{df_stat.loc[["max"],["vibration"]]}\n"
      f"Maximum vibration shows the highest observed vibration value.")
print(f"{df_stat.loc[["min"],["pressure"]]}\n"
      f"Minimum pressure shows the lowest observed pressure value.")
print(f"{anomaly_count}\n"
      f"Anomaly count is the number of records satisfying the anomaly condition.")
anomaly_rate=anomaly_count/len(df_anomaly)
print(f"{anomaly_rate}\n"
      f"Anomaly rate represents the proportion of anomalys records in the dataset.")

# EXERCISE 16 — GroupBy
"""
REAL QUESTION
-------------
"Do records with different status labels show different sensor behavior?"

Group by:
    status

For each status calculate:
- record count
- mean temperature
- mean vibration

Optional:
sort by mean temperature descending.
"""

# TODO
print(df_clean.groupby("status").count())
print(df_clean.groupby("status")[["temperature", "vibration"]].mean())
summary1= df_clean.groupby("status")[["temperature", "vibration"]].mean()
print(summary1.sort_values("temperature",ascending=False))
"""
filtering      → satırları seç
groupby        → satırları gruplara ayır
aggregation    → grupları özetle
sorting        → sonucu sırala"""

# EXERCISE 17 — Sorting
"""
REAL QUESTION
-------------
"Which records should I inspect first if I care about extreme readings?"

Create:

1. top 3 hottest machine records
2. top 3 highest-vibration machine records

Display machine_id and useful sensor/status columns.
"""

# TODO
print(df_clean.sort_values("temperature",ascending=False).head(3)[["machine_id", "temperature", "vibration", "pressure", "status"]])
print(df_clean.sort_values("vibration",ascending=False).head(3)[["machine_id", "temperature", "vibration", "pressure", "status"]])

# EXERCISE 18 — Simple Risk Score
"""
LEARNING-ONLY IDEA
------------------
Create a simple transparent score:

+1 temperature > 80
+1 vibration > 2.0
+1 pressure > 55

You may design another simple rule if you explain it.

TASK
----
- create risk_score
- sort descending
- display the highest scores
- explain why this is NOT a production predictive-maintenance model

The important point:
this is a rule-based coding exercise, not a trained ML model.
"""


df_risk_score=df_clean.copy()
#this part creat Bool value . if we query in a df it's create dataframe
df_risk_score["temperature_flag"] = df_clean["temperature"] > 80
df_risk_score["vibration_flag"] = df_clean["vibration"] > 2.0
df_risk_score["pressure_flag"] = df_clean["pressure"] > 55

df_risk_score["risk_score"]=df_risk_score[["temperature_flag","vibration_flag","pressure_flag"]].sum(axis=1)# sum(axis=1) means sum along rows,sum(axis=0) means sum along columns
print(df_risk_score)
df_risk_score=df_risk_score.drop(columns=["temperature","vibration","pressure","status"]) # it may write in this way df_risk_score.drop(["temperature", "vibration", "pressure"],axis=1,inplace=True)
# axis=1 → columns
# axis=0 → rows
# inplace=True → modify the same DataFrame
print(df_risk_score.sort_values("risk_score",ascending=False))

# This is a simple rule-based risk score, not a trained ML model.
# The thresholds are manually defined for temperature, vibration, and pressure.
# The score does not learn patterns from historical data or use train/test evaluation.


# ============================================================
# BLOCK D — REUSABLE FUNCTIONS
# Same CSV workflow, now turn repeated code into functions.
# ============================================================


# EXERCISE 19 — Loader
"""
REAL PURPOSE
------------
Tomorrow another shift could produce another CSV with the same structure.

Write:
    load_sensor_data(path)

Requirements:
- read CSV
- return DataFrame
- handle FileNotFoundError clearly

Test it first with:
    DATA_PATH
"""

def load_sensor_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print("there is no such a file")
        return None


# EXERCISE 20 — Cleaner
"""
REAL PURPOSE
------------
Instead of manually repeating Block B every time,
put your cleaning logic into one reusable function.

Write:
    clean_sensor_data(df)

Requirements:
- consider df.copy()
- remove duplicates
- normalize status
- convert temperature to numeric
- apply YOUR missing-value strategy from Exercise 11
- return cleaned DataFrame

Do not invent a new cleaning strategy here.
Reuse the decisions you already made.
"""

def clean_sensor_data(df):
    df_c=df.copy()
    df_c=df_c.drop_duplicates()

    df_c["status"]= df_c["status"].str.strip().str.lower()
    df_c["temperature"]=pd.to_numeric(df_c["temperature"],errors="coerce")
    df_c[["temperature","vibration","pressure"]]=df_c[["temperature","vibration","pressure"]].fillna(df_c[["temperature","vibration","pressure"]].mean())

    return df_c


print(f"flg:{clean_sensor_data(df_raw)}")

# EXERCISE 21 — Feature Creation
"""
REAL PURPOSE
------------
Apply the same anomaly rule to any cleaned machine DataFrame.

Write:
    add_anomaly_feature(df)

Add:
- anomaly
temperature > 85 OR vibration > 2.5
- optional risk_score
+1 temperature > 80
+1 vibration > 2.0
+1 pressure > 55
Return DataFrame.

Reuse the rule you already practiced in Block C.
"""

def add_anomaly_feature(df):
    df_anomaly=df.copy()
    df_anomaly["anomaly"]=(df["temperature"]>85) | (df["vibration"]>2.5)

    df_anomaly["temperature_flag"]=(df["temperature"]>80)
    df_anomaly["vibration_flag"]=(df["vibration"]>2.0)
    df_anomaly["pressure_flag"]=(df["pressure"]>55)

    df_anomaly["risk_score"] =df_anomaly[["temperature_flag","vibration_flag","pressure_flag"]].sum(axis=1)
    anomaly_feature=df_anomaly.sort_values("risk_score",ascending=False)[["machine_id","temperature","vibration","pressure","anomaly","risk_score"]]
    return anomaly_feature

result_df= add_anomaly_feature(df_clean)
print(result_df)

# EXERCISE 22 — Summary Function
"""
REAL PURPOSE
------------
Another function or report may need a compact Python dictionary,
not the entire DataFrame.

Write:
    summarize_sensor_data(df)

Return dictionary with at least:

- row_count
- mean_temperature
- max_vibration
- anomaly_count
- anomaly_rate
"""

def summarize_sensor_data(df):
    row_Count=int(len(df))
    mean_Temperature=float(df["temperature"].mean())
    max_Vibration=float(df["vibration"].max())
    anomaly_Count=int(((df["temperature"]>85)| (df["vibration"]>2.5)).sum())
    anomaly_Rate=float(anomaly_Count/row_Count)
    summary={
        "row_count":row_Count,
        "mean_temperature":mean_Temperature,
        "max_vibration":max_Vibration,
        "anomaly_count":anomaly_Count,
        "anomaly_rate":anomaly_Rate
    }

    print(f"row_count        : {summary["row_count"]}\n"
          f"mean_temperature : {summary["mean_temperature"]:.2f}\n"
          f"max_vibration    : {summary["max_vibration"]:.2f}\n"
          f"anomaly_count    : {summary["anomaly_count"]:.2f}\n"
          f"anomaly_rate     : {summary["anomaly_rate"]:.2%}\n"
          )
    return summary



summarize_sensor_data(df_clean)


# EXERCISE 23 — End-to-End Pipeline
"""
REAL PURPOSE
------------
Run the whole workflow for machine_sensor_dirty.csv using reusable pieces.

Write:
    run_pipeline(input_path, output_path)

Flow:

load
-> clean
-> add anomaly
-> summarize
-> save cleaned CSV
-> return summary

Use the functions from Exercises 19–22.

Do not create one giant function containing duplicate logic.
"""

def run_pipeline(input_path, output_path):
    df_r=load_sensor_data(input_path)
    df_c=clean_sensor_data(df_r)
    df_a=add_anomaly_feature(df_c)
    summary=summarize_sensor_data(df_a)

    df_c.to_csv(output_path)

    return summary


CSV_cleaned_file_path = "machine_sensor_cleaned.csv"
CSV_file_path = "machine_sensor_dirty.csv"
summary=run_pipeline(CSV_file_path,CSV_cleaned_file_path)



# EXERCISE 24 — JSON Summary
"""
REAL PURPOSE
------------
The cleaned CSV contains detailed records.
A lightweight summary can be saved separately as JSON.

Use the summary dictionary produced by your pipeline.

Save:
    sensor_summary.json

Then read it again and print two selected fields such as:

- row_count
- anomaly_rate

Practice:
json.dump
json.load
"""

# TODO
json_file_path = "sensor_summary.json"

with open(json_file_path, "w") as file:
    json.dump(summary, file)

with open(json_file_path, "r") as file:
    sensor_summary = json.load(file)
    print(sensor_summary)


# ============================================================
# PYTEST PRACTICE
# ============================================================
"""
Create:
    test_day02_python_data.py

Design tests yourself for:

- classify_temperature
  boundaries: 69, 70, 85, 86

- filter_high_readings
  normal / no-match / empty

- calculate_average
  normal / single / empty

- find_machine
  found / not found

- build_anomaly_report
  none / some / all anomalies

- clean_sensor_data
  duplicate removal
  dtype conversion
  status cleanup

Use small test data.
Do not make the tests depend on the full CSV unless the test specifically
needs file loading.
"""


# ============================================================
# FINAL CHALLENGE — 45 MIN, NO AI
# USE THE SAME machine_sensor_dirty.csv
# ============================================================
"""
You do NOT need a second CSV today.

Use the SAME:
    machine_sensor_dirty.csv

But create a NEW blank Python file and do not look at the code above
for the first 45 minutes.

From memory:

1. Read the CSV.
2. Inspect shape, dtypes, missing values, duplicates.
3. Clean obvious problems.
4. Create anomaly column.
5. Create or reuse a simple risk score.
6. Print 5 riskiest records.
7. Produce 3 useful summary statistics.
8. Save cleaned CSV.
9. Wrap the workflow in at least one reusable function.
10. Write at least 3 pytest tests.
11. Write 5–8 lines explaining assumptions and limitations.

WHY USE THE SAME CSV?
---------------------
Today the goal is fluency and independent repetition,
not surprise-data difficulty.

Later, after this workflow becomes easier,
you can repeat the same challenge on an unseen CSV.
"""


# ============================================================
# END-OF-DAY REVIEW
# ============================================================
"""
1. Which functions could I write without syntax help?
2. Which mistakes repeated from yesterday?
3. Which mistakes did NOT repeat?
4. Can I explain print vs return from memory?
5. Can I explain list vs tuple vs dict?
6. Can I write loop + accumulator from memory?
7. Can I filter a DataFrame from memory?
8. Can I detect missing values and duplicates from memory?
9. Can I safely convert dirty numeric data?
10. Can I explain what each sensor column represents?
11. Where did I still rely on AI?
12. Which two tasks will I rewrite tomorrow from a blank file?
"""


if __name__ == "__main__":
    pass