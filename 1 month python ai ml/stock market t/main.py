# ==============================================================================
# NETFLIX (NFLX) STOCK PRICE PREDICTION USING STACKED LSTM
# ==============================================================================
# This script loads historical Netflix stock price data, normalizes the close price,
# converts time series into 100-day sliding window sequences, trains a stacked 
# Long Short-Term Memory (LSTM) deep learning network, evaluates model accuracy, 
# visualizes predictions against actual prices, and forecasts the next 30 days.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------------------------
import numpy as np                 # For numerical array operations and data manipulation
import pandas as pd                # For loading and processing tabular CSV data
import seaborn as sns              # Advanced statistical data visualization library
import matplotlib.pyplot as plt    # Plotting library for charts and graph visualizations
from sklearn.preprocessing import MinMaxScaler  # Normalizes feature data to [0, 1] range

import tensorflow as tf            # Deep learning framework
from tensorflow.keras.models import Sequential       # Sequential model wrapper for stacking layers
from tensorflow.keras.layers import LSTM, Dense, Dropout  # Neural network layers (LSTM, Fully-Connected, Dropout)

# ------------------------------------------------------------------------------
# 2. DATA LOADING & EXPLORATORY DATA ANALYSIS (EDA)
# ------------------------------------------------------------------------------
# Read Netflix stock market dataset with 'Date' column parsed as datetime index
data = pd.read_csv("NFLX - NFLX.csv", index_col="Date", parse_dates=True)

# Display dataset overview in terminal
print("--- Data Head (First 5 rows) ---")
print(data.head())

print("\n--- Data Summary Statistics ---")
print(data.describe())

print("\n--- Data Columns ---")
print(data.columns)

print("\n--- Data Info ---")
data.info()

print("\n--- Data Tail (Last 5 rows) ---")
print(data.tail())

# ------------------------------------------------------------------------------
# 3. DATA VISUALIZATION (PLOTTING HISTORICAL PRICES)
# ------------------------------------------------------------------------------
# Plot each individual feature (Open, High, Low, Close, Adj Close, Volume) over time
for column in data.columns:
    plt.figure(figsize=(12, 4))
    plt.title(f"Stock {column} Price")
    plt.plot(data.index, data[column])
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Plot all price columns together (excluding Volume due to scale difference)
plt.figure(figsize=(12, 4))
plt.title("Netflix Stock Prices (Open, High, Low, Close, Adj Close)")
for column in data.columns:
    if column != "Volume":
        plt.plot(data.index, data[column], label=column)
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# ------------------------------------------------------------------------------
# 4. DATA PREPARATION & NORMALIZATION
# ------------------------------------------------------------------------------
# Select target column: 'Close' price for stock prediction
close_data = data["Close"]
print(f"\nTotal Close price data points: {close_data.shape[0]}")

# Initialize MinMaxScaler to scale stock values into the range [0, 1]
# LSTMs are sensitive to scale of data; feature scaling speeds up convergence
scaler = MinMaxScaler(feature_range=(0, 1))

# Reshape 1D Series into 2D array of shape (N, 1) and fit_transform using scaler
df = scaler.fit_transform(np.array(close_data).reshape([close_data.shape[0], 1]))

# ------------------------------------------------------------------------------
# 5. CREATE SLIDING WINDOW SEQUENCES (TIME-STEP CREATION)
# ------------------------------------------------------------------------------
# Function to convert consecutive price values into sequence datasets:
# X contains input sequences of length `time_step` (e.g., 100 days)
# y contains the target label (price on day 101)
def create_seq(dataset, time_step=100):
    X_seq = []
    y_seq = []
    # Loop over dataset to form window sequences
    for i in range(len(dataset) - time_step - 1):
        X_seq.append(dataset[i : (i + time_step)])
        y_seq.append(dataset[i + time_step])
    return X_seq, y_seq

# Define window size (100 days look-back period)
time_step = 100
X, y = create_seq(df, time_step)

print(f"Total sequence samples generated: {len(X)}")

# Convert lists to NumPy arrays
X = np.array(X)
y = np.array(y)

# Reshape input X to 3D array: [samples, time-steps, features] required by Keras LSTM
X = X.reshape(X.shape[0], X.shape[1], 1)
print(f"Input shape (X): {X.shape}, Target shape (y): {y.shape}")

# ------------------------------------------------------------------------------
# 6. TRAIN / TEST SPLIT
# ------------------------------------------------------------------------------
# Split dataset chronologically: 80% for training, 20% for testing
split_ratio = 0.8
train_size = int(close_data.shape[0] * split_ratio)

X_train = X[:train_size]
X_test = X[train_size:]
y_train = y[:train_size]
y_test = y[train_size:]

print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")

# ------------------------------------------------------------------------------
# 7. BUILD STACKED LSTM NEURAL NETWORK MODEL
# ------------------------------------------------------------------------------
# Instantiate a Sequential Keras architecture
model = Sequential()

# Layer 1: First LSTM layer with 128 units, return_sequences=True to feed 2nd LSTM
model.add(LSTM(128, return_sequences=True, input_shape=(X_train.shape[1], 1)))

# Layer 2: Second LSTM layer with 64 units, return_sequences=True to feed 3rd LSTM
model.add(LSTM(64, return_sequences=True))

# Layer 3: Third LSTM layer with 32 units (returns 1D summary vector)
model.add(LSTM(32))

# Layer 4: Dense fully connected hidden layer with 16 neurons and ReLU activation
model.add(Dense(16, activation="relu"))

# Layer 5: Output Dense layer with 1 neuron (predicting continuous price)
model.add(Dense(1))

# Compile model using Adam optimizer, Mean Squared Error loss, and Root Mean Squared Error metric
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss="mean_squared_error",
    metrics=[tf.keras.metrics.RootMeanSquaredError()],
)

# Print neural network summary architecture table
model.summary()

# ------------------------------------------------------------------------------
# 8. TRAIN MODEL
# ------------------------------------------------------------------------------
print("\n--- Training Model ---")
# Train network for 100 epochs with training data
history = model.fit(X_train, y_train, epochs=100, batch_size=64, verbose=1)

# ------------------------------------------------------------------------------
# 9. EVALUATE & PREDICT ON TRAIN/TEST SETS
# ------------------------------------------------------------------------------
# Generate predictions on training set and test set
trainPred = model.predict(X_train)
testPred = model.predict(X_test)

# Reverse MinMax normalization to convert predicted values back to actual dollar prices
trainPred = scaler.inverse_transform(trainPred)
testPred = scaler.inverse_transform(testPred)

# Evaluate model performance on unseen test data
eval_result = model.evaluate(X_test, y_test)
print(f"Test Loss (MSE): {eval_result[0]:.4f}, Test RMSE: {eval_result[1]:.4f}")

# ------------------------------------------------------------------------------
# 10. VISUALIZE MODEL PREDICTIONS VS ACTUAL PRICES
# ------------------------------------------------------------------------------
look_back = time_step

# Prepare arrays filled with NaN to align graph timelines for plotting
trainPredPlot = np.empty_like(scaler.inverse_transform(df))
trainPredPlot[:] = np.nan
# Align training predictions on plot timeframe
trainPredPlot[look_back : len(trainPred) + look_back] = trainPred

testPredPlot = np.empty_like(scaler.inverse_transform(df))
testPredPlot[:] = np.nan
# Align testing predictions on plot timeframe
testPredPlot[len(trainPred) + look_back : len(trainPred) + look_back + len(testPred)] = testPred

# Plot actual vs predicted closing prices
plt.figure(figsize=(14, 6))
plt.title("Netflix Stock Price Prediction using Stacked LSTM")
plt.plot(scaler.inverse_transform(df), label="Actual Close Price", color="blue")
plt.plot(trainPredPlot, label="Training Set Prediction", color="orange")
plt.plot(testPredPlot, label="Testing Set Prediction", color="green")
plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

# ------------------------------------------------------------------------------
# 11. RECURSIVE 30-DAY FUTURE STOCK PRICE FORECASTING
# ------------------------------------------------------------------------------
# Extract last 100 days of closing price data as seed sequence for future forecast
prediction_data = np.array(close_data[-time_step:])
prediction_data = prediction_data.reshape([prediction_data.shape[0], 1])

# Function to recursively forecast future stock prices day by day
def predict_future_days(input_data, days=30):
    # Scale input window data
    current_window = scaler.transform(input_data)
    future_predictions = []
    
    for _ in range(1, days + 1):
        # Predict next day using current 100-day window (reshaped to [1, 100, 1])
        nxt_day_pred = model.predict(current_window.reshape(1, time_step, 1), verbose=0)
        
        # Un-scale predicted price and append to result list
        unscaled_pred = scaler.inverse_transform(nxt_day_pred)[0]
        future_predictions.append(unscaled_pred)
        
        # Shift 100-day window forward by removing oldest day and appending predicted day
        current_window[:-1] = current_window[1:]
        current_window[-1] = nxt_day_pred[0]
        
    return np.array(future_predictions).squeeze()

# Forecast stock price for next 30 days
future_days = 30
future_forecast = predict_future_days(prediction_data, days=future_days)

# Prepare array for plotting historical 100 days + 30 forecast days
forecastPlot = np.zeros(shape=[len(prediction_data) + future_days])
forecastPlot[:] = np.nan
# Align forecast line to start after last known date
forecastPlot[len(prediction_data) :] = future_forecast

# Plot recent 100 days and 30 days future forecast
plt.figure(figsize=(12, 5))
plt.title(f"Next {future_days}-Day Future Netflix Stock Price Forecast")
plt.plot(prediction_data, label="Recent Actual Close Price (Last 100 Days)", color="blue")
plt.plot(forecastPlot, label=f"Next {future_days}-Day Future Forecast", color="red", linestyle="--")
plt.xlabel("Days")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()
