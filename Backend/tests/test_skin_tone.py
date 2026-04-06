import os
from Backend.scripts.skin_tone import detect_skin_properties, recommend_colors

# Test image
img = os.path.join("Backend", "image", "0.jpg")

print("File exists:", os.path.exists(img))

assert os.path.exists(img), "Image not found"

# Run detection
result = detect_skin_properties(img)

print("Result:", result)

assert isinstance(result, dict)
assert result["tone"] in ["dark", "medium", "fair"]
assert result["undertone"] in ["warm", "cool", "neutral"]

print("Skin detection working")

# Test colors
colors = recommend_colors(result["tone"], result["undertone"])

print("Colors:", colors)

assert isinstance(colors, list)
assert len(colors) > 0

print("Color recommendation working")