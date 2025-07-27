import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Total number of samples
total_samples = 200000
classes = ['Affected', 'Carrier', 'Non Affected']
samples_per_class = total_samples // len(classes)  # ~66667 per class
remainder = total_samples % len(classes)  # 2 extra rows to assign

# Initialize lists to store data for each class
dfs = []

# Define feature generation for each class with significant overlap and noise
for status in classes:
    if status == classes[-1]:  # Assign remainder to the last class
        n_samples = samples_per_class + remainder
    else:
        n_samples = samples_per_class

    # Adjust feature distributions with more overlap and noise
    if status == 'Affected':
        mother_MCV = np.random.normal(loc=65, scale=8, size=n_samples).clip(50, 80)
        father_MCV = np.random.normal(loc=65, scale=8, size=n_samples).clip(50, 80)
        mother_HbA2 = np.random.uniform(3, 9, size=n_samples)
        father_HbA2 = np.random.uniform(3, 9, size=n_samples)
        mother_RDW = np.random.normal(loc=14, scale=0.6, size=n_samples).clip(13, 14.5)
        father_RDW = np.random.normal(loc=14, scale=0.6, size=n_samples).clip(13, 14.5)
        mother_Hb = np.random.normal(loc=10, scale=1.2, size=n_samples).clip(8, 13)
        father_Hb = np.random.normal(loc=11, scale=1.2, size=n_samples).clip(9, 14)
        mother_HbF = np.random.uniform(1, 10, size=n_samples)
        father_HbF = np.random.uniform(1, 10, size=n_samples)
        mother_MCH = np.random.normal(loc=29, scale=1.5, size=n_samples).clip(27, 32)
        father_MCH = np.random.normal(loc=29, scale=1.5, size=n_samples).clip(27, 32)
        mother_RBC = np.random.normal(loc=4.8, scale=0.4, size=n_samples).clip(4.0, 5.5)
        father_RBC = np.random.normal(loc=4.8, scale=0.4, size=n_samples).clip(4.0, 5.5)
    elif status == 'Carrier':
        mother_MCV = np.random.normal(loc=70, scale=8, size=n_samples).clip(55, 85)
        father_MCV = np.random.normal(loc=82, scale=8, size=n_samples).clip(70, 100)
        mother_HbA2 = np.random.uniform(2.5, 7, size=n_samples)
        father_HbA2 = np.random.uniform(1.5, 4, size=n_samples)
        mother_RDW = np.random.normal(loc=13.8, scale=0.7, size=n_samples).clip(12.5, 14.5)
        father_RDW = np.random.normal(loc=13, scale=0.7, size=n_samples).clip(11.5, 14)
        mother_Hb = np.random.normal(loc=11, scale=1.2, size=n_samples).clip(9, 14)
        father_Hb = np.random.normal(loc=13, scale=1.2, size=n_samples).clip(11, 15)
        mother_HbF = np.random.uniform(0.5, 8, size=n_samples)
        father_HbF = np.random.uniform(0, 5, size=n_samples)
        mother_MCH = np.random.normal(loc=29.5, scale=1.5, size=n_samples).clip(27, 33)
        father_MCH = np.random.normal(loc=30.5, scale=1.5, size=n_samples).clip(28, 34)
        mother_RBC = np.random.normal(loc=4.6, scale=0.4, size=n_samples).clip(3.8, 5.3)
        father_RBC = np.random.normal(loc=4.5, scale=0.4, size=n_samples).clip(3.8, 5.3)
    else:  # Non Affected
        mother_MCV = np.random.normal(loc=85, scale=8, size=n_samples).clip(70, 100)
        father_MCV = np.random.normal(loc=85, scale=8, size=n_samples).clip(70, 100)
        mother_HbA2 = np.random.uniform(1, 4.5, size=n_samples)
        father_HbA2 = np.random.uniform(1, 4.5, size=n_samples)
        mother_RDW = np.random.normal(loc=12.8, scale=0.8, size=n_samples).clip(11.5, 14)
        father_RDW = np.random.normal(loc=12.8, scale=0.8, size=n_samples).clip(11.5, 14)
        mother_Hb = np.random.normal(loc=12.5, scale=1.2, size=n_samples).clip(10, 15)
        father_Hb = np.random.normal(loc=13.5, scale=1.2, size=n_samples).clip(11, 15)
        mother_HbF = np.random.uniform(0, 5, size=n_samples)
        father_HbF = np.random.uniform(0, 5, size=n_samples)
        mother_MCH = np.random.normal(loc=30.5, scale=1.5, size=n_samples).clip(28, 34)
        father_MCH = np.random.normal(loc=30.5, scale=1.5, size=n_samples).clip(28, 34)
        mother_RBC = np.random.normal(loc=4.5, scale=0.4, size=n_samples).clip(3.8, 5.3)
        father_RBC = np.random.normal(loc=4.5, scale=0.4, size=n_samples).clip(3.8, 5.3)

    # Add random noise to key features to increase misclassification
    noise_factor = 2.1  # 210% noise
    mother_MCV += np.random.normal(0, noise_factor * (mother_MCV.std()), size=n_samples)
    father_MCV += np.random.normal(0, noise_factor * (father_MCV.std()), size=n_samples)
    mother_HbA2 += np.random.normal(0, noise_factor * (mother_HbA2.std()), size=n_samples)
    father_HbA2 += np.random.normal(0, noise_factor * (father_HbA2.std()), size=n_samples)
    mother_RDW += np.random.normal(0, noise_factor * (mother_RDW.std()), size=n_samples)
    father_RDW += np.random.normal(0, noise_factor * (father_RDW.std()), size=n_samples)

    # Clip again to ensure values stay within realistic ranges
    mother_MCV = np.clip(mother_MCV, 50, 100)
    father_MCV = np.clip(father_MCV, 50, 100)
    mother_HbA2 = np.clip(mother_HbA2, 1, 10)
    father_HbA2 = np.clip(father_HbA2, 1, 10)
    mother_RDW = np.clip(mother_RDW, 11.5, 14.5)
    father_RDW = np.clip(father_RDW, 11.5, 14.5)

    # Common features across all classes
    data = {
        'mother_age': np.round(np.random.normal(loc=30, scale=5, size=n_samples).clip(0, 45)).astype(int),
        'mother_Hb': np.round(mother_Hb, 2),
        'mother_HbA2': np.round(mother_HbA2, 2),
        'mother_HbF': np.round(mother_HbF, 2),
        'mother_MCV': np.round(mother_MCV, 2),
        'mother_MCH': np.round(mother_MCH, 2),
        'mother_RBC': np.round(mother_RBC, 2),
        'mother_RDW': np.round(mother_RDW, 2),
        'father_age': np.round(np.random.normal(loc=32, scale=5, size=n_samples).clip(0, 45)).astype(int),
        'father_Hb': np.round(father_Hb, 2),
        'father_HbA2': np.round(father_HbA2, 2),
        'father_HbF': np.round(father_HbF, 2),
        'father_MCV': np.round(father_MCV, 2),
        'father_MCH': np.round(father_MCH, 2),
        'father_RBC': np.round(father_RBC, 2),
        'father_RDW': np.round(father_RDW, 2),
        'status': [status] * n_samples
    }

    # Create DataFrame for this class
    df_class = pd.DataFrame(data)
    dfs.append(df_class)

# Concatenate all DataFrames
df = pd.concat(dfs, ignore_index=True)

# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv('thalassemia_200000.csv', index=False)

print("Saved as 'thalassemia_200000.csv'")
print("Shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nStatus distribution:")
print(df['status'].value_counts())