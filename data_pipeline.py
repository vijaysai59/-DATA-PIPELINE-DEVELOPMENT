# Import required libraries
import pandas as pd
import warnings
from sklearn.preprocessing import LabelEncoder, StandardScaler

# ----------------------------
# Suppress Warnings
# ----------------------------
warnings.filterwarnings("ignore")

# ----------------------------
# Step 1: Load the Excel Dataset
# ----------------------------
df = pd.read_excel('dataset.xlsx')  # Ensure dataset.xlsx is in the same folder
print("Original Data:")
print(df.head())

# ----------------------------
# Step 2: Handle Missing Values
# ----------------------------
# Fill numeric columns with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill categorical columns with mode
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nAfter Handling Missing Values:")
print(df.head())

# ----------------------------
# Step 3: Encode Categorical Variables
# ----------------------------
label_encoders = {}

for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

print("\nAfter Encoding Categorical Columns:")
print(df.head())

# ----------------------------
# Step 4: Feature Scaling
# ----------------------------
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Convert scaled data back to DataFrame
df_scaled = pd.DataFrame(scaled_data, columns=df.columns)

print("\nAfter Feature Scaling:")
print(df_scaled.head())

# ----------------------------
# Step 5: Save Transformed Data
# ----------------------------
df_scaled.to_excel('transformed_dataset.xlsx', index=False)
print("\nTransformed data saved as 'transformed_dataset.xlsx'")
