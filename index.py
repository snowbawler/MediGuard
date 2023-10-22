import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import joblib
import tensorflow as tf

#for data preprocessing
from sklearn.decomposition import PCA

#for modeling
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest

#filter warnings
import warnings

from components.sidebar import sidebar
from components.uploadData import dataTab
from components.medical_bill_fraud_detection import ML, preprocessing, removeComma

ae = joblib.load("components/model_filename.pkl")
y_scores = pd.Series(ae.decision_scores_)
risk = 0
st.set_page_config(page_title="MediGuard", page_icon="📖", layout="wide")
st.markdown("<h1 style='text-align: center;'>📖 MediGuard</h1>", unsafe_allow_html=True)

provider_first, provider_last, submitted_charge, has_med, med_payment, HCPCS = dataTab()
sidebar()

with open("form_submit_state.txt", "r") as file:
    form_submit_state = file.read()

def runModel(ae, y_scores, pF, pL, sC, hM, mP):
    raw_data = pd.read_csv("Healthcare Providers.csv")

    # user input

    provider_first = str(pF)
    provider_last = str(pL)
    submitted_charge = float(sC)
    if hM:
        med_payment = float(mP)
    else:
        med_payment = 0

    # find the row data of the provider
    row = raw_data.loc[(raw_data['Last Name/Organization Name of the Provider'] == provider_last)
                & (raw_data['First Name of the Provider'] == provider_first)].copy()

    # find the row index of the provider
    row_index = raw_data.index[(raw_data['Last Name/Organization Name of the Provider'] == provider_last)
                & (raw_data['First Name of the Provider'] == provider_first)][0]

    # save the old score before finding the new one
    old_score = y_scores[row_index]

    # update the row
    row['Number of Services'] = str(int(row['Number of Services']) + 1)
    if (hM == 1):
        row['Average Medicare Payment Amount'] = str((float(row['Average Medicare Payment Amount']) * int(row['Number of Medicare Beneficiaries']) + med_payment) / (int(row['Number of Medicare Beneficiaries']) + 1))
        row['Number of Medicare Beneficiaries'] = str(int(row['Number of Medicare Beneficiaries']) + 1)
    row['Average Submitted Charge Amount'] = str((float(row['Average Submitted Charge Amount']) * (int(row['Number of Services']) - 1) + submitted_charge) / int(row['Number of Services']))

    temp_data = pd.concat([row,raw_data], ignore_index=True)

    temp_data = preprocessing(temp_data)

    temp_data.head()

    temp_row = temp_data.iloc[0,:]
    temp_row = temp_row.to_numpy()
    temp_row = temp_row[np.newaxis, :]

    new_score = ae.decision_function(temp_row)
    result = ae.predict(temp_row)
    print(new_score)
    print(old_score)
    print(result)

    if (new_score[0] > old_score and result[0] == 1):
        return 2 #High Risk
    elif (new_score[0] > old_score and result[0] == 0 or new_score[0] < old_score and result[0] == 1):
        return 1
    else:
        return 0 #Low Risk

if form_submit_state == "pressed":
    risk = runModel(ae, y_scores, provider_first, provider_last, submitted_charge, has_med, med_payment)

