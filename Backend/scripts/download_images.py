import pandas as pd
import requests
import os
from tqdm import tqdm

# Paths
DATA_PATH = "Backend/data/fashion_dataset.csv"
SAVE_FOLDER = "Backend/image"

# Create folder if not exists
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)

print("Total images to download:", len(df))

# Download images
success = 0
failed = 0

for i, url in tqdm(enumerate(df["img"]), total=len(df)):

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            with open(f"{SAVE_FOLDER}/{i}.jpg", "wb") as f:
                f.write(response.content)
            success += 1
        else:
            failed += 1

    except:
        failed += 1

print("\nDownload completed")
print("Success:", success)
print("Failed:", failed)