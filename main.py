import csv

employee_data_path = r"C:\20LPA\Smart-Data-Validation-Analytics-Engine\Data\1_Raw_Data\employees.csv"

with open(employee_data_path, "r") as file:

    reader = csv.DictReader(file)

    data = [row for row in reader]

for employee in data:

    print(employee["id"])