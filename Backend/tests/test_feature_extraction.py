from Backend.scripts.feature_extraction import extract_features
img_path = "Backend/image/0.jpg"

features = extract_features(img_path)

print("Feature length:", len(features))

assert len(features) == 2048, "Feature size incorrect"

print("Feature extraction test passed")