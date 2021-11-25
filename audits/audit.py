# query enrolments for a given student number join that certain student
from datetime import datetime

from datamodel.models import Enrolment, Course
from StudentTrackingSystemApp.configfuncs import excel_in_dict as xls_confs
from StudentTrackingSystemApp.configfuncs import get_all_cores
from audits.audit_data import AuditData


UNPOP = "UNPOPULATED"


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
        conf_mat_sheet = _best_fit_config_matrix(student)
        audit_response["target_student"] = _target_student_data(student)
        audit_response["latests_enrolment_term"] = enrolments[0].term
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

        # populate progress from student's enrolments
        print("enrolments", list(map(lambda e: e.course.course_code, enrolments)))
        for enrolment in filter(lambda e: e.course.course_type != None, enrolments):
            status = "completed"
            if enrolment.grade == "nan" or enrolment is None:
                print("not grade, grade is:", enrolment.grade)
                status = "in_progress"
            audit_response.add_course(status, enrolment.course)
            if enrolment.course.course_type == "CORE":
                audit_response.remove_course("remaining", enrolment.course)

    return (audit_response, mapped_courses)


def _target_student_data(student):
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
        "status": UNPOP,
    }


def _best_fit_config_matrix(student):
    # TODO: use the cohort instead of the student's start date
    target_year = student.start_date.year

    def is_target_year(sheet):
        mat_start_year = sheet.split("-")[0]
        if mat_start_year.isnumeric():
            try:
                mat_start_year = int(mat_start_year)
            except ValueError:
                return False
            return mat_start_year == target_year
        return False

    student_mat = list(filter(is_target_year, xls_confs.keys()))
    if len(student_mat) < 1:
        raise RuntimeError(
            "No suitable matrix in configration file for start year {}".format(
                target_year
            )
        )

    return student_mat[0]
