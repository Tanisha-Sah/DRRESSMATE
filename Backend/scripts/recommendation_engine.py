import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from Backend.scripts.feature_extraction import extract_features
from Backend.scripts.skin_tone import detect_skin_properties, recommend_colors
from Backend.scripts.body_shape import detect_body_shape, recommend_style

# Paths
EMBED_PATH = "Backend/data/fashion_embeddings.npy"
DATA_PATH = "Backend/data/fashion_with_clusters.csv"

# Load once
embeddings = np.load(EMBED_PATH)
df = pd.read_csv(DATA_PATH)

# Helper Functions
def color_score(item_color, preferred_colors):

    if pd.isna(item_color):
        return 0

    item_color = str(item_color).lower()

    if item_color in [c.lower() for c in preferred_colors]:
        return 1

    return 0


def style_score(row, preferred_styles):

    item_type = str(row.get("articleType", "")).lower()

    for style in preferred_styles:
        if style.lower() in item_type:
            return 1

    return 0


# MAIN RECOMMEND FUNCTION

def recommend(image_path, top_n=5):

    #Feature extraction
    query_features = extract_features(image_path).reshape(1, -1)

    similarities = cosine_similarity(query_features, embeddings)[0]

    # Find cluster
    best_index = similarities.argmax()
    query_cluster = df.iloc[best_index]["cluster"]

    cluster_indices = df[df["cluster"] == query_cluster].index
    filtered_embeddings = embeddings[cluster_indices]

    filtered_sim = cosine_similarity(query_features, filtered_embeddings)[0]

    # Skin tone analysis
    skin = detect_skin_properties(image_path)

    tone = skin["tone"]
    undertone = skin["undertone"]

    preferred_colors = recommend_colors(tone, undertone)


    print("\n--- Skin Analysis ---")
    print("Tone:", tone)
    print("Undertone:", undertone)
    print("Colors:", preferred_colors)

    # Body shape analysis
    body_shape = detect_body_shape(image_path)

    preferred_styles = recommend_style(body_shape)

    print("\n--- Body Shape ---")
    print("Shape:", body_shape)
    print("Styles:", preferred_styles)

    #  Hybrid scoring
    final_scores = []

    for i, idx in enumerate(cluster_indices):

        sim_score = filtered_sim[i]

        col_score = color_score(
            df.iloc[idx].get("baseColour"),
            preferred_colors
        )

        sty_score = style_score(
            df.iloc[idx],
            preferred_styles
        )

        # FINAL SCORE
        score = (
            0.6 * sim_score +
            0.2 * sty_score +
            0.2 * col_score
        )

        final_scores.append(score)

    final_scores = np.array(final_scores)

    # Top results

    top_indices = final_scores.argsort()[-top_n:][::-1]

    final_indices = cluster_indices[top_indices]

    results = df.iloc[final_indices]

    return results[[
        "img",
        "cluster",
        "colour",
        "dress_category",
        "occasion"
    ]]