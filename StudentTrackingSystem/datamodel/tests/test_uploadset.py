from django.test import TestCase
from datetime import date
from tempfile import NamedTemporaryFile

from ..models import UploadSet


class UploadSetTests(TestCase):
    def test_create_null_upload_set(self):
        today = date.today()
        us = UploadSet(upload_date=today)
        us.save()
        self.assertEqual(us.upload_date, today)
        self.assertFalse(us.course_data_file)
        self.assertFalse(us.person_data_file)
        self.assertFalse(us.transfer_data_file)
        return us

    def test_create_empty_upload_set(self):
        today = date.today()
        with NamedTemporaryFile() as course_file, NamedTemporaryFile() as person_file, NamedTemporaryFile() as transfer_file:
            us = UploadSet(upload_date=today)
            us.course_data_file.name = course_file.name
            us.person_data_file.name = person_file.name
            us.transfer_data_file = transfer_file.name
            us.save()
            self.assertEqual(us.upload_date, today)
            self.assertTrue(us.course_data_file)
            self.assertTrue(us.person_data_file)
            self.assertTrue(us.transfer_data_file)
        return us
