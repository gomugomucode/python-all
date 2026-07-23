# Heart Disease Prediction using Artificial Neural Network (ANN)

## Overview

This project predicts the likelihood of a patient developing coronary heart disease (CHD) within the next 10 years using an **Artificial Neural Network (ANN)**. The model is trained on the **Framingham Heart Disease Dataset**, a well-known dataset containing patient health information and risk factors.

The project demonstrates the complete machine learning workflow, including:

- Data loading
- Data preprocessing
- Handling missing values
- Exploratory Data Analysis (EDA)
- Feature scaling
- Training an Artificial Neural Network
- Model evaluation
- Visualization of training performance

---

# Dataset

**Dataset Name:** Framingham Heart Disease Dataset

> **Note:** Although the file is named `breast_cancer.csv` in this project, it actually contains the **Framingham Heart Disease Dataset**. The filename was changed for convenience, but the data remains the same.

### Target Variable

**TenYearCHD**

- **0** → No risk of developing coronary heart disease within 10 years
- **1** → Risk of developing coronary heart disease within 10 years

---

# Features

The dataset contains several medical and lifestyle features, including:

- Age
- Gender
- Smoking status
- Cigarettes per day
- Blood pressure medication
- Stroke history
- Hypertension
- Diabetes
- Total cholesterol
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Body Mass Index (BMI)
- Heart Rate
- Glucose Level

These features are used to predict the target variable **TenYearCHD**.

---

# Technologies Used

- Python 3
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / Keras

---

# Project Workflow

## 1. Import Required Libraries

The project begins by importing all the required Python libraries for data analysis, visualization, preprocessing, and deep learning.

---

## 2. Load the Dataset

The dataset is loaded into a Pandas DataFrame.

```python
df = pd.read_csv("breast_cancer.csv")
```

---

## 3. Data Exploration

The following functions are used to understand the dataset:

- `head()`
- `shape`
- `info()`
- `describe()`
- `columns`

This helps identify:

- Number of rows and columns
- Data types
- Summary statistics
- Feature names

---

## 4. Data Cleaning

Missing values are checked using:

```python
df.isnull().sum()
```

Rows containing missing values are removed using:

```python
df.dropna()
```

---

## 5. Exploratory Data Analysis (EDA)

A correlation heatmap is created to visualize relationships between features.

```python
sns.heatmap(df.corr(), annot=True)
```

This helps identify which features are strongly related to the target variable.

---

## 6. Feature Selection

The dataset is divided into:

### Features (X)

All independent variables.

### Target (y)

```python
TenYearCHD
```

---

## 7. Feature Scaling

The input features are normalized using **MinMaxScaler**.

Scaling improves neural network performance by bringing all feature values into the same range.

---

## 8. Train-Test Split

The dataset is divided into:

- **80% Training Data**
- **20% Testing Data**

This ensures the model is evaluated on unseen data.

---

## 9. Building the ANN Model

The Artificial Neural Network consists of:

- Input Layer
- Hidden Layer (32 neurons, ReLU activation)
- Hidden Layer (16 neurons, ReLU activation)
- Output Layer (1 neuron, Sigmoid activation)

The output layer predicts the probability of heart disease.

---

## 10. Model Compilation

The model is compiled using:

- **Optimizer:** Adam
- **Loss Function:** Binary Crossentropy
- **Evaluation Metric:** Accuracy

---

## 11. Model Training

The model is trained using:

- Epochs: 20
- Batch Size: 32
- Validation Split: 20%

Training allows the neural network to learn patterns from the data.

---

## 12. Model Evaluation

After training, the model is evaluated on the testing dataset to measure its prediction accuracy.

---

## 13. Performance Visualization

Two graphs are generated:

### Accuracy Graph

Shows the comparison between:

- Training Accuracy
- Validation Accuracy

### Loss Graph

Shows the comparison between:

- Training Loss
- Validation Loss

These graphs help determine whether the model is learning effectively or overfitting.

---

# Folder Structure

```
Heart-Disease-Prediction/
│
├── breast_cancer.csv
├── main.py
├── README.md
└── requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd Heart-Disease-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

# Required Libraries

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
tensorflow
```

Install them with:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow
```

---

# Results

The ANN learns patterns from patient health records to predict whether a patient is likely to develop coronary heart disease within the next 10 years.

Model performance can be monitored using:

- Test Accuracy
- Training Accuracy
- Validation Accuracy
- Loss Curves

---

# Future Improvements

- Perform hyperparameter tuning.
- Handle missing values using imputation instead of removing rows.
- Add confusion matrix and classification report.
- Compare ANN with other machine learning models such as:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Support Vector Machine (SVM)
  - K-Nearest Neighbors (KNN)

- Save the trained model for future predictions.

---

# Conclusion

This project demonstrates how an Artificial Neural Network (ANN) can be used for binary classification to predict the risk of coronary heart disease. It covers the complete machine learning pipeline, including data preprocessing, feature scaling, model training, evaluation, and visualization. The project serves as a practical example of applying deep learning techniques to healthcare data and can be extended with additional models and optimization techniques for improved performance.
