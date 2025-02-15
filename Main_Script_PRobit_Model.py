# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 23:24:13 2025

@author: rodri
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

Data = pd.read_csv('merged_data_final.csv')


y = Data['ydependent']

T = len(y)

X = np.column_stack((np.ones(T),Data['speedLimit'],Data['length'],Data['temp'],Data['precip'],Data['speedLimit']*Data['precip']))


probit_model = sm.Probit(y, X)
probit_result = probit_model.fit()

print(probit_result.summary())

yhat = 1 - probit_result.predict()

yhat = np.asarray(yhat)

yhat_series = pd.Series(yhat)  # Convert to pandas Series

# Apply rolling mean with window size of 20
yhat_SMTH = yhat_series.rolling(window=20, center=True).mean()

# Convert back to NumPy array if needed
yhat_SMTH = yhat_SMTH.to_numpy()

plt.plot(yhat_SMTH, label='Predicted Values')
plt.xlabel('Street Id')
plt.ylabel('Probability')
plt.title('Probability of Road Damage')
plt.legend()
plt.show()


Street_Names = Data['address1']

St_Name    = Street_Names[10:20]
Prob_Index = yhat_SMTH[10:20]

plt.bar(St_Name,Prob_Index)
plt.xlabel('Street Name') 
plt.xticks(rotation=45)
plt.ylabel('Probabilities')
plt.legend()
plt.show()

