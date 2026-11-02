"""
Siemens AI/ML Working Student Preparation
Day 1 — Python Reactivation Exercises

Purpose
-------
This file is a structured practice worksheet for rebuilding independent
Python coding reflexes before moving into Pandas, NumPy, scikit-learn,
predictive maintenance, anomaly detection, and visual quality inspection.

Working Rule
------------
1. Read the task.
2. Break the problem into small steps in your own words.
3. Try for 10–15 minutes without AI help.
4. Run the code and read the error message carefully.
5. If stuck, ask only for:
   a) a small hint,
   b) syntax reminder,
   c) minimum correction,
   d) full solution only as a last resort.
6. After finishing, rewrite at least one similar task from a blank file.

Important
---------
Do not treat this file as a tutorial to copy from.
The TODO sections are intentionally left incomplete so that you write
the actual solution yourself.

Author: Elif Kalender
Target role: Part Time Working Student (AI/ML & Data Science Engineer)
Context: Siemens Smart Infrastructure — Gebze EP Factory
"""
from fontTools.misc.cython import returns
from numpy.ma.core import append

# ============================================================
# 0. QUICK NOTES
# ============================================================

# Core Python concepts to reactivate today:
# - variables
# - if / elif / else
# - for loops
# - functions
# - lists
# - dictionaries
# - file read/write
# - CSV
# - JSON
# - basic debugging
#
# Industrial-data mindset:
# Input -> Validation -> Processing -> Decision -> Output


# ============================================================
# EXERCISE 1 — Temperature Status
# ============================================================

"""
Task:
Given a temperature value:

- below 70       -> "Normal"
- between 70-85  -> "Warning"
- above 85       -> "Critical"

Before coding:
Write the conditions in plain language.

Concepts:
- if
- elif
- else
- comparison operators
"""

temperature = 78

def temperature_comparison(t):
    if t < 70:
        return("Normal")
    elif 70 <= t <= 85:
        return("Warning")
    elif t > 85:
        return("Critical")

temperature_comparison(temperature)


# Write your solution below.


# ============================================================
# EXERCISE 2 — Find High-Temperature Readings
# ============================================================

"""
Task:
Find all temperature values greater than 80 and store them
in a new list.

Restriction:
Do NOT use list comprehension yet. "[NE_DÖNECEK for ELEMAN in LİSTE if KOŞUL]"

Concepts:
- list
- for loop
- if
- append
"""
temperatures = [63, 67, 91, 72, 88, 69, 95, 74]

def find_high_temperatures(t_list):
    high_temperatures = []

    for t in t_list:
        if t>80:
            high_temperatures.append(t)

    return high_temperatures
print(find_high_temperatures(temperatures))


print([t for t in temperatures if t>80])#append'e gerek yok list comprehansion zaten bunu yapıyor

# Loop over temperatures and fill high_temperatures.


# ============================================================
# EXERCISE 3 — Average Vibration
# ============================================================

"""
Task:
Calculate the average vibration value.

Then:
If the average is greater than 2, print:
"High vibration"

You may use:
- sum()
- len()

Concepts:
- numeric operations
- list
- condition
"""

vibration = [1.2, 1.5, 1.1, 2.8, 1.4]

def find_high_vibration(v_list):
    total = 0
    for v in v_list:
        total += v
    average=total/len(v_list)
    if average>2:
        return "High vibration"
    else:
        return "Normal vibration"


print(find_high_vibration(vibration))

# Calculate average_vibration.


# ============================================================
# EXERCISE 4 — Pressure Check Function
# ============================================================

"""
Task:
Create a function named:

    check_pressure(...)

Rules:
- pressure < 20   -> "Low"
- 20 to 50        -> "Normal"
- pressure > 50   -> "High"

Test the function with:
15, 35, 75

Concepts:
- function
- parameter
- return
- condition
"""


def check_pressure(pressure):
    # Return a pressure status string.

    if pressure < 20:
        return "Low"
    elif 20 <= pressure <= 50:
        return "Normal"
    else:
        return "High"


# Implement the decision logic yourself.
print(check_pressure(15))
print(check_pressure(35))
print(check_pressure(75))
# Call check_pressure() with 15, 35, and 75.


# ============================================================
# EXERCISE 5 — Machine Dictionary
# ============================================================

"""
Task:
Using the dictionary below:

1. Print the machine ID.
2. Increase temperature by 5.
3. Add:
       "status": "running"
4. Print every key-value pair using a loop.

Concepts:
- dictionary access
- dictionary update
- iteration
"""

