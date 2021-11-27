# TODO: don't remove courses / CH if already 0
import json
from copy import deepcopy

from datamodel.models import Course


class AuditData:
    @staticmethod
    def default_non_core_remaining_progress_data():
        return deepcopy({"num_courses": 0, "credit_hours": 0})

    @staticmethod
    def default_progress_data():
        return deepcopy({"courses": [], "credit_hours": 0})

    @staticmethod
    def default_core_progress():
        return deepcopy(
            {
                "completed": AuditData.default_progress_data(),
                "remaining": AuditData.default_progress_data(),
                "in_progress": AuditData.default_progress_data(),
            }
        )

    @staticmethod
    def default_non_core_progress():
        return deepcopy(
            {
                "completed": AuditData.default_progress_data(),
                "remaining": AuditData.default_non_core_remaining_progress_data(),
                "in_progress": AuditData.default_progress_data(),
            }
        )

    def __init__(self):
        self.data = {
            "target_student": {},
            "progress": {},
        }

    def add_course(self, status: str, course: Course):
        progress = self.data["progress"]
        type_progress = progress.get(course.course_type, {})
        if status not in type_progress:
            type_progress[status] = AuditData.default_progress_data()
        type_progress[status]["courses"].append(course.course_code.replace("*", ""))
        type_progress[status]["credit_hours"] += course.credit_hours
        self.data["progress"][course.course_type] = type_progress

    def remove_course(self, status: str, course: Course):
        progress = self.data["progress"]
        type_progress = progress.get(course.course_type, {})
        if status not in type_progress:
            return

        if course.course_type == "CORE":
            try:
                type_progress[status]["courses"].remove(
                    course.course_code.replace("*", "")
                )
            except ValueError:
                pass  # course already removed
            if type_progress[status]["credit_hours"] > course.credit_hours:
                type_progress[status]["credit_hours"] -= course.credit_hours
            self.data["progress"][course.course_type] = type_progress

        else:
            if type_progress[status]["num_courses"] > 0:
                type_progress[status]["num_courses"] -= 1
            if type_progress[status]["credit_hours"] > course.credit_hours:
                type_progress[status]["credit_hours"] -= course.credit_hours
            self.data["progress"][course.course_type] = type_progress

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __str__(self):
        return json.dumps(self.data)

    def toJSON(self):
        return json.dumps(self.data)
