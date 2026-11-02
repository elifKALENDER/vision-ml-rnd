"""
MIUUL Python Practice — Homework 01
Core Python Reactivation

Source basis:
- data_structures.py
- functions_conditions_loops_comprehensions.py

Purpose
-------
This file turns the course-note examples into independent coding exercises.
Do not copy the source examples while solving.

Rules
-----
1. Read the task.
2. Try from a blank TODO area.
3. Use the MIUUL note files only as reference if you forget syntax.
4. If still stuck, ask for a small hint.
5. Prefer return over print for reusable functions unless the task explicitly asks for output.
6. Add pytest tests for reusable functions.
"""

# ============================================================
# SECTION 1 — DATA STRUCTURES
# ============================================================

# EXERCISE 1 — Type Recognition
"""
Create one variable for each type:
- int
- float
- str
- bool
- list
- dict
- tuple
- set

Print the type of each variable using type().
"""

# TODO


# EXERCISE 2 — String Indexing and Slicing
"""
Given:
text = "industrial artificial intelligence"

Tasks:
1. Print the first character.
2. Print the last character.
3. Print the first 10 characters.
4. Check whether "artificial" is inside the string.
5. Convert the whole string to uppercase.
"""

text = "industrial artificial intelligence"

# TODO


# EXERCISE 3 — String Methods
"""
Given:
raw_status = "  WARNING_MACHINE  "

Create a cleaned version that:
- removes surrounding whitespace
- converts to lowercase
- replaces "_" with " "

Expected logical result:
"warning machine"
"""

raw_status = "  WARNING_MACHINE  "

# TODO


# EXERCISE 4 — List Operations
"""
Given:
temperatures = [65, 72, 91, 88]

Tasks:
1. Add 79 to the end.
2. Insert 70 at index 1.
3. Remove the element at index 0 using pop().
4. Replace one value using index assignment.
5. Print the final length.
"""

temperatures = [65, 72, 91, 88]

# TODO


# EXERCISE 5 — Nested List Access
"""
Given:
sensor_batches = [
    ["M01", [65, 1.2]],
    ["M02", [91, 2.8]],
    ["M03", [72, 1.1]],
]

Print:
- "M02"
- 91
- 2.8

Use indexing only.
"""

sensor_batches = [
    ["M01", [65, 1.2]],
    ["M02", [91, 2.8]],
    ["M03", [72, 1.1]],
]

# TODO


# EXERCISE 6 — Dictionary Basics
"""
Given:
machine = {
    "id": "M01",
    "temperature": 82,
    "vibration": 1.8
}

Tasks:
1. Read temperature using key access.
2. Read vibration using get().
3. Update temperature to 87.
4. Add "status": "running".
5. Print keys, values and items.
"""

machine = {
    "id": "M01",
    "temperature": 82,
    "vibration": 1.8
}

# TODO


# EXERCISE 7 — Dictionary Lookup
"""
Create a dictionary mapping short model codes to names.

Example idea:
"LR" -> "Logistic Regression"

Tasks:
1. Check whether a chosen key exists using 'in'.
2. Retrieve one value.
3. Add a new key-value pair using update().
"""

# TODO


# EXERCISE 8 — Tuple
"""
Create:
reading = ("M01", 82, 1.8)

Tasks:
1. Access the first element.
2. Slice the first two elements.
3. Unpack into:
   machine_id, temperature, vibration
4. Try to explain in a comment why direct item assignment should not be used.
"""

# TODO


# EXERCISE 9 — Set Operations
"""
Given:
set_a = {"M01", "M02", "M03"}
set_b = {"M02", "M03", "M04"}

Find:
- difference A-B
- difference B-A
- intersection
- union
- whether they are disjoint
"""

set_a = {"M01", "M02", "M03"}
set_b = {"M02", "M03", "M04"}

# TODO


# ============================================================
# SECTION 2 — FUNCTIONS
# ============================================================

# EXERCISE 10 — Basic Function
"""
Write:

    scale_temperature(value, factor)

Return value * factor.

Call it with at least 3 different inputs.
"""

def scale_temperature(value, factor):
    # TODO
    pass


# EXERCISE 11 — Default Parameter
"""
Write:

    add_margin(value, margin=5)

Return value + margin.

Test:
- with the default margin
- with a custom margin
"""

def add_margin(value, margin=5):
    # TODO
    pass


# EXERCISE 12 — Return Multiple Values
"""
Write:

    sensor_summary(temperature, vibration)

Return:
- original temperature
- original vibration
- temperature * 2
- vibration * 2

Unpack all returned values into separate variables.
"""

def sensor_summary(temperature, vibration):
    # TODO
    pass


# EXERCISE 13 — Function Calling Another Function
"""
Write two functions:

    normalize_value(value, max_value)
    calculate_score(temperature, vibration)

calculate_score should call normalize_value at least once.

Keep the logic simple; the goal is function composition.
"""

def normalize_value(value, max_value):
    # TODO
    pass


def calculate_score(temperature, vibration):
    # TODO
    pass


# EXERCISE 14 — Local vs Global
"""
Create a global list:
history = []

Write:
    store_result(value)

The function should append value to history.

Then write a comment explaining:
- which variable is global
- which variable is local
"""

history = []

def store_result(value):
    # TODO
    pass


# ============================================================
# SECTION 3 — CONDITIONS
# ============================================================

# EXERCISE 15 — if / elif / else
"""
Write:
    classify_pressure(pressure)

Rules:
pressure > 50 -> "High"
pressure < 20 -> "Low"
otherwise     -> "Normal"
"""

def classify_pressure(pressure):
    # TODO
    pass


# EXERCISE 16 — Combined Conditions
"""
Write:
    machine_alert(temperature, vibration)

Return "Alert" if:
temperature > 85 OR vibration > 2.5

Otherwise return "Normal".
"""

def machine_alert(temperature, vibration):
    # TODO
    pass


# ============================================================
# SECTION 4 — LOOPS
# ============================================================

# EXERCISE 17 — For Loop
"""
Given:
salaries = [1000, 2000, 3000, 4000, 5000]

Create a new list where:
- salary >= 3000 -> increase by 10%
- otherwise      -> increase by 20%

Use a normal for loop first.
"""

salaries = [1000, 2000, 3000, 4000, 5000]

# TODO


# EXERCISE 18 — break / continue
"""
Given:
values = [10, 20, 30, 40, 50]

A) Stop the loop when value == 40.
B) In a second loop, skip value == 30.

Print the processed values.
"""

values = [10, 20, 30, 40, 50]

# TODO


# EXERCISE 19 — while
"""
Use a while loop to print numbers from 1 to 5.

Then modify it to collect the values into a list instead of only printing.
"""

# TODO


# ============================================================
# SECTION 5 — ENUMERATE / ZIP
# ============================================================

# EXERCISE 20 — Enumerate
"""
Given:
machines = ["M01", "M02", "M03", "M04"]

Create two lists:
- even-index machines
- odd-index machines

Use enumerate().
"""

machines = ["M01", "M02", "M03", "M04"]

# TODO


# EXERCISE 21 — Zip
"""
Given:
machines = ["M01", "M02", "M03"]
temperatures = [65, 91, 72]
vibrations = [1.2, 2.8, 1.1]

Use zip() to iterate over all three together.

Then create a list of tuples from them.
"""

machines = ["M01", "M02", "M03"]
temperatures = [65, 91, 72]
vibrations = [1.2, 2.8, 1.1]

# TODO


# ============================================================
# SECTION 6 — LAMBDA / MAP / FILTER / REDUCE
# ============================================================

# EXERCISE 22 — map
"""
Given:
values = [1, 2, 3, 4, 5]

Use:
1. a normal function + map()
2. lambda + map()

to square every value.
"""

values = [1, 2, 3, 4, 5]

# TODO


# EXERCISE 23 — filter
"""
Given:
temperatures = [63, 67, 91, 72, 88, 69, 95]

Use filter() + lambda to keep only values > 80.
Convert the result to a list.
"""

temperatures = [63, 67, 91, 72, 88, 69, 95]

# TODO


# EXERCISE 24 — reduce
"""
Given:
values = [1, 2, 3, 4]

Use reduce() to calculate the total.

Then compare the result with sum(values).
"""

values = [1, 2, 3, 4]

# TODO


# ============================================================
# SECTION 7 — COMPREHENSIONS
# ============================================================

# EXERCISE 25 — List Comprehension
"""
Given:
values = [10, 20, 30, 40, 50]

Create:
A) a list containing each value * 2
B) a list containing only values > 25
C) a list that returns "high" if value > 25 else "low"
"""

values = [10, 20, 30, 40, 50]

# TODO


# EXERCISE 26 — Dict Comprehension
"""
Given:
numbers = range(10)

Create a dictionary:
- key   = even number
- value = square of that number

Use dict comprehension.
"""

numbers = range(10)

# TODO


# EXERCISE 27 — Column-Name Style Transformation
"""
Given:
columns = [
    "temperature",
    "vibration",
    "pressure",
    "machine_id"
]

Create a new list where:
- names containing "machine" get prefix "ID_"
- all others get prefix "SENSOR_"

Use a comprehension.
"""

columns = [
    "temperature",
    "vibration",
    "pressure",
    "machine_id"
]

# TODO


# ============================================================
# FINAL CHALLENGE — NO NOTES FOR 30 MINUTES
# ============================================================

"""
Build a small machine-analysis program using only core Python.

Input:
records = [
    {"id": "M01", "temperature": 65, "vibration": 1.2},
    {"id": "M02", "temperature": 91, "vibration": 2.8},
    {"id": "M03", "temperature": 72, "vibration": 1.1},
    {"id": "M04", "temperature": 88, "vibration": 3.0},
    {"id": "M05", "temperature": 69, "vibration": 1.5},
]

Requirements:
1. Write a function to detect anomaly.
2. Write a function to return only anomalous records.
3. Calculate anomaly count.
4. Calculate anomaly rate.
5. Return a summary dictionary.
6. Use at least one comprehension.
7. Use at least one enumerate() or zip().
8. Write pytest tests in a separate file.
9. Do not use Pandas.
"""

records = [
    {"id": "M01", "temperature": 65, "vibration": 1.2},
    {"id": "M02", "temperature": 91, "vibration": 2.8},
    {"id": "M03", "temperature": 72, "vibration": 1.1},
    {"id": "M04", "temperature": 88, "vibration": 3.0},
    {"id": "M05", "temperature": 69, "vibration": 1.5},
]

# TODO


# ============================================================
# SELF REVIEW
# ============================================================

"""
After finishing, answer:

1. Which syntax did I need to look up?
2. Which syntax did I remember without help?
3. Which mistake repeated more than once?
4. Can I explain print vs return?
5. Can I explain list vs tuple vs dict vs set?
6. Can I write a function from memory?
7. Can I write a for loop with accumulator from memory?
8. Can I use enumerate and zip without help?
9. Can I write a list comprehension without help?
10. Which 3 exercises should I rewrite tomorrow from a blank file?
"""
