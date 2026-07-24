# Netflix Stock Price Prediction using Stacked LSTM

A deep learning project that builds and trains a **Stacked Long Short-Term Memory (LSTM)** neural network model to predict Netflix (`NFLX`) stock closing prices and forecast future stock price trends for the next 30 days.

---

## 📌 Project Overview

Stock market prices are time-series data with complex non-linear patterns. Recurrent Neural Networks (RNNs), specifically **LSTM (Long Short-Term Memory)** networks, are well-suited for time-series forecasting because they maintain long-term memory dependencies without suffering from vanishing gradients.

This project performs:
1. **Exploratory Data Analysis (EDA)** on historical Netflix stock prices (`Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`).
2. **MinMax Normalization** to scale prices into a normalized range $[0, 1]$.
3. **Sliding Window Sequence Creation** (100 days of historical prices used as features $X$ to predict day 101 target $y$).
4. **80/20 Train-Test Splitting** preserving chronological order.
5. **Stacked LSTM Architecture** construction using TensorFlow / Keras.
6. **Model Training & Evaluation** with loss/RMSE metrics and inverse scaling.
7. **Visualization** comparing actual vs predicted prices on both training and test periods.
8. **Recursive 30-Day Future Forecasting** to predict future stock price trends.

---

## 📁 Repository Structure

```text
c:\Users\Anupam Baral\Downloads\python\1 month python ai ml\stock market t\
├── NFLX - NFLX.csv         # Netflix historical stock market dataset
├── main.py                 # Main Python script containing data processing & LSTM model
└── README.md               # Project documentation & usage guide
```

---

## 📊 Dataset Description

The dataset file `NFLX - NFLX.csv` contains historical stock performance data for Netflix:
- `Date`: Date of stock trading (used as datetime index).
- `Open`: Opening price of the stock for the day.
- `High`: Highest price reached during the day.
- `Low`: Lowest price reached during the day.
- `Close`: Closing price of the stock (primary target feature for prediction).
- `Adj Close`: Adjusted closing price considering stock splits/dividends.
- `Volume`: Number of shares traded during the day.

---

## 🧠 Model Architecture

The neural network is built with Keras `Sequential` API with stacked LSTM layers:

| Layer | Type | Configuration / Units | Details |
| :--- | :--- | :--- | :--- |
| **Layer 1** | `LSTM` | 128 units, `return_sequences=True` | Accepts input shape `(100, 1)` and passes sequence outputs. |
| **Layer 2** | `LSTM` | 64 units, `return_sequences=True` | Second recurrent feature extraction layer. |
| **Layer 3** | `LSTM` | 32 units | Final LSTM layer returning a 1D state summary vector. |
| **Layer 4** | `Dense` | 16 units, `activation='relu'` | Fully connected hidden layer for non-linear combination. |
| **Layer 5** | `Dense` | 1 unit | Output layer predicting the continuous scaled close price. |

### Compilation Parameters
- **Optimizer**: `Adam(learning_rate=0.001)`
- **Loss Function**: `mean_squared_error` (MSE)
- **Evaluation Metric**: `RootMeanSquaredError` (RMSE)
- **Training Epochs**: 100 epochs, `batch_size=64`

---

## ⚙️ How It Works (Step-by-Step)

### 1. Data Normalization
Neural networks perform best when input values are scaled. `MinMaxScaler(feature_range=(0, 1))` scales the stock price range:
$$x_{\text{scaled}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

### 2. Time-Step Windowing (`time_step = 100`)
The dataset is converted into 3D input arrays of shape `(samples, 100, 1)`:
- $X_i = [\text{Price}_{i}, \text{Price}_{i+1}, \dots, \text{Price}_{i+99}]$
- $y_i = \text{Price}_{i+100}$

### 3. Chronological Train-Test Split
- **Training Set (80%)**: Used to fit model weights over 100 epochs.
- **Testing Set (20%)**: Evaluates model generalization on unseen future dates.

### 4. Recursive 30-Day Future Prediction
To predict beyond the dataset, the script extracts the last 100 known days as a seed sequence and iteratively predicts day $t+1$, appends the new prediction to the input window, drops the oldest day, and repeats for 30 steps.

---

## 🚀 Getting Started & Execution

### Prerequisites
Make sure your Python environment (or virtual environment) has the required dependencies installed:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow
```

### Running the Project

1. Open your terminal and navigate to the project directory:
   ```bash
   cd "C:\Users\Anupam Baral\Downloads\python\1 month python ai ml\stock market t\"
   ```

2. Activate your virtual environment (if using one):
   ```powershell
   ..\..\..\.venv\Scripts\activate
   ```

3. Run `main.py`:
   ```bash
   python main.py
   ```

---

## 📈 Visualizations Output

Running `main.py` generates the following plots:
1. **Stock Feature Trends**: Individual plots for Open, High, Low, Close, Adj Close, and Volume.
2. **Combined Stock Price Trend**: Overlay plot of price columns over time.
3. **Actual vs Predicted Stock Price**: Full dataset comparison showing Training predictions (Orange) and Testing predictions (Green) against Actual Close Prices (Blue).
4. **30-Day Future Forecast Plot**: Historical 100-day trend with dotted red line forecasting the upcoming 30 days.
