from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 2],
              [1, 4],   
              [1, 0],
                  [4, 2],
                  [4, 4],
                  [4, 0]])

model = KMeans(n_clusters=2, random_state=0)
model.fit(X)    
print(model.labels_)




# # underfitting
# from sklearn.linear_model import LinearRegression
# import numpy as np

# X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y =np.array([1, 1, 2, 2])
# model = LinearRegression().fit(X, y)
# model.fit(X, y)
# print(model.predict([[1 ]]))



# # overfitting

# from sklearn.tree import DecisionTreeRegressor
# X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = np.array([1, 1, 2, 2])
# model = DecisionTreeRegressor().fit(X, y)
# model.fit(X, y)
# print(model.predict([[1 ]]))