def high_salary_employees(employee):
    #Salary Threshold for High Salary Employees
    salary_threshold=50000

    #Iterating through each employee and filtering out high paying employees
    high_salary_employees_data=[emp for emp in employee if emp['salary']>=salary_threshold]

    return high_salary_employees_data

def very_high_salary_employees(employee):
    #Salary Threshold for High Salary Employees
    salary_threshold=90000

    #Iterating through each employee and filtering out very high paying employees
    very_high_salary_employees_data=[emp for emp in employee if emp['salary']>=salary_threshold]

    return very_high_salary_employees_data

def low_salary_employees(employee):
    #salary Threshold
    salary_threshold=30000

    #Iterating through each employee and filtering out low paying employees
    low_salary_employees_data=[emp for emp in employee if emp['salary']<30000]

    return low_salary_employees_data

def department_filter_employees(employee):

    hashset=set()
    for emp in employee:
        hashset.add(emp['department'])

    hashmap=dict()

    for dep in hashset:
        list_of_employees=[emp for emp in employee if dep==emp['department']]
        hashmap[dep]=list_of_employees

    return hashmap

def experience_filter_employees(employee):

    hashmap=dict()

    list_of_fresher_employees=[emp for emp in employee if emp['experience']<=2]
    hashmap['Fresher']=list_of_fresher_employees

    list_of_midlevel_employees=[emp for emp in employee if emp['experience']>2 and emp['experience']<=5]
    hashmap['MidLevel']=list_of_midlevel_employees

    list_of_senior_employees=[emp for emp in employee if emp['experience']>5]
    hashmap['Senior']=list_of_senior_employees

    return hashmap

def high_salary_it_employees(employee):

    list_of_high_salary_it_employees=[emp for emp in employee if emp['department']=="IT"]

    return list_of_high_salary_it_employees

def experienced_finance_employees(employee):

    list_of_experienced_finance_employees_data=[emp for emp in employee if emp['department']=='FINANCE' and emp['experience']>=5]

    return list_of_experienced_finance_employees_data

def junior_hr_employees(employee):

    junior_hr_employees_data=[emp for emp in employee if emp['department']=='HR' and emp['experience']<=3]

    return junior_hr_employees_data

def employees_above_average_salary(employee):
    
    total_employees_salary=0
    total_employees_count=0

    for emp in employee:
        total_employees_salary+=emp['salary']
        total_employees_count+=1
    
    average_salary=total_employees_salary/total_employees_count

    employees_above_average_salary_data=[emp for emp in employee if emp['salary']>average_salary]

    return employees_above_average_salary_data

def employees_below_average_salary(employee):
    
    total_employees_salary=0
    total_employees_count=0

    for emp in employee:
        total_employees_salary+=emp['salary']
        total_employees_count+=1
    
    average_salary=total_employees_salary/total_employees_count

    employees_below_average_salary_data=[emp for emp in employee if emp['salary']<average_salary]

    return employees_below_average_salary_data

def employee_search_by_id(employee,employee_id):

    employee_search_by_id_data=[emp for emp in employee if employee_id==emp['id']]

    return employee_search_by_id_data

def employee_search_by_name(employee,employee_name):

    employee_name=employee_name.lower()

    employee_search_by_name_data=[emp for emp in employee if employee_name==emp['name'].lower()]

    return employee_search_by_name_data

def employee_search_with_exact_experience(employee,experience):

    employee_search_with_exact_experience_data=[emp for emp in employee if emp['experience']==experience]

    return employee_search_with_exact_experience_data

    




    
    

