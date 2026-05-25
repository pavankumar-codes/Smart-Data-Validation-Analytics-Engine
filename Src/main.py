# =========================
# main.py
# =========================

import csv

from validator import (

    validate_name,
    validate_id,
    validate_duplicate_id,
    validate_salary,
    validate_experience,
    validate_department
)

from cleaner import (
    name_cleaner,
    employee_id_cleaner,
    salary_cleaner,
    department_cleaner,
    experience_cleaner
    )

from filters import (
    high_salary_employees,
    very_high_salary_employees,
    low_salary_employees,
    department_filter_employees,
    experience_filter_employees,
    high_salary_it_employees,
    experienced_finance_employees,
    junior_hr_employees,
    employees_above_average_salary,
    employees_below_average_salary,
    employee_search_by_id,
    employee_search_by_name,
    employee_search_with_exact_experience
)


# CSV File Path
employee_data_path = r"C:\20LPA\Smart-Data-Validation-Analytics-Engine\Data\1_Raw_Data\employees.csv"

# Read CSV Data
with open(employee_data_path, "r") as file:

    reader = csv.DictReader(file)

    data = [row for row in reader]

# Store Final Outputs
valid_data = []

invalid_data = []

# Collect All IDs
all_employee_ids = []

for employee in data:

    all_employee_ids.append(employee["id"])

# Detect Duplicate IDs
duplicate_ids = validate_duplicate_id(all_employee_ids)

# =========================
# VALIDATION LOOP
# =========================

for employee in data:

    errors = []

    # Extract Fields
    employee_name = employee["name"]

    employee_id = employee["id"]

    employee_salary = employee["salary"]

    employee_experience = employee["experience"]

    employee_department = employee["department"]

    # Run Validators
    name_errors = validate_name(employee_name)

    id_errors = validate_id(employee_id)

    salary_errors = validate_salary(employee_salary)

    experience_errors = validate_experience(employee_experience)

    department_errors = validate_department(employee_department)

    # Collect Errors
    if name_errors:

        errors.extend(name_errors)

    if id_errors:

        errors.extend(id_errors)

    if salary_errors:

        errors.extend(salary_errors)

    if experience_errors:

        errors.extend(experience_errors)

    if department_errors:

        errors.extend(department_errors)

    # Duplicate ID Validation
    if employee_id in duplicate_ids:

        errors.append("Duplicate Employee ID Detected")

    # Separate Valid & Invalid Data
    if len(errors) == 0:

        valid_data.append(employee)

    else:

        invalid_data.append({

            "employee": employee,

            "errors": errors
        })

# =========================
# OUTPUT SECTION
# =========================

print("\n================ VALID RECORDS ================\n")

for employee in valid_data:

    print(employee)

print("\nTotal Valid Records :", len(valid_data))

print("\n================ INVALID RECORDS ================\n")

for item in invalid_data:

    print("Employee Record :")

    print(item["employee"])

    print("\nErrors Found :")

    for error in item["errors"]:

        print(" -", error)

    print("\n-------------------------------------------\n")

print("Total Invalid Records :", len(invalid_data))

print("\n-------------------------------------------\n")

#Store Final Cleaned Valid Data
cleaned_valid_data=[]



for employee in valid_data:

    #Cleaned Employee Information In Dict
    cleaned_employee_info=dict()

    #Extract Fields
    employee_name=employee["name"]

    employee_id=employee["id"]

    employee_salary=employee["salary"]

    employee_department=employee["department"]

    employee_experience=employee["experience"]


    #Cleaning Data
    cleaned_employee_name=name_cleaner(employee_name)

    cleaned_employee_id=employee_id_cleaner(employee_id)

    cleaned_employee_salary=salary_cleaner(employee_salary)

    cleaned_employee_department=department_cleaner(employee_department)

    cleaned_employee_experience=experience_cleaner(employee_experience)

    #Adding Information as Dictionary
    cleaned_employee_info["id"]=cleaned_employee_id

    cleaned_employee_info["name"]=cleaned_employee_name

    cleaned_employee_info["salary"]=cleaned_employee_salary

    cleaned_employee_info["department"]=cleaned_employee_department

    cleaned_employee_info["experience"]=cleaned_employee_experience

    #Appending Cleaned Valid Data To a List
    cleaned_valid_data.append(cleaned_employee_info)


print("\n================ CLEANED VALID RECORDS ================\n")

for employee in cleaned_valid_data:
    print("Employee Record : ")
    print(employee)
    print("\n")

#High Salary Employees Data
high_salary_employees_data=high_salary_employees(cleaned_valid_data)

#Very High Salary Employees Data
very_high_salary_employees_data=very_high_salary_employees(cleaned_valid_data)

#Low Salary Employees Data
low_salary_employees_data=low_salary_employees(cleaned_valid_data)


#Employees by department
employees_by_department_data=department_filter_employees(cleaned_valid_data)

#Employees by Experience
employees_by_experience_data=experience_filter_employees(cleaned_valid_data)

#High Salary IT employees
high_salary_it_employees_data=high_salary_it_employees(high_salary_employees_data)

#Experienced Finance Employees
experienced_finance_employees_data=experienced_finance_employees(cleaned_valid_data)

#Junior Hr Employees
junior_hr_employees_data=junior_hr_employees(cleaned_valid_data)

#Employees Above Average Salary
employees_above_average_salary_data=employees_above_average_salary(cleaned_valid_data)

#Employees Below Average Salary
employees_below_average_salary_data=employees_below_average_salary(cleaned_valid_data)

#Employee Search By Id
employee_search_by_id_data=employee_search_by_id(cleaned_valid_data,12)

#Employee Search By Names
employee_search_by_name_data=employee_search_by_name(cleaned_valid_data,'Sanjay')

#Employees With Exact Experience Condition
employee_search_with_exact_experience_data=employee_search_with_exact_experience(cleaned_valid_data,5)













