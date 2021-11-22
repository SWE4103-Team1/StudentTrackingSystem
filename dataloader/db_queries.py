from django.db import transaction


def bulk_save(models):
    with transaction.atomic():
        for model in models:
            model.save()
