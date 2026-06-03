from exceptions import InvalidDatasetError, InvalidInputError, InvalidRangeError


def sort_by_salary(employee,order):
    if len(employee)==0:
       raise InvalidDatasetError("DataSet is Empty")
    if not isinstance(order,bool):
       raise InvalidInputError("order should be boolean")
       
    return sorted(employee,key=lambda x:x['salary'],reverse=order)


def sort_by_name(employee,order):
   if len(employee)==0:
      raise InvalidDatasetError("Dataset is Empty")
   if not isinstance(order,bool):
      raise InvalidInputError("order should be boolean")
   return sorted(employee,key=lambda x:x['name'],reverse=order)

def sort_by_experience(employee,order):
   if len(employee)==0:
      raise InvalidDatasetError("Dataset is Empty")
   if not isinstance(order,bool):
      raise InvalidInputError("order should be boolean")   
   return sorted(employee,key=lambda x:x['experience'],reverse=order)

def multi_key_sort_department_experience(employee,order):
   if len(employee)==0:
      raise InvalidDatasetError("Dataset is Empty")
   if not isinstance(order,bool):
      raise InvalidInputError("order should be boolean")   
   return sorted(employee,key=lambda x:(x['department'],x['experience']),reverse=order)

def multi_key_sort_department_salary_experience(employee,order):
   if len(employee)==0:
      raise InvalidDatasetError("Dataset is Empty")
   if not isinstance(order,bool):
      raise InvalidInputError("order should be boolean")
   return sorted(employee,key=lambda x:(x['department'],x['salary'],x['experience']),reverse=order)

def search_by_department(employee,department):
   if len(employee)==0:
      raise InvalidDatasetError("DataSet is Empty")
   
   available_departments={emp['department'] for emp in employee}
   if department not in available_departments:
      raise InvalidInputError("Department is not available")
    
   search_by_department_data=[emp for emp in employee if emp['department']==department]
   return search_by_department_data

def search_by_salary_range(employee,min_salary,max_salary):
   if len(employee)==0:
      raise InvalidDatasetError("Dataset Is Empty")
   
   if min_salary>max_salary:
      raise InvalidInputError("Minimum Salary Should Be less than Max Salary")
   
   if min_salary<0 or max_salary<0:
      raise InvalidRangeError("Min or Max Salary cannot be negative")
   
   search_by_salary_range_data=[emp for emp in employee if emp['salary']>=min_salary and emp['salary']<=max_salary ]
   return search_by_salary_range_data

def search_by_experience_range(employee,min_exp,max_exp):
   if len(employee)==0:
      raise InvalidDatasetError("Dataset Is Empty")
   
   if min_exp>max_exp:
      raise InvalidInputError("Minimum Experience Should Be less than Max Experience")
   
   if min_exp<0 or max_exp<0:
      raise InvalidRangeError("Experience range cannot contain negative values")   
   
   search_by_experience_range_data=[emp for emp in employee if emp['experience']>=min_exp and emp['experience']<=max_exp ]
   return search_by_experience_range_data

def top_n_highest_paid_employees(employee,n):
   if len(employee)==0:
      raise InvalidDatasetError("Dataset Is Empty")
   if n<=0:
      raise InvalidRangeError("N should be greater than zero")
   if n>len(employee):
      raise InvalidRangeError(f"Requested N exceeds dataset size as there are only {len(employee)} employees")
   sort_by_salary_data=sort_by_salary(employee,True)
   return sort_by_salary_data[:n]

def bottom_n_paid_employees(employee,n):
   if len(employee)==0:
      raise InvalidDatasetError("Dataset Is Empty")
   if n<=0:
      raise InvalidRangeError("N should be greater than zero")
   if n>len(employee):
      raise InvalidRangeError(f"Requested N exceeds dataset size as there are only {len(employee)} employees")  
   sort_by_salary_data=sort_by_salary(employee,False)
   return sort_by_salary_data[:n]

def top_n_most_experienced_employees(employee,n):
   if len(employee)==0:
      raise InvalidDatasetError("Dataset Is Empty")
   if n<=0:
      raise InvalidRangeError("N should be greater than zero")
   if n>len(employee):
      raise InvalidRangeError(f"Requested N exceeds dataset size as there are only {len(employee)} employees")
   sort_by_experience_data=sort_by_experience(employee,True)
   return sort_by_experience_data[:n]