import pandas as pd
from datamodel.models import Enrolment

# the excel file
xls = None

# a dict to hold the pages within the excel file
ranks_in_dict = {}
# grades to exclude from the calculations
exception_grade = ['F', 'W', 'NCR']


def set_prereq_file(filename):
    """
    Sets the pre-req file to the global variable xls

        Param:
            filename : the file that is passed in
    """
    # refer to the global variables
    global xls, ranks_in_dict

    # parses the excel file
    xls = pd.ExcelFile(filename)
    df = xls.parse('Sheet1')

    # gets each column with the header as key, and following cells as list
    ranks_in_dict = df.to_dict(orient='list')


def get_rank_by_CH(student_number, student_enrolments=None):
    """
    returns the rank based on the credit hours that the student has

        Param:
            student_number : The student number to calculate the rank for
            student_enrolments : the enrolments related to the given student. If not given, it will query the db for it

        Return:
            the student rank based on the number of credit hours they have
    """

    # takes the first cell in each of these columns
    JUN_CH = ranks_in_dict['JUN'][0]
    SOP_CH = ranks_in_dict['SOP'][0]
    SEN_CH = ranks_in_dict['SEN'][0]

    # the CH counter
    total_ch = 0

    # queries the DB for student's enrolments if not given
    if student_enrolments is None:
        student_enrolments = Enrolment.objects.filter(
            student__student_number=student_number
        )

    for e in student_enrolments:
        if e.grade not in exception_grade:  # if they dint fail the class, count the CH
            total_ch += e.course.credit_hours

    # if the total credit hours are lower than the required credit hours, return that rank
    if total_ch <= JUN_CH:
        return 'JUN'
    elif total_ch <= SOP_CH:
        return 'SOP'
    elif total_ch <= SEN_CH:
        return 'SEN'


def get_rank_by_PREREQ(student_number, student_enrolments=None):
    """
    returns the rank based on a pre-req list of courses

        Param:
            student_number : The student number to calculate the rank for
            student_enrolments : the enrolments related to the given student. If not given, it will query the db for it

        Return:
            the student rank based on what courses they have PASSED
    """

    # queries the DB for student's enrolments if not given
    if student_enrolments is None:
        student_enrolments = Enrolment.objects.filter(
            student__student_number=student_number
        )

    # gets the number of courses needed for each rank (-1 to exclude the credit hours)
    JUN = len(ranks_in_dict["JUN"]) - 1
    SOP = len(ranks_in_dict["SOP"]) - 1

    # counter to count the number of courses within each rank
    jun_c, sop_c, sen_c = 0, 0, 0

    # to keep track of courses that are being taken more than once
    counted = set()

    for e in student_enrolments:
        # if the course code found is within the "JUN" column AND its hasn't been counted yet AND they din't fail the course, add a count to that rank counter
        if e.course.course_code in ranks_in_dict["JUN"] and e.course.course_code not in counted and e.grade not in exception_grade:
            counted.add(e.course.course_code)
            jun_c += 1
        elif e.course.course_code in ranks_in_dict["SOP"] and e.course.course_code not in counted and e.grade not in exception_grade:
            counted.add(e.course.course_code)
            sop_c += 1
        elif e.course.course_code in ranks_in_dict["SEN"] and e.course.course_code not in counted and e.grade not in exception_grade:
            counted.add(e.course.course_code)
            sen_c += 1

    if jun_c < JUN:
        return "JUN"
    elif sop_c < SOP:
        return "SOP"
    else:
        return "SEN"


def prereq_exist():
    """
    returns a boolean value of whether the pre-req excel file have been uploaded first

        Return:
            a boolean value of whether the pre-req excel file have been uploaded first
    """
    return xls != None
