from exceptions import InvalidDatasetError, InvalidInputError, InvalidRangeError
import logging
from logger_config import *

logger = logging.getLogger(__name__)
def sort_by_salary(employee, order):

    if len(employee) == 0:
        logger.error("Salary sorting failed: Dataset is empty")
        raise InvalidDatasetError("DataSet is Empty")

    if not isinstance(order, bool):
        logger.error("Salary sorting failed: Order should be boolean")
        raise InvalidInputError("order should be boolean")

    return sorted(employee, key=lambda x: x['salary'], reverse=order)


def sort_by_name(employee, order):

    if len(employee) == 0:
        logger.error("Name sorting failed: Dataset is empty")
        raise InvalidDatasetError("Dataset is Empty")

    if not isinstance(order, bool):
        logger.error("Name sorting failed: Order should be boolean")
        raise InvalidInputError("order should be boolean")

    return sorted(employee, key=lambda x: x['name'], reverse=order)


def sort_by_experience(employee, order):

    if len(employee) == 0:
        logger.error("Experience sorting failed: Dataset is empty")
        raise InvalidDatasetError("Dataset is Empty")

    if not isinstance(order, bool):
        logger.error("Experience sorting failed: Order should be boolean")
        raise InvalidInputError("order should be boolean")

    return sorted(employee, key=lambda x: x['experience'], reverse=order)


def multi_key_sort_department_experience(employee, order):

    if len(employee) == 0:
        logger.error("Department-Experience sorting failed: Dataset is empty")
        raise InvalidDatasetError("Dataset is Empty")

    if not isinstance(order, bool):
        logger.error("Department-Experience sorting failed: Order should be boolean")
        raise InvalidInputError("order should be boolean")

    return sorted(
        employee,
        key=lambda x: (x['department'], x['experience']),
        reverse=order
    )


def multi_key_sort_department_salary_experience(employee, order):

    if len(employee) == 0:
        logger.error("Department-Salary-Experience sorting failed: Dataset is empty")
        raise InvalidDatasetError("Dataset is Empty")

    if not isinstance(order, bool):
        logger.error("Department-Salary-Experience sorting failed: Order should be boolean")
        raise InvalidInputError("order should be boolean")

    return sorted(
        employee,
        key=lambda x: (
            x['department'],
            x['salary'],
            x['experience']
        ),
        reverse=order
    )


def search_by_department(employee, department):

    if len(employee) == 0:
        logger.error("Department search failed: Dataset is empty")
        raise InvalidDatasetError("DataSet is Empty")

    available_departments = {
        emp['department']
        for emp in employee
    }

    if department not in available_departments:
        logger.warning(
            f"Department search failed: {department} not found"
        )
        raise InvalidInputError("Department is not available")

    return [
        emp
        for emp in employee
        if emp['department'] == department
    ]


def search_by_salary_range(employee, min_salary, max_salary):

    if len(employee) == 0:
        logger.error("Salary range search failed: Dataset is empty")
        raise InvalidDatasetError("Dataset Is Empty")

    if min_salary > max_salary:
        logger.error("Salary range search failed: Invalid salary range")
        raise InvalidInputError(
            "Minimum Salary Should Be less than Max Salary"
        )

    if min_salary < 0 or max_salary < 0:
        logger.error("Salary range search failed: Negative salary range")
        raise InvalidRangeError(
            "Min or Max Salary cannot be negative"
        )

    return [
        emp
        for emp in employee
        if min_salary <= emp['salary'] <= max_salary
    ]


def search_by_experience_range(employee, min_exp, max_exp):

    if len(employee) == 0:
        logger.error("Experience range search failed: Dataset is empty")
        raise InvalidDatasetError("Dataset Is Empty")

    if min_exp > max_exp:
        logger.error("Experience range search failed: Invalid experience range")
        raise InvalidInputError(
            "Minimum Experience Should Be less than Max Experience"
        )

    if min_exp < 0 or max_exp < 0:
        logger.error("Experience range search failed: Negative experience range")
        raise InvalidRangeError(
            "Experience range cannot contain negative values"
        )

    return [
        emp
        for emp in employee
        if min_exp <= emp['experience'] <= max_exp
    ]


def top_n_highest_paid_employees(employee, n):

    if len(employee) == 0:
        logger.error("Top N highest paid employees failed: Dataset is empty")
        raise InvalidDatasetError("Dataset Is Empty")

    if n <= 0:
        logger.error("Top N highest paid employees failed: Invalid N")
        raise InvalidRangeError("N should be greater than zero")

    if n > len(employee):
        logger.error("Top N highest paid employees failed: N exceeds dataset size")
        raise InvalidRangeError(
            f"Requested N exceeds dataset size as there are only {len(employee)} employees"
        )

    return sort_by_salary(employee, True)[:n]


def bottom_n_paid_employees(employee, n):

    if len(employee) == 0:
        logger.error("Bottom N paid employees failed: Dataset is empty")
        raise InvalidDatasetError("Dataset Is Empty")

    if n <= 0:
        logger.error("Bottom N paid employees failed: Invalid N")
        raise InvalidRangeError("N should be greater than zero")

    if n > len(employee):
        logger.error("Bottom N paid employees failed: N exceeds dataset size")
        raise InvalidRangeError(
            f"Requested N exceeds dataset size as there are only {len(employee)} employees"
        )

    return sort_by_salary(employee, False)[:n]


def top_n_most_experienced_employees(employee, n):

    if len(employee) == 0:
        logger.error("Top N experienced employees failed: Dataset is empty")
        raise InvalidDatasetError("Dataset Is Empty")

    if n <= 0:
        logger.error("Top N experienced employees failed: Invalid N")
        raise InvalidRangeError("N should be greater than zero")

    if n > len(employee):
        logger.error("Top N experienced employees failed: N exceeds dataset size")
        raise InvalidRangeError(
            f"Requested N exceeds dataset size as there are only {len(employee)} employees"
        )

    return sort_by_experience(employee, True)[:n]