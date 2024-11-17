# Ukázka animace pomocí FuncAnimation z modulu matplotlib

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from matplotlib.animation import FuncAnimation

# 1. Generate sample data
np.random.seed(42)
n_samples = 500
n_clusters = 4
cluster_std = 5

X, y_true = make_blobs(n_samples=n_samples, centers=n_clusters, cluster_std=cluster_std)


# 2. Function to initialize the plot
fig, ax = plt.subplots()


# Scatter plot of data points without clustering
sc = ax.scatter(X[:, 0], X[:, 1], s=30, color='gray')
centers_plot = ax.scatter([], [], s=200, c='red', marker='X', label="Centroids")
legend = ax.legend(loc="upper right")


# 4. Function to update each frame in the animation
def update(frame):
    # Fit KMeans model for one more iteration
    kmeans = KMeans(n_clusters=3, init="random", random_state=42, max_iter=frame+1)
    kmeans.fit(X)
    
    # Get updated centroids and labels
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    # Update data point colors based on cluster labels
    sc.set_color([plt.cm.tab10(label) for label in labels])
    
    # Update centroid positions
    centers_plot.set_offsets(centroids)

    ax.set_title(f"K-means Clustering - Animation step {frame+1}")


# 5. Create the animation
num_steps = 10

anim = FuncAnimation(fig, update, frames=num_steps, interval=500, repeat=False)
plt.show()