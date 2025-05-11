import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

# Get the project root directory (two levels up from this script)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
data_path = os.path.join(project_root, 'data', 'iris_dataset.csv')
models_dir = os.path.join(project_root, 'models')
os.makedirs(models_dir, exist_ok=True)

# Load the dataset
iris_df = pd.read_csv(data_path)

# Split features and target
X = iris_df.drop('target', axis=1)
y = iris_df['target']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Support Vector Machine (SVM) model
model = SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)

# Save the trained model
model_path = os.path.join(models_dir, 'iris_model.joblib')
joblib.dump(model, model_path)

print(f"Model trained and saved to {model_path}")
