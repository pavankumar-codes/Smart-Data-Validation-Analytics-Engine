from exceptions import InvalidDatasetError, InvalidInputError, InvalidRangeError


def department_employee_count(employee):
    hashmap=dict()
    for emp in employee:
        hashmap[emp['department']]=hashmap.get(emp['department'],0)+1
    return hashmap


def salary_mapping(employee):

    hashmap=dict()
    for emp in employee:
        hashmap[emp['id']]=emp['salary']
    return hashmap
        
def name_mapping(employee):
    hashmap=dict()
    for emp in employee:
        hashmap[emp['id']]=emp['name']
    return hashmap

def department_salary_mapping(employee):
    hashmap=dict()
    for emp in employee:
        if emp['department'] not in hashmap:
            hashmap[emp['department']]=[]
        hashmap[emp['department']].append(emp['salary'])
    return hashmap

def department_experience_mapping(employee):
    hashmap={}
    for emp in employee:
        if emp['department'] not in hashmap:
            hashmap[emp['department']]=[]
        hashmap[emp['department']].append(emp['experience'])
    return hashmap

def kpi_mapping(employee):

    hashmap=dict()
    
    total_employees=len(employee)

    total_salary=0
    total_experience=0
    if len(employee)==0:
        raise InvalidDatasetError("Employee Dataset Is Empty")
    empl=employee[0]
    highest_salary=empl['salary']
    lowest_salary=empl['salary']
    highest_experience=empl['experience']
    lowest_experience=empl['experience']
    for emp in employee:
        total_salary+=emp['salary']
        total_experience+=emp['experience']
        
        if highest_salary<emp['salary']:
            highest_salary=emp['salary']

        if lowest_salary>emp['salary']:
            lowest_salary=emp['salary']

        if highest_experience<emp['experience']:
            highest_experience=emp['experience']
        
        if lowest_experience>emp['experience']:
            lowest_experience=emp['experience']
        
        average_salary=total_salary/total_employees
        average_experience=total_experience/total_employees

    hashmap['total_employees']=total_employees
    hashmap['highest_salary']=highest_salary
    hashmap['lowest_salary']=lowest_salary
    hashmap['highest_experience']=highest_experience
    hashmap['lowest_experience']=lowest_experience
    hashmap['average_salary']=average_salary
    hashmap['average_experience']=average_experience
    return hashmap

def department_analytics_mapping(employee):

    if len(employee)==0:
        raise InvalidDatasetError("Employee DataSet is Empty")

    department_wise_employee_count=department_employee_count(employee)

    department_wise_salary_mapping=department_salary_mapping(employee)
    department_wise_avg_salary_mapping=dict()
    department_wise_highest_salary=dict()
    department_wise_lowest_salary=dict()

    department_wise_exp_mapping=department_experience_mapping(employee)
    department_wise_average_experience=dict()


    for key,value in department_wise_salary_mapping.items():
        total_salary=0
        for salary in value:
            total_salary+=salary
        avg_salary=total_salary/len(value)
        department_wise_avg_salary_mapping[key]=avg_salary
    
    for key,value in department_wise_salary_mapping.items():
        highest_salary=0
        lowest_salary=999999999
        for salary in value:
            if highest_salary<salary:
                highest_salary=salary
            if lowest_salary>salary:
                lowest_salary=salary
        department_wise_highest_salary[key]=highest_salary
        department_wise_lowest_salary[key]=lowest_salary
    
    for key,value in department_wise_exp_mapping.items():
        total_exp=0
        for exp in value:
            total_exp+=exp
        avg_exp=total_exp/len(value)
        department_wise_average_experience[key]=avg_exp

    hashmap=dict()
    for emp in employee:
        if emp['department'] not in hashmap:
            hashmap[emp['department']]=dict()

    for department in hashmap:
        hashmap[department].update({'employee_count':department_wise_employee_count[department]})
        hashmap[department].update({'average_salary':department_wise_avg_salary_mapping[department]})
        hashmap[department].update({'highest_salary':department_wise_highest_salary[department]})
        hashmap[department].update({'lowest_salary':department_wise_lowest_salary[department]})
        hashmap[department].update({'average_experience':department_wise_average_experience[department]})

    return hashmap


def highest_paid_employee(employee):
    kpi_data=kpi_mapping(employee)
    highest_paid_employee=[emp for emp in employee  if emp['salary']==kpi_data['highest_salary']]
    return highest_paid_employee

def lowest_paid_employee(employee):
    kpi_data=kpi_mapping(employee)
    lowest_paid_employee=[emp for emp in employee  if emp['salary']==kpi_data['lowest_salary']]
    return lowest_paid_employee

def most_experienced_employee(employee):
    kpi_data=kpi_mapping(employee)
    most_experienced_employee=[emp for emp in employee  if emp['experience']==kpi_data['highest_experience']]
    return most_experienced_employee

def least_experienced_employee(employee):
    kpi_data=kpi_mapping(employee)
    least_experienced_employee=[emp for emp in employee  if emp['experience']==kpi_data['lowest_experience']]
    return least_experienced_employee

def department_with_highest_average_salary(employee):
    department_insights=department_analytics_mapping(employee)
    highest_average_salary=0
    department_with_highest_average_salary_data=[]
    for key,value in department_insights.items():
        if highest_average_salary<value['average_salary']:
            highest_average_salary=value['average_salary']
    for key,value in department_insights.items():
        if value['average_salary']==highest_average_salary:
            department_with_highest_average_salary_data.append(key)
    return department_with_highest_average_salary_data

def department_with_lowest_average_salary(employee):
    department_insights=department_analytics_mapping(employee)
    lowest_average_salary=99999999999
    for key,value in department_insights.items():
        if lowest_average_salary>value['average_salary']:
            lowest_average_salary=value['average_salary']
    department_with_lowest_average_salary_data=[key for key,value in department_insights.items() if value['average_salary']==lowest_average_salary ]
    return department_with_lowest_average_salary_data

def department_with_most_employees(employee):
    department_insights=department_analytics_mapping(employee)
    most_count=0
    for key,value in department_insights.items():
        if most_count<value['employee_count']:
            most_count=value['employee_count']
    department_with_most_employees_data=[key for key,value in department_insights.items() if value['employee_count']==most_count]
    return department_with_most_employees_data

def department_with_least_employees(employee):
    department_insights=department_analytics_mapping(employee)
    least_count=99999999999
    for key,value in department_insights.items():
        if least_count>value['employee_count']:
            least_count=value['employee_count']
    department_with_least_employees_data=[key for key,value in department_insights.items() if value['employee_count']==least_count]
    return department_with_least_employees_data

def salary_distribution_analytics(employee,lowsalary,highsalary):
    if len(employee)==0:
        raise InvalidDatasetError("DataSet Is Empty")
    if (lowsalary>highsalary):
        raise InvalidInputError("Low Salary is greater than high salary")
    if ((lowsalary<=0) or (highsalary<=0)):
        raise InvalidRangeError("Salary cannot be negative")

    hashmap=dict()
    hashmap['low_salary_employees']=[]
    hashmap['mid_salary_employees']=[]
    hashmap['high_salary_employees']=[]
    for emp in employee:
        if emp['salary']<=lowsalary:
            hashmap['low_salary_employees'].append(emp)
        elif emp['salary']>lowsalary and emp['salary']<=highsalary:
            hashmap['mid_salary_employees'].append(emp)
        else:
            hashmap['high_salary_employees'].append(emp)
    return hashmap

    

    




            
        





        



