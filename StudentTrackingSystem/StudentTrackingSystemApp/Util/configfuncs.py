#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 21:44:25 2021

@author: tylertravis, Elliot

Last Edit : Elliot, 9.11.2021 8:14PM
"""

import math
from numpy import true_divide

import pandas as pd

# Temporary Course Excel URL
excelurl = 'SWEProgram.xlsx'


def insert_space(string, integer):
    return string[0:integer] + ' ' + string[integer:]


class SheetData:

    excel_in_dict = {}

    def __init__(self, datasheet):
        # gets the excel file and store it on xls
        xls = pd.ExcelFile(datasheet)

        # creates a dict to store the excel data to prevent multiple calls to read the data from the file
        excel_in_dict = {}

        # store each sheet in a dict
        # call the sheets by doing "self.excel_in_dict[sheet_name_to_call]"
        for sheet_name in xls.sheet_names:
            self.excel_in_dict[sheet_name] = xls.parse(sheet_name)

        # Declaration
        # Declaring Pre-Req Table

        self.excel_in_dict["prereqs"].columns = [
            "Course", "PreReqs1", "PreReqs2", "PreReqs3", "PreReqs4"]

        # self.dfprereqs = pd.read_excel(
        #     datasheet, sheet_name="prereqs")

        # this is all called at the top in the dict

        # # Declearing exception | valid tags | replacements
        # self.exceptions = pd.read_excel(
        #     datasheet, sheet_name="exceptions").to_dict(orient="list")
        # self.valid_tags = pd.read_excel(
        #     datasheet, sheet_name="valid-tags").to_dict(orient="list")
        # self.replacement = pd.read_excel(
        #     datasheet, sheet_name="replacements").to_dict(orient="list")

        # # Declaring CourseGroup Table
        # self.course_groups = pd.read_excel(
        #     datasheet, sheet_name='course-groups').to_dict(orient="list")

    ###########################
    # Elliot's version - START
    ###########################

    def get_pre_req(self, classcode):
        """
        Takes in a class code and returns the list of pre-requesites for the class

            Param:
                classcode : the class code to get the pre requesites from

            Return:
                the list of pre-requesites for the given class code
        """
        # formats the classcode to work both with spacing and no spacing
        if " " not in classcode:
            # takes the prefix of the class code (only the letter part of the class code)
            tag = self.get_course_tag(classcode)
            # adds spacing in between the class code
            classcode = tag + " " + classcode[len(tag):]

        pre_reqs = []
        # get all the pre-reqs given the course code (in the form of list)

        for item in self.excel_in_dict["prereqs"].loc[self.excel_in_dict["prereqs"]["Course"] == classcode].values[0]:
            try:
                # since each pre-req is returned in the form of a list, so i only take the first element from 'item'
                # if the element is nan, this would be true, else it would throw an exception
                # break once the first nan is met since once nan is met the remaining elements will be nan too
                if math.isnan(item):
                    break
            except:
                # since it throws an exception, its not "nan", so add it to the list
                pre_reqs.append(item)
        # return the pre-req list without including the original given classcode
        return pre_reqs[1:]
    ###########################
    # Elliot's version - END
    ###########################

    def getPreReqs(self, classcode):
        """
        Parameters
        ----------
        classcode : String
            Used to identify classes pre-requisites.

        Returns
        -------
        List of Prerequisites
        """

        indexofnumbers = []

        for i in range(len(classcode)):
            if classcode[i].isdigit():
                indexofnumbers.append(i)

        # Finding First Space Index

        spaceindex = min(indexofnumbers)

        # Inserting Space

        classcode = insert_space(classcode, spaceindex)

        # Setting Temp Variable To Work With

        preReqs = self.excel_in_dict["prereqs"]

        # Filtering By CourseID (needs to be fixed to user preference)

        courseline = preReqs[preReqs["Course"].str.contains(classcode)]

        # Converting To List
        coursedata = courseline.values

        # Extracting First Part/ Cleaning Up
        coursedata = coursedata[0][1::]

        # Iterating Through Data, Cleaning Nan
        cleanedarray = []

        # Cleaning Out All nans
        for i in range(len(coursedata)):
            if (len(str(coursedata[i])) > 3):
                cleanedarray.append(coursedata[i])

        return cleanedarray

    ###################################################
    # Not sure where this is used so i commented it
    # #################################################

    # def getCategory(self, classcode):

    #     # Getting Column Data for Each

    #     math = self.coursegroups['MATH'].values.tolist()
    #     science = self.coursegroups['SCIENCE'].values.tolist()
    #     fundementals = self.coursegroups['FUNDAMENTALS'].values.tolist()
    #     specialized = self.coursegroups["SPECIALIZED"].values.tolist()

    #     # Return results since in.

    #     if classcode in math:
    #         return "MATH"
    #     elif classcode in science:
    #         return "SCIENCE"
    #     elif classcode in fundementals:
    #         return "FUNDAMENTALS"
    #     elif classcode in specialized:
    #         return "SPECIALIZED"
    #     else:
    #         return None

    def validate_tag(self, course_code):
        """
        check if the given course_code exist within the "valid-tag" page of the excel file
        Param:
            course_code : the course code of the course
        Return:
            returns the column header
        """
    # takes the prefix of the course code (EX: SWE4103 -> SWE)
        course_tag = self.get_course_tag(course_code)

        for key, value in self.excel_in_dict["valid-tags"].to_dict(orient="list").items():
            # for each item, if the prefix is in valid-tag or the entire course code (only for CSE-ITS)
            # return the key (course type)
            if course_tag in value or course_code in value:
                return key
        return None

    def is_exception(self, course_code, course_type):
        """
        Checks if the given course_code is in the column of the exception page
            Param:
                course_code : the course code 
                course_type : the course type

            Return:
                Returns a true boolean value if the course type exist and contains the given course code
                else returns false if the course type exist and DOES NOT contains the given course code

                Returns None of the given course_code does not have a valid tag
        """
        # if the given course_tag is not a valid tag
        if course_type is None:
            return None

        for value in self.excel_in_dict["exceptions"].to_dict(orient="list").values():
            if course_code in value:
                return True
        return False

    def get_course_tag(self, course_code):
        """
        Gets the prefix of the course code (EX: SWE4103 -> SWE)

            Param:
                course_code : the course code to get the prefix of

            Return:
                the course tag (EX: given 'SWE4103', it will return 'SWE')
        """
        course_tag = ""
        i = 0
        # takes all characters up to the first digit in the course code
        while course_code is not None and i < len(course_code) and not course_code[i].isdigit():
            course_tag += course_code[i]
            i += 1
        return course_tag

    def is_course_group(self, course_code):
        """
        Returns the course_type if it is found within the 'course-groups' page

            Param:
                course_code : the course code

            Return:
                the course type if the given course code is found within the 'course-groups' page
        """
        for key, value in self.excel_in_dict["course-groups"].to_dict(orient="list").items():
            if course_code in value:
                return key
        return None

    def get_course_type(self, course_code):
        """
        Gets the course type

            Param:
                course_code : the course code

            Return:
                the course type of the given course
        """

        # if is valid tag, and is not in exception, return course type
        if self.validate_tag(course_code) == "NS" and not self.is_exception(course_code, "NS"):
            return "SCIENCE"

        elif self.validate_tag(course_code) == "CSE-ITS" and not self.is_exception(course_code, "CSE-ITS"):
            return "CSE-ITS"

        elif self.validate_tag(course_code) == "CSE-HSS" and not self.is_exception(course_code, "CSE-HSS"):
            return "CSE-HSS"

        elif self.validate_tag(course_code) == "CSE-OPEN" and not self.is_exception(course_code, "CSE-OPEN"):
            return "CSE-OPEN"

        # if the tag is TE, check if its in the course_group first
        elif self.validate_tag(course_code) == "TE" and not self.is_exception(course_code, "TE"):
            # gets the course type from within 'course-groups' page if the given course code is found
            course_group = self.is_course_group(course_code)

            # since it can't validate_tag, check if course is in course_group
            if course_group is not None:
                return course_group
            else:
                return "TE"

        else:
            return None



#####################################################
# Testing the functions within this module only
#####################################################

# This method works both with or without spacing
print(SheetData(excelurl).get_pre_req("ECE 2214"))
print(SheetData(excelurl).get_pre_req("ECE2214"))

# Testing my get course type functions
print(SheetData(excelurl).get_course_type("ECE3221"))  # Specialized
print(SheetData(excelurl).get_course_type("PHYS2505"))  # None
print(SheetData(excelurl).get_course_type("CS4725"))  # TE
print(SheetData(excelurl).get_course_type("HIST3925"))  # CSE-ITS
print(SheetData(excelurl).get_course_type("ENGL10"))  # CSE-HSS
print(SheetData(excelurl).get_course_type("CS1003"))  # None

# Tyler's original method
print(SheetData(excelurl).getPreReqs("ECE2214"))
# ---------------