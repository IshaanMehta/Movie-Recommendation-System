from movie_posters import fetch_posters

def get_recommendations(title, cosine_sim, data_new):
    try:
        idx = data_new[data_new['title'] == title].index[0]
    except IndexError:
        return ["Movie not found"], []

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:6]

    movie_indices = [i[0] for i in sim_scores]
    movies_list = [data_new['title'].iloc[i] for i in movie_indices]
    poster_list = [fetch_posters(data_new['id'].iloc[i]) for i in movie_indices]

    return movies_list, poster_list