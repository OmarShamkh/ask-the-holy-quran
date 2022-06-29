from flask import jsonify, make_response
from flask_restful import Resource
from gensim.models import KeyedVectors, Word2Vec
from .preprocess import get_quran_clean_text
from .maximizing_methods import *
from .pooling import *

model_ksucca = KeyedVectors.load("./references/model.pkl")
# model_tw = Word2Vec.load('./references/full_grams_cbow_100_twitter.mdl')
# model_wiki = Word2Vec.load('./references/full_grams_cbow_300_wiki.mdl')

quran_clean_text = get_quran_clean_text()

class MostSimilarWord(Resource):

    def get(self, word):
        '''Outputs the 10 most similar words [from the Holy Quran],
        besides their relative similarity scores for the given word.'''

        word_scores = []
        for verse in quran_clean_text:
            for word in verse.split():
                score = model_ksucca.similarity(word, verse)
                word_scores.append((score, word))

        word_scores.sort(reverse=True)

        # TODO: check max length of verses_scores

        out, idx = [], 0
        for score, term in word_scores:
            if idx == 10:
                break

            out.append((term, score))
            idx += 1

        return make_response(jsonify({'results': out}), 200)


class MostSimilarVerse(Resource):

    def get(self, query):
        '''Outputs the 10 most similar words from the Holy Quran,
        besides their relative frequency scores for the given query.'''

        out = get_pooling_results(query.split(), model_ksucca, get_avg_pooling_vec)

        return make_response(jsonify({'results': out}), 200)
