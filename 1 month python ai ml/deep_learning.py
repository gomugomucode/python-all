import os

# Hide TensorFlow info and warning messages (0 = all logs, 1 = hide INFO, 2 = hide INFO/WARNING, 3 = hide ALL)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# # sigmoid activation function

# import numpy as np

# x = np.array([-1.0, 0.0, 1.0, 2.0, 3.0])

# sigmoid = 1 / (1 + np.exp(x))
# print(sigmoid)


# # relu activation function
# relu = np.maximun(0, x)
# print(relu)


# # softmax activation function
# softmax = np.exp(x) / np.sum(np.exp(x))
# print(softmax)


# # tanh activation function   (1 to -1)
# print(np.tanh(x))


# # dense layer


# def dense(input, weights, bias):
#     return np.dot(input, weights) + bias


# tenserflow

# import tensorflow as tf

# model = tf.keras.Sequential(
#     [
#         tf.keras.layers.Dense(units=16, activation="relu"),
#         tf.keras.layers.Dense(units=8, activation="relu"),
#         tf.keras.layers.Dense(units=1, activation="sigmoid"),
#     ]
# )

# model.summary()
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

# 1. Setup training data
X = np.array([1, 2, 3], dtype=np.float32)
y = np.array([1, 2, 3], dtype=np.float32)

# 2. Define the model structural flow correctly for Keras 3
model = Sequential(
    [
        tf.keras.Input(shape=(1,)),  # Explicitly define input tracking here
        Dense(units=1, activation="linear"),  # No input_shape inside Dense
    ]
)

# 3. Compile, train, and run prediction
model.compile(optimizer="sgd", loss="mse")
model.fit(X, y, epochs=100, verbose=0)  # verbose=0 keeps the terminal clean

print("Prediction output:")
print(model.predict(X))

# convolational neural network

# 1 training data
# 2 input layer
# ?3 hidden layer
# 4 activcation layer
# 5 output layer\
# 6 prediction
# 7 lossfunction
# 8 back propogation
# 9 upgrade weight
# 10 next epach output

# dataset ➔ Sequential model ➔ dense layer ➔ training ➔ forward propagation ➔ loss calculation ➔ backward propagation ➔ upgrade weight ➔ repeat next epoch ➔ trained model ➔ prediction
