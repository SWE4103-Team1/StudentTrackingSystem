from audits.audit_data import AuditData

statuses = ["JUST ENTERED", "EXPECTED TO GRADUATE", "CLEAR TO GRADUATE", "IN PROGRESS"]


def student_status(audit_data: AuditData):
    status = "JUST ENTERED"
