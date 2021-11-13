#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 21:44:25 2021

@author: tylertravis, Elliot

Last Edit : Elliot, 9.11.2021 8:14PM
"""

import math
import pandas as pd
import os

# Temporary Course Excel URL

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "SWEprogram.xlsx")

def insert_space(string, integer):
    return string[0:integer] + ' ' + string[integer:]

excel_in_dict = {}

# gets the excel file and store it on xls
xls = pd.ExcelFile(filename)

# store each sheet in a dict
# call the sheets by doing "excel_in_dict[sheet_name_to_call]"
for sheet_name in xls.sheet_names:
    excel_in_dict[sheet_name] = xls.parse(sheet_name)

# Declaring Pre-Req Table
excel_in_dict["prereqs"].columns = [
    "Course", "PreReqs1", "PreReqs2", "PreReqs3", "PreReqs4"]

def get_pre_req(classcode):
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
        tag = get_course_tag(classcode)
        # adds spacing in between the class code
        classcode = tag + " " + classcode[len(tag):]

    pre_reqs = []
    # get all the pre-reqs given the course code (in the form of list)

    for item in excel_in_dict["prereqs"].loc[excel_in_dict["prereqs"]["Course"] == classcode].values[0]:
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

# def getPreReqs(, classcode):
#     """
#     Parameters
#     ----------
#     classcode : String
#         Used to identify classes pre-requisites.

#     Returns
#     -------
#     List of Prerequisites
#     """

#     indexofnumbers = []

#     for i in range(len(classcode)):
#         if classcode[i].isdigit():
#             indexofnumbers.append(i)

#     # Finding First Space Index

#     spaceindex = min(indexofnumbers)

#     # Inserting Space

#     classcode = insert_space(classcode, spaceindex)

#     # Setting Temp Variable To Work With

#     preReqs = excel_in_dict["prereqs"]

#     # Filtering By CourseID (needs to be fixed to user preference)

#     courseline = preReqs[preReqs["Course"].str.contains(classcode)]

#     # Converting To List
#     coursedata = courseline.values

#     # Extracting First Part/ Cleaning Up
#     coursedata = coursedata[0][1::]

#     # Iterating Through Data, Cleaning Nan
#     cleanedarray = []

#     # Cleaning Out All nans
#     for i in range(len(coursedata)):
#         if (len(str(coursedata[i])) > 3):
#             cleanedarray.append(coursedata[i])

#     return cleanedarray

def validate_tag(course_code):
    """
    check if the given course_code exist within the "valid-tag" page of the excel file
    Param:
        course_code : the course code of the course
    Return:
        returns the column header
    """
# takes the prefix of the course code (EX: SWE4103 -> SWE)
    course_tag = get_course_tag(course_code)

    if course_tag == "ENGG" or course_code == "ME3232":
        return "FUNDAMENTALS"

    for key, value in excel_in_dict["valid-tags"].to_dict(orient="list").items():
        # for each item, if the prefix is in valid-tag or the entire course code (only for CSE-ITS)
        # return the key (course type)
        if course_tag in value or course_code in value:
            return key
    return None

def is_exception(course_code, course_type):
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

    for value in excel_in_dict["exceptions"].to_dict(orient="list").values():
        if course_code in value:
            return True
    return False

def get_course_tag(course_code):
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

def is_course_group(course_code):
    """
    Returns the course_type if it is found within the 'course-groups' page

        Param:
            course_code : the course code

        Return:
            the course type if the given course code is found within the 'course-groups' page
    """
    for key, value in excel_in_dict["course-groups"].to_dict(orient="list").items():
        if course_code in value:
            return key
    return None

def get_course_type(course_code):
    """
    Gets the course type

        Param:
            course_code : the course code

        Return:
            the course type of the given course
    """
    
    # replace the spacing and * if present
    course_code = course_code.replace("*", "")
    course_code = course_code.replace(" ", "")

    course_type = validate_tag(course_code)

    # if is valid tag, and is not in exception, return course type
    if course_type == "NS" and not is_exception(course_code, "NS"):
        return "SCIENCE"

    elif course_type == "CSE-ITS" and not is_exception(course_code, "CSE-ITS"):
        return "CSE-ITS"

    elif course_type == "CSE-HSS" and not is_exception(course_code, "CSE-HSS"):
        return "CSE-HSS"

    elif course_type == "CSE-OPEN" and not is_exception(course_code, "CSE-OPEN"):
        return "CSE-OPEN"
    
    elif course_type == "FUNDAMENTALS" and is_course_group(course_code) == "FUNDAMENTALS":
        return "FUNDAMENTALS"

    # if the tag is TE, check if its in the course_group first
    elif validate_tag(course_code) == "TE" and not is_exception(course_code, "TE"):
        # gets the course type from within 'course-groups' page if the given course code is found
        course_group = is_course_group(course_code)
        
        if course_group is not None:
            return course_group
        else:
            # since its not in the course group, but validate_tag is under "TE", return TE instead
            return "TE"
    else:
        return None
