import google.generativeai as genai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv

load_dotenv()

# API key from environment variables
secret_key = os.getenv("API_KEY")


if not secret_key:
    raise ValueError("API_KEY not found in .env file")


# Initialize the client 
genai.configure(api_key=secret_key)

# Sample Movie Data
movies = [
    {"title": "Love & Laughter", "desc": "A romantic comedy about two clumsy chefs who fall in love."},
    {"title": "Galactic Wars", "desc": "An epic sci-fi tale of rebellion in a galaxy far away."},
    {"title": "Haunted Whisper", "desc": "A horror thriller set in an abandoned mansion with dark secrets."},
    {"title": "Time Loop", "desc": "A time travel mystery where a detective relives the same day."},
    {"title": "Café Paris", "desc": "Two strangers meet in a café and discover their intertwined past."}
]


# Get embedding for a given text
def get_embedding(text):
    response = genai.embed_content(
        model="models/embedding-001", 
        content=text
    )
    return response['embedding']

# Generate embeddings for all movie descriptions
for movie in movies:
    movie["embedding"] = get_embedding(movie["desc"])


# Recommend top movies based on user query
def recommend_movies(user_query, top_k=3):
    query_embedding = get_embedding(user_query)

    similarities = []
    for movie in movies:
        score = cosine_similarity([query_embedding], [movie["embedding"]])[0][0]
        similarities.append((movie["title"], score))

    # Sort by similarity score (high to low)
    top_matches = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]
    return top_matches



# sample query
user_input = "romantic comedy with emotional story"
top_movies = recommend_movies(user_input)



# Show recommendations
print(f"\n🎯 Top recommendations for: '{user_input}'\n")
for title, score in top_movies:
    print(f"🎬 {title} — Similarity Score: {score:.3f}")
