# ==========================================
# Heart Disease Prediction using ANN
# Dataset: Framingham Heart Disease Dataset
# ==========================================

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("breast_cancer.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# -------------------------------
# Missing Values
# -------------------------------
print(df.isnull().sum())

df = df.dropna()

print("Dataset Shape after removing missing values:", df.shape)

# -------------------------------
# Correlation Heatmap
# -------------------------------
plt.figure(figsize=(12,10))
sns.heatmap(df.corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------
# Feature Selection
# -------------------------------
X = df.drop("TenYearCHD", axis=1)
y = df["TenYearCHD"]

print("Feature Shape:", X.shape)

# -------------------------------
# Feature Scaling
# -------------------------------
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# DO NOT SCALE THE TARGET
# y should remain 0 and 1

# -------------------------------
# Train Test Split
# -------------------------------
x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(x_train.shape)
print(x_test.shape)

# -------------------------------
# Build ANN Model
# -------------------------------
model = Sequential()

model.add(Input(shape=(x_train.shape[1],)))
model.add(Dense(32, activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# -------------------------------
# Train Model
# -------------------------------
history = model.fit(
    x_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# -------------------------------
# Evaluate Model
# -------------------------------
loss, accuracy = model.evaluate(x_test, y_test)

print("Test Accuracy:", accuracy)

# -------------------------------
# Accuracy Graph
# -------------------------------
plt.figure(figsize=(8,5))

plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")

plt.title("Training vs Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()

plt.show()

# -------------------------------
# Loss Graph
# -------------------------------
plt.figure(figsize=(8,5))

plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")

plt.title("Training vs Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()

plt.show()