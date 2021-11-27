# TODO: use the cohort instead of the student's start date when finding best matrix

from datetime import datetime

from datamodel.models import Enrolment, Course
from StudentTrackingSystemApp.configfuncs import get_all_cores
from audits.audit_data import AuditData
from audits.confmatrix import best_fit_config_matrix, non_core_requirements
from audits import status


UNPOP = "UNPOPULATED"
pass_grades = {"nan", "CR", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+", "T"}


def audit_student(student_number, enrolments=None, courses=None, mapped_courses=None):
    """
    Audits a student with the given student number. All default parameters are
    to improve performance for load-extract and can be omitted for a basic
    audit.
    enrolments is a list of Enrolments, sorted in descending order by term
    courses is a list of Courses, sorted in descending order by upload_datetime
    mapped_courses is a dict, mapping the course code, without asterisks, to the course
    """
    # Query the enrolments for the given student number
    if enrolments is None:
        enrolments = Enrolment.objects.filter(
            student__student_number=student_number,
        ).order_by("term")

    if len(enrolments) <= 0:
        raise KeyError("Student {} has no enrolments".format(student_number))

    # Get credit hours for courses
    if courses is None:
        # TODO: look for unique
        courses = Course.objects.all().order_by("upload_set__upload_datetime")
    if mapped_courses is None:
        # new courses will overwrite older
        mapped_courses = {c.course_code.replace("*", ""): c for c in courses}

    # Populate audit response with enrolment data
    audit_response = AuditData()
    student = enrolments[0].student
    conf_mat_sheet = best_fit_config_matrix(student)
    audit_response["latest_enrolment_term"] = enrolments[0].term
    audit_response["base_program"] = "SWE{}".format(conf_mat_sheet)
    progress = audit_response["progress"]

    # fill core's remaining with all cores
    core_codes = get_all_cores(conf_mat_sheet)
    progress["CORE"] = AuditData.default_core_progress()
    progress["CORE"]["remaining"] = {
        "courses": core_codes,
        "credit_hours": sum(
            map(
                lambda c: mapped_courses.get(c, Course(credit_hours=0)).credit_hours,
                core_codes,
            )
        ),
    }

    # fill non-core's reamining sections with all non-cores
    non_core_reqs = non_core_requirements(conf_mat_sheet)
    for course_type, reqs in non_core_reqs.items():
        progress[course_type] = AuditData.default_non_core_progress()
        progress[course_type]["remaining"] = reqs

    # populate progress from student's enrolments, removing remaining appropriately
    applicables = filter(
        lambda e: e.course.course_type != None and e.grade in pass_grades,
        enrolments,
    )
    for enrolment in applicables:
        course_status = "completed"
        if enrolment.grade == "nan":
            course_status = "in_progress"
        audit_response.add_course(course_status, enrolment.course)
        audit_response.remove_course("remaining", enrolment.course)

    student_status = status.student_status(progress)
    audit_response["target_student"] = _student_data(student, student_status)
    return (audit_response, enrolments, mapped_courses)


def _student_data(student, status):
    # years_in calculated as current year minus start year, plus
    # the portion of the current year, in months, that have passed
    # the current month is ignored, which is why now.month - 1 is used
    now = datetime.now()
    years_in = float(now.year - student.upload_set.upload_datetime.year)
    years_in = round(years_in + (now.month - 1) / 12, 1)
    return {
        "student_number": student.student_number,
        "full_name": student.name,
        "cohort": UNPOP,
        "rank": student.rank,
        "years_in": years_in,
        "status": status,
    }
