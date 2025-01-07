# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:22:57 2025

@author: anjali
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved model

diabetes_model = pickle.load(open('C:\Users\anjal\OneDrive\Desktop\ML model\diabetes_model.sav','rb'))


# sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Diabetes Prediction System',icons =['activity'], default_index = 0)
    
  
# diabetes prediction page
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    

        Pregnancies = st.text_input('Number of Pregnancies')        
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Presssure value')
        SkinThickness = st.text_input('Skin Thickness value')
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI value')
        DiabetesPredigreeFunction = st.text_input('Diabetes Pedigree Function value')
        Age = st.text_input('Age of the Person')
         
      #code for prediction
      diab_diagnosis = ''
      
      #creating a button for prediction
      
      if st.button('Diabetes Test Result'):
          diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,Blood Presssure,Skin Thickness,Insulin,BMI,Diabetes Pedigree Function,Age]])
          
          if (diab_prediction[0]==1):
              diab_diagnosis = 'The person is Diabetic'
              
           else:
               diab_diagnosis = 'The person is Not Diabetic'
               
       st.success(diab_diagnosis)         
          
          
          
          
          
          
          
          
          
          
          
          
          
          