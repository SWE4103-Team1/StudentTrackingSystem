# import prerequisite table from datamodel
from datamodel.models import Student, Enrolment

#To be removed
prereq = [
    'MATH*1003',
     'MATH*1503',
     'CS*1073',
     'PHSY*1081',
     'ENGG*1003',
     'ENGG*1015',
     'ENGG*1001',
     'MATH*1013',
     'INFO*1103',
     'CS*1083',
     'ECE*1813',
     'CHEM*1982',
     'CHEM*1987',
     'CS*2043',
     'CS*1303',
     'CS*2613',
     'ECE*2701',
     'ECE*2214',
     'ECE*2215',
     'CS*2333',
     'STAT*2593',
     'ECE*2412',
     'CS*3113',
     'CE*3963',
     'ME*3232',
     'CS*2263',
     'CS*2383',
     'ECE*3221',
     'SWE*4103',
     'SWE*4403',
     'CS*3503',
     'ECE*3232',
     'ECE*3242',
     'ENGG*4000',
     'CS*3383',
     'CS*3413',
     'CS*3873',
     'ECE*3812',
     'SWE*4203',
     'ENGG*4013'
     ]

def calculateRank(student_number):
    '''
    Cross-references the prerequisite table to calculate the number of 
    prerequisite courses that have been completed by the student (rank_score)

        Parameters:
            student (Student) : the student rank to calculate

        Returns:
            an int score of the given student
    '''
    rank_score = 0
    enrolment_list = Enrolment.objects.all()
    for enrolment in enrolment_list:
        if enrolment.student.student_number == student_number and enrolment.course.course_code in prereq:
            rank_score+=1
    
    return rank_score

