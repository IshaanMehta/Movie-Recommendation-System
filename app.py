import streamlit as st
import os
from data_processing import load_data, load_cosine_sim
from recommender import get_recommendations

@st.cache_data
def memoized_load_data(file_path):
    return load_data(file_path)

@st.cache_resource
def memoized_load_cosine_sim(file_path_model):
    return load_cosine_sim(file_path_model)

def main():
    # loading data
    package_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(package_dir, 'movies.csv')

    data = memoized_load_data(file_path)

    # loading similarity matrix
    package_dir_sim = os.path.dirname(os.path.abspath(__file__))
    file_path_sim = os.path.join(package_dir_sim, 'cosine_sim.pkl')

    cosin_sim = memoized_load_cosine_sim(file_path_sim)

    st.header('Movie Recommendation System')

    movies_list = [''] + list(data['title'].values)
    movie = st.selectbox('Enter Movie Title:', movies_list)

    if st.button('Get Recommendations'):
        if movie:
            recommendations, posters = get_recommendations(movie, cosin_sim, data)
            cols = st.columns(5)  

            for col, recommend, poster in zip(cols, recommendations, posters):
                with col:
                    st.write(recommend)
                    if poster:
                        st.image(poster, use_column_width=True)
                    else:
                        st.write("Poster not available")
        else:
            st.warning('Please select a movie.')

if __name__ == "__main__":
    main()