# ❤️ Heart Disease Prediction using Artificial Neural Network (ANN)

A machine learning project that predicts the risk of developing coronary heart disease (CHD) within the next 10 years using the **Framingham Heart Study Dataset** and an **Artificial Neural Network (ANN)** built with TensorFlow/Keras.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help identify individuals at high risk and enable preventive healthcare.

This project uses the **Framingham Heart Study dataset** to train an Artificial Neural Network that predicts whether a patient is likely to develop coronary heart disease within the next 10 years.

The model performs data preprocessing, feature scaling, model training, evaluation, and visualization of training performance.

---

## 🎯 Objective

- Predict whether a person will develop heart disease within the next 10 years.
- Apply data preprocessing techniques.
- Train an Artificial Neural Network.
- Evaluate model performance.
- Visualize training and validation accuracy/loss.

---

## 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / Keras

---

## 📂 Dataset

**Dataset:** Framingham Heart Disease Dataset

Each row represents one patient's health information.

### Features

| Feature         | Description                                               |
| --------------- | --------------------------------------------------------- |
| male            | Gender (1 = Male, 0 = Female)                             |
| age             | Age of the patient                                        |
| education       | Education level                                           |
| currentSmoker   | Smoking status                                            |
| cigsPerDay      | Cigarettes smoked per day                                 |
| BPMeds          | Blood pressure medication                                 |
| prevalentStroke | Previous stroke history                                   |
| prevalentHyp    | Hypertension                                              |
| diabetes        | Diabetes status                                           |
| totChol         | Total cholesterol                                         |
| sysBP           | Systolic blood pressure                                   |
| diaBP           | Diastolic blood pressure                                  |
| BMI             | Body Mass Index                                           |
| heartRate       | Heart rate                                                |
| glucose         | Blood glucose level                                       |
| TenYearCHD      | Target variable (1 = Heart Disease, 0 = No Heart Disease) |

---

## 📊 Sample Dataset

| male | age | education | smoker | cholesterol | glucose | CHD |
| ---- | --- | --------- | ------ | ----------- | ------- | --- |
| 1    | 39  | 4         | No     | 195         | 77      | 0   |
| 0    | 46  | 2         | No     | 250         | 76      | 0   |
| 1    | 48  | 1         | Yes    | 245         | 70      | 0   |
| 0    | 61  | 3         | Yes    | 225         | 103     | 1   |

---

## ⚙️ Workflow

```
Load Dataset
      │
      ▼
Explore Dataset
      │
      ▼
Handle Missing Values
      │
      ▼
Correlation Analysis
      │
      ▼
Feature Selection
      │
      ▼
Feature Scaling
      │
      ▼
Train-Test Split
      │
      ▼
Build ANN Model
      │
      ▼
Train Model
      │
      ▼
Evaluate Model
      │
      ▼
Visualize Results
```

---

## 🧠 Artificial Neural Network Architecture

```
Input Layer
      │
      ▼
Dense Layer (32 neurons, ReLU)
      │
      ▼
Dense Layer (16 neurons, ReLU)
      │
      ▼
Output Layer (1 neuron, Sigmoid)
```

---

## 📈 Model Configuration

| Parameter        | Value               |
| ---------------- | ------------------- |
| Optimizer        | Adam                |
| Loss Function    | Binary Crossentropy |
| Metric           | Accuracy            |
| Epochs           | 20                  |
| Batch Size       | 32                  |
| Validation Split | 20%                 |

---

## 📊 Visualizations

The project generates:

- Correlation Heatmap
- Training Accuracy Graph
- Validation Accuracy Graph
- Training Loss Graph
- Validation Loss Graph

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/heart-disease-ann.git
```

Move into the project

```bash
cd heart-disease-ann
```

Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
```

Run the project

```bash
python main.py
```

---

## 📁 Project Structure

```
Heart-Disease-Prediction/
│
├── breast_cancer.csv
├── main.py
├── README.md
└── requirements.txt
```

> **Note:** Although the dataset file is named `breast_cancer.csv`, it actually contains the **Framingham Heart Disease dataset**. Renaming the file does not change the dataset.

---

## 📌 Machine Learning Steps

- Load dataset
- Explore data
- Remove missing values
- Correlation analysis
- Feature scaling using MinMaxScaler
- Split data into training and testing sets
- Build ANN model
- Train model
- Evaluate model
- Plot accuracy and loss curves

---

## 📉 Evaluation

The trained ANN is evaluated using:

- Test Accuracy
- Training Accuracy
- Validation Accuracy
- Binary Cross-Entropy Loss

---

## 🚀 Future Improvements

- Hyperparameter tuning
- Dropout layers
- Early stopping
- Cross-validation
- Model saving/loading
- ROC Curve
- Confusion Matrix
- Precision, Recall, and F1-Score
- Compare ANN with Decision Tree, Random Forest, SVM, and Logistic Regression

---

## 👨‍💻 Author

**Anupam Baral**

BCA Student | Full Stack Developer | AI & Machine Learning Enthusiast

GitHub: https://github.com/gomugomucode

Portfolio: https://www.anupambaral.com.np

---

## 📄 License

This project is created for educational and learning purposes.
