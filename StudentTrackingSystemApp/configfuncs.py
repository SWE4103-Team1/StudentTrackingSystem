#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 21:44:25 2021

@author: tylertravis, Elliot

"""

import math
import pandas as pd
import re

# Temporary Course Excel URL

excel_in_dict = {}
xls = None


def set_config_file(filename):
    """
    Sets the global variable to the config file

        Param:
            filename : the config file
    """
    global xls

    xls = pd.ExcelFile(filename)

    # store each sheet in a dict
    # call the sheets by doing "excel_in_dict[sheet_name_to_call]"
    for sheet_name in xls.sheet_names:
        excel_in_dict[sheet_name] = xls.parse(sheet_name)


def config_file_exist():
    """
    returns a boolean vlaue of whether the config excel file have been uploaded first
    """
    return xls != None


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
        tag = _get_course_tag(classcode)
        # adds spacing in between the class code
        classcode = tag + " " + classcode[len(tag):]

    pre_reqs = []
    # get all the pre-reqs given the course code (in the form of list)

    for item in (excel_in_dict["prereqs"].loc[
            excel_in_dict["prereqs"]["Course"] == classcode].values[0]):
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

    # check for replacements first
    temp = _get_replacements(course_code)
    # if a replacment is found, overwrite the course_code for the replacment code
    if temp is not None:
        course_code = temp

    course_type = _validate_tag(course_code)

    if _is_core(course_code):
        return "CORE"

    # special case for CSE-HSS courses, since they overlap with CSE-OPEN courses
    # if its an exception for either CSE-HSS or CSE-ITS, but is is not an exception for CSE-OPEN, return CSE-OPEN instead
    if course_type == "CSE-HSS" or course_type == "CSE-ITS":
        if (_is_exception(course_code, "CSE-ITS") or _is_exception(course_code, "CSE-HSS")) and not _is_exception(course_code, "CSE-OPEN"):
            return "CSE-OPEN"

    # if its a valid tag and is not in the exceptions list
    if _is_exception(course_code, course_type):
        return None
    else:
        return course_type


def _validate_tag(course_code):
    """
    check if the given course_code exist within the "valid-tag" page of the excel file
    Param:
        course_code : the course code of the course
    Return:
        returns the column header
    """

    # takes the prefix of the course code (EX: SWE4103 -> SWE)
    course_tag = _get_course_tag(course_code)

    for key, value in excel_in_dict["valid-tags"].to_dict(
            orient="list").items():
        # for each item, if the prefix is in valid-tag or the entire course code (only for CSE-ITS)
        # return the key (course type)
        if course_tag in value or course_code in value:
            return key
    return None


def _is_exception(course_code, course_type):
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

    return course_code in excel_in_dict["exceptions"][course_type].to_list()


def _get_course_tag(course_code):
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
    while (course_code is not None and i < len(course_code)
           and not course_code[i].isdigit()):
        course_tag += course_code[i]
        i += 1
    return course_tag


def _get_matrix_courses(matrix_year):
    """
    returns a list of core courses found within the given year matrix

    Param:
        matrix_year : the pear of the matrix to search

    Returns:
        the list of courses within the matrix
    """
    core_courses = []
    matrix = excel_in_dict[matrix_year]

    for i, row in matrix.iterrows():
        for j, value in row.items():
            if type(value) is not float and type(value) is str:
                value = value.replace(" ", "")
                course_codes_only = re.findall(r"\b[A-Z]{2,4}[0-9]{2,4}\b",
                                               str(value))
                if not not course_codes_only:
                    core_courses += (course_codes_only)

    return core_courses


def _get_all_cores(year=None):
    """
    Returns all the core courses based on the given year, else return all core courses

        Param:
            year : the year to return the core courses found in the matrix
                    (leave blank for all the core corses for existing matrix)

        Return:
            the core courses found within the given year matrix
            (all core courses found within the config file if year is None)
    """

    # if you enter the year 2015, it will replace it to 2015-16
    if year is not None and '-' not in year:
        year += "-" + str(int(year[1:]) + 1)

    keys = []
    cores = {}

    for sheet_name in excel_in_dict:
        # check if the sheet name is the matrix year
        if '-' in sheet_name and len(
                sheet_name) == 7 and sheet_name is not None:
            keys.append(sheet_name)

    # use the matrix years as key for the dict
    for key in keys:
        cores[key] = _get_matrix_courses(key)

    if year is not None:
        return cores[year]

    return cores


def _is_core(course_code, year=None):
    """
    Returns a boolean value if the course_code is within a specific year's matrix, or in any of the matrices

        Param:
            course_code : the course_code to check 
            year : the year of the matrix to check in

        Return:
            The boolean value if the course_code is found within the matrix
    """

    cores = _get_all_cores(year)

    all_courses = []

    # if the year is not given, combine all the courses from all the matrices
    if year is None:
        for courses in cores.values():
            all_courses += courses

        return course_code in all_courses
    # else if a year is given, only return the list of courses within that year's matrix
    else:
        return course_code in cores


def _get_replacements(course_code):
    """
    Returns the equivalent course for the given course_code

        Param:
            course_code : the course code to find the replacements

        Return:
            the equivalent course code of the given course_code if found in the replacement sheet
    """

    # fix the formatting of course_code
    course_code = course_code.replace(" ", "")
    course_code = course_code.replace("*", "")

    # gets the replacement sheet
    replacement_sheet = excel_in_dict['replacements']

    # converts all the replacments to a dict
    all_years = replacement_sheet.set_index(
        'ALL YEARS')['Unnamed: 1'].to_dict()
    before_19 = replacement_sheet.set_index(
        'Before 2019')['Unnamed: 3'].to_dict()

    # combine all the replacment dict to a single dict
    all_years.update(before_19)

    # check each value in the dict, if a replacment is found, return the key (replacement course code)
    for key, value in all_years.items():
        if type(value) is not float:
            if course_code in value:
                return key

    return None
