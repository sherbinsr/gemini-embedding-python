# Gemini-Powered Movie Recommendation System

This project is a content-based movie recommendation system that leverages the Google Gemini API to perform semantic search on movie descriptions. It provides movie suggestions based on the contextual meaning of a user's query, rather than just keyword matching.

## Features

-   **Semantic Search**: Understands the user's query in a contextual way.
-   **Content-Based Recommendations**: Suggests movies based on plot summaries and descriptions.
-   **Powered by Google Gemini**: Uses state-of-the-art embedding models for vector representations.
-   **Easy to Use**: Simple command-line interface to get recommendations.

## How It Works

The system works by converting both the movie descriptions and the user's query into high-dimensional vectors (embeddings) using the `embedding-001` model from the Google Gemini API. These embeddings capture the semantic essence of the text.

When a user enters a query (e.g., "a scary movie with ghosts"), the system calculates the **cosine similarity** between the query's vector and the vector of each movie in the database. The movies with the highest similarity scores are then returned as the top recommendations.

This approach allows the system to understand complex queries and find movies that are thematically related, even if they don't share exact keywords.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
    *Note: On Windows, use `venv\Scripts\activate`.*

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your API key:**
    -   Copy the example `.env` file:
        ```bash
        cp .env.example .env
        ```
    -   Add your Google Gemini API key to the `.env` file:
        ```
        SECRET_KEY=your_secret_key_here
        ```

## Running the Application

To get movie recommendations, run the `main.py` script:

```bash
python main.py
```

The script will output recommendations for predefined sample queries. You can modify the `user_input` variable in `main.py` to test your own queries.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

