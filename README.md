# Smart Data Validation & Analytics Engine v1.0

## Overview

The Smart Data Validation & Analytics Engine is a Python-based data processing and analytics platform designed to validate, clean, analyze, search, sort, and generate business-ready reports from employee datasets.

The system automatically transforms raw CSV employee data into validated datasets, business insights, KPI analytics, and Excel reports.

---

## Project Architecture

```text
Raw CSV Data
      │
      ▼
Validation Engine
      │
      ▼
Data Cleaning Engine
      │
      ▼
Filtering & Search Engine
      │
      ▼
Analytics Engine
      │
      ▼
Business Insights Engine
      │
      ▼
Excel Reporting Engine
```

---

## Example Input Dataset

employees.csv

```csv
id,name,salary,department,experience
1,Pavan,75000,IT,4
2,Sanjay,95000,Finance,7
3,NULL,50000,HR,3
4,Rahul123,abc,IT,-1
```

---

## Validation Example

### Invalid Records Detected

```text
Employee ID : 3

Errors:
- Invalid placeholder name detected
```

```text
Employee ID : 4

Errors:
- Name should not contain digits
- Salary should be numeric
- Experience cannot be negative
```

---

## Data Cleaning Example

Before Cleaning

```text
{
    "id": " 10 ",
    "name": " A r u n ",
    "salary": " 50000 ",
    "department": " it ",
    "experience": " 5 "
}
```

After Cleaning

```text
{
    "id": 10,
    "name": "Arun",
    "salary": 50000.0,
    "department": "IT",
    "experience": 5.0
}
```

---

## Analytics Generated

### Global KPI Analytics

```text
Highest Salary      : 95000
Lowest Salary       : 30000
Average Salary      : 67500
Highest Experience  : 10
Lowest Experience   : 1
Average Experience  : 4.8
```

---

### Department Analytics

Example:

```text
IT
Employee Count      : 3
Average Salary      : 72000
Highest Salary      : 95000
Lowest Salary       : 50000
Average Experience  : 4.3
```

---

### Business Insights

```text
Highest Paid Employee:
Sanjay - Finance - 95000
```

```text
Lowest Paid Employee:
Karthik - HR - 30000
```

```text
Most Experienced Employee:
Mohan - IT - 10 Years
```

```text
Least Experienced Employee:
Rahul - HR - 1 Year
```

---

### Department Insights

```text
Department With Highest Average Salary:
Finance
```

```text
Department With Lowest Average Salary:
HR
```

```text
Department With Most Employees:
IT
```

```text
Department With Least Employees:
Sales
```

---

### Salary Distribution Analytics

```text
Low Salary Employees  : 2
Mid Salary Employees  : 8
High Salary Employees : 4
```

---

## Excel Reports Generated

The system automatically generates the following reports:

### Cleaned Valid Data Report

Contains all cleaned employee records.

### Invalid Data Report

Contains invalid employee records and validation errors.

### Global KPI Report

Contains organization-wide KPI metrics.

### Department Analytics Report

Contains department-wise analytics.

### Business Insights Report

Contains employee-level business insights.

### Department Insights Report

Contains department-level business insights.

### Salary Distribution Analytics Report

Contains salary category summaries and employee distributions.

### Executive Summary Report

Management-level dashboard report containing:

* Total Records
* Valid Records
* Invalid Records
* Validation Success Rate
* Salary KPIs
* Experience KPIs
* Department Statistics

---

## Generated Folder Structure

```text
Smart-Data-Validation-Analytics-Engine

│
├── Data
│   │
│   ├── 1_Raw_Data
│   │   └── employees.csv
│   │
│   ├── 2_Valid_Data
│   │   └── Cleaned_Valid_Data.xlsx
│   │
│   ├── 3_Invalid_Data
│   │   └── Invalid_Data.xlsx
│   │
│   └── 4_Data_Analytics
│       ├── Global_KPI_Report.xlsx
│       ├── Department_Analytics_Report.xlsx
│       ├── Business_Insights_Report.xlsx
│       ├── Department_Insights_Report.xlsx
│       ├── Salary_Distribution_Analytics_Report.xlsx
│       └── Executive_Summary_Report.xlsx
│
├── validator.py
├── cleaner.py
├── filters.py
├── sorting_searching.py
├── analytics.py
├── report_generator.py
├── exceptions.py
├── logger_config.py
├── main.py
│
└── README.md
```

---

## Technologies Used

* Python
* CSV Module
* OpenPyXL
* Logging
* Exception Handling
* Dictionaries
* Lists
* Hash Maps
* Sorting Algorithms
* Searching Algorithms
* Data Validation
* Data Cleaning
* Business Analytics
* Excel Automation

---

## Skills Demonstrated

* Data Validation
* Data Cleaning
* Data Transformation
* Data Analytics
* Business Intelligence
* Exception Handling
* Logging
* Excel Automation
* Modular Python Development
* Sorting & Searching Algorithms

---

## Future Enhancements

* Pandas Integration
* SQL Database Integration
* Automated Scheduling
* Dashboard Development
* Cloud Deployment
* PySpark Integration
* Databricks Integration

---

## Author

Pavan Kumar

Data Engineer | Driver Drowsiness Detection (DDD)

Bosch Global Software Technologies
