import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load data with error handling
@st.cache_data
def load_data():
    try:
        movies = pd.read_csv(r'C:\Users\Surface Laptop 3\OneDrive\Documents\DataScience\movie_recommender_project\data\movies.csv')
        
        # Extract year from title safely
        def extract_year(title):
            if isinstance(title, str):
                import re
                match = re.search(r'\((\d{4})\)', title)
                return int(match.group(1)) if match else 1900
            return 1900
        
        movies['year'] = movies['title'].apply(extract_year)
        movies['title_clean'] = movies['title'].str.replace(r'\s*\(\d{4}\)\s*', '', regex=True)
        
        # Create genre matrix safely
        movies['genres'] = movies['genres'].fillna('')
        genre_matrix = movies['genres'].str.get_dummies(sep='|')
        
        return movies, genre_matrix
    except Exception as e:
        st.error(f"Error loading data: {e}")
        # Return empty dataframes to prevent crash
        return pd.DataFrame(), pd.DataFrame()

def main():
    st.set_page_config(page_title="Movie Recommender", layout="wide")
    
    st.title("🎬 Movie Recommender")
    st.markdown("A simple content-based recommendation system")
    
    # Load data
    movies, genre_matrix = load_data()
    
    if movies.empty:
        st.error("Could not load movie data. Please check data/movies.csv exists.")
        return
    
    # Tab 1: Find Similar Movies
    st.header("Find Similar Movies")
    
    # Movie selector
    movie_titles = movies['title'].tolist()
    selected_movie = st.selectbox("Choose a movie:", movie_titles)
    
    if selected_movie and st.button("Find Similar Movies"):
        try:
            # Find movie index
            movie_idx = movies[movies['title'] == selected_movie].index[0]
            
            # Calculate similarities
            movie_vector = genre_matrix.iloc[movie_idx:movie_idx+1]
            similarities = cosine_similarity(movie_vector, genre_matrix)[0]
            
            # Get top 10 similar
            similar_indices = np.argsort(similarities)[::-1][1:11]
            
            # Display results
            st.subheader(f"Movies similar to '{selected_movie}':")
            
            for i, idx in enumerate(similar_indices, 1):
                movie = movies.iloc[idx]
                similarity = similarities[idx]
                
                st.write(f"{i}. **{movie['title_clean']}** ({movie['year']})")
                st.write(f"   Genres: {movie['genres']}")
                st.write(f"   Similarity: {similarity:.1%}")
                st.write("---")
                
        except Exception as e:
            st.error(f"Error finding similar movies: {e}")
    
    st.markdown("---")
    
    # Tab 2: Browse by Genre (simplified)
    st.header("Browse Movies by Genre")
    
    # Get all unique genres
    all_genres = []
    for genres in movies['genres'].str.split('|'):
        if isinstance(genres, list):
            all_genres.extend(genres)
    unique_genres = sorted(set(all_genres))
    
    # Genre selector
    selected_genre = st.selectbox("Select genre:", [""] + unique_genres)
    
    if selected_genre:
        # Filter movies with this genre
        filtered = movies[movies['genres'].str.contains(selected_genre, na=False)]
        st.write(f"Found {len(filtered)} movies with genre '{selected_genre}':")
        
        if not filtered.empty:
            # Show top 20
            for _, movie in filtered.head(20).iterrows():
                st.write(f"• **{movie['title_clean']}** ({movie['year']})")
        else:
            st.write("No movies found with this genre.")

if __name__ == "__main__":
    main()