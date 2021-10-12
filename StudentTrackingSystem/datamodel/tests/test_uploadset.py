from django.test import TestCase
from django.core.files import File as DjangoFile
from datetime import date, timedelta
from tempfile import NamedTemporaryFile
import os

from ..models import UploadSet


def mktemp():
    tmp_file = NamedTemporaryFile("w+", prefix=os.path.join(os.getcwd(), ""))
    dj_file = DjangoFile(tmp_file)
    return dj_file


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

    def test_create_empty_upload_set(self, today=date.today()):
        with mktemp() as course_file, mktemp() as person_file, mktemp() as transfer_file:
            us = UploadSet(upload_date=today)
            us.course_data_file.save("course_test_file", course_file)
            us.person_data_file.save("person_test_file", person_file)
            us.transfer_data_file.save("transfer_test_file", transfer_file)
            us.save()

            self.assertEqual(us.upload_date, today)
            self.assertTrue(us.course_data_file)
            self.assertTrue(us.person_data_file)
            self.assertTrue(us.transfer_data_file)

        return us

    def test_create_upload_set(self, today=date.today()):
        with mktemp() as course_file, mktemp() as person_file, mktemp() as transfer_file:
            course_file.write(course_contents := "course file contents")
            person_file.write(person_contents := "person file contents")
            transfer_file.write(transfer_contents := "transfer file contents")

            us = UploadSet(upload_date=today)
            us.course_data_file.save("course_test_file", course_file)
            us.person_data_file.save("person_test_file", person_file)
            us.transfer_data_file.save("transfer_test_file", transfer_file)

            self.assertEqual(us.upload_date, today)
            self.assertEqual(
                us.course_data_file.read(), bytearray(course_contents, "utf-8")
            )
            self.assertEqual(
                us.person_data_file.read(), bytearray(person_contents, "utf-8")
            )
            self.assertEqual(
                us.transfer_data_file.read(), bytearray(transfer_contents, "utf-8")
            )

        return us

    def test_query_upload_set(self):
        today = date.today()
        us = self.test_create_upload_set(today)

        # query it from DB
        db_us = UploadSet.objects.get(upload_date=today)

        self.assertIsNotNone(db_us)
        self.assertEqual(db_us.upload_date, today)
        self.assertTrue(db_us.course_data_file)
        self.assertTrue(db_us.person_data_file)
        self.assertTrue(db_us.transfer_data_file)

        return db_us

    def test_same_upload_set_with_different_date(self):
        yesterday = date.today() - timedelta(days=1)
        us = self.test_create_upload_set(yesterday)

        # query it from DB
        db_us = UploadSet.objects.get(upload_date=yesterday)

        self.assertIsNotNone(db_us)
        self.assertEqual(db_us.upload_date, yesterday)
        self.assertTrue(db_us.course_data_file)
        self.assertTrue(db_us.person_data_file)
        self.assertTrue(db_us.transfer_data_file)

        return db_us
