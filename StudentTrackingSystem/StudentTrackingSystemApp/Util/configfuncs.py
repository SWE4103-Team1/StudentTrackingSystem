#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 21:44:25 2021

@author: tylertravis, Elliot

Last Edit : Elliot, 9.11.2021 10:22AM
"""

import math

import pandas as pd

# Temporary Course Excel URL
excelurl = 'SWEProgram.xlsx'


def insert_space(string, integer):
    return string[0:integer] + ' ' + string[integer:]


class SheetData:
    def __init__(self, datasheet):

        # Declaration
        # Declaring Pre-Req Table
        self.dfprereqs = pd.read_excel(
            datasheet, sheet_name="prereqs")
        self.dfprereqs.columns = [
            "Course", "PreReqs1", "PreReqs2", "PreReqs3", "PreReqs4"]

        self.prereqs = pd.read_excel(
            datasheet, sheet_name="prereqs")

        # Declearing exception nad valid tags
        self.exceptions = pd.read_excel(
            datasheet, sheet_name="exceptions").to_dict(orient="list")
        self.valid_tags = pd.read_excel(
            datasheet, sheet_name="valid-tags").to_dict(orient="list")

        # Declaring CourseGroup Table
        self.course_groups = pd.read_excel(
            datasheet, sheet_name='course-groups').to_dict(orient="list")

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
        for item in self.prereqs.loc[self.prereqs["Course"] == classcode].values[0]:
            try:
                # since each pre-req is returned in the form of a list, so i only take the first element from 'item'
                # if the element is nan, this would be true, else it would throw an exception
                if math.isnan(item):
                    continue
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

        preReqs = self.dfprereqs

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
        for key, value in self.valid_tags.items():
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

        if course_code in self.exceptions[course_type]:
            return True
        else:
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
        for key, value in self.course_groups.items():
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
        elif self.validate_tag(course_code) == "TE" and not self.is_exception(course_code, "TE"):
            return "TE"

        else:
            # gets the course type from within 'course-groups' page if the given course code is found
            course_group = self.is_course_group(course_code)
            # since it can't validate_tag, check if course is in course_group
            if course_group is not None:
                return course_group
            else:
                return None


# This method works both with or without spacing
print(SheetData(excelurl).get_pre_req("ECE 2214"))
print(SheetData(excelurl).get_pre_req("ECE2214"))

# Your original method
print(SheetData(excelurl).getPreReqs("ECE2214"))

# ---------------
