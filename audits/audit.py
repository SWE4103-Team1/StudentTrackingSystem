# query enrolments for a given student number join that certain student
from datetime import datetime
import json
from copy import deepcopy

from datamodel.models import Enrolment, Course
from StudentTrackingSystemApp.configfuncs import excel_in_dict as xls_confs
from StudentTrackingSystemApp.configfuncs import get_all_cores

UNPOP = "UNPOPULATED"


def _find_if(compare, list):
    for elem in list:
        if compare(elem):
            return elem
    return None


class AuditData:
    empty_progress_data = {"courses": [], "credit_hours": 0}
    empty_progress = {
        "completed": deepcopy(empty_progress_data),
        "in_progress": deepcopy(empty_progress_data),
    }

    def __init__(self):
        self.data = {
            "target_student": {},
            "progress": {},
        }

    def add_course(self, status: str, course: Course):
        progress = self.data["progress"]
        type_progress = progress.get(
            course.course_type, deepcopy(AuditData.empty_progress)
        )
        if status not in type_progress:
            type_progress[status] = deepcopy(AuditData.empty_progress_data)
        type_progress[status]["courses"].append(course.course_code.replace("*", ""))
        type_progress[status]["credit_hours"] += course.credit_hours
        self.data["progress"][course.course_type] = type_progress

    def remove_course(self, status: str, course: Course):
        progress = self.data["progress"]
        type_progress = progress.get(
            course.course_type, deepcopy(AuditData.empty_progress)
        )
        if status not in type_progress:
            return
        try:
            type_progress[status]["courses"].remove(course.course_code.replace("*", ""))
            type_progress[status]["credit_hours"] -= course.credit_hours
            self.data["progress"][course.course_type] = type_progress
        except ValueError:
            pass  # course already removed from lits, that's ok

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __str__(self):
        return json.dumps(self.data)

    def toJSON(self):
        return json.dumps(self.data)


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
        for enrolment in enrolments:
            status = "completed"
            if enrolment.grade == "nan" or enrolment is None:
                print("not grade, grade is:", enrolment.grade)
                status = "in_progress"
            audit_response.add_course(status, enrolment.course)
            if enrolment.course.course_type == "CORE":
                audit_response.remove_course("remaining", enrolment.course)

    return (audit_response, mapped_courses)


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
