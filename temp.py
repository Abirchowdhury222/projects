# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/chowd/OneDrive/Desktop/projectsss/trained_model.sav', 'rb'))

# Define an example input as a dictionary
input_data = {
    'Gender': 'male',
    'Age': 30,
    'Height': 175,
    'Weight': 75,
    'Duration': 60,
    'Heart_Rate': 110,
    'Body_Temp': 37
}

# Preprocess the input data and convert it to a DataFrame
input_df = pd.DataFrame([input_data])

# Encode categorical variables (if any)
input_df['Gender'] = input_df['Gender'].replace({'male': 0, 'female': 1})

# Make a prediction using the XGBoost model
y_pred = loaded_model.predict(input_df)

print(f"Predicted calories burnt: {y_pred[0]}")
