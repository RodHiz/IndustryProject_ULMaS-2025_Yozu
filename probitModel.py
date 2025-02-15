import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

print("running...")
# Load datasets
pothole_data = pd.read_csv(r"C:\Users\rodri\OneDrive\Documents\School - ULMaS\Industry Project - Yozu\data\merged_data.csv")
weather_data = pd.read_csv(r"C:\Users\rodri\OneDrive\Documents\School - ULMaS\Industry Project - Yozu\data\leedsWeather.csv")

# Convert dates to datetime for merging
pothole_data['ordered_date'] = pd.to_datetime(pothole_data['ordered_date'], dayfirst=True, errors='coerce')
weather_data['datetime'] = pd.to_datetime(weather_data['datetime'], errors='coerce')

# Merge datasets on nearest date
pothole_data = pothole_data.sort_values('ordered_date')
weather_data = weather_data.sort_values('datetime')
merged_data = pd.merge_asof(pothole_data, weather_data, left_on='ordered_date', right_on='datetime', direction='backward')
print("running 2")
# Ensure columns are lowercase to avoid KeyErrors
merged_data.columns = merged_data.columns.str.strip().str.lower()

# Create Proxy for Damage Probability (Binary Target)
merged_data['damage_probability'] = (
    (merged_data['order_cost'] > merged_data['order_cost'].median()) |
    (merged_data['priority'].isin(['CAT1 carriageway', 'CAT2 carriageway']))
).astype(int)

print("running again")
# Define Features for Probit Model
features = ['temp', 'precipitation', 'speed limit', 'length', 'order_cost']
target = 'damage_probability'

# Handle missing values
merged_data.fillna(merged_data.mean(), inplace=True)

# Encode categorical variables
merged_data = pd.get_dummies(merged_data, columns=['urban/rural'], drop_first=True)
print("almost done \n")
# Train-test split
X = merged_data[features]
y = merged_data[target]
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Add Constant (Probit Model Requires It)
#X_train = sm.add_constant(X_train)
#X_test = sm.add_constant(X_test)

# Fit Probit Model
probit_model = sm.Probit(y, X)
probit_result = probit_model.fit()

# Predict Probabilities
y_pred_prob = probit_result.predict(X)

# Convert Probabilities to Binary Predictions (Threshold = 0.5)
#y_pred = (y_pred_prob > 0.5).astype(int)

# Evaluate Model
#accuracy = accuracy_score(y_test, y_pred)
#print(f'Accuracy: {accuracy}')
#print('Classification Report:\n', classification_report(y_test, y_pred))

# Print Model Summary
print(probit_result.summary())
