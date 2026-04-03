import pandas as pd

df = pd.read_csv("Backend/data/fashion_with_clusters.csv")

print("Columns:", df.columns)

assert "cluster" in df.columns, "Cluster column missing"

print("Unique clusters:", df["cluster"].nunique())

print("Clustering test passed")