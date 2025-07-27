import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import warnings
warnings.filterwarnings('ignore')

# Loading the dataset
data = pd.read_csv('thalassemia_200000.csv')

# Checking for missing values
if data.isnull().sum().any():
    data = data.fillna(data.mean(numeric_only=True))

# Define features explicitly to ensure correct order
FEATURES = [
    'mother_age', 'mother_Hb', 'mother_HbA2', 'mother_HbF', 'mother_MCV', 'mother_MCH', 'mother_RBC', 'mother_RDW',
    'father_age', 'father_Hb', 'father_HbA2', 'father_HbF', 'father_MCV', 'father_MCH', 'father_RBC', 'father_RDW'
]
X = data[FEATURES]
y = data['status']

# Encoding the target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Scaling numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting data into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)

# Training the Random Forest model
model = RandomForestClassifier(n_estimators=50, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Calculating test accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nTest Set Accuracy: {accuracy * 100:.2f}%")

# Printing classification report
target_names = label_encoder.classes_
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Save the model, scaler, and label encoder
joblib.dump(model, 'thalassemia_model.joblib')
joblib.dump(scaler, 'thalassemia_scaler.joblib')
joblib.dump(label_encoder, 'thalassemia_label_encoder.joblib')
print("Model, scaler, and label encoder saved as 'thalassemia_model.joblib', 'thalassemia_scaler.joblib', and 'thalassemia_label_encoder.joblib'.")