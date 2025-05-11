import os
import pandas as pd
from sklearn.datasets import load_iris

# Get the project root directory (two levels up from this script)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
data_dir = os.path.join(project_root, 'data')
os.makedirs(data_dir, exist_ok=True)

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Convert to DataFrame
iris_df = pd.DataFrame(X, columns=iris.feature_names)
iris_df['target'] = y

# Save as CSV in the data folder
iris_df.to_csv(os.path.join(data_dir, 'iris_dataset.csv'), index=False)

print("Iris dataset saved to data/iris_dataset.csv")
