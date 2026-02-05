import streamlit as st
import pickle
import pandas as pd
import gzip

st.set_page_config(page_title="Movie Recommender", layout="centered")

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))

with gzip.open('similarity_compressed.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

movies = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

st.title("🎬 Movie Recommendation System")
st.write("Select a movie to get similar recommendations")

selected_movie = st.selectbox("Choose a Movie", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write("✅", movie)
