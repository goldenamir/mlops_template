# sample_mlops

Project created with MLOps-Template cookiecutter. For more info: https://mlopsstudygroup.github.io/mlops-guide/

## 📋 Requirements

- Python 3
- pip or conda
- DVC (optional, for data versioning)
- IBM Cloud Object Storage (optional, for cloud storage)
- See `requirements.txt` for Python dependencies

## 🚀 Getting Started

### 1. Install Dependencies

Using pip:
```bash
pip install -r requirements.txt
```
Or using conda:
```bash
conda install --file requirements.txt
pip install ibm_watson_machine_learning  # If not available via conda
```

### 2. Prepare the Data

Run the script to save the Iris dataset as a CSV file in the `data` folder:
```bash
python src/scripts/save_iris_dataset.py
```

### 3. Train the Model

Run the script to train a Support Vector Machine (SVM) model on the Iris dataset and save it to the `models` folder:
```bash
python src/scripts/train_iris_model.py
```

### 4. Output

- The dataset will be saved as `data/iris_dataset.csv`.
- The trained model will be saved as `models/iris_model.joblib`.

## ✅ Pre-commit Testings

To activate pre-commit testing, you need `pre-commit`:

```bash
pip install pre-commit
pre-commit install
```

Now, every time you make a commit, it will run tests defined in `.pre-commit-config.yaml` before allowing your commit.

## ⚗️ Using DVC

Download data from the DVC repository (analogous to `git pull`):
```bash
dvc pull
```

Reproduce the pipeline using DVC:
```bash
dvc repro
```

---

## �� Project Structure