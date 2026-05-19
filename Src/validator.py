def validate_name(name):

    errorbit = ""

    # Datatype Validation
    if not isinstance(name, str):

        return " - Name should be string datatype"

    # Remove Leading & Trailing Spaces
    name = name.strip()

    # Empty Name Validation
    if name == "":

        errorbit += " - Empty Name \n "

    # Minimum Length Validation
    if len(name) < 2:

        errorbit += " - Name does not meet minimum length requirement \n "

    # Maximum Length Validation
    if len(name) > 100:

        errorbit += " - Name exceeded maximum length \n "

    # Fake/Placeholder Value Validation
    if name.upper() in ["NA", "N/A", "NULL", "UNKNOWN", "TEST"]:

        errorbit += " - Invalid placeholder name detected \n "

    # Character-Level Validation
    reject_digit_flag = False
    reject_special_flag = False

    for ch in name:

        # Allow Alphabets & Spaces
        if ch.isalpha() or ch.isspace():

            continue

        # Reject Digits
        elif ch.isdigit():

            if not reject_digit_flag:

                errorbit += " - Name should not contain digits \n "

                reject_digit_flag = True

        # Reject Special Characters
        else:

            if not reject_special_flag:

                errorbit += " - Name should not contain special characters \n"

                reject_special_flag = True

        # Stop Loop If Both Errors Already Found
        if reject_digit_flag and reject_special_flag:

            break

    # Final Validation Result
    if errorbit == "":

        return None

    return errorbit


def validate_id(id):
    if not isinstance(id,str):
        return "Id Should Be Integer in String DataType"
    id=id.strip()

    if id=="":
        return "Id Cannot be empty"
    
    if not id.isdigit():
        return "Id can only be in Integer Format"
    
    try:
        id=int(id)
    except ValueError:
        return "Id Should Be Integer format"
    
    if id<0:
        return "Id Cannot Be Negative"

def validate_duplicate_id(id):
    hashtable=dict()
    for num in id:
        hashtable[num]=hashtable.get(num,0)+1
    duplicate_id=[num for num,count in hashtable.items() if count>1]
    unique_id=[num for num,count in hashtable.items() if count==1]

    return duplicate_id


def validate_salary(salary):
    if not isinstance(salary,str):
        return "Salary should be in String format but Integer values"
    
    salary=salary.replace(",","")

    if salary=="" or None:
        return "Salary should not be empty"
    
    if salary.count(".")>1:
        return "Invalid Salary Format"
    
    try:
        salary=float(salary)
    except ValueError:
        return "Invalid Salary Format"
    
    if salary<0:
        return "Salary Cannot be Negative"
    return None



def validate_experience(experience):
    if not isinstance(experience,str):
        return "Experience should be in String"
    experience=experience.strip()

    if experience=="":
        return "Experience should not be empty"
    
    if experience.count(".")>1:
        return "Experience in invalid format"
    
    try:
        experience=float(experience)
    except ValueError:
        return " Experience should be in Floating Values"
    
    if experience<0:
        return "experience cannot be negative"
    return None

def validate_department(department):
    if not isinstance(department,str):
        return "Department Should Be String"
    department=department.strip().upper()
    department=department.replace(" ","")

    if department=="":
        return "Department Should Not Be Empty"
    
    if not department.isalpha():
        return "Department should only be in Alphabets"
    
    if department not in {"HR","IT","SALES","FINANCE"}:
        return "Unknown Department"



            

    
    
