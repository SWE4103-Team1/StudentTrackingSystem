# query enrolments for a given student number join that certain student
import datetime

from datamodel.models import Enrolment
from StudentTrackingSystemApp.configfuncs import excel_in_dict

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
        audit_response["base_program"] = student
        audit_response["as_of"] = enrolments[0].term

    return audit_response


def _target_student_data(student):
    return {
        "student_number": student.student_number,
        "full_name": student.name,
        "cohort": UNPOP,
        "rank": student.rank,
        "years_in": datetime.date().year - student.upload_set.upload_datetime.year,
        "status": UNPOP,
    }


# def _completed_progress_data(enrolments):
