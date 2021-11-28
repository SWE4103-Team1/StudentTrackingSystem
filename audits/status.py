def student_status(student_progress: dict):
    # no remaining or in progress -> clear to grad
    # no remaining -> expected to graduate
    # grade in CS1073 -> in progress
    # else -> just entered
    has_remaining = False
    has_in_progress = False
    has_cs1073 = False

    # check enrolment qualifications
    for type_progress in student_progress.values():
        completed = type_progress.get("completed", None)
        in_progress = type_progress.get("in_progress", None)
        remaining = type_progress.get("remaining", None)

        if not has_remaining and remaining:
            has_remaining = remaining["credit_hours"] != 0

        if not has_in_progress and in_progress:
            has_in_progress = in_progress["credit_hours"] != 0

        if not has_cs1073 and completed:
            has_cs1073 = "CS1073" in completed["courses"]

        if has_remaining and has_in_progress and has_cs1073:
            break  # all flags met, no more searching req.

    # resolve status from qualifications
    status = "IN PROGRESS"
    if not has_remaining:
        status = "EXPECTED TO GRADUATE" if has_in_progress else "CLEAR TO GRADUATE"
    elif not has_cs1073:
        status = "JUST ENTERED"

    return status
