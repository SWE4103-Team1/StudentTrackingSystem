# query enrolments for a given student number join that certain student
from datetime import datetime

from datamodel.models import Enrolment
from StudentTrackingSystemApp.configfuncs import excel_in_dict as xls_confs

UNPOP = "UNPOPULATED"


def audit_student(student_number, upload_set_datetime=None):
    # Query the enrolments for the given student number
    enrolments = Enrolment.objects.filter(
        student__student_number=student_number,
    ).order_by("term")

    if upload_set_datetime is not None:
        enrolments = enrolments.filter(upload_set__upload_datetime=upload_set_datetime)

    # Populate audit response with enrolment data
    audit_response = {}
    if len(enrolments):
        student = enrolments[0].student
        audit_response["target_student"] = _target_student_data(student)
        audit_response["as_of"] = enrolments[0].term
        mat_cohort = _best_fit_config_matrix(student)
        audit_response["base_program"] = "SWE" + mat_cohort[0]
        audit_response["progress"] = {}
        _best_fit_config_matrix(student)
    return audit_response


def _target_student_data(student):
    return {
        "student_number": student.student_number,
        "full_name": student.name,
        "cohort": UNPOP,
        "rank": student.rank,
        "years_in": 7,  # datetime().year - student.upload_set.upload_datetime.year(),
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


def _completed__progress_data(enrolments):
    pass
