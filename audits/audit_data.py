import json
from copy import deepcopy

from datamodel.models import Course


class AuditData:
    empty_progress_data = {"courses": [], "credit_hours": 0}

    def __init__(self):
        self.data = {
            "target_student": {},
            "progress": {},
        }

    def add_course(self, status: str, course: Course):
        progress = self.data["progress"]
        type_progress = progress.get(course.course_type, {})
        if status not in type_progress:
            type_progress[status] = deepcopy(AuditData.empty_progress_data)
        type_progress[status]["courses"].append(course.course_code.replace("*", ""))
        type_progress[status]["credit_hours"] += course.credit_hours
        self.data["progress"][course.course_type] = type_progress

    def remove_course(self, status: str, course: Course):
        progress = self.data["progress"]
        type_progress = progress.get(course.course_type, {})
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
