def sort_by_salary(employee,order):
    if len(employee)==0:
       raise ValueError("DataSet is Empty")
    if not isinstance(order,bool):
       raise ValueError("order should be boolean")
       
    return sorted(employee,key=lambda x:x['salary'],reverse=order)


def sort_by_name(employee,order):
   return sorted(employee,key=lambda x:x['name'],reverse=order)

def sort_by_experience(employee,order):
   return sorted(employee,key=lambda x:x['experience'],reverse=order)

def multi_key_sort_department_experience(employee,order):
   return sorted(employee,key=lambda x:(x['department'],x['experience']),reverse=order)

def multi_key_sort_department_salary_experience(employee,order):
   return sorted(employee,key=lambda x:(x['department'],x['salary'],x['experience']),reverse=order)

def search_by_department(employee,department):
   search_by_department_data=[emp for emp in employee if emp['department']==department]
   return search_by_department_data

def search_by_salary_range(employee,min_salary,max_salary):
   search_by_salary_range_data=[emp for emp in employee if emp['salary']>=min_salary and emp['salary']<=max_salary ]
   return search_by_salary_range_data

def search_by_experience_range(employee,min_exp,max_exp):
   search_by_experience_range_data=[emp for emp in employee if emp['experience']>=min_exp and emp['experience']<=max_exp ]
   return search_by_experience_range_data

def top_n_highest_paid_employees(employee,n):
   sort_by_salary_data=sort_by_salary(employee,True)
   return sort_by_salary_data[:n]

def bottom_n_paid_employees(employee,n):
   sort_by_salary_data=sort_by_salary(employee,False)
   return sort_by_salary_data[:n]

def top_n_most_experienced_employees(employee,n):
   sort_by_experience_data=sort_by_experience(employee,True)
   return sort_by_experience_data[:n]