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