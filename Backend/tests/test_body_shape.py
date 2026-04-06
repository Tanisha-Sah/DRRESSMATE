import os
from Backend.scripts.body_shape import detect_body_shape, recommend_style

# CHANGE IMAGE HERE (ONLY THIS LINE)

img = os.path.join("Backend", "image", "10030.jpg")


# CHECK IMAGE
print("Image path:", img)
print("Exists:", os.path.exists(img))

assert os.path.exists(img), "Image not found! Check path"


# BODY SHAPE DETECTION

shape = detect_body_shape(img)

print("Detected shape:", shape)

assert shape in [
    "hourglass",
    "pear",
    "inverted_triangle",
    "rectangle",
    "apple",
    "athletic",
    "unknown"
]

# STYLE RECOMMENDATION

styles = recommend_style(shape)

print("Recommended styles:", styles)

assert isinstance(styles, list)
assert len(styles) > 0


print("Body shape test working perfectly")