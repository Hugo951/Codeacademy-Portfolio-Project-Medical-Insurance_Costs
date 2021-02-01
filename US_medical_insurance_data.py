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

# dict to which all the information is combined
def data_dict(age, sex, bmi, children, smoker, region, charges): 
    datas = {}
    for i in range(len(age)): 
        datas[i] = {"Age": age[i], "Sex": sex[i], "Bmi": bmi[i], "Children": children[i],
                       "Smoker": smoker[i], "Region": region[i], "Charges": charges[i]} 
    return datas

# store all the information in the dict variable dd
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
print("AGE: " + "\n" +
      " - Average age: " + str(avg_age) + "\n" +
      " - Minimum age: " + str(min(age)) + "\n" +
      " - Maximum age: " + str(max(age)) + "\n" +
      "BMI: " + "\n" +
      " - Average bmi: " + str(avg_bmi) + "\n" +
      " - Minimum bmi: " + str(min(bmi_lst)) + "\n" +
      " - Maximum bmi: " + str(max(bmi_lst)) + "\n" +
      "CHARGES: " + "\n" +
      " - Average charges: " + str(avg_charges) +"\n" +
      " - Minimum charges: " + str(min(charges_lst)) + "\n" +
      " - Maximum charges: " + str(max(charges_lst)))

# compare insurance costs between smokers and non-smokers  
# function for combining 2 lists to dict and add the values
def smoker_data(dd):
    smoker_dict = {}
    smoker_min_ch = 1000000
    smoker_max_ch = 0
    non_smoker_min_ch = 1000000
    non_smoker_max_ch = 0
    for k in dd:
        if dd[k]['Smoker'] not in smoker_dict:
            smoker_dict[dd[k]['Smoker']] = float(dd[k]['Charges'])
            if dd[k]['Smoker'] == 'yes'and float(dd[k]['Charges']) < smoker_min_ch:
                smoker_min_ch = float(dd[k]['Charges'])
            if dd[k]['Smoker'] == 'yes'and float(dd[k]['Charges']) > smoker_max_ch:
                smoker_max_ch = float(dd[k]['Charges'])
            if dd[k]['Smoker'] == 'no'and float(dd[k]['Charges']) < non_smoker_min_ch:
                non_smoker_min_ch = float(dd[k]['Charges'])
            if dd[k]['Smoker'] == 'no'and float(dd[k]['Charges']) > non_smoker_max_ch:
                non_smoker_max_ch = float(dd[k]['Charges'])        
        else:
            smoker_dict[dd[k]['Smoker']] += float(dd[k]['Charges'])
            if dd[k]['Smoker'] == 'yes'and float(dd[k]['Charges']) < smoker_min_ch:
                smoker_min_ch = float(dd[k]['Charges'])
            if dd[k]['Smoker'] == 'yes'and float(dd[k]['Charges']) > smoker_max_ch:
                smoker_max_ch = float(dd[k]['Charges'])
            if dd[k]['Smoker'] == 'no'and float(dd[k]['Charges']) < non_smoker_min_ch:
                non_smoker_min_ch = float(dd[k]['Charges'])
            if dd[k]['Smoker'] == 'no'and float(dd[k]['Charges']) > non_smoker_max_ch:
                non_smoker_max_ch = float(dd[k]['Charges']) 
    return smoker_dict, smoker_min_ch, smoker_max_ch, non_smoker_min_ch, non_smoker_max_ch

# dict for smokers and non-smokers charges
smoke, smic, smac, nsmic, nsmac = smoker_data(dd)

# count smokers and non-smokers average chargers
smokers_avg_charges = smoke['yes'] / smoker.count('yes')
non_smokers_avg_charges = smoke['no'] / smoker.count('no')

# print results of smokers and non-smokers average charges          
print("Smokers: " + "\n" +
      " - num of people: " + str(smoker.count('yes')) + "\n" +
      " - min charge: " + str(smic) + "\n" +
      " - max charge: " + str(smac) + "\n" +
      " - average charges: " + str(smokers_avg_charges) + "\n" +
      "Non-smokers: " + "\n" +
      " - num of people: " + str(smoker.count('no')) + "\n" +
      " - min charge: " + str(nsmic) + "\n" +
      " - max charge: " + str(nsmac) + "\n" +
      " - average charges: " + str(non_smokers_avg_charges) + "\n")

# compare charges (min, max, average) and number of people for both smoker/non-smoker female and men 
# function for combining dd dict and add the values
def sex_data(dd):
    num_of_smoker_female = 0
    num_of_non_smoker_female = 0
    num_of_smoker_male = 0
    num_of_non_smoker_male = 0
    charges_of_smoker_female = 0
    charges_of_non_smoker_female = 0
    charges_of_smoker_male = 0
    charges_of_non_smoker_male = 0
    min_charges_of_smoker_female = 100000
    max_charges_of_smoker_female = 0
    min_charges_of__non_smoker_female = 100000
    max_charges_of_non_smoker_female = 0
    min_charges_of_smoker_male = 100000
    max_charges_of_smoker_male = 0
    min_charges_of_non_smoker_male = 100000
    max_charges_of_non_smoker_male = 0
    for k in dd:
        if dd[k]['Sex'] == "female" and dd[k]['Smoker'] == 'yes':
            num_of_smoker_female += 1 
            charges_of_smoker_female += float(dd[k]['Charges'])
            if float(dd[k]['Charges']) < min_charges_of_smoker_female:
                min_charges_of_smoker_female = float(dd[k]['Charges'])
            if float(dd[k]['Charges']) > max_charges_of_smoker_female: 
                max_charges_of_smoker_female = float(dd[k]['Charges'])
        elif dd[k]['Sex'] == "female" and dd[k]['Smoker'] == 'no':
            num_of_non_smoker_female += 1
            charges_of_non_smoker_female += float(dd[k]['Charges'])
            if float(dd[k]['Charges']) < min_charges_of__non_smoker_female:
                min_charges_of__non_smoker_female = float(dd[k]['Charges'])
            if float(dd[k]['Charges']) > max_charges_of_non_smoker_female: 
                max_charges_of_non_smoker_female = float(dd[k]['Charges'])
        elif dd[k]['Sex'] == "male" and dd[k]['Smoker'] == 'yes':
            num_of_smoker_male += 1
            charges_of_smoker_male += float(dd[k]['Charges'])
            if float(dd[k]['Charges']) < min_charges_of_smoker_male:
                min_charges_of_smoker_male = float(dd[k]['Charges'])
            if float(dd[k]['Charges']) > max_charges_of_smoker_male: 
                max_charges_of_smoker_male = float(dd[k]['Charges'])  
        elif dd[k]['Sex'] == "male" and dd[k]['Smoker'] == 'no':
            num_of_non_smoker_male += 1
            charges_of_non_smoker_male += float(dd[k]['Charges'])
            if float(dd[k]['Charges']) < min_charges_of_non_smoker_male:
                min_charges_of_non_smoker_male = float(dd[k]['Charges'])
            if float(dd[k]['Charges']) > max_charges_of_non_smoker_male: 
                max_charges_of_non_smoker_male = float(dd[k]['Charges'])
            
    return num_of_smoker_female, num_of_non_smoker_female, num_of_smoker_male, num_of_non_smoker_male, charges_of_smoker_female, charges_of_non_smoker_female, charges_of_smoker_male, charges_of_non_smoker_male, min_charges_of_smoker_female, max_charges_of_smoker_female, min_charges_of__non_smoker_female, max_charges_of_non_smoker_female, min_charges_of_smoker_male, max_charges_of_smoker_male, min_charges_of_non_smoker_male, max_charges_of_non_smoker_male

