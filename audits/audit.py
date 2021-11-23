# query enrolments for a given student number join that certain student
from datetime import datetime

from datamodel.models import Enrolment
from StudentTrackingSystemApp.configfuncs import excel_in_dict as xls_confs

UNPOP = "UNPOPULATED"


def _find_if(compare, list):
    for elem in list:
        if compare(elem):
            return elem
    return None


def audit_student(student_number):
    # Query the enrolments for the given student number
    enrolments = Enrolment.objects.filter(
        student__student_number=student_number,
    ).order_by("term")

    # Populate audit response with enrolment data
    audit_response = {}
    if len(enrolments):
        student = enrolments[0].student
        audit_response["target_student"] = _target_student_data(student)
        audit_response["as_of"] = enrolments[0].term
        audit_response["base_program"] = "SWE" + UNPOP
        audit_response["progress"] = {}

        for enrolment in enrolments:
            _lookup_course_type(enrolment.course)

            print(enrolment)

    return audit_response


def _lookup_course_type(course):
    replacements = xls_confs["replacements"].to_dict(orient="list")
    course_types = xls_confs["valid-tags"].to_dict(orient="list")
    exceptions = xls_confs["exceptions"].to_dict(orient="list")

    # print("replacements", replacements)
    # print("exceptions", exceptions)

    course_type = None
    joined_code = "".join(course.course_code.split("*"))

    def _code_matches_course_in_type(target_course):

        return joined_code.startswith(target_course)  # and not

    # Match to valid tags
    for type, courses_in_type in course_types.items():
        if joined_code in exceptions[type]:
            break

        found = _find_if(_code_matches_course_in_type, courses_in_type)
        if len(found):
            return type
            # iterate through found, checking if

    return course_type


def _target_student_data(student):
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


def _completed_progress_data(enrolments):
    pass


# read in valid tags
