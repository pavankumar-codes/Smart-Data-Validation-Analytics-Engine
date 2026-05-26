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
