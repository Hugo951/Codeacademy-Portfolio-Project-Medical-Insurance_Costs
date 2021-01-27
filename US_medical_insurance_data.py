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

def data_dict(age, sex, bmi, children, smoker, region, charges): 
    datas = {}
    for i in range(len(age)): 
        datas[i] = {"Age": age[i], "Sex": sex[i], "Bmi": bmi[i], "Children": children[i],
                       "Smoker": smoker[i], "Region": region[i], "Charges": charges[i]} 
    return datas

dd = data_dict(age, sex, bmi, children, smoker, region, charges)

# function for calculating average value
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

# print average, minimum and maximum values for age, bmi and charges
print("Average age: " + str(avg_age) + ", Minimum age: " + str(min(age)) + 
      ", Maximum age: " + str(max(age)))
print("Average bmi: " + str(avg_bmi) + ", Minimum bmi: " + str(min(bmi_lst)) +
      ", Maximum bmi: " + str(max(bmi_lst)))
print("Average charges: " + str(avg_charges) + ", Minimum charges: " + str(min(charges_lst)) +
      ", Maximum charges: " + str(max(charges_lst)))

# comparing insurance costs between smokers and non-smokers  
# function for combining 2 lists to dict and add the values
def smoker_data(dd):
    smoker_dict = {}
    for k in dd:
        if dd[k]['Smoker'] not in smoker_dict:
            smoker_dict[dd[k]['Smoker']] = float(dd[k]['Charges'])
        else:
            smoker_dict[dd[k]['Smoker']] += float(dd[k]['Charges'])
    return smoker_dict

# dict for smokers and non-smokers charges
smoke = smoker_data(dd)

# count smokers and non-smokers average chargers
smokers_avg_charges = smoke['yes'] / smoker.count('yes')
non_smokers_avg_charges = smoke['no'] / smoker.count('no')
              
print("Smokers average charges: " + str(smokers_avg_charges) + 
      ", Non-smokers average charges: " + str(non_smokers_avg_charges))

def sex_data(dd):
    num_of_smoker_female = 0
    num_of_non_smoker_female = 0
    num_of_smoker_male = 0
    num_of_non_smoker_male = 0
    charges_of_smoker_female = 0
    charges_of_non_smoker_female = 0
    charges_of_smoker_male = 0
    charges_of_non_smoker_male = 0
    for k in dd:
        if dd[k]['Sex'] == "female" and dd[k]['Smoker'] == 'yes':
            num_of_smoker_female += 1 
            charges_of_smoker_female += float(dd[k]['Charges'])
        elif dd[k]['Sex'] == "female" and dd[k]['Smoker'] == 'no':
            num_of_non_smoker_female += 1
            charges_of_non_smoker_female += float(dd[k]['Charges'])
        elif dd[k]['Sex'] == "male" and dd[k]['Smoker'] == 'yes':
            num_of_smoker_male += 1
            charges_of_smoker_male += float(dd[k]['Charges'])
        elif dd[k]['Sex'] == "male" and dd[k]['Smoker'] == 'no':
            num_of_non_smoker_male += 1
            charges_of_non_smoker_male += float(dd[k]['Charges'])
    return num_of_smoker_female, num_of_non_smoker_female, num_of_smoker_male, num_of_non_smoker_male, charges_of_smoker_female, charges_of_non_smoker_female, charges_of_smoker_male, charges_of_non_smoker_male

nosfe, nonsfe, nosm, nonsm, cosf, consf, cosm, consm = sex_data(dd)

print("Number of smoker female: " + str(nosfe) + " and their avarage charges is: " + str(cosf/nosfe) + "\n" +
      "Number of non-smoker female: " + str(nonsfe) + " and their avarage charges is: " + str(consf/nonsfe) + "\n" +
      "Number of smoker male: " + str(nosm) + " and their avarage charges is: " + str(cosm/nosm) + "\n" +
      "Number of non-smoker nmale: " + str(nonsm) + " and their avarage charges is: " + str(consm/nonsm))

def location_data(region, charges):
    location_tuple = list(zip(region, charges))
    sw_charge = []
    se_charge = []
    nw_charge = []
    ne_charge = []
    for i in location_tuple:
        if i[0] == 'southwest':
            sw_charge.append(float(i[1]))
        elif i[0] == 'souteast':
            se_charge.append(float(i[1]))
        elif i[0] == 'northwest':
            nw_charge.append(float(i[1]))
        elif i[0] == 'northeast':
            ne_charge.append(float(i[1]))
    return sw_charge, se_charge, nw_charge, ne_charge

sw_charges, se_charges, nw_charges, ne_charges = location_data(region, charges)
 
print("Southeast number of people: "+ str(len(se_charges)) + " and average charges: " + str(sum(se_charges) / len(se_charges)) + "\n" +
      "Southeast min charges: " + str(min(se_charges)) + " and max charges: " + str(min(se_charges)) + "\n" +
      "Southwest number of people: "+ str(len(sw_charges)) + " and average charges: " + str(sum(sw_charges) / len(sw_charges)) + "\n" +
      "Southwest min charges: " + str(min(sw_charges)) + " and max charges: " + str(min(sw_charges)) + "\n" +
      "Northeast number of people: "+ str(len(ne_charges)) + " and average charges: " + str(sum(ne_charges) / len(ne_charges)) + "\n" +
      "Northeast min charges: " + str(min(ne_charges)) + " and max charges: " + str(min(ne_charges)) + "\n" +
      "Northwest number of people: "+ str(len(nw_charges)) + " and average charges: " + str(sum(nw_charges) / len(nw_charges)) + "\n" +
      "orthwest min charges: " + str(min(nw_charges)) + " and max charges: " + str(min(nw_charges)))



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



 
 
 
    
    
    

