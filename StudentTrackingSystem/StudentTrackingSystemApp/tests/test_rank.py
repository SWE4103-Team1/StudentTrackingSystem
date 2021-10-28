from django.test import TestCase

from ..rankings import calculateRank
from datamodel.tests.test_enrolment import EnrolmentTests

class RankTests(TestCase):
	def test_calculate_rank(self):
		enrollment_tester = EnrolmentTests()
		enrollment = enrollment_tester.test_create_enrolment()
	
		self.assertTrue(calculateRank(enrollment.student.id) == 'FIR')

