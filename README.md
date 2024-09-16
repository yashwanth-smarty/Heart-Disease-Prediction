# Heart Disease Prediction

This project involves building a machine learning model to predict the likelihood of heart disease based on various patient attributes using Logistic Regression.

## Table of Contents

- Project Description
- Data
- Requirements
- Installation
- Usage
- Results

## Project Description

The goal of this project is to predict the presence of heart disease in patients based on their medical attributes. The model uses Logistic Regression to classify the data into two categories: presence or absence of heart disease.

## Data

The dataset used in this project is `heart_disease_data.csv`. It contains the following features:
- `age`: Age of the patient
- `sex`: Gender of the patient (1 = male, 0 = female)
- `cp`: Type of chest pain (4 types)
- `trestbps`: Resting blood pressure (mm Hg)
- `chol`: Serum cholesterol (mg/dl)
- `fbs`: Fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
- `restecg`: Resting electrocardiographic results (values 0, 1, 2)
- `exang`: Exercise induced angina (1 = yes; 0 = no)
- `oldpeak`: Depression induced by exercise relative to rest
- `slope`: Slope of the peak exercise ST segment
- `ca`: Number of major vessels (0-3) colored by fluoroscopy
- `thal`: Thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)
- `target`: Presence or absence of heart disease (1 = presence; 0 = absence)

## Requirements

To run this project, you need to have Python 3.x installed along with the following libraries:
- `numpy`
- `pandas`
- `scikit-learn`

You can install the required libraries using pip:
```bash
pip install numpy pandas scikit-learn
```

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/heart-disease-prediction.git
    ```

2. Navigate to the project directory:
    ```bash
    cd heart-disease-prediction
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your data file `heart_disease_data.csv` and place it in the project directory.

2. Run the script to train the model and make predictions:
    ```bash
    python heart_disease_prediction.py
    ```

## Results

- Model Accuracy on Training Data: `accuracy_score(pred, y_train)`
- Model Accuracy on Test Data: `accuracy_score(pred2, y_test)`

The code also includes a sample prediction:
```python
ip = [55, 1, 0, 132, 353, 0, 1, 132, 1, 1.2, 1, 1, 3]
tc = np.asarray(ip)
abc = tc.reshape(1, -1)
res = model.predict(abc)
