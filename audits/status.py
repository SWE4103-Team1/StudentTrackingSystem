from audits.audit_data import AuditData

statuses = ["JUST ENTERED", "EXPECTED TO GRADUATE", "CLEAR TO GRADUATE", "IN PROGRESS"]

# no remaining or in progress -> completed
# no remaining -> expected to graduate
# grade in CS1073


def student_status(student_progress: dict):
    status = "JUST ENTERED"
    for course_type, type_progress in student_progress.items():
        if type_progress.get("remaining")
        pass
    return status
