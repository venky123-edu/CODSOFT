import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
movies_data = {
    'title': ['The Dark Knight', 'Inception', 'Pulp Fiction', 'The Shawshank Redemption', 
              'The Matrix', 'Forrest Gump', 'Fight Club', 'Interstellar'],
    'genres': ['Action Crime Drama', 'Sci-Fi Action Thriller', 'Crime Drama Thriller', 
               'Drama', 'Sci-Fi Action', 'Drama Romance', 'Drama Thriller', 
               'Sci-Fi Drama Adventure']
}

# Create DataFrame
movies_df = pd.DataFrame(movies_data)

# Function to create movie feature vectors
def create_movie_features():
    # Convert genres to feature vectors
    vectorizer = CountVectorizer()
    genre_matrix = vectorizer.fit_transform(movies_df['genres'])
    return genre_matrix, vectorizer

# Function to get recommendations
def get_recommendations(user_preferences, n_recommendations=3):
    genre_matrix, vectorizer = create_movie_features()
    
    # Convert user preferences to feature vector
    user_vector = vectorizer.transform([user_preferences])
    
    # Calculate similarity between user preferences and movies
    similarity_scores = cosine_similarity(user_vector, genre_matrix)
    
    # Get indices of top similar movies
    similar_movie_indices = similarity_scores.argsort()[0][::-1][:n_recommendations]
    
    # Return recommended movie titles
    return movies_df['title'].iloc[similar_movie_indices].tolist()

# Example usage
def main():
    # Example user preferences
    user_prefs = "Sci-Fi Action"
    recommendations = get_recommendations(user_prefs)
    
    print(f"Recommendations for user who likes '{user_prefs}':")
    for i, movie in enumerate(recommendations, 1):
        print(f"{i}. {movie}")

if __name__ == "__main__":
    main()