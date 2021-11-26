from django.db import transaction


def bulk_save(models):
    with transaction.atomic():
        for model in models:
            model.save()


def group_enrolments_by_student_num(enrolments: list):
    """returns dict of lists, where key is student number and value is a sorted
    list of their enrolments"""
    # group enrolments
    groups = dict()
    for enrolment in enrolments:
        s_num = enrolment.student.student_number
        existing = groups.get(s_num)
        if existing is None:
            groups[s_num] = [enrolment]
        else:
            existing.append(enrolment)

    # sort the grouped enrolments
    for s_num, enrolments in groups.items():
        enrolments.sort(key=lambda e: e.term, reverse=True)

    return groups
