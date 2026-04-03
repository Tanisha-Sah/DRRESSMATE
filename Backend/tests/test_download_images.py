import os

folder = "Backend/image"

files = os.listdir(folder)

print("Total images:", len(files))

assert len(files) > 14200, "Too few images downloaded"

print("Image download test passed")