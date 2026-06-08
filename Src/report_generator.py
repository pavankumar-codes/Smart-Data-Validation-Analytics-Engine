import openpyxl
import os

from exceptions import InvalidDatasetError

def generate_cleaned_valid_data_report(employee):

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Cleaned_Data"

    if len(employee) == 0:
        raise InvalidDatasetError("Cleaned Valid Dataset is Empty")

    sheet.append(list(employee[0].keys()))

    for emp in employee:
        sheet.append(list(emp.values()))

    folder_path = os.path.join(
        os.getcwd(),
        'Data',
        '2_Valid_Data'
    )

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    cleaned_valid_data_report_path = os.path.join(
        folder_path,
        'Cleaned_Valid_Data.xlsx'
    )

    wb.save(cleaned_valid_data_report_path)

def generate_invalid_data_report(employee):
    wb=openpyxl.Workbook()
    sheet=wb.active
    sheet.title = "Invalid_Data"

    if len(employee) == 0:
        raise InvalidDatasetError("InValid Dataset is Empty")
    
    header=list(employee[0]['employee'].keys())
    header.append('errors')
    sheet.append(header)

    for emp in employee:
        values=list(emp['employee'].values())
        error_string=", ".join(emp['errors'])
        values.append(error_string)
        sheet.append(values)
    #for emp in employee:
        #sheet.append(list(emp['employee'].values()))
    #sheet.cell(row=1,column=1,value="id")
    #sheet.cell(row=1,column=2,value="name")
    #sheet.cell(row=1,column=3,value="salary")
    #sheet.cell(row=1,column=4,value="department")
    #sheet.cell(row=1,column=5,value="experience")
    #sheet.cell(row=1,column=6,value="errors")
    #row=2
    #for emp in employee:
        #sheet.cell(row=row,column=1,value=emp['employee']['id'])
        #sheet.cell(row=row,column=2,value=emp['employee']['name'])
        #sheet.cell(row=row,column=3,value=emp['employee']['salary'])
        #sheet.cell(row=row,column=4,value=emp['employee']['department'])
        #sheet.cell(row=row,column=5,value=emp['employee']['experience'])
        #error_string=",".join(emp['errors'])
        #sheet.cell(row=row,column=6,value=error_string)
        #row+=1
    folder_path=os.path.join(os.getcwd(),'Data','3_Invalid_Data')
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    invalid_data_report_path=os.path.join(folder_path,'Invalid_Data.xlsx')
    
    wb.save(invalid_data_report_path)
   
def generate_global_kpi_report(global_kpi_report):
    wb=openpyxl.Workbook()
    sheet=wb.active
    sheet.title='Global_KPI_Report'
    
    if len(global_kpi_report)==0:
        raise InvalidDatasetError("Global KPI Dataset is Empty")
    sheet.cell(row=1,column=1,value='KPI')
    sheet.cell(row=1,column=2,value='Value')
    row=2
    row_column=1
    column=2
    for key,value in global_kpi_report.items():
        sheet.cell(row=row,column=row_column,value=key)
        sheet.cell(row=row,column=column,value=value)
        row+=1
    folder_path = os.path.join(
        os.getcwd(),
        'Data',
        '4_Data_Analytics'
    )

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    global_kpi_report_path = os.path.join(
        folder_path,
        'Global_KPI_Report.xlsx'
    )

    wb.save(global_kpi_report_path)