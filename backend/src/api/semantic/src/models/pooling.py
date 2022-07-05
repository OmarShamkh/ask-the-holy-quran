from .preprocess import clean_word, get_quran_clean_text
import numpy as np

quran_clean_text = get_quran_clean_text()


def get_max_pooling_vec(tokens, model_vectors):
    arr = [-1e9 for idx in range(100)]
    max_pooling_vec = np.copy(np.array(arr))  # avoid read-only error

    for token in tokens:
        if clean_word(token) not in model_vectors:
            # print(clean_word(token))
            continue

        vec = model_vectors[clean_word(token)]
        for idx in range(100):
            max_pooling_vec[idx] = max(max_pooling_vec[idx], vec[idx])

    return max_pooling_vec


def get_avg_pooling_vec(tokens, model_vectors):
    arr = [0 for idx in range(100)]
    avg_pooling_vec = np.copy(np.array(arr))  # avoid read-only error

    for token in tokens:
        if clean_word(token) not in model_vectors:
            continue

        vec = model_vectors[clean_word(token)]
        for idx in range(100):
            avg_pooling_vec[idx] += vec[idx]

    for idx in range(100):
        avg_pooling_vec[idx] /= len(tokens)

    return avg_pooling_vec


def get_pooling_results(query_tokens, model_vectors, method):
    query_method_pooling_vec = method(query_tokens, model_vectors)

    verse_scores, index = [], 0
    for verse in quran_clean_text:
        verse_method_pooling_vec = method(verse.split(), model_vectors)
        cosine_similarity = np.dot(query_method_pooling_vec, verse_method_pooling_vec) / (
            np.linalg.norm(query_method_pooling_vec) * np.linalg.norm(verse_method_pooling_vec))

        # score = model_vectors.similarity(query_max_pooling_vec, verse_max_pooling_vec)
        # will fail, because we generated new vectors that doesn't belong to any model

        verse_scores.append((cosine_similarity, index))
        index += 1

    verse_scores.sort(reverse=True)

    # TODO: check max length of verses_scores
    most_similar_verses = [(score, quran_clean_text[index])
                           for score, index in verse_scores[:10]]

    return most_similar_verses
