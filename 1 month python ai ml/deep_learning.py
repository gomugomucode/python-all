# sigmoid activation function

import numpy as np

x = np.array([-1.0, 0.0, 1.0, 2.0, 3.0])

sigmoid = 1 / (1 + np.exp(x))
print(sigmoid)


# relu activation function
relu = np.maximum(0, x)
print(relu)


# softmax activation function
softmax = np.exp(x) / np.sum(np.exp(x))
print(softmax)


# tanh activation function   (1 to -1)
print(np.tanh(x))


# dense layer


def dense(input, weights, bias):
    return np.dot(input, weights) + bias


# tenserflow

import tensorflow as tf

model = tf.keras.Sequential(
    [
        tf.keras.Input(shape=(4,)),  # Define input shape here in Keras 3.x
        tf.keras.layers.Dense(units=16, activation="relu"),
        tf.keras.layers.Dense(units=8, activation="relu"),
        tf.keras.layers.Dense(units=1, activation="sigmoid"),
    ]
)

model.summary()
