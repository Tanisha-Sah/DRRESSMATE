from Backend.scripts.skin_tone import detect_skin_tone
from Backend.scripts.skin_tone import recommend_colors

img = "Backend/image/15.jpg"
tone = detect_skin_tone(img)
print("Detected tone:", tone)
assert tone in ["dark", "medium", "fair"]
print("Advanced skin tone test passed")

colors = recommend_colors("medium")
print(colors)
assert isinstance(colors, list)
print("Color recommendation test passed")