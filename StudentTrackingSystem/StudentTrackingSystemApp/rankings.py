# import prerequisite table from datamodel
from datamodel.models import Student, Enrolment

# To be removed
prereq = {
    'MATH*1003': 'FIR',
    'MATH*1503': 'FIR',
    'CS*1073': 'FIR',
    'PHSY*1081': 'FIR',
    'ENGG*1003': 'FIR',
    'ENGG*1015': 'FIR',
    'ENGG*1001':  'FIR',
    'MATH*1013': 'FIR',
    'INFO*1103': 'FIR',
    'CS*1083': 'FIR',
    'ECE*1813': 'FIR',
    'CHEM*1982': 'FIR',
    'CHEM*1987': 'FIR',
    'CS*2043': 'SOP',
    'CS*1303': 'SOP',
    'CS*2613': 'SOP',
    'ECE*2701': 'SOP',
    'ECE*2214': 'SOP',
    'ECE*2215': 'SOP',
    'CS*2333': 'SOP',
    'STAT*2593': 'SOP',
    'ECE*2412': 'SOP',
    'CS*3113': 'JUN',
    'CE*3963': 'JUN',
    'ME*3232': 'JUN',
    'CS*2263': 'JUN',
    'CS*2383': 'JUN',
    'ECE*3221': 'JUN',
    'SWE*4103': 'JUN',
    'SWE*4403': 'SEN',
    'CS*3503': 'SEN',
    'ECE*3232': 'SEN',
    'ECE*3242': 'SEN',
    'ENGG*4000': 'SEN',
    'CS*3383': 'SEN',
    'CS*3413': 'SEN',
    'CS*3873': 'SEN',
    'ECE*3812': 'SEN',
    'SWE*4203': 'SEN',
    'ENGG*4013': 'SEN'
}


def calculateRank(student_number):
    '''
    Cross-references the prerequisite table to calculate the number of
    prerequisite courses that have been completed by the student (rank_score)

        Parameters:
            student (Student) : the student rank to calculate

        Returns:
            an int score of the given student
    '''
    enrolment_list = Enrolment.objects.all()

    # keeps the count of rank of courses they have taken
    FIR, SOP, JUN, SEN = 0, 0, 0, 0

    # keeps the count of number of pre-reqs in each ranks
    FIR_count, JUN_count, SOP_count, SEN_count = 0, 0, 0, 0

    # this for loop goes through the pre-req table to get the ranks of each course and add it to the count of the rank
    for course in prereq.values():
        if course == 'FIR':
            FIR_count += 1
        elif course == 'JUN':
            JUN_count += 1
        elif course == 'SOP':
            SOP_count += 1
        elif course == 'SEN':
            SEN_count += 1

    # takes each enrolment from the enrolmentlist
    for enrolment in enrolment_list:

        # seperates the course code from the enrolment course
        course_code = enrolment.course.course_code

        # checks if the enrolment student number is the same as the input student number, then checks if the course code of that enrolment is in the prereq table
        if enrolment.student.student_number == student_number and course_code in prereq:
            # depending on the course rank that is in the pre-req table, add the count to the specified rank of the course
            if prereq[course_code] == 'FIR':
                FIR += 1
            elif prereq[course_code] == 'SOP':
                SOP += 1
            elif prereq[course_code] == 'JUN':
                JUN += 1
            elif prereq[course_code] == 'SEN':
                SEN += 1

    # return the coresponding rank depending on whether they completed all the courses in that rank
    # EX: if the student's courses with the rank of 'FIR' is the same length as the FIR pre-req length, then return FIR
    # EX: if the student needs 1 more FIR course, but completed all JUN courses, it will still return as first year since they are still missing FIR courses
    if FIR <= FIR_count:
        return 'FIR'
    elif JUN <= JUN_count:
        return 'JUN'
    elif SOP <= SOP_count:
        return 'SOP'
    elif SEN <= SEN_count:
        return 'SEN'
