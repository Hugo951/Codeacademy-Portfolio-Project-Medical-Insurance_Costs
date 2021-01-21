# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:32:02 2021

@author: jouko
"""
# import csv reader
from csv import reader

# establish lists for different data
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

# read "insurance.csv" file as a list of lists  
with open('C:\DATA SCIENCE\PYTHON\PROJECT\PORTFOLIO PROJECT_US Medical Insurance Costs\python-portfolio-project-starter-files\insurance.csv', newline='') as insurance_csv:
  insurance_reader = reader(insurance_csv)
  list_of_rows = list(insurance_reader)
  for item in list_of_rows:
      # skip header information
      if item[0] == 'age' or item[1] == 'sex' or item[2] == bmi or item[3] == children or item[4] == smoker or item[5] == region or item[6] == charges:
          pass
      # add information to named lists
      else:
          age.append(item[0])
          sex.append(item[1])
          bmi.append(item[2]) 
          children.append(item[3])
          smoker.append(item[4])
          region.append(item[5])
          charges.append(item[6])

# will be checked len = number of patient (1338)    
print(len(age))
print(len(sex))
print(len(bmi))
print(len(children))
print(len(smoker))
print(len(region))
print(charges)

# function for averaging
def avg_data(lst):
    sum_of_lst = 0
    avg_lst = 0
    for value in lst:
        sum_of_lst += float(value)
    avg_lst = sum_of_lst / len(lst)
    return avg_lst, sum_of_lst

# the averages are stored in the variables
avg_age = avg_data(age)
avg_bmi = avg_data(bmi)
avg_charges = avg_data(charges)

# (39.21, 30.66, 13270.42)
print(avg_age, avg_bmi, avg_charges)

# comparing insurance costs between smokers and non-smokers  
# function for combining 2 lists to dict and add the values
def dict_data(lst1, lst2):
    res = {}
    for i in range(len(lst1)):
        if lst1[i] not in res:
            res[lst1[i]] = float(lst2[i])
        else:
            res[lst1[i]] += float(lst2[i])
    return res

# dict for smokers and non-smokers insurance costs
smoke = dict_data(smoker, charges)

# count number of smokers and non-smokers
number_of_smokers = smoker.count('yes')
number_of_non_smokers = smoker.count('no')

# count smokers and non-smokers average insurance costs
smokers_avg_charges = smoke['yes'] / number_of_smokers
non_smokers_avg_charges = smoke['no'] / number_of_non_smokers
              
print(smokers_avg_charges, non_smokers_avg_charges)

# dict for insurance costs by location
location_data = dict_data(region, charges)

print(location_data)

# count number of people in defferent locations
number_of_southwest_people = region.count('southwest')
number_of_southeast_people = region.count('southeast')
number_of_northwest_people = region.count('northwest')
number_of_northeast_people = region.count('northeast')

# count average insurance costs by locations
southwest_avg_charges = location_data['southwest'] / number_of_southwest_people
southeast_avg_charges = location_data['southeast'] / number_of_southeast_people
northwest_avg_charges = location_data['northwest'] / number_of_northwest_people
northeast_avg_charges = location_data['northeast'] / number_of_northeast_people
 
print(southeast_avg_charges, southwest_avg_charges, northeast_avg_charges, northwest_avg_charges)

def dict_data2(lst3, lst4):
    children_data = {}
    count = {}
    avg_data2 = {}
    for i in range(len(lst4)):
        if lst3[i] not in children_data:
            children_data[lst3[i]] = float(lst4[i])
            count[lst3[i]] = 1
        else:
            children_data[lst3[i]] += float(lst4[i])
            count[lst3[i]] += 1
            avg_data2[lst3[i]] = children_data[lst3[i]] / count[lst3[i]] 
    return avg_data2
               
avg_bmi_per_child = dict_data2(children, bmi)
avg_charges_per_child = dict_data2(children, charges)
    
print(avg_bmi_per_child)
print(avg_charges_per_child)  
    
    
    

