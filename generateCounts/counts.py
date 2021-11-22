from datamodel.models import Student, Course, Enrolment, UploadSet


def count_coop_students_by_semester(term_):
    added_students=[]
    coop_course_ids =[]

    coop_courses = list(Course.objects.filter(name = "CO-OP WORK TERM").values('id'))

    for coop_course in coop_courses:
        coop_course_ids.append(coop_course['id'])

    for enrolmentValues in Enrolment.objects.filter(term = term_).values('course','student').iterator():
        course_id = enrolmentValues['course']
        student_id =  enrolmentValues['student']
        if course_id in coop_course_ids and not student_id in added_students:
            added_students.append(student_id)

    return len(added_students)

def count_coop_students_by_start_date(start_date_):
    coop_course_ids =[]
    added_students = []
    student_id_list = []

    coop_courses = list(Course.objects.filter(name = "CO-OP WORK TERM").values('id'))
    students = list(Student.objects.filter(start_date = start_date_).values('id'))

    for coop_course in coop_courses:
        coop_course_ids.append(coop_course['id'])

    for student in students :
        student_id_list.append(student['id'])

    for enrolmentValues in Enrolment.objects.all().values('course','student').iterator():
        course_id = enrolmentValues['course']
        student_id =  enrolmentValues['student']
        if course_id in coop_course_ids and student_id in student_id_list and not student_id in added_students:
            added_students.append(student_id)

    return len(added_students)

def count_total_students_by_semester(term_):
    studentList = []
    enrolmentQuerySet = Enrolment.objects.filter(term=term_)
    student_ids = []
    added_students = []
    students = list(Enrolment.objects.filter(term=term_).values('student_id'))
    for student in students:
        student_ids.append(student['student_id'])

    student_ids = list(set(student_ids)) #Gets rid of duplicates
    return len(student_ids)

def count_total_students_by_start_date(start_date_):
    added_students =[]
    student_id_list = []

    students = Student.objects.filter(start_date=start_date_).values('id')

    for student in students :
        student_id_list.append(student['id'])

    for enrolmentValues in Enrolment.objects.all().values('course','student').iterator():
        student_id = enrolmentValues['student']
        if student_id in student_id_list and not student_id in added_students:
            added_students.append(student_id)

    return len(added_students)

def count_students_by_rank_semester(term_):
    FIR =0
    SOP = 0
    JUN = 0
    SEN = 0
    enrolled_student_ids = []

    enrolled_students = list(Enrolment.objects.filter(term=term_).values('student_id'))

    for enrolled_student in enrolled_students :
        enrolled_student_ids.append(enrolled_student['student_id'])

    enrolled_student_ids = list(set(enrolled_student_ids))

    for studentValues in Student.objects.all().values('id','rank').iterator():
        student_id = studentValues['id']
        student_rank = studentValues['rank']
        if student_id in enrolled_student_ids:
            if student_rank == 'FIR':
                FIR +=1
            elif student_rank == 'SOP':
                SOP += 1
            elif student_rank == 'JUN':
                JUN += 1
            elif student_rank == 'SEN':
                SEN += 1
        else:
            pass

    rank_counts = {'FIR':FIR,'SOP':SOP,'JUN':JUN,'SEN':SEN}

    return rank_counts

def count_students_by_rank_start_date(start_date_):
    FIR =0
    SOP = 0
    JUN = 0
    SEN = 0
    enrolled_student_ids = []

    students = list(Student.objects.filter(start_date=start_date_).values('rank'))
    for student in students:
        if student['rank'] == 'FIR':
            FIR +=1
        elif student['rank'] == 'SOP':
            SOP += 1
        elif student['rank'] == 'JUN':
            JUN += 1
        elif student['rank'] == 'SEN':
            SEN += 1

    rank_counts = {'FIR':FIR,'SOP':SOP,'JUN':JUN,'SEN':SEN}

    return rank_counts
