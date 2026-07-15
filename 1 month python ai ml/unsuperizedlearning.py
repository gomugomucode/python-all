import matplotlib as plt
from sklearn.cluster import KMeans

X = [[2000] , [3000],[4000]]
kmeans = KMeans(n_clusters=2 , random_state=42)
kmeans.fit(X)
print(kmeans.labels_)
print(kmeans.cluster_centers_)