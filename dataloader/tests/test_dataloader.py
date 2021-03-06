from django.core.files import File as DjangoFile
from django.utils import timezone
from django.test import TestCase
import unittest

import os
from os import path
import time
from tempfile import NamedTemporaryFile

from dataloader.load_extract import DataFileExtractor
from datamodel.models import UploadSet, Student, Course, Enrolment
from StudentTrackingSystem.settings import BASE_DIR


def mktemp():
    tmp_file = NamedTemporaryFile(
        "w+", suffix=".txt", prefix=os.path.join(os.getcwd(), "")
    )
    dj_file = DjangoFile(tmp_file)
    return dj_file


class DataLoaderTests(unittest.TestCase):
    def test_get_upload_set(self):
        with mktemp() as course_file, mktemp() as person_file, mktemp() as transfer_file:
            time = timezone.now()
            us = UploadSet(upload_datetime=time)
            us.course_data_file.save("course_test_file", course_file)
            us.person_data_file.save("person_test_file", person_file)
            us.transfer_data_file.save("transfer_test_file", transfer_file)
            us.save()

            uploader = DataFileExtractor(us)
            self.assertEqual(uploader.get_upload_set().upload_datetime, time)
            self.assertTrue(uploader.get_upload_set().course_data_file)
            self.assertTrue(uploader.get_upload_set().person_data_file)
            self.assertTrue(uploader.get_upload_set().transfer_data_file)

    # NOT CURRENTLY RUN AUTOMATICALLY
    def _sample_upload_set(self):
        personfile = open(path.join(BASE_DIR, "data", "personData.txt"), "r")
        transferfile = open(path.join(BASE_DIR, "data", "transferData.txt"), "r")
        coursefile = open(path.join(BASE_DIR, "data", "courseData.txt"), "r")
        start_time = time.time()
        uploader = DataFileExtractor()
        uploader.uploadAllFiles(personfile, coursefile, transferfile)
        end_time = time.time()
        return end_time - start_time

    def test_upload_all_files(self):
        with mktemp() as course_file, mktemp() as person_file, mktemp() as transfer_file:
            course_data = [
                "Student_ID\tProgram\tTerm\tCourse\tTitle\tGrade\tCredit_Hrs\tGrade_Pts\tSection\tInt_Transfers\tNotes_Codes\n",
                "5773669\tBSSWE\t2021/WI\tCHEM*1982\tGENERAL APPLIED CHEMISTRY\tA\t3.00\t12.0\tFR01B\n",
                "5773669\tBSSWE\t2021/WI\tPHYS*1081\tFOUNDATIONS OF PHYS FOR ENGG\tA\t3.00\t12.0\tFR01B\n",
                "5773669\tBSSWE\t2021/WI\tPHYS*1081\tFOUNDATIONS OF PHYS FOR ENGG\tA\t3.00\t12.0\tFR01B\n",
            ]
            person_data = [
                "Student_ID\tFname-Lname\tGender\tBirthDay\tAddress_1\tAddress_2\tEmail\tProgram\tCampus\tStart_Date\n",
                "5773669\tFletcher Donaldson\tM\t1-481-403-4584\t8851 Golf Lane\tSomerset, NJ 08873\tFDONALDSO\tBSSWE\tFR\t2020-09-01\n",
                "5783443\tBob MacDonald\tM\t1-481-403-4584\t8851 Golf Lane\tSomerset, NJ 08873\tFDONALDSO\tBSSWE\tFR\t2020-09-01\n",
                "5782137\tAurelio Huffman\tM\t1-824-453-4120\t111 San Pablo St.\tGarfield, NJ 07026\tAHUFFMA2\tBSSWE\tFR\t2020-09-01",
            ]
            transfer_data = [
                "Student_ID\tCourse\tTitle\tCredit_Hrs\tInstitution\tTransfer_Degrees\tTransfer_Date\n",
                "5773669\tMATH*1013\tINTRO TO CALCULUS II\t3.00\tBSE\tBSSWE\t2018/06/30\n",
                "5773669		A-LEVEL PHYSICS	10.00		BSE  BSSWE	2018/06/30\n",
                "5773669		BLOCK TRANSFER	60.00		BAM	2007/06/22\n",
            ]

            course_file.writelines(course_data)
            course_file.open("r")

            person_file.writelines(person_data)
            person_file.open("r")

            transfer_file.writelines(transfer_data)
            transfer_file.open("r")

            uploader = DataFileExtractor()
            uploader.uploadAllFiles(person_file, course_file, transfer_file)

            db_students = Student.objects.filter()
            self.assertTrue(db_students)
            self.assertTrue(Course.objects.filter())
            self.assertTrue(Enrolment.objects.filter())
            self.assertEquals(db_students[0].rank, "FIR")
            self.assertEquals(len(db_students), 1)

            self.assertTrue(
                Course.objects.filter(course_code="EXTRA")
            )
            self.assertTrue(
                Course.objects.filter(course_code="BAS SCI")
            )
