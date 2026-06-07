# =========================
# validator.py
# =========================
import logging
from logger_config import *
logger = logging.getLogger(__name__)

def validate_name(name):

    errors = []

    # Datatype Validation
    if not isinstance(name, str):

        return ["Name should be string datatype"]

    # Remove Spaces
    name = name.strip()

    name=name.replace(" ", "")

    # Empty Validation
    if name == "":

        errors.append("Empty Name")

    # Minimum Length Validation
    if len(name) <= 2:

        errors.append("Name does not meet minimum length requirement")

    # Maximum Length Validation
    if len(name) > 100:

        errors.append("Name exceeded maximum length")

    # Fake Placeholder Validation
    if name.upper() in ["NA", "N/A", "NULL", "UNKNOWN", "TEST"]:

        errors.append("Invalid placeholder name detected")

    # Character Validation
    reject_digit_flag = False
    reject_special_flag = False

    for ch in name:

        # Allow Alphabets & Spaces
        if ch.isalpha() or ch.isspace():

            continue

        # Reject Digits
        elif ch.isdigit():

            if not reject_digit_flag:

                errors.append("Name should not contain digits")

                reject_digit_flag = True

        # Reject Special Characters
        else:

            if not reject_special_flag:

                errors.append("Name should not contain special characters")

                reject_special_flag = True

        # Stop Early If Both Errors Found
        if reject_digit_flag and reject_special_flag:

            break

    return errors if errors else None


# =====================================

def validate_id(emp_id):

    errors = []

    # Datatype Validation
    if not isinstance(emp_id, str):

        return ["ID should be string datatype"]

    emp_id = emp_id.strip()
    emp_id = emp_id.replace(" ","")

    # Empty Validation
    if emp_id == "":

        errors.append("ID cannot be empty")

        return errors

    # Numeric Validation
    if not emp_id.isdigit():

        errors.append("ID should contain only digits")

        return errors

    # Integer Conversion
    emp_id = int(emp_id)

    # Positive Validation
    if emp_id <= 0:

        errors.append("ID cannot be negative or zero")

    return errors if errors else None


# =====================================

def validate_duplicate_id(employee_ids):

    logger.info("Starting duplicate employee ID validation")

    hash_table = {}

    for emp_id in employee_ids:

        hash_table[emp_id] = hash_table.get(emp_id, 0) + 1

    duplicate_ids = [

        emp_id

        for emp_id, count in hash_table.items()

        if count > 1
    ]

    if len(duplicate_ids)==0:
        logger.info("No Duplicate Id's Found")
    else:
        logger.warning(f"Duplicate employee IDs detected. Count: {len(duplicate_ids)}")

    return duplicate_ids


# =====================================

def validate_salary(salary):

    errors = []

    # Datatype Validation
    if not isinstance(salary, str):

        return ["Salary should be string datatype"]

    salary = salary.replace(" ", "").strip()

    # Empty Validation
    if salary == "":

        errors.append("Salary should not be empty")

        return errors

    # Decimal Validation
    if salary.count(".") > 1:

        errors.append("Invalid salary format")

    # Numeric Conversion
    try:

        salary = float(salary)

    except ValueError:

        errors.append("Salary should be numeric")

        return errors

    # Business Validation
    if salary <= 0:

        errors.append("Salary cannot be negative or zero")

    return errors if errors else None


# =====================================

def validate_experience(experience):

    errors = []

    # Datatype Validation
    if not isinstance(experience, str):

        return ["Experience should be string datatype"]

    experience = experience.strip()
    experience=experience.replace(" ","")

    # Empty Validation
    if experience == "":

        errors.append("Experience should not be empty")

        return errors

    # Decimal Validation
    if experience.count(".") > 1:

        errors.append("Invalid experience format")

    # Numeric Conversion
    try:

        experience = float(experience)

    except ValueError:

        errors.append("Experience should be numeric")

        return errors

    # Business Validation
    if experience < 0:

        errors.append("Experience cannot be negative")

    return errors if errors else None


# =====================================

def validate_department(department):

    errors = []

    # Datatype Validation
    if not isinstance(department, str):

        return ["Department should be string datatype"]

    department = department.strip().upper()

    # Empty Validation
    if department == "":

        errors.append("Department should not be empty")

        return errors

    # Character Validation
    if not department.replace(" ", "").isalpha():

        errors.append("Department should contain only alphabets")

    # Domain Validation
    valid_departments = {
    "HR",
    "IT",
    "SALES",
    "FINANCE",
    "MARKETING",
    "OPERATIONS",
    "SUPPORT",
    "MANAGEMENT"
    }

    if department not in valid_departments:

        errors.append("Unknown Department")

    return errors if errors else None