from pyxdameraulevenshtein import damerau_levenshtein_distance as dldistance
from tqdm import tqdm_notebook
import numpy as np

def edit_distance(onsets1, onsets2):
    assert onsets1.shape == onsets2.shape
    distance = 0
    for i in range(onsets1.shape[1]):
        c1 = onsets1[:, i].squeeze().tolist()
        c2 = onsets2[:, i].squeeze().tolist()
        distance += dldistance(c1, c2)
    return distance

def get_similarity_matrix(matrices_onsets, matrices_genres, GENRES, matrices_target,  target_genre):
    # threshold to ignore too weak onsets
    THRESHOLD = 0.15

    # store distances
    distances = []
    for _, genre in enumerate(GENRES):
        dist = []
        distances.append(dist)

    # calculate distances with all patterns in all genres
    for i in tqdm_notebook(range(matrices_genres.shape[0])):
        genre1 = matrices_genres[i]
        onsets1 = matrices_onsets[i]
        onsets1[onsets1 < THRESHOLD] = 0 # ignore too weak onsets!

        for _,onsets2 in enumerate(matrices_target):
            onsets2[onsets2 < THRESHOLD] = 0 # ignore weak onsets!
            
            dist = edit_distance(onsets1, onsets2)
            distances[genre1].append(dist)     

    # calculate distances within target patterns
    distances_inter = []
    for i in tqdm_notebook(range(matrices_target.shape[0])):
        onsets1 = matrices_target[i]
        onsets1[onsets1 < THRESHOLD] = 0 # ignore too weak onsets!

        for j,onsets2 in enumerate(matrices_target):
            if i != j:
                onsets2[onsets2 < THRESHOLD] = 0 # ignore weak onsets!
                dist = edit_distance(onsets1, onsets2)
                distances_inter.append(dist)  
                
    # return result
    all_dists = [np.array(l).mean() for l in distances]
    all_dists.append(np.array(distances_inter).mean())

    genre_names = list(GENRES)
    genre_names.append(target_genre)

    return all_dists, genre_names