machine = {
    "id": "M01",
    "temperature": 82,
    "vibration": 1.8,
    "pressure": 42,
}

print(machine["id"])
machine["temperature"]+=5
print(machine["temperature"])
machine["status"]="running"
print(machine)
for key in machine.keys():
    print(key,machine[key] )

list(machine.keys())

# Complete all four operations.


# ============================================================
# EXERCISE 6 — Multiple Machines
# ============================================================

"""
Task:
Find the IDs of machines whose temperature is greater than 80.

Expected logical result:
M02
M04

Concepts:
- list of dictionaries
- nested data access
- loop
- condition
"""

machines = [
    {"id": "M01", "temperature": 65},
    {"id": "M02", "temperature": 91},
    {"id": "M03", "temperature": 72},
    {"id": "M04", "temperature": 88},
]

for dict in machines:
    if dict["temperature"]>80:
        print(dict["id"])

# Find and print the relevant machine IDs.


# ============================================================
# EXERCISE 7 — Simple Anomaly Function
# ============================================================

"""
Task:
Write:

    is_anomaly(temperature, vibration)

Return True if at least one condition is true:

- temperature > 85
- vibration > 2.5

Otherwise return False.

Test data:
(70, 1.2)
(90, 1.0)
(72, 3.1)

Concepts:
- function
- boolean logic
- or
- return
"""


def is_anomaly(temperature, vibration):
    """Return True when the reading matches the anomaly rule."""
    conditions=(temperature,vibration)

    if conditions[0]>85 or conditions[1]>2.5:
        return True
    else:
        return False
print(is_anomaly(70,1.2))
print(is_anomaly(90,1.0))
print(is_anomaly(72,3.1))

# Test the function with all three samples.


# ============================================================
# EXERCISE 8 — Text File Read / Write
# ============================================================

"""
Task:
Create a text file and write:

M01,65
M02,91
M03,72

Then:
1. Open the file again.
2. Read its lines.
3. Print each line.
4. Split each line by ",".

Restriction:
Do NOT use the csv module yet.

Concepts:
- open()
- with
- write
- read / iteration
- split
"""

text_file_path = "machine_temperatures.txt"

with open(text_file_path,"w") as file:
    file.write("M01,65\n")
    file.write("M02,91\n")
    file.write("M03,72\n")

# Write the file.

with open(text_file_path,"r") as file:
    content=file.read()
    print(content)
# Read the file.

with open(text_file_path,"r") as file:
    for lines in file:
        parts=lines.strip().split(",")
        print(parts)


# Split the lines.


# ============================================================
# EXERCISE 9 — CSV Reading
# ============================================================

"""
Task:
Create/read a CSV with these columns:

machine_id,temperature,vibration
M01,65,1.2
M02,91,2.8
M03,72,1.1
M04,88,3.0

Then print machines whose temperature is greater than 80.

Important observation:
CSV values may arrive as strings.
Think about which values need type conversion.

Concepts:
- csv module
- row iteration
- string -> int/float conversion
"""

#import csv
#csv_file_path = "machine_sensor_data.csv"
import pandas as pd
import os
#print(os.getcwd())




data = {
"machine_id":["M01","M02","M03","M04"],
"temperature":[65,91,72,88],
"vibration":[1.2,2.8,1.1,3.0]
}
df=pd.DataFrame(data)
df.to_csv("machine_sensor_data.csv",
               index=False)
# Optionally create the CSV file here.


df=pd.read_csv("machine_sensor_data.csv"
               )
print(df.head())
# Read the CSV file with Python's csv module.

print(df["temperature"].dtype)
print(df["vibration"].dtype)
print(df["machine_id"].dtype)
# Convert required values to numeric types.

# TODO:
# Print machines with temperature > 80.
filtered=df[df["temperature"]>80]
print(filtered["machine_id"])


# ============================================================
# EXERCISE 10 — Mini Industrial Anomaly Report
# ============================================================

"""
Task:
Given the sensor_data below, mark a machine as anomalous if:

temperature > 85
OR
vibration > 2.5

At the end, produce:

Toplam makine: ?
Anomaly sayısı: ?
Normal makine sayısı: ?
Anomaly makineleri: [...]
Anomaly rate: ?

This is today's main mini-problem.

Try to structure the code instead of writing everything in one block.

Suggested thinking process:
1. What is the input?
2. What variables do I need?
3. What will I loop over?
4. What condition defines an anomaly?
5. What do I store?
6. What do I print at the end?

Concepts:
- list of dictionaries
- loop
- boolean condition
- counters
- list accumulation
- simple metric calculation
"""

sensor_data = [
    {"machine": "M01", "temperature": 65, "vibration": 1.2},
    {"machine": "M02", "temperature": 91, "vibration": 2.8},
    {"machine": "M03", "temperature": 72, "vibration": 1.1},
    {"machine": "M04", "temperature": 88, "vibration": 3.0},
    {"machine": "M05", "temperature": 69, "vibration": 1.5},
]
# Write your full solution here.
df=pd.DataFrame(sensor_data)
df.to_csv("machine_sensor_data_1.csv",
               index=False)
df=pd.read_csv("machine_sensor_data_1.csv")


#Toplam makine
total_machine= 0
for t in df["machine"]:
    total_machine +=1
    #total_machine_str = str(total_machine)
print(f"Toplam makine:{total_machine}")

#Anomaly sayısı
total_anomaly=0
for t,v in zip(df["temperature"],df["vibration"]):
    if t > 85 or v > 2.5:
        total_anomaly +=1

print(f"Anomaly sayısı:{total_anomaly}")

#Normal makine sayısı
total_normal_machine= total_machine - total_anomaly
print(f"Normal makine sayısı: {total_normal_machine}")

#Anomaly makineleri
anomaly_records= df[
    (df["temperature"]> 85) | (df["vibration"]> 2.5)
]
print(anomaly_records)
print(f"Anomaly makineleri: \n{anomaly_records["machine"]}")

#Anomaly rate

anomaly_rate= total_anomaly/total_machine
print(f"anomaly rate: {anomaly_rate}")






# Write your full solution here.



# ============================================================
# OPTIONAL EXERCISE 11 — JSON PRACTICE
# ============================================================

"""
Task:
Save a small machine record to JSON, then load it again.

Suggested record:
{
    "machine_id": "M01",
    "temperature": 72,
    "vibration": 1.4,
    "status": "running"
}

After loading:
Print machine_id and temperature.

Concepts:
- json.dump
- json.load
"""

import json

json_file_path = "machine_record.json"

# TODO:
# Create a dictionary.
machine_record= {
    "machine_id": "M01",
    "temperature": 72,
    "vibration": 1.4,
    "status": "running"
}

# TODO:
# Write it to JSON.
with open(json_file_path,"w") as file:
    json.dump(machine_record,file)
# TODO:
# Read it back.
with open(json_file_path,"r") as file:
    FILE=json.load(file)
    print(FILE)
# TODO:
# Print selected fields.
print(FILE["temperature"])
print(FILE.items())
print(FILE.keys())
print(FILE.values())
for key, value in FILE.items():
    print(key, value)

# ============================================================
# OPTIONAL EXERCISE 12 — BASIC ERROR HANDLING
# ============================================================

"""
Task:
Try to open a file that may not exist.

Handle the error so that the program prints a clear message
instead of crashing.

Concepts:
- try
- except
- FileNotFoundError

Professional note:
In real data pipelines, failures should usually be explicit and
understandable. Silent failure makes debugging harder.
"""

missing_file = "does_not_exist.csv"

# TODO:
# Add try/except around file reading.

try:
    with open(missing_file,"r") as file:
        content=file.read()
        #df= pd.read_csv(file)
except FileNotFoundError:
    print("Dosya bulunamadı.")

# ============================================================
# END-OF-DAY SELF REVIEW
# ============================================================

"""
Answer these in your own words after completing the exercises.

1. Which tasks could I start from a blank file without help?

2. Which syntax did I forget most often?

3. Could I explain the difference between:
   - list
   - dictionary
   - tuple

4. Could I write a function without looking at an example?

5. Could I read a CSV and convert numeric strings correctly?

6. When I got an error:
   - Did I read the final line of the traceback?
   - Did I identify the line that failed?
   - Did I understand the error type?

7. Which exercise should I rewrite tomorrow from a blank file?

8. What part of today's work resembles an industrial AI/data pipeline?
"""


# ============================================================
# DEBUGGING LOG
# ============================================================

"""
Use this area as a short experiment log.

Example format:

Problem:
What failed?

Error:
What error/message did Python give?

Hypothesis:
Why do I think it failed?

Change:
What did I modify?

Result:
Did it work?

Do not erase failed attempts immediately.
Understanding why something failed is part of engineering practice.
"""


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    # You do not have to move all exercises here today.
    # This block is included so you become familiar with the
    # structure commonly seen in Python scripts.
    pass
