# Smart Data Validation & Analytics Engine

A Python-based data validation and analytics system built using core Python concepts. This project processes structured employee data, validates records, handles invalid inputs, removes duplicates, and generates analytical summaries.

The main goal of this project is to strengthen Python fundamentals through real-world data processing and validation logic similar to ETL and backend systems.

---

## Features

- Employee record validation
- Duplicate ID detection
- Invalid salary handling
- Missing field validation
- Negative salary checks
- Clean and invalid record separation
- Salary analytics generation
- Exception handling for faulty records
- Modular Python functions

---

## Python Concepts Used

- Lists
- Dictionaries
- Sets
- Tuples
- Loops
- Conditionals
- Functions
- List Comprehensions
- Dictionary Comprehensions
- Exception Handling

---

## Example Input

```python
employees = [

    {"id": 1, "name": "Pavan", "salary": "50000"},

    {"id": 2, "name": "", "salary": "abc"},

    {"id": 1, "name": "Arun", "salary": "70000"}

]

```

## Example Output

```
Valid Employees: 1
Invalid Employees: 2
Duplicate IDs Found: 1
Average Salary: 50000
```
