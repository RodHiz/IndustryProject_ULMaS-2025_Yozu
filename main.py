import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load datasets (replace with actual file paths)
pothole_data = pd.read_csv('pothole_data.csv')  # Historic pothole data
weather_data = pd.read_csv('weather_data.csv')  # Rainfall, temperature, freeze-thaw cycles
traffic_data = pd.read_csv('traffic_data.csv')  # Vehicle volume, percentage of HGVs
road_attributes = pd.read_csv('road_attributes.csv')  # Surface material, road age, etc.
geospatial_data = pd.read_csv('geospatial_data.csv')  # Elevation, slope, urban/rural

# Merge datasets on common keys (e.g., location, date)
data = pothole_data.merge(weather_data, on=['location', 'date'], how='left')
data = data.merge(traffic_data, on=['location', 'date'], how='left')
data = data.merge(road_attributes, on=['location'], how='left')
data = data.merge(geospatial_data, on=['location'], how='left')

# Feature selection
features = ['rainfall', 'temperature', 'freeze_thaw_cycles', 'vehicle_volume', 'hgv_percentage',
            'surface_material', 'road_age', 'maintenance_frequency', 'surface_thickness',
            'elevation', 'slope', 'urban_rural']
target = 'damage_probability'

# Handle missing values (simple imputation for now)
data.fillna(data.mean(), inplace=True)

# Train-test split
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MAE: {mae}')
print(f'R^2 Score: {r2}')