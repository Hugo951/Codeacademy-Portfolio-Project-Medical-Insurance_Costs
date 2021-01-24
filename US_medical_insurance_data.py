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

# check lens = number of patient (1338)    
print(len(age))
print(len(sex))
print(len(bmi))
print(len(children))
print(len(smoker))
print(len(region))
print(len(charges))

# function for averaging
def avg_data(lst):
    sum_of_lst = 0
    avg_lst = 0
    for value in lst:
        sum_of_lst += float(value)
    avg_lst = sum_of_lst / len(lst)
    return avg_lst

# the averages are stored in the variables
avg_age = avg_data(age)
avg_bmi = avg_data(bmi)
avg_charges = avg_data(charges)
# convert string to float
bmi_lst = [float(i) for i in bmi]
charges_lst = [float(i) for i in charges]

# print average, minimum and maximum vealues for age, bmi and charges
print("Average age: " + str(avg_age) + ", Minimum age: " + str(min(age)) + 
      ", Maximum age: " + str(max(age)))
print("Average bmi: " + str(avg_bmi) + ", Minimum bmi: " + str(min(bmi_lst)) +
      ", Maximum bmi: " + str(max(bmi_lst)))
print("Average charges: " + str(avg_charges) + ", Minimum charges: " + str(min(charges_lst)) +
      ", Maximum charges: " + str(max(charges_lst)))

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

# dict for smokers and non-smokers charges
smoke = dict_data(smoker, charges)

# count smokers and non-smokers average chargers
smokers_avg_charges = smoke['yes'] / smoker.count('yes')
non_smokers_avg_charges = smoke['no'] / smoker.count('no')
              
print("Smokers average charges: " + str(smokers_avg_charges) + 
      ", Non-smokers average charges: " + str(non_smokers_avg_charges))

# dict for chargers by location
location_data = dict_data(region, charges)

# count average chargers by locations
southwest_avg_charges = location_data['southwest'] / region.count('southwest')
southeast_avg_charges = location_data['southeast'] / region.count('southeast')
northwest_avg_charges = location_data['northwest'] / region.count('northwest')
northeast_avg_charges = location_data['northeast'] / region.count('northeast')
 
print("Southeast average charges: "+ str(southeast_avg_charges) + 
      ", Southwest average charges: " + str(southwest_avg_charges) + 
      ", Northeast average charges: " + str(northeast_avg_charges) +
      ", Northwest average charges: " + str(northwest_avg_charges))

# average charges for different numbers of children   
# function for combining 2 lists to dict and add the values 
def children_data(lst3, lst4):
    child_data = {}
    count = {}
    avg_data2 = {}
    for i in range(len(lst4)):
        if lst3[i] not in child_data:
            child_data[lst3[i]] = float(lst4[i])
            count[lst3[i]] = 1
        else:
            child_data[lst3[i]] += float(lst4[i])
            count[lst3[i]] += 1
            avg_data2[lst3[i]] = child_data[lst3[i]] / count[lst3[i]] 
    return (avg_data2, count)

# dict for average bmi of different numbers of children and number of people       
avg_bmi_per_child, people_count_bmi = children_data(children, bmi)
# dict for average chargers of different numbers of children and number of people 
avg_charges_per_child, people_count_ch = children_data(children, charges)

# print results for average bmi and chargers 
# and number of people of different number of children
for k in sorted(avg_bmi_per_child):
    print("Number of children: " + k + ", average bmi: " + str(avg_bmi_per_child[k]) + 
          ", average charges: " + str(avg_charges_per_child[k]) + ", number of people: " 
          + str(people_count_bmi[k]))
 



 
 
    
    
    

