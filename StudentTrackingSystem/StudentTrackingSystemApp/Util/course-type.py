import pandas as pd

#The excel file to read in
xls_file = pd.ExcelFile("SWEProgram.xlsx")

course_group = pd.read_excel(xls_file, sheet_name="course-groups").to_dict(orient="list")
exceptions = pd.read_excel(xls_file, sheet_name="exceptions").to_dict(orient="list")
valid_tags = pd.read_excel(xls_file, sheet_name="valid-tags").to_dict(orient="list")

def validate_tag(course_code):
    """
    check if the given course_code exist within the "valid-tag" page of the excel file
        Param:
            course_code : the course code of the course
        Return:
            returns the column header
    """
    #takes the prefix of the course code (EX: SWE4103 -> SWE)
    course_tag = get_course_tag(course_code)
    for key,value in valid_tags.items():
        #for each item, if the prefix is in valid-tag or the entire course code (only for CSE-ITS)
        #return the key (course type)
        if course_tag in value or course_code in value:
            return key
    return None


def is_exception(course_code, course_type):
    """
    Checks if the given course_code is in the column of the exception page
    
        Param:
            course_code : the course code 
            course_type : the course type

        Return:
            Returns a true boolean value if the course type exist and contains the given course code
            else returns false if the course type exist and DOES NOT contains the given course code

            Returns None of the given course_code does not have a valid tag
    """
    # if the given course_tag is not a valid tag
    if course_type is None:
        return None

    if course_code in exceptions[course_type]:
        return True
    else:
        return False

def get_course_tag(course_code):
    """
    Gets the prefix of the course code (EX: SWE4103 -> SWE)
    
        Param:
            course_code : the course code to get the prefix of

        Return:
            the course tag (EX: given 'SWE4103', it will return 'SWE')
    """
    course_tag = ""
    i = 0
    # takes all characters up to the first digit in the course code
    while course_code is not None and i < len(course_code) and not course_code[i].isdigit():
        course_tag += course_code[i]
        i += 1
    return course_tag

def is_course_group(course_code):
    """
    Returns the course_type if it is found within the 'course-groups' page

        Param:
            course_code : the course code

        Return:
            the course type if the given course code is found within the 'course-groups' page
    """
    for key,value in course_group.items():
        if course_code in value:
            return key
    return None



##########################################
# The only function needed to be called 
##########################################
def get_course_type (course_code):
    """
    Gets the course type

        Param:
            course_code : the course code

        Return:
            the course type of the given course
    """

    #if is valid tag, and is not in exception, return course type
    if validate_tag(course_code) == "NS" and not is_exception(course_code, "NS"):
        return "SCIENCE"
    
    elif validate_tag(course_code) == "CSE-ITS" and not is_exception(course_code, "CSE-ITS"):
        return "CSE-ITS"

    elif validate_tag(course_code) == "CSE-HSS" and not is_exception(course_code,"CSE-HSS"):
        return "CSE-HSS"

    elif validate_tag(course_code) == "CSE-OPEN" and not is_exception(course_code, "CSE-OPEN"):
        return "CSE-OPEN"

    else:
        #gets the course type from within 'course-groups' page if the given course code is found
        course_group = is_course_group(course_code)
        #since it can't validate_tag, check if course is in course_group
        if course_group is not None:
                return course_group
        else:
            return None




