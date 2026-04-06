# from Backend.scripts.recommendation_engine import recommend

# # CHANGE IMAGE HERE
# img = "Backend/image/0.jpg"

# results = recommend(img, top_n=5)

# print("\n--- FINAL RESULTS ---")
# print(results)

# assert len(results) == 5

# print("\nFULL AI SYSTEM WORKING")

import os
import cv2
import requests
import numpy as np
from Backend.scripts.recommendation_engine import recommend

# Input image
img = "Backend/uploads/OIP.jpg"

results = recommend(img, top_n=5)

print("\n--- SHOWING RECOMMENDED IMAGES ---")

for i, row in results.iterrows():

    img_url = row["img"]

    print("Showing:", img_url)

    try:
        # Download image from URL
        response = requests.get(img_url, timeout=10)

        img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if image is not None:
            cv2.imshow(f"Recommendation {i}", image)
            cv2.waitKey(0)

    except Exception as e:
        print("Failed to load:", img_url)

cv2.destroyAllWindows()