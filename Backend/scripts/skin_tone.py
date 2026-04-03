import cv2
import numpy as np

# FUNCTION 1: Detect skin tone
def detect_skin_tone(image_path):

    img = cv2.imread(image_path)

    if img is None:
        return "medium"   # fallback

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        x, y, w, h = faces[0]
        face = img_rgb[y:y+h, x:x+w]
    else:
        h, w, _ = img_rgb.shape
        face = img_rgb[h//4:h//2, w//4:w//2]

    lab = cv2.cvtColor(face, cv2.COLOR_RGB2LAB)
    L, A, B = cv2.split(lab)

    avg_L = np.mean(L)

    if avg_L < 80:
        return "dark"
    elif avg_L < 140:
        return "medium"
    else:
        return "fair"

