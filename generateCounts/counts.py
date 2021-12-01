from datamodel.models import Student, Course, Enrolment, UploadSet
from django.db.models import Q


def latest_upload_set():
    return UploadSet.objects.order_by("upload_datetime").last()


def count_coop_students_by_semester(term_):
    added_students = []
    coop_course_ids = []
    latest_us = latest_upload_set()

    coop_courses = list(
        Course.objects.filter(upload_set=latest_us, name="CO-OP WORK TERM").values("id")
    )

    for coop_course in coop_courses:
        coop_course_ids.append(coop_course["id"])

    for enrolmentValues in (
        Enrolment.objects.filter(upload_set=latest_us, term=term_)
        .values("course", "student")
        .iterator()
    ):
        course_id = enrolmentValues["course"]
        student_id = enrolmentValues["student"]
        if course_id in coop_course_ids and not student_id in added_students:
            added_students.append(student_id)

    return len(added_students)


def count_coop_students_by_cohort(cohort):
    coop_course_ids = []
    added_students = []
    student_id_list = []
    latest_us = latest_upload_set()

    # Since parameter is passed as year-nextYear we need to extract the year
    year = cohort[:4]
    nextYear = cohort[5:]

    # We want to find students that start in september of the above year
    # or winter/summer of the following year
    fall = year + "-09"
    winter = nextYear + "-01"
    summer = nextYear + "-05"

    # Maybe use __contains = [fall, winter, summer]
    coop_courses = list(
        Course.objects.filter(upload_set=latest_us, name="CO-OP WORK TERM").values("id")
    )
    students = list(
        Student.objects.filter(
            Q(upload_set=latest_us),
            Q(start_date__contains=fall)
            | Q(start_date__contains=winter)
            | Q(start_date__contains=summer),
        ).values("id")
    )

    for coop_course in coop_courses:
        coop_course_ids.append(coop_course["id"])

    for student in students:
        student_id_list.append(student["id"])

    for enrolmentValues in (
        Enrolment.objects.filter(upload_set=latest_us)
        .values("course", "student")
        .iterator()
    ):
        course_id = enrolmentValues["course"]
        student_id = enrolmentValues["student"]
        if (
            course_id in coop_course_ids
            and student_id in student_id_list
            and not student_id in added_students
        ):
            added_students.append(student_id)

    return len(added_students)


def count_total_students_by_semester(term_):
    student_ids = []
    latest_us = latest_upload_set()
    students = list(
        Enrolment.objects.filter(upload_set=latest_us, term=term_).values("student_id")
    )
    for student in students:
        student_ids.append(student["student_id"])

    student_ids = list(set(student_ids))  ##Gets rid of duplicates
    return len(student_ids)


def count_total_students_by_cohort(cohort):
    added_students = []
    student_id_list = []
    latest_us = latest_upload_set()

    # Since parameter is passed as year-nextYear we need to extract the year
    year = cohort[:4]
    nextYear = cohort[5:]

    # We want to find students that start in september of the above year
    # or winter/summer of the following year
    fall = year + "-09"
    winter = nextYear + "-01"
    summer = nextYear + "-05"

    students = list(
        Student.objects.filter(
            Q(upload_set=latest_us),
            Q(start_date__contains=fall)
            | Q(start_date__contains=winter)
            | Q(start_date__contains=summer),
        ).values("id")
    )

    for student in students:
        student_id_list.append(student["id"])

    for enrolmentValues in (
        Enrolment.objects.filter(upload_set=latest_us)
        .values("course", "student")
        .iterator()
    ):
        student_id = enrolmentValues["student"]
        if student_id in student_id_list and not student_id in added_students:
            added_students.append(student_id)

    return len(added_students)


def count_students_by_rank_semester(term_):
    FIR = 0
    SOP = 0
    JUN = 0
    SEN = 0
    enrolled_student_ids = []
    latest_us = latest_upload_set()

    enrolled_students = list(
        Enrolment.objects.filter(upload_set=latest_us, term=term_).values("student_id")
    )

    for enrolled_student in enrolled_students:
        enrolled_student_ids.append(enrolled_student["student_id"])

    enrolled_student_ids = list(set(enrolled_student_ids))

    for studentValues in (
        Student.objects.filter(upload_set=latest_us).values("id", "rank").iterator()
    ):
        student_id = studentValues["id"]
        student_rank = studentValues["rank"]
        if student_id in enrolled_student_ids:
            if student_rank == "FIR":
                FIR += 1
            elif student_rank == "SOP":
                SOP += 1
            elif student_rank == "JUN":
                JUN += 1
            elif student_rank == "SEN":
                SEN += 1
        else:
            pass

    rank_counts = {"FIR": FIR, "SOP": SOP, "JUN": JUN, "SEN": SEN}

    return rank_counts


def count_students_by_rank_cohort(cohort):
    FIR = 0
    SOP = 0
    JUN = 0
    SEN = 0
    enrolled_student_ids = []

    # Since parameter is passed as year-nextYear we need to extract the years
    year = cohort[:4]
    nextYear = cohort[5:]

    # We want to find students that start in september of the above year
    # or winter/summer of the following year
    fall = year + "-09"
    winter = nextYear + "-01"
    summer = nextYear + "-05"

    students = list(
        Student.objects.filter(
            Q(upload_set=latest_upload_set()),
            Q(start_date__contains=fall)
            | Q(start_date__contains=winter)
            | Q(start_date__contains=summer),
        ).values("rank")
    )

    for student in students:
        if student["rank"] == "FIR":
            FIR += 1
        elif student["rank"] == "SOP":
            SOP += 1
        elif student["rank"] == "JUN":
            JUN += 1
        elif student["rank"] == "SEN":
            SEN += 1

    rank_counts = {"FIR": FIR, "SOP": SOP, "JUN": JUN, "SEN": SEN}

    return rank_counts
