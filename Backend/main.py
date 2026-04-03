from fastapi import FastAPI, UploadFile, File
import shutil
import os

# from Backend.scripts.recommendation_engine import recommend

app = FastAPI()

# Root
@app.get("/")
def read_root():
    return {"status": "ok", "message": "FashionAI API is running"}

# # Health
# @app.get("/health")
# def health():
#     return {"status": "healthy"}


# # FIXED RECOMMEND API
# @app.post("/api/recommend/image")
# def recommend_image(file: UploadFile = File(...)):

#     try:
#         # Ensure upload folder exists
#         os.makedirs("Backend/uploads", exist_ok=True)

#         file_path = f"Backend/uploads/{file.filename}"

#         # Save file
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)

#         # Call recommendation
#         results = recommend(file_path, top_n=5)

#         return {
#             "status": "success",
#             "recommendations": results.to_dict(orient="records")
#         }

#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e)
#         }