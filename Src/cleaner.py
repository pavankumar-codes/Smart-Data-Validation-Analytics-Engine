def name_cleaner(employee_name):
    #Remove Leading/Trailing Spaces
    employee_name=employee_name.strip()

    #Remove multiple internal spaces
    employee_name_list=employee_name.split()
    employee_name="".join(employee_name_list)

    #Standardize Capitalization
    employee_name=employee_name.title()

    return employee_name

def employee_id_cleaner(employee_id):
    #Remove Leading/Trailing Spaces
    employee_id=employee_id.strip()

    #Remove Multuple Internal Spaces
    employee_id_list=employee_id.split()
    employee_id="".join(employee_id_list)

    #DataType Standardization
    employee_id=int(employee_id)

    return employee_id

def salary_cleaner(salary):
    #Remove Leading and Trailing Spaces
    salary=salary.strip()

    #Remove Multiple Internal Spaces
    salary_list=salary.split()
    salary="".join(salary_list)

    #DataType Standardization
    salary=float(salary)

    return salary

def department_cleaner(department):
    #Remove Leading and Trailing Spaces
    department=department.strip()

    #Remove Multiple internal Spaces
    department_list=department.split()
    department="".join(department_list)

    #Standard Capitalization
    department=department.upper()

    return department



def experience_cleaner(experience):
    #Remove Leading and Trailing Spaces
    experience=experience.strip()

    #Remove Multiple internal Spaces
    experience_list=experience.split()
    experience="".join(experience_list)

    #DataType Standardization
    experience=float(experience)

    return experience




    