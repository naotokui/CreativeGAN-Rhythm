from pyxdameraulevenshtein import damerau_levenshtein_distance as dldistance
from tqdm import tqdm_notebook
import numpy as np

# threshold to ignore too weak onsets
THRESHOLD = 0.25

def edit_distance(onsets1, onsets2, threshold = 0.0):
    assert onsets1.shape == onsets2.shape
    
    onsets1 = onsets1.copy()
    onsets2 = onsets2.copy()
    
    onsets1[onsets1 <= threshold] = 0 # ignore too weak onsets!
    onsets1[onsets1 > threshold] = 1 
    onsets1 = onsets1.astype(np.int)
        
    onsets2[onsets2 <= threshold] = 0 # ignore weak onsets!
    onsets2[onsets2 > threshold] = 1
    onsets2 = onsets2.astype(np.int)
    
    distance = 0
    for i in range(onsets1.shape[1]):
        c1 = onsets1[:, i].squeeze().tolist()
        c2 = onsets2[:, i].squeeze().tolist()
        distance += dldistance(c1, c2)

    return distance

def get_similarity_matrix(matrices_onsets, matrices_genres, GENRES, matrices_target = None,  target_genre = None, threshold = THRESHOLD):
    # store distances
    distances = []
    for _, genre in enumerate(GENRES):
        dist = []
        distances.append(dist)

    # calculate distances with all patterns in all genres
    for i in tqdm_notebook(range(matrices_genres.shape[0])):
        genre1 = matrices_genres[i]
        onsets1 = matrices_onsets[i]
        
        for _,onsets2 in enumerate(matrices_target):            
            dist = edit_distance(onsets1, onsets2, threshold )
            distances[genre1].append(dist)     

    # calculate distances within target patterns
    if matrices_target is not None:
        distances_inter = []
        for i in tqdm_notebook(range(matrices_target.shape[0])):
            onsets1 = matrices_target[i]

            for j,onsets2 in enumerate(matrices_target):
                if i != j:
                    dist = edit_distance(onsets1, onsets2, threshold)
                    distances_inter.append(dist)  
                
    # return result
    all_dists = [np.array(l).mean() for l in distances]
    if matrices_target is not None:
        all_dists.append(np.array(distances_inter).mean())

    genre_names = list(GENRES)
    if matrices_target is not None:
        genre_names.append(target_genre)

    return all_dists, genre_names