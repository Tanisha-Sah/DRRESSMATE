from Backend.scripts.recommendation_engine import recommend

# Test image
test_image = "Backend/images/0.jpg"

results = recommend(test_image, top_n=5)

print(results)

assert len(results) == 5, "Recommendation failed"

print("Recommendation test passed")