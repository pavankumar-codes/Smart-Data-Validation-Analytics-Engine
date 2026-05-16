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
        return "Id Should Not Be Empty"
    if id[0]=="-":
        return "Id should not be negative"
    if id=="0":
        return "Id cannot be Zero"
    if not id.isdigit():
        return "Id cannot be alphabets"
    return None

def validate_duplicate_id(id):
    hashtable=dict()
    for num in id:
        hashtable[num]=hashtable.get(num,0)+1
    duplicate_id=[num for num,count in hashtable.items() if count>1]
    unique_id=[num for num,count in hashtable.items() if count==1]

    return duplicate_id,unique_id




            

    
    
