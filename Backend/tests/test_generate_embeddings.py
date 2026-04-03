import numpy as np

emb = np.load("Backend/data/fashion_embeddings.npy")

print("Shape:", emb.shape)

assert emb.shape[1] == 2048, "Embedding dimension incorrect"
assert emb.shape[0] > 0, "No embeddings found"

print("Embedding generation test passed")