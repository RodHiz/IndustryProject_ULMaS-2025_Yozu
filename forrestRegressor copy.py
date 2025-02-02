import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load datasets
pothole_data = pd.read_csv(r"C:\Users\rodri\OneDrive\Documents\School - ULMaS\Industry Project - Yozu\data\cleanedRoadData.csv")
weather_data = pd.read_csv(r"C:\Users\rodri\OneDrive\Documents\School - ULMaS\Industry Project - Yozu\data\leedsWeather.csv")

# Convert dates to datetime
pothole_data['ordered_date'] = pd.to_datetime(pothole_data['ordered_date'], dayfirst=True, errors='coerce')
weather_data['datetime'] = pd.to_datetime(weather_data['datetime'], errors='coerce')

# Merge datasets on nearest date
pothole_data = pothole_data.sort_values('ordered_date')
weather_data = weather_data.sort_values('datetime')
merged_data = pd.merge_asof(pothole_data, weather_data, left_on='ordered_date', right_on='datetime', direction='backward')

# Define damage probability proxy
merged_data['damage_probability'] = (
    (merged_data['order_cost'] > merged_data['order_cost'].median()) |
    (merged_data['target_days_to_repair'] > merged_data['target_days_to_repair'].median()) |
    (merged_data['priority'].isin(['CAT1 carriageway', 'CAT2 carriageway']))
).astype(int)

# Feature selection
features = ['temp', 'precipitation', 'speed limit', 'length', 'order_cost']
target = 'damage_probability'

# Handle missing values
merged_data.fillna(merged_data.mean(), inplace=True)

# Encode categorical variables
merged_data = pd.get_dummies(merged_data, columns=['urban/rural'], drop_first=True)

# Train-test split
X = merged_data[features]
y = merged_data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classification model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print('Classification Report:\n', classification_report(y_test, y_pred))
