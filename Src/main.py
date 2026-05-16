import csv
from validator import validate_name,validate_id,validate_duplicate_id


employee_data_path = r"C:\20LPA\Smart-Data-Validation-Analytics-Engine\Data\1_Raw_Data\employees.csv"

with open(employee_data_path, "r") as file:

    reader = csv.DictReader(file)
    data = [row for row in reader]

name_validation=[]
id_validation=[]
valid_id=[]
for employee in data:

    name_validation_data=validate_name(employee["name"])
    name_validation.append([employee["name"],name_validation_data])


    id_validation_data=validate_id(employee["id"])
    id_validation.append([employee["id"],id_validation_data])

    if id_validation_data is None:
        duplicate_id,unique_id=valid_id.append(employee["id"])
        print(duplicate_id)
        print(unique_id)






valid_names=[emp[0] for emp in name_validation if emp[1] is None]
invalid_names=[emp[0] for emp in name_validation if emp[1] is not None]

id_duplicate_data=validate_duplicate_id(valid_id)






