import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from Backend.scripts.feature_extraction import extract_features
from Backend.scripts.skin_tone import detect_skin_tone

# Paths
EMBED_PATH = "Backend/data/fashion_embeddings.npy"
DATA_PATH = "Backend/data/fashion_with_clusters.csv"

# Load once (global)
embeddings = np.load(EMBED_PATH)
df = pd.read_csv(DATA_PATH)


def recommend(image_path, top_n=5):

    #Extract query features
    query_features = extract_features(image_path).reshape(1, -1)

    #Find closest match (to detect cluster)
    similarities = cosine_similarity(query_features, embeddings)[0]
    best_index = similarities.argmax()

    #Get cluster of best match
    query_cluster = df.iloc[best_index]["cluster"]

    #Filter dataset by same cluster
    cluster_indices = df[df["cluster"] == query_cluster].index

    filtered_embeddings = embeddings[cluster_indices]

    #Compute similarity within cluster
    filtered_sim = cosine_similarity(query_features, filtered_embeddings)[0]

    #Get top results
    top_indices = filtered_sim.argsort()[-top_n:][::-1]

    final_indices = cluster_indices[top_indices]

    results = df.iloc[final_indices]

    return results[["img", "cluster"]]
