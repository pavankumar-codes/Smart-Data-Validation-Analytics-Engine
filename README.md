# Smart Data Validation & Analytics Engine

## Overview

The Smart Data Validation & Analytics Engine is a Python-based data processing pipeline designed to validate, clean, analyze, sort, search, and generate business insights from employee datasets.

The project demonstrates real-world data engineering concepts such as:

* Data Validation
* Data Cleaning
* Exception Handling
* Logging
* Data Analytics
* Filtering
* Sorting & Searching
* Business Rule Enforcement
* Modular Python Development

---

## Project Architecture

```text
CSV Data
    │
    ▼
Validation Engine
    │
    ▼
Data Cleaning Engine
    │
    ▼
Filtering & Search
    │
    ▼
Analytics Engine
    │
    ▼
Business Insights
    │
    ▼
Logging & Monitoring
```

---

## Features

### 1. Data Validation

Validates employee records against multiple business rules.

#### Name Validation

* Empty name detection
* Minimum length validation
* Maximum length validation
* Digit detection
* Special character detection
* Placeholder value detection

Examples:

```text
P@van
pk123
NULL
TEST
```

---

#### Employee ID Validation

* Empty ID detection
* Numeric validation
* Positive value validation
* Duplicate ID detection

Examples:

```text
a1
5ab
0
Duplicate IDs
```

---

#### Salary Validation

* Empty salary detection
* Numeric validation
* Negative salary detection
* Invalid salary format detection

Examples:

```text
abc
not_available
-2000
700,00
```

---

#### Experience Validation

* Empty experience detection
* Numeric validation
* Negative experience detection

Examples:

```text
-1
abc
```

---

#### Department Validation

Supported Departments:

```text
HR
IT
SALES
FINANCE
```

Detects:

* Empty departments
* Invalid department names
* Unknown departments

---

## 2. Data Cleaning

The cleaning module standardizes employee records.

### Name Cleaning

```text
" A r u n "
```

becomes

```text
Arun
```

---

### Employee ID Cleaning

```text
" 10 "
```

becomes

```text
10
```

---

### Salary Cleaning

```text
" 50000 "
```

becomes

```text
50000.0
```

---

### Department Cleaning

```text
" it "
```

becomes

```text
IT
```

---

### Experience Cleaning

```text
" 5 "
```

becomes

```text
5.0
```

---

## 3. Filtering Module

Supports multiple employee filters.

### Available Filters

* High Salary Employees
* Very High Salary Employees
* Low Salary Employees
* Department-wise Employees
* Experience-wise Employees
* High Salary IT Employees
* Experienced Finance Employees
* Junior HR Employees
* Employees Above Average Salary
* Employees Below Average Salary
* Employee Search By ID
* Employee Search By Name
* Employee Search By Exact Experience

---

## 4. Sorting Module

### Single Key Sorting

* Sort By Salary
* Sort By Name
* Sort By Experience

### Multi-Key Sorting

* Department + Experience
* Department + Salary + Experience

Supports:

```python
Ascending Order
Descending Order
```

---

## 5. Searching Module

### Department Search

```python
search_by_department()
```

### Salary Range Search

```python
search_by_salary_range()
```

### Experience Range Search

```python
search_by_experience_range()
```

---

## 6. Analytics Module

### KPI Analytics

Calculates:

* Total Employees
* Highest Salary
* Lowest Salary
* Average Salary
* Highest Experience
* Lowest Experience
* Average Experience

---

### Department Analytics

Calculates:

* Employee Count
* Average Salary
* Highest Salary
* Lowest Salary
* Average Experience

for every department.

---

### Business Insights

Identifies:

* Highest Paid Employee
* Lowest Paid Employee
* Most Experienced Employee
* Least Experienced Employee
* Department With Highest Average Salary
* Department With Lowest Average Salary
* Department With Most Employees
* Department With Least Employees

---

### Salary Distribution Analytics

Groups employees into:

```text
Low Salary Employees
Mid Salary Employees
High Salary Employees
```

based on configurable salary ranges.

---

## 7. Exception Handling

Custom Exceptions Implemented:

```python
InvalidDatasetError
InvalidInputError
InvalidRangeError
```

Used throughout the project to enforce business rules and improve error handling.

---

## 8. Logging Framework

Application activity is logged using Python's logging module.

Logged Events:

* Application Startup
* Data Loading
* Validation Execution
* Data Cleaning
* Analytics Execution
* Sorting Operations
* Searching Operations
* Error Events
* Application Shutdown

Example Log:

```text
2026-06-08 00:26:15 INFO analytics KPI mapping started
2026-06-08 00:26:15 INFO analytics KPI mapping completed
```

---

## Project Structure

```text
Smart-Data-Validation-Analytics-Engine/
│
├── Data/
│   └── employees.csv
│
├── validator.py
├── cleaner.py
├── filters.py
├── sorting_searching.py
├── analytics.py
├── exceptions.py
├── logger_config.py
├── main.py
│
├── project.log
│
└── README.md
```

---

## Technologies Used

* Python
* CSV Module
* Logging Module
* Exception Handling
* Dictionaries
* Lists
* List Comprehensions
* Hash Maps
* Modular Programming

---

## Learning Outcomes

This project demonstrates:

* Data Validation Techniques
* Data Cleaning Pipelines
* Logging Best Practices
* Exception Handling
* Business Analytics
* Python Data Structures
* Modular Software Design
* Real-World Data Processing Workflows

---

## Future Enhancements

* Excel Report Generation (openpyxl)
* Dashboard Visualization
* Pandas Integration
* SQL Database Support
* Automated Reporting
* REST API Integration
* Unit Testing
* Configuration Management

---

## Author

Pavan Kumar

Python | Data Engineering | Machine Learning | Software Development
