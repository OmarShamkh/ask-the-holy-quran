from .preprocess import clean_word, get_quran_clean_text
from pyarabic.araby import tokenize
import numpy as np

quran_clean_text = get_quran_clean_text()
vec_size = 300

def get_max_pooling_vec(query_text, model):
    '''
    Get the max pooling vector for the given tokens.

    @param query_text: list of words
    @type query_text: list
    @param model: the model to use
    @type model: Word2Vec or KeyedVectors
    @return: max pooling vector
    @rtype: numpy array
    '''

    # Warning: checkout the shape of the vectors
    arr = [-1e9 for idx in range(vec_size)]
    # Avoid read-only error
    max_pooling_vec = np.copy(np.array(arr))
    
    for query_word in query_text:
        if query_word not in model:
            continue
        model_vec = model[query_word]
        for index in range(vec_size):
            max_pooling_vec[index] = max(
                max_pooling_vec[index], model_vec[index])

    return max_pooling_vec


def get_avg_pooling_vec(query_text, model):

    # Warning: checkout the shape of the vectors
    arr = [0 for idx in range(vec_size)]
    # Avoid read-only error
    avg_pooling_vec = np.copy(np.array(arr))
    
    words_cnt = 0
    for query_word in query_text:
        if query_word not in model:
            continue
            
        words_cnt += 1
        model_vec = model[query_word]
        for index in range(vec_size):
            avg_pooling_vec[index] += model_vec[index]

<<<<<<< HEAD
    for index in range(100):
        avg_pooling_vec[index] /= max(1, words_cnt) # Avoid zero division
=======
    for index in range(vec_size):
        avg_pooling_vec[index] /= len(query_text)
>>>>>>> 4fdd1ca (update code)

    return avg_pooling_vec


def get_pooling_results(query_text, model, method):
    
    query_text = tokenize(clean_word(query_text))
    query_method_pooling_vec = method(query_text, model)

    verse_scores, verse_id = [], 0
    for verse in quran_clean_text:
        verse_method_pooling_vec = method(verse, model)
        cosine_similarity = np.dot(query_method_pooling_vec, verse_method_pooling_vec) / (
            np.linalg.norm(query_method_pooling_vec) * np.linalg.norm(verse_method_pooling_vec))

        # score = model_vectors.similarity(query_max_pooling_vec, verse_max_pooling_vec)
        # will fail, because we generated new vectors that doesn't belong to any model

        verse_scores.append((cosine_similarity, verse_id))
        verse_id += 1

    verse_scores.sort(reverse=True)

    # Return at most 50 verses
    max_out_length = min(len(verse_scores), 50)
    most_similar_verses = [(score, verse_id, quran_clean_text[verse_id])
                           for score, verse_id in verse_scores[:max_out_length]]

    return most_similar_verses
