import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
#reading the data and making the date is the index
data=pd.read_csv('/content/NFLX.csv',index_col='Date',parse_dates=True)
data
data.head()
data.describe()
data.columns
data.info()
data.head()
data.tail()


# ```
# This is formatted as code
# ```

# - There is no NaN data
# - Date handled already
# - next step is ploting our Data to see what is the important feature
# # Ploting Data
data.columns
for columns in data.columns:
    plt.figure(figsize=(12,4))
    plt.title(f"Stock {columns} Price")
    plt.plot(data.index,data[columns])
    plt.xticks(rotation=45)
plt.figure(figsize=(12,4))
plt.title("Stock Price")
for columns in data.columns:
    if(columns !='Volume'):
        plt.plot(data.index,data[columns],label=columns)
plt.xticks(rotation=45)
plt.legend()
# - after ploting Data we decide to take High feature to predict when the stock will be high
# - next step we Data normalization
# Data Normalization
data=data['Close']
data.shape

data
np.array(data)
scaler =  MinMaxScaler(feature_range=(0,1))
np.array(data).reshape([data.shape[0],1])
data.shape
# df=scaler.fit_transform(np.array(data['Close']).reshape(-1,1))
df=scaler.fit_transform(np.array(data).reshape([data.shape[0],1]))
df
# from sklearn.model_selection import train_test_split
# X_train,X_test=train_test_split(df,test_size=0.2,random_state=0)
# X_train.shape
# X_test.shape
# Convert array Values into a dataset values
X = []
y = []
for i in range(len(data)-100-1):
    X.append(data[i:(i+100)])
    y.append(data[i+100])

print(X,y)
def create_seq(data,time_step=100):
    X=[]
    y=[]
    for i in range(len(data)-time_step-1):
        X.append(data[i:(i+time_step)])
        y.append(data[i+time_step])
        # print(data[i:(i+time_step)],data[i+time_step])
    return X,y
time_step=100
X,y=create_seq(df,time_step)
X
y
len(X),len(y)
y
## reshape input to be [samples, time-steps, features] which is required for LSTM
np.array(X).shape
np.array(y).shape
X=np.array(X)
X=X.reshape(X.shape[0],X.shape[1],1)
y=np.array(y)
X.shape,y.shape
## Splitting the data
X_train,X_test,y_train,y_test=X[:int(data.shape[0]*0.8)],X[int(data.shape[0]*0.8):],y[:int(data.shape[0]*0.8)],y[int(data.shape[0]*0.8):]
X_train.shape,X_test.shape,y_train.shape,y_test.shape
X_train[0].shape
# Model
model=Sequential()
model.add(LSTM(128,return_sequences=True,input_shape=X_train[0].shape))
model.add(LSTM(64,return_sequences=True))
model.add(LSTM(32))
model.add(Dense(16,activation='relu'))
model.add(Dense(1))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss="mean_squared_error", metrics=[tf.keras.metrics.RootMeanSquaredError()])
model.summary()
## Training the Model
model.fit(X_train,y_train,epochs=100)
## Test the Model
trainPred=model.predict(X_train)
testPred=model.predict(X_test)

trainPred=scaler.inverse_transform(trainPred)
testPred=scaler.inverse_transform(testPred)
trainPred
testPred
## Model performance
model.evaluate(X_test,y_test)
df
## Ploting Performance

time_step = 100
look_back=time_step
# shift train predictions for plotting (time step)

trainPredPlot=np.empty_like(scaler.inverse_transform(df))

trainPredPlot[:]=np.nan
trainPredPlot[look_back:len(trainPred)+look_back]=trainPred

# #shift test predictions for plotting(time_step)
testPredPlot=np.empty_like(scaler.inverse_transform(df))
testPredPlot[:]=np.nan
testPredPlot[len(trainPred)+look_back:len(trainPred)+look_back+len(testPred)]=testPred

plt.plot(scaler.inverse_transform(df),label="Actual close price")
plt.plot(trainPredPlot,label="Training prediction close price")
plt.plot(testPredPlot,label="Predicted close price")
plt.legend()
plt.show()
# Next 30 days prediction
predection_data=np.array(data[-time_step:])
predection_data=predection_data.reshape([predection_data.shape[0],1])
def predication(data,days=30):
    data=scaler.transform(data)
    pred=[]
    for i in range(1,days+1):
        nxt_day=model.predict([data],verbose=0)
        pred.append(scaler.inverse_transform(nxt_day)[0])
        data[:-1]=data[1:]
        data[-1]=nxt_day[0]
    return np.array(pred).squeeze()
days=30
res=predication(predection_data,days)
trainPredPlot=np.zeros(shape=[len(predection_data)+1+days])
trainPredPlot[:]=np.nan
trainPredPlot[len(predection_data)]=res[-1]
trainPredPlot[len(predection_data)+1:]=res
df_=predection_data
plt.plot(df_,label="Actual close price")
plt.plot(trainPredPlot,label="Predicted close price")
plt.legend()
plt.show()