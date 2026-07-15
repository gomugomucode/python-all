import matplotlib as plt
from sklearn.cluster import KMeans

X = [[2000] , [3000],[4000]]
kmeans = KMeans(n_clusters=2 , random_state=42)
kmeans.fit(X)
print(kmeans.labels_)
print(kmeans.cluster_centers_)


# hierarchical clustering

from scipy.cluster.hierarchy import dendrogram , linkage
import matplotlib as plt

Z = linkage(X , method='ward')
dendrogram(Z)
plt.show()


# DBSCAN