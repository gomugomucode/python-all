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