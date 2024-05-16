import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_cast = []
    recommended_movie_cast2 = []
    for i in distances[1:6]:
        rec = cast.loc[(cast["title"] == movies.iloc[i[0]].title), ['crew']]
        recommended_movie_cast.append(rec)
        recommended_movie_names.append(movies.iloc[i[0]].title)
    for i in range(0, len(recommended_movie_cast)):
        recommended_movie_cast2.append(recommended_movie_cast[i].values[0][0])
    return recommended_movie_names, recommended_movie_cast2


st.title('Movie Recommender System :popcorn:')
st.subheader("", divider='rainbow')
st.image('movieimg.jpeg')
st.subheader("", divider='rainbow')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_cast = pickle.load(open('movie_cast.pkl', 'rb'))
cast = pd.DataFrame(movie_cast)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):

    recommended_movie_names, cast = recommend(selected_movie)
    st.header('You would like these movies :clapper:', divider='rainbow')
    for i in range(0, 4):
        s = ""
        st.subheader(recommended_movie_names[i])
        for j in cast[i]:
            s = s + " " + j + ","
        s = "Movie by - " + s[0:len(s) - 1]
        st.caption(s)
st.subheader("", divider='rainbow')


def recommend(musics):
    music_index = music[music['title'] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_music = []
    recommended_artist = []
    recommended_artist2 = []
    for i in music_list:
        recommended_music.append(music.iloc[i[0]].title)
        rec = record.loc[(record["Song-Name"] == music.iloc[i[0]].title), ['Singer/Artists']]
        recommended_artist.append(rec)
    for i in range(0, len(recommended_artist)):
        recommended_artist2.append(recommended_artist[i].values[0][0])

    return recommended_music, recommended_artist2


music_dict = pickle.load(open('musicrec.pkl', 'rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open('similarities.pkl', 'rb'))
st.title('Music Recommendation System :headphones:')
st.subheader("", divider='rainbow')
st.image('musicimg.jpg')
st.subheader("", divider='rainbow')
music_org = pickle.load(open('musicorg.pkl', 'rb'))
record = pd.DataFrame(music_org)

selected_music_name = st.selectbox('Select a music you like', music['title'].values)

if st.button('Recommend'):
    names, artist = recommend(selected_music_name)
    st.header('You would like these songs :musical_note:', divider='rainbow')
    for i in range(0, 4):
        st.subheader(names[i])
        st.caption("Song by - " + artist[i])
st.subheader("", divider='rainbow')
