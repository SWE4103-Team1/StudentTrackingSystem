# import prerequisite table from datamodel
from datamodel.models import Student, Enrolment

# To be removed
prereq = {
    "MATH*1003": "FIR",
    "MATH*1503": "FIR",
    "CS*1073": "FIR",
    "PHSY*1081": "FIR",
    "ENGG*1003": "FIR",
    "ENGG*1015": "FIR",
    "ENGG*1001": "FIR",
    "CS*1083": "SOP",
    "CS*2043": "SOP",
    "CS*1303": "SOP",
    "CS*2613": "SOP",
    "ECE*2701": "SOP",
    "ECE*2214": "SOP",
    "ECE*2215": "SOP",
    "CS*2333": "SOP",
    "STAT*2593": "SOP",
    "ECE*2412": "SOP",
    "CS*3113": "JUN",
    "CE*3963": "JUN",
    "ME*3232": "JUN",
    "CS*2263": "JUN",
    "CS*2383": "JUN",
    "ECE*3221": "JUN",
    "SWE*4103": "JUN",
    "SWE*4403": "SEN",
    "CS*3503": "SEN",
    "ECE*3232": "SEN",
    "ECE*3242": "SEN",
    "ENGG*4000": "SEN",
    "CS*3383": "SEN",
    "CS*3413": "SEN",
    "CS*3873": "SEN",
    "ECE*3812": "SEN",
    "SWE*4203": "SEN",
    "ENGG*4013": "SEN",
}


def calculateRank(student_number, student_enrolments=None):
    if student_enrolments is None:
        student_enrolments = Enrolment.objects.filter(
            student__student_number=student_number
        )

    # keeps the count of number of pre-reqs in each ranks
    FIR_count, JUN_count, SOP_count, SEN_count = 0, 0, 0, 0
    FIR, JUN, SOP, SEN = 0, 0, 0, 0

    # this for loop goes through the pre-req table to get the ranks of each course and add it to the count of the rank
    for course in prereq.values():
        if course == "FIR":
            FIR_count += 1
        elif course == "JUN":
            JUN_count += 1
        elif course == "SOP":
            SOP_count += 1
        elif course == "SEN":
            SEN_count += 1

    # return the coresponding rank depending on whether they completed all the courses in that rank
    # EX: if the student's courses with the rank of 'FIR' is the same length as the FIR pre-req length, then return FIR
    # EX: if the student needs 1 more FIR course, but completed all JUN courses, it will still return as first year since they are still missing FIR courses
    for e in student_enrolments:
        if e.course.course_code in prereq and (prereq[e.course.course_code] == "FIR"):
            FIR += 1
        elif e.course.course_code in prereq and (prereq[e.course.course_code] == "JUN"):
            JUN += 1
        elif e.course.course_code in prereq and (prereq[e.course.course_code] == "SOP"):
            SOP += 1
        elif e.course.course_code in prereq and (prereq[e.course.course_code] == "SEN"):
            SEN += 1

    if FIR < FIR_count:
        return "FIR"
    elif JUN < JUN_count:
        return "JUN"
    elif SOP < SOP_count:
        return "SOP"
    elif SEN <= SEN_count:
        return "SEN"
    else:
        return ""
