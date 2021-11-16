from django.test import TestCase

from ..configfuncs import get_pre_req, get_course_type

class ConfigTests(TestCase):
	def test_get_pre_req(self):
		prereqDict = {
			"ECE 2412": ["CS 1073", "ECE 1813", "MATH 1013", "MATH 1503"],
			"CS 3503": ["CS 1103"],
			"ECE 2214": ["CS 1073", "ECE 2215*"],
			"ENGG 1015": ["ENGG1003*", "PHYS 1081*", "MATH 1003*", "MATH 1503*"]
		}

		for course in prereqDict:
			self.assertEqual(get_pre_req(course), prereqDict[course])

	def test_get_course_type(self):
		typeDict = {
			"BIOL": "SCIENCE",
			"ENVS2003": "CSE-ITS",
			"ANTH": "CSE-HSS",
			"ADM": "CSE-OPEN",
			"ME3232": "FUNDAMENTALS",
			"SWE": "TE"
		}
		
		for course in typeDict:
			self.assertEqual(get_course_type(course), typeDict[course])