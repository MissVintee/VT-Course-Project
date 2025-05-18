import pickle
import streamlit as st

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    for i in movie_list[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names


st.header('Movie Recommender System')
movies = pickle.load(open(r'C:\Users\VINTEE CHAUHAN\OneDrive\Desktop\GITHUB\VT-Course-Project\movie_list.pkl','rb'))
similarity = pickle.load(open(r'C:\Users\VINTEE CHAUHAN\OneDrive\Desktop\GITHUB\VT-Course-Project\similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)