# TODO: calculate the student's status
# TODO: use the cohort instead of the student's start date when finding best matrix

from datetime import datetime

from datamodel.models import Enrolment, Course
from dataloader.load_extract import DataFileExtractor
from StudentTrackingSystemApp.configfuncs import get_all_cores
from audits.audit_data import AuditData
from audits.confmatrix import best_fit_config_matrix, non_core_requirements


UNPOP = "UNPOPULATED"
passing_grades = {
    "CR",
    "C-",
    "C",
    "C+",
    "B-",
    "B",
    "B+",
    "A-",
    "A",
    "A+",
    DataFileExtractor._transfer_marker,
}


def audit_student(student_number, mapped_courses=None):
    # Get credit hours for courses
    if mapped_courses is None:
        courses = Course.objects.all().order_by("upload_set__upload_datetime")
        # new courses will overwrite older
        mapped_courses = {c.course_code.replace("*", ""): c for c in courses.reverse()}

    # Query the enrolments for the given student number
    enrolments = Enrolment.objects.filter(
        student__student_number=student_number,
    ).order_by("term")

    # Populate audit response with enrolment data
    audit_response = AuditData()
    student_status = "JUST ENTERED"
    if len(enrolments):
        student = enrolments[0].student
        conf_mat_sheet = best_fit_config_matrix(student)
        audit_response["latest_enrolment_term"] = enrolments[0].term
        audit_response["base_program"] = "SWE{}".format(conf_mat_sheet)
        progress = audit_response["progress"]

        # fill core's remaining with all cores
        core_codes = get_all_cores(conf_mat_sheet)
        progress["CORE"] = {
            "remaining": {
                "courses": core_codes,
                "credit_hours": sum(
                    map(
                        lambda c: mapped_courses.get(
                            c, Course(credit_hours=0)
                        ).credit_hours,
                        core_codes,
                    )
                ),
            }
        }

        # fill non-core's reamining sections with all non-cores
        non_core_reqs = non_core_requirements(conf_mat_sheet)
        for course_type, reqs in non_core_reqs.items():
            progress[course_type] = {"remaining": reqs}

        # populate progress from student's enrolments, removing remaining appropriately
        applicables = filter(
            lambda e: e.course.course_type != None and e.grade in passing_grades,
            enrolments,
        )
        for enrolment in applicables:
            course_status = "completed"
            if enrolment.grade == "nan" or enrolment is None:
                course_status = "in_progress"

            audit_response.add_course(course_status, enrolment.course)
            audit_response.remove_course("remaining", enrolment.course)

        audit_response["target_student"] = _student_data(student, student_status)
    return (audit_response, mapped_courses)


def _student_data(student, student_status):
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
        "status": student_status,
    }
