# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:15:54 2023

@author: chowd
"""

import pandas as pd
import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/chowd/OneDrive/Desktop/projectsss/trained_model.sav', 'rb'))

# creating a function for Prediction
def calories_prediction(input_data):
    # Preprocess the input data and convert it to a DataFrame
    input_df = pd.DataFrame([input_data], columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])
    # Convert object data types to numeric data types
    input_df['Age'] = pd.to_numeric(input_df['Age'])
    input_df['Height'] = pd.to_numeric(input_df['Height'])
    input_df['Weight'] = pd.to_numeric(input_df['Weight'])
    input_df['Duration'] = pd.to_numeric(input_df['Duration'])
    input_df['Heart_Rate'] = pd.to_numeric(input_df['Heart_Rate'])
    input_df['Body_Temp'] = pd.to_numeric(input_df['Body_Temp'])
    # Encode categorical variables (if any)
    input_df['Gender'] = input_df['Gender'].replace({'male': 0, 'female': 1})
    # Make a prediction using the XGBoost model
    y_pred = loaded_model.predict(input_df)
    return f"Predicted calories burnt: {y_pred[0]}"

def main():
    # giving a title
    st.title('Calories Prediction Web App')
    # getting the input data from the user
    Gender = st.selectbox('Gender', ['male', 'female'])
    Age = st.text_input('Age')
    Height = st.text_input('Height')
    Weight = st.text_input('Weight')
    Duration = st.text_input('Duration')
    Heart_Rate = st.text_input('Heart Rate')
    Body_Temp = st.text_input('Body Temperature')
    # code for Prediction
    diagnosis = ''
    # creating a button for Prediction
    if st.button('Calories Test Result'):
        diagnosis = calories_prediction([Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp])
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