# store results of both smoker/non-smoker female and men in the variables 
nosfe, nonsfe, nosm, nonsm, cosf, consf, cosm, consm, min_cosf, max_cosf, min_consf, max_consf, min_cosm, max_cosm, min_consm, max_consm  = sex_data(dd)

# print results for both smoker/non-smoker female and men
print("Smoker female: " + "\n" +
      " - number of people: " + str(nosfe) + "\n" +
      " - avarage charges: " + str(cosf/nosfe) + "\n" +
      " - min charge: " + str(min_cosf) + "\n" +
      " - max charge: " + str(max_cosf) + "\n" +
      "Non-smoker female: " + "\n" +
      " - number of people: " + str(nonsfe) + "\n" +
      " - avarage charges: " + str(consf/nonsfe) + "\n" +
      " - min charge: " + str(min_consf) + "\n" +
      " - max charge: " + str(max_consf) + "\n" +
      "Smoker male: " + "\n" +
      " - number of people: " + str(nosm) + "\n" +
      " - avarage charges: " + str(cosm/nosm) + "\n" +
      " - min charge: " + str(min_cosm) + "\n" +
      " - max charge: " + str(max_cosm) + "\n" +
      "Non-smoker nmale: " + "\n" +
      " - number of people: " + str(nonsm) + "\n" +
      " - avarage charges: " + str(consm/nonsm) + "\n" +
      " - min charge: " + str(min_consm) + "\n" +
      " - max charge: " + str(max_consm) + "\n")

# function for comparing charges by location
def location_data(region, charges):
    location_tuple = list(zip(region, charges))
    sw_charge = []
    se_charge = []
    nw_charge = []
    ne_charge = []
    for i in location_tuple:
        if i[0] == 'southwest':
            sw_charge.append(float(i[1]))
        elif i[0] == 'southeast':
            se_charge.append(float(i[1]))
        elif i[0] == 'northwest':
            nw_charge.append(float(i[1]))
        elif i[0] == 'northeast':
            ne_charge.append(float(i[1]))
    return sw_charge, se_charge, nw_charge, ne_charge

# store results of charges by location in the variables
sw_charges, se_charges, nw_charges, ne_charges = location_data(region, charges)
 
# print different results by location 
print("Southeast: " + "\n" +
      " - number of people: " + str(len(se_charges)) + "\n" +
      " - average charges: " + str(sum(se_charges) / len(se_charges)) + " \n" +
      " - min charges: " + str(min(se_charges)) + " \n" +
      " - max charges: " + str(max(se_charges)) + "\n" +
      "Southwest: " + "\n" +
      " - number of people: " + str(len(sw_charges)) + "\n" +
      " - average charges: " + str(sum(sw_charges) / len(sw_charges)) + " \n" +
      " - min charges: " + str(min(sw_charges)) + " \n" +
      " - max charges: " + str(max(sw_charges)) + "\n" +
      "Northeast: " + "\n" +
      " - number of people: " + str(len(ne_charges)) + "\n" +
      " - average charges: " + str(sum(ne_charges) / len(ne_charges)) + " \n" +
      " - min charges: " + str(min(ne_charges)) + " \n" +
      " - max charges: " + str(max(ne_charges)) + "\n" +
      "Northwest: " + "\n" +
      " - number of people: " + str(len(nw_charges)) + "\n" +
      " - average charges: " + str(sum(nw_charges) / len(nw_charges)) + " \n" +
      " - min charges: " + str(min(nw_charges)) + " \n" +
      " - max charges: " + str(max(nw_charges)) + "\n")
      

# min, max and average values for different numbers of children   
# function for combining 2 lists to dict and add the values 
def children_data(lst3, lst4):
    child_data = {}
    count = {}
    avg_data2 = {}
    min_value = {}
    max_value = {}
    for i in range(len(lst4)):
        if lst3[i] not in child_data:
            child_data[lst3[i]] = float(lst4[i])
            count[lst3[i]] = 1
            min_value[lst3[i]] = float(lst4[i])
            max_value[lst3[i]] = float(lst4[i])                                    
        else:
            child_data[lst3[i]] += float(lst4[i])
            count[lst3[i]] += 1
            if lst3[i] == '0' and float(lst4[i]) < min_value['0']:
                min_value['0'] = float(lst4[i])
            if lst3[i] == '0' and float(lst4[i]) > max_value['0']:
                max_value['0'] = float(lst4[i])
            if lst3[i] == '1' and float(lst4[i]) < min_value['1']:
                min_value['1'] = float(lst4[i])
            if lst3[i] == '1' and float(lst4[i]) > max_value['1']:
                max_value['1'] = float(lst4[i])
            if lst3[i] == '2' and float(lst4[i]) < min_value['2']:
                min_value['2'] = float(lst4[i])
            if lst3[i] == '2' and float(lst4[i]) > max_value['2']:
                max_value['2'] = float(lst4[i])
            if lst3[i] == '3' and float(lst4[i]) < min_value['3']:
                min_value['3'] = float(lst4[i])
            if lst3[i] == '3' and float(lst4[i]) > max_value['3']:
                max_value['3'] = float(lst4[i])
            if lst3[i] == '4' and float(lst4[i]) < min_value['4']:
                min_value['4'] = float(lst4[i])
            if lst3[i] == '4' and float(lst4[i]) > max_value['4']:
                max_value['4'] = float(lst4[i])
            if lst3[i] == '5' and float(lst4[i]) < min_value['5']:
                min_value['5'] = float(lst4[i])
            if lst3[i] == '5' and float(lst4[i]) > max_value['5']:
                max_value['5'] = float(lst4[i])
            avg_data2[lst3[i]] = child_data[lst3[i]] / count[lst3[i]] 
    return avg_data2, count, min_value, max_value

# dict for min, max and average bmi of different numbers of children and number of people       
avg_bmi_per_child, people_count_bmi, min_bmi, max_bmi = children_data(children, bmi)
# dict for min, max and average chargers of different numbers of children and number of people 
avg_charges_per_child, people_count_ch, min_ch, max_ch = children_data(children, charges)

# print results for min bmi, max bmi, average bmi, min chargers, max charges and average charges 
# and number of people of different number of children
for k in sorted(avg_bmi_per_child):
    print("Number of children: " + k + "\n" +
          " - min bmi: " + str(min_bmi[k]) + "\n" +
          " - max bmi: " + str(max_bmi[k]) + "\n" +
          " - average bmi: " + str(avg_bmi_per_child[k]) + "\n" +
          " - min charge: " + str(min_ch[k]) + "\n" +
          " - max charge: " + str(max_ch[k]) + "\n" +
          " - average charge: " + str(avg_charges_per_child[k]) + "\n" +
          " - number of people: " + str(people_count_bmi[k]))
    

# function for combining dd dict and add the values
def age_data(dd):
    smoker_female_age_20 = []
    smoker_female_age_30 = []
    smoker_female_age_40 = []
    smoker_female_age_50 = []
    smoker_female_age_60 = []
    smoker_female_age_over_60 = []
    sf_data = [[] for _ in range(6)]
    non_smoker_female_age_20 = []
    non_smoker_female_age_30 = []
    non_smoker_female_age_40 = []
    non_smoker_female_age_50 = []
    non_smoker_female_age_60 = []
    non_smoker_female_age_over_60 = []
    nsf_data = [[] for _ in range(6)]
    smoker_male_age_20 = []
    smoker_male_age_30 = []
    smoker_male_age_40 = []
    smoker_male_age_50 = []
    smoker_male_age_60 = []
    smoker_male_age_over_60 = []
    sm_data = [[] for _ in range(6)]
    non_smoker_male_age_20 = []
    non_smoker_male_age_30 = []
    non_smoker_male_age_40 = []
    non_smoker_male_age_50 = []
    non_smoker_male_age_60 = []
    non_smoker_male_age_over_60 = []
    nsm_data = [[] for _ in range(6)]
    for k in dd:
        if dd[k]['Sex'] == "female" and dd[k]['Age'] <= '20' and dd[k]['Smoker'] == 'yes':
            smoker_female_age_20.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] <= '30' and dd[k]['Smoker'] == 'yes':
            smoker_female_age_30.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] <= '40' and dd[k]['Smoker'] == 'yes':
            smoker_female_age_40.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] <= '50' and dd[k]['Smoker'] == 'yes':
            smoker_female_age_50.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] <= '60' and dd[k]['Smoker'] == 'yes':
            smoker_female_age_60.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] > '60' and dd[k]['Smoker'] == 'yes':
            smoker_female_age_over_60.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] <= '20' and dd[k]['Smoker'] == 'no':
            non_smoker_female_age_20.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] <= '30' and dd[k]['Smoker'] == 'no':
            non_smoker_female_age_30.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] <= '40' and dd[k]['Smoker'] == 'no':
            non_smoker_female_age_40.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] <= '50' and dd[k]['Smoker'] == 'no':
            non_smoker_female_age_50.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] <= '60' and dd[k]['Smoker'] == 'no':
            non_smoker_female_age_60.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "female" and dd[k]['Age'] > '60' and dd[k]['Smoker'] == 'no':
            non_smoker_female_age_over_60.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] <= '20' and dd[k]['Smoker'] == 'yes':
            smoker_male_age_20.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] <= '30' and dd[k]['Smoker'] == 'yes':
            smoker_male_age_30.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] <= '40' and dd[k]['Smoker'] == 'yes':
            smoker_male_age_40.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] <= '50' and dd[k]['Smoker'] == 'yes':
            smoker_male_age_50.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] <= '60' and dd[k]['Smoker'] == 'yes':
            smoker_male_age_60.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] > '60' and dd[k]['Smoker'] == 'yes':
            smoker_male_age_over_60.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] <= '20' and dd[k]['Smoker'] == 'no':
            non_smoker_male_age_20.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] <= '30' and dd[k]['Smoker'] == 'no':
            non_smoker_male_age_30.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] <= '40' and dd[k]['Smoker'] == 'no':
            non_smoker_male_age_40.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] <= '50' and dd[k]['Smoker'] == 'no':
            non_smoker_male_age_50.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] <= '60' and dd[k]['Smoker'] == 'no':
            non_smoker_male_age_60.append(float(dd[k]['Charges']))
        elif dd[k]['Sex'] == "male" and dd[k]['Age'] > '60' and dd[k]['Smoker'] == 'no':
            non_smoker_male_age_over_60.append(float(dd[k]['Charges']))
    
    sf_data[0].append(min(smoker_female_age_20))
    sf_data[0].append(max(smoker_female_age_20))
    sf_data[0].append(sum(smoker_female_age_20) / len(smoker_female_age_20))
    sf_data[0].append(len(smoker_female_age_20))
    sf_data[1].append(min(smoker_female_age_30))
    sf_data[1].append(max(smoker_female_age_30))
    sf_data[1].append(sum(smoker_female_age_30) / len(smoker_female_age_30))
    sf_data[1].append(len(smoker_female_age_30))
    sf_data[2].append(min(smoker_female_age_40))
    sf_data[2].append(max(smoker_female_age_40))
    sf_data[2].append(sum(smoker_female_age_40) / len(smoker_female_age_40))
    sf_data[2].append(len(smoker_female_age_40))
    sf_data[3].append(min(smoker_female_age_50))
    sf_data[3].append(max(smoker_female_age_50))
    sf_data[3].append(sum(smoker_female_age_50) / len(smoker_female_age_50))
    sf_data[3].append(len(smoker_female_age_50))
    sf_data[4].append(min(smoker_female_age_60))
    sf_data[4].append(max(smoker_female_age_60))
    sf_data[4].append(sum(smoker_female_age_60) / len(smoker_female_age_60))
    sf_data[4].append(len(smoker_female_age_60))
    sf_data[5].append(min(smoker_female_age_over_60))
    sf_data[5].append(max(smoker_female_age_over_60))
    sf_data[5].append(sum(smoker_female_age_over_60) / len(smoker_female_age_over_60))
    sf_data[5].append(len(smoker_female_age_over_60))
    
    nsf_data[0].append(min(non_smoker_female_age_20))
    nsf_data[0].append(max(non_smoker_female_age_20))
    nsf_data[0].append(sum(non_smoker_female_age_20) / len(non_smoker_female_age_20))
    nsf_data[0].append(len(non_smoker_female_age_20))
    nsf_data[1].append(min(non_smoker_female_age_30))
    nsf_data[1].append(max(non_smoker_female_age_30))
    nsf_data[1].append(sum(non_smoker_female_age_30) / len(non_smoker_female_age_30))
    nsf_data[1].append(len(non_smoker_female_age_30))
    nsf_data[2].append(min(non_smoker_female_age_40))
    nsf_data[2].append(max(non_smoker_female_age_40))
    nsf_data[2].append(sum(non_smoker_female_age_40) / len(non_smoker_female_age_40))
    nsf_data[2].append(len(non_smoker_female_age_40))
    nsf_data[3].append(min(non_smoker_female_age_50))
    nsf_data[3].append(max(non_smoker_female_age_50))
    nsf_data[3].append(sum(non_smoker_female_age_50) / len(non_smoker_female_age_50))
    nsf_data[3].append(len(non_smoker_female_age_50))
    nsf_data[4].append(min(non_smoker_female_age_60))
    nsf_data[4].append(max(non_smoker_female_age_60))
    nsf_data[4].append(sum(non_smoker_female_age_60) / len(non_smoker_female_age_60))
    nsf_data[4].append(len(non_smoker_female_age_60))
    nsf_data[5].append(min(non_smoker_female_age_over_60))
    nsf_data[5].append(max(non_smoker_female_age_over_60))
    nsf_data[5].append(sum(non_smoker_female_age_over_60) / len(non_smoker_female_age_over_60))
    nsf_data[5].append(len(non_smoker_female_age_over_60))
    
    sm_data[0].append(min(smoker_male_age_20))
    sm_data[0].append(max(smoker_male_age_20))
    sm_data[0].append(sum(smoker_male_age_20) / len(smoker_male_age_20))
    sm_data[0].append(len(smoker_male_age_20))
    sm_data[1].append(min(smoker_male_age_30))
    sm_data[1].append(max(smoker_male_age_30))
    sm_data[1].append(sum(smoker_male_age_30) / len(smoker_male_age_30))
    sm_data[1].append(len(smoker_male_age_30))
    sm_data[2].append(min(smoker_male_age_40))
    sm_data[2].append(max(smoker_male_age_40))
    sm_data[2].append(sum(smoker_male_age_40) / len(smoker_male_age_40))
    sm_data[2].append(len(smoker_male_age_40))
    sm_data[3].append(min(smoker_male_age_50))
    sm_data[3].append(max(smoker_male_age_50))
    sm_data[3].append(sum(smoker_male_age_50) / len(smoker_male_age_50))
    sm_data[3].append(len(smoker_male_age_50))
    sm_data[4].append(min(smoker_male_age_60))
    sm_data[4].append(max(smoker_male_age_60))
    sm_data[4].append(sum(smoker_male_age_60) / len(smoker_male_age_60))
    sm_data[4].append(len(smoker_male_age_60))
    sm_data[5].append(min(smoker_male_age_over_60))
    sm_data[5].append(max(smoker_male_age_over_60))
    sm_data[5].append(sum(smoker_male_age_over_60) / len(smoker_male_age_over_60))
    sm_data[5].append(len(smoker_male_age_over_60))
    
    nsm_data[0].append(min(non_smoker_male_age_20))
    nsm_data[0].append(max(non_smoker_male_age_20))
    nsm_data[0].append(sum(non_smoker_male_age_20) / len(non_smoker_male_age_20))
    nsm_data[0].append(len(non_smoker_male_age_20))
    nsm_data[1].append(min(non_smoker_male_age_30))
    nsm_data[1].append(max(non_smoker_male_age_30))
    nsm_data[1].append(sum(non_smoker_male_age_30) / len(non_smoker_male_age_30))
    nsm_data[1].append(len(non_smoker_male_age_30))
    nsm_data[2].append(min(non_smoker_male_age_40))
    nsm_data[2].append(max(non_smoker_male_age_40))
    nsm_data[2].append(sum(non_smoker_male_age_40) / len(non_smoker_male_age_40))
    nsm_data[2].append(len(non_smoker_male_age_40))
    nsm_data[3].append(min(non_smoker_male_age_50))
    nsm_data[3].append(max(non_smoker_male_age_50))
    nsm_data[3].append(sum(non_smoker_male_age_50) / len(non_smoker_male_age_50))
    nsm_data[3].append(len(non_smoker_male_age_50))
    nsm_data[4].append(min(non_smoker_male_age_60))
    nsm_data[4].append(max(non_smoker_male_age_60))
    nsm_data[4].append(sum(non_smoker_male_age_60) / len(non_smoker_male_age_60))
    nsm_data[4].append(len(non_smoker_male_age_60))
    nsm_data[5].append(min(non_smoker_male_age_over_60))
    nsm_data[5].append(max(non_smoker_male_age_over_60))
    nsm_data[5].append(sum(non_smoker_male_age_over_60) / len(non_smoker_male_age_over_60))
    nsm_data[5].append(len(non_smoker_male_age_over_60))
    
    
    return sf_data, nsf_data, sm_data, nsm_data

sf_datas, nsf_datas, sm_datas, nsm_datas = age_data(dd)
age_level = ['0-20', '21-30', '31-40', '41-50', '51-60', '60+']

for i in range(len(sf_datas)):
        print("\n" + str(age_level[i]) + " year old smoker female: " + "\n" +
              " - min charge: " + str(sf_datas[i][0]) + "\n" +
              " - max charge: " + str(sf_datas[i][1]) + "\n" +
              " - average charge: " + str(sf_datas[i][2]) + "\n" +
              " - number of people: " + str(sf_datas[i][3]) + "\n" +
              "\n" +
              str(age_level[i]) + " year old non-smoker female: " + "\n" +
              " - min charge: " + str(nsf_datas[i][0]) + "\n" +
              " - max charge: " + str(nsf_datas[i][1]) + "\n" +
              " - average charge: " + str(nsf_datas[i][2]) + "\n" +
              " - number of people: " + str(nsf_datas[i][3]) + "\n" +
              "\n" +
              str(age_level[i]) + " year old smoker male: " + "\n" +
              " - min charge: " + str(sm_datas[i][0]) + "\n" +
              " - max charge: " + str(sm_datas[i][1]) + "\n" +
              " - average charge: " + str(sm_datas[i][2]) + "\n" +
              " - number of people: " + str(sm_datas[i][3]) + "\n" +
              "\n" +
              str(age_level[i]) + " year old non-smoker male: " + "\n" +
              " - min charge: " + str(nsm_datas[i][0]) + "\n" +
              " - max charge: " + str(nsm_datas[i][1]) + "\n" +
              " - average charge: " + str(nsm_datas[i][2]) + "\n" +
              " - number of people: " + str(nsm_datas[i][3]))
  
 
    
    
    

