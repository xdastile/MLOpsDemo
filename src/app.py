

# import the necessary packages
from fastapi import FastAPI
from typing import List, Dict, Any
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
import os
import json
import requests
import io
import logging

#CORS
from fastapi.middleware.cors import CORSMiddleware



# create a fastapi instance
app = FastAPI()

app.add_middleware(
        CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"])



# create a class for the input data
class InputData(BaseModel):
    data: List[Dict[str, Any]]

# Usage:
sample_data = [{
    "Account_Balance": 1,
    "Duration_of_Credit_monthly": 18,
    "Payment_Status_of_Previous_Credit": 4,
    "Purpose": 2,
    "Credit_Amount": 1049,
    "Value_Savings_Stocks": 1,
    "Length_of_current_employment": 2,
    "Instalment_per_cent": 4,
    "Sex_Marital_Status": 2,
    "Guarantors": 1,
    "Duration_in_Current_address": 4,
    "Most_valuable_available_asset": 2,
    "Age_years": 21,
    "Concurrent_Credits": 3,
    "Type_of_apartment": 1,
    "No_of_Credits_at_this_Bank": 1,
    "Occupation": 3,
    "No_of_dependents": 1,
    "Telephone": 1,
    "Foreign_Worker": 1
}]


# create a class for the output data
class OutputData(BaseModel):
    prediction: List[List[float]]

# Usage:
sample_prediction = [[0.7, 0.3]]


# Rest of the code remains unchanged.

# create a class for the model
class Model:
    def __init__(self):
        # Load the trained model from blob storage or local file (model/model.pkl)
        self.model = pickle.load(open('model/model.pkl', 'rb'))

    def predict(self, input_data):
        # Convert the input data to a DataFrame
        input_data = pd.DataFrame(input_data)

        output = self.model.predict_proba(input_data)

        # Return the output
        return output

# create an instance of the model
model = Model()

# Define the root endpoint
@app.get('/')
async def root():
    # Return a welcome message
    return 'Welcome to the API'

# Define the predict endpoint
@app.post('/predict', response_model=OutputData)
async def predict(data: InputData):
    # Get the input data
    input_data = data.data

    # Predict the output
    output = model.predict(input_data)

    # Return the output
    return {'prediction': output}