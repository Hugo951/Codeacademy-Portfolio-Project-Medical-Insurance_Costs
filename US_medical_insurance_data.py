# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:32:02 2021

@author: jouko
"""

import csv

age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

def insurance_data(total_data, column):
  with open('C:\DATA SCIENCE\PYTHON\PROJECT\PORTFOLIO PROJECT_US Medical Insurance Costs\python-portfolio-project-starter-files\insurance.csv', newline='') as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        total_data.append(row[column])
  return total_data

insurance_data(age,'age')
insurance_data(age,'sex')
insurance_data(age,'bmi')
insurance_data(age,'children')
insurance_data(age,'smoker')
insurance_data(age,'region')
insurance_data(age,'charges')

        
print(age)

        
        
      


      

      
  
