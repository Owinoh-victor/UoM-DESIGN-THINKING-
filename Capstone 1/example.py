# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:00:33 2020

@author: pc
"""

# Declaring Variables to be input by User

temp = float()   
dry_cough = str()
sore_throat=str()    
chest_pain=()
dificulty_breathing()=str()

# Asking the user to input sysmtpms
temp = float(input("Please enter your Temperature in degree celcious(°C):  "))
dry_cough = str(input("Do you have a dry cough? (Type 'yes' or 'no'):  "))
sore_throat = str(input("Do you have a sore throat? (Type 'yes' or 'no'):  "))
chest_pain = str(input("Do you have chest pain? (Type 'yes' or 'no'):  "))
dificulty_breathing = str(input("Do you have Difficulty Breathing? (Type 'yes' or 'no'):  "))

# using if structure to test probalility of covid-19

symptoms=[" dry_cough","high_fever", "sore_throat", "diffuculty in breathing","chest_pain"]
symp_data=[]
true_symp=[]
count_symp=0

# asking the useer to confirm the number of symptoms he/she have
my_symp=int(input(" Chech the list above and Enter the number of Symptoms you have:"))
while (count_symp < my_symp):
    my_=str(input("Enter the symtopms You have:"))
  
  if (symp_data in symptoms):
      true_symp.append(symp_data)
      corona_symptoms_cart.append(symptoms)
  else:
      corona_symptoms_cart.append(symptoms)
      cart_value=cart_value + 1
      dataset_length=int(len(corona_df))
      positive_length=int(len(positive))
      symptoms_length=int(len(corona_symptoms_cart))
      corona_chances=(symptoms_length/dataset_length)*100
      positive_result=(positive_length/dataset_length)*100

