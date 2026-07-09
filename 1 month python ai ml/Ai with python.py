# from sklearn.linear_model import LinearRegression
# import numpy as np

# model = LinearRegression()

# x = np.array([[1], [2], [3], [4], [5]])
# y = np.array([2, 4, 6, 8, 10])

# model.fit(x, y)

# result = model.predict([[6]])
# print(result) 




from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])  # Binary target variable

model = LogisticRegression()
model.fit(X, y)

# result = model.predict([[15]])
# result = model.predict_proba([[15]])

result = model.predict([[9]])

print(result)