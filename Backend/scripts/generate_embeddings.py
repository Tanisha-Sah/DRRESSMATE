import numpy as np
import pandas as pd

from feature_extraction import extract_features

DATA_PATH = "Backend/data/fashion_dataset.csv"
SAVE_PATH = "Backend/data/fashion_embeddings.npy"
IMAGE_FOLDER = "Backend/image"

df = pd.read_csv(DATA_PATH)

embeddings = []

print("Generating embeddings...")

for i in range(len(df)):

    img_path = f"{IMAGE_FOLDER}/{i}.jpg"

    try:
        features = extract_features(img_path)
        embeddings.append(features)

    except:
        # If image fails, add zero vector
        embeddings.append(np.zeros(2048))

    if i % 100 == 0:
        print(f"Processed {i} images")

embeddings = np.array(embeddings)

np.save(SAVE_PATH, embeddings)

print("Embeddings saved")
print("Shape:", embeddings.shape)