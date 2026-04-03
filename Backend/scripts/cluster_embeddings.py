import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# Paths
EMBED_PATH = "Backend/data/fashion_embeddings.npy"
DATA_PATH = "Backend/data/fashion_dataset.csv"
SAVE_PATH = "Backend/data/fashion_with_clusters.csv"

# Load data
embeddings = np.load(EMBED_PATH)
df = pd.read_csv(DATA_PATH)

print("Embeddings shape:", embeddings.shape)

# Number of clusters
K = 20

# Apply KMeans
kmeans = KMeans(n_clusters=K, random_state=42)
clusters = kmeans.fit_predict(embeddings)

# Add cluster column
df["cluster"] = clusters

# Save
df.to_csv(SAVE_PATH, index=False)

print("Clustering completed")
print("Saved:", SAVE_PATH)