#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 21:44:25 2021

@author: tylertravis
"""

import pandas as pd

    
# Temporary Course Excel URL
excelurl = 'SWEProgram.xlsx'  

def insert_space(string, integer):
    return string[0:integer] + ' ' + string[integer:]
    
class SheetData:
    def __init__(self, datasheet):
        
        # Declaration
        
        # Declaring Pre-Req Table
        self.dfprereqs = pd.read_excel(open(datasheet, 'rb'), sheet_name='prereqs')
        self.dfprereqs.columns = ["Course", "PreReqs1","PreReqs2","PreReqs3","PreReqs4"]
        
        # Declaring CourseGroup Table
        self.coursegroups = pd.read_excel(open(datasheet, 'rb'), sheet_name = 'course-groups')
        
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
    
    def getCategory(self, classcode):
        
        # Getting Column Data for Each
        
        math = self.coursegroups['MATH'].values.tolist()
        science = self.coursegroups['SCIENCE'].values.tolist()
        fundementals = self.coursegroups['FUNDAMENTALS'].values.tolist()
        specialized = self.coursegroups["SPECIALIZED"].values.tolist()
         
        
        # Return results since in.
        
        if classcode in math:
            return "MATH"
        elif classcode in science:
            return "SCIENCE"
        elif classcode in fundementals:
            return "FUNDAMENTALS"
        elif classcode in specialized:
            return "SPECIALIZED"
        else:
            return None
        

a = SheetData(excelurl)
b = a.getPreReqs("ECE2701")
print(b)



# ---------------


