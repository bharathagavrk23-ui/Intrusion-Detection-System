# save this as train_model.py
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load your phishing dataset
df = pd.read_csv('phishing_data.csv')  # Make sure this file exists

# Select only the 10 features you use in features.py
columns_used = [
    'having_IP_Address',
    'URL_Length',
    'SSLfinal_State',
    'Prefix_Suffix',
    'Shortining_Service',
    'having_At_Symbol',
    'double_slash_redirecting',
    'HTTPS_token',
    'Result'
]

X = df[columns_used[:-1]]  # all but 'Result'
y = df['Result']




# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model/phishing_model.pkl')
print("✅ Model trained and saved to 'model/phishing_model.pkl'")
