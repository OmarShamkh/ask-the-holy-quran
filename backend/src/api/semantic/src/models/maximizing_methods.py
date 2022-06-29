from gensim.models import KeyedVectors, Word2Vec
from pyarabic.araby import tokenize
from .helpers import get_stopwords
from .preprocess import clean_word, get_quran_clean_text

model_ksucca = KeyedVectors.load("./references/model.pkl")
# model_tw = Word2Vec.load('./references/full_grams_cbow_100_twitter.mdl')
# model_wiki = Word2Vec.load('./references/full_grams_cbow_300_wiki.mdl')

stopwords = get_stopwords()
quran_clean_text = get_quran_clean_text()

def get_verse_max_score(query_word, verse_text, model):
  # remove .wv while using ksucca (KeyedVectors vs. Word2Vec)
  if model == model_ksucca:
    model_vectors = model
  else:
    model_vectors = model.wv

  maxi = -1
  for verse_word in verse_text.split():
    if query_word not in model_vectors \
      or verse_word not in model_vectors \
        or verse_word in stopwords:
      continue 
    
    maxi = max(model_vectors.similarity(query_word, verse_word), maxi)
  return maxi
  
def get_verse_frequency_score(query_word, verse_text, model):
  '''
  Calculate the frequency score of a verse with a given word
  '''
  if model == model_ksucca:
    model_vectors = model
  else:
    model_vectors = model.wv

  freq = 0
  for verse_word in verse_text.split():
    if query_word not in model_vectors \
      or verse_word not in model_vectors \
        or verse_word in stopwords:
      continue 

    score = model_vectors.similarity(query_word, verse_word)

    if score > 0.3:
      freq += 1
  return freq
  
def get_avg_score(query_word, verse_text, model):
  if model == model_ksucca:
    model_vectors = model
  else:
    model_vectors = model.wv
  
  verse_vector = [0]
  for verse_word in verse_text.split():
    if query_word not in model_vectors \
      or verse_word not in model_vectors \
        or verse_word in stopwords:
      continue 

    score = model_vectors.similarity(query_word, verse_word)
    # ignore negative scores
    if score > 0 :
      verse_vector.append(score)

  avg = sum(verse_vector) / len(verse_vector)
  return avg

def get_most_similar_verses(query_word, model, method, model_number):
	'''
	Get the most similar verses to the query word based on the 3 methods(max_score , freq , avg)
	'''
	if query_word in stopwords:
	  return "من فضلك، أدخل كلامًا ذا معنى"

	verse_scores, index = [], 0
	for verse in quran_clean_text:
	  score = method(clean_word(query_word), verse, model)
	  verse_scores.append((score, index))
	  index += 1
	  
	verse_scores.sort(reverse=True)
	
	# TODO: check max length of verses_scores
	most_similar_verses = [(score, quran_clean_text[index]) for score, index in verse_scores[:10]]
	return most_similar_verses

def get_most_similar_verses_by_query_text(query_text, model, method):
  # better than the split method
  tokens = tokenize(query_text)

  verse2score = {}
  for i in range(len(tokens)):
    if tokens[i] in stopwords:
      continue

    most_similar_verses1 = get_most_similar_verses(clean_word(tokens[i]), model, method)
    for score, verse in most_similar_verses1:
      verse2score[verse] = score
    
    if i + 1 != len(tokens):
      term = tokens[i] + "_" + tokens[i + 1]
      most_similar_verses2 = get_most_similar_verses(clean_word(term), model, method)

      for score, verse in most_similar_verses2:
        verse2score[verse] = score
      
  best_ranked_verses = [(rank, verse) for verse, rank in verse2score.items()]
  best_ranked_verses.sort(reverse=True)

  return best_ranked_verses[:10]
  
def get_combined_models_results(query_text, method):
  verse2score = {}
  for model in [model_wiki, model_tw, model_ksucca]:
    score2verse = get_most_similar_verses_by_query_text(query_text, model, method)

    for score, verse in score2verse:
      if verse in verse2score:
        verse2score[verse] += score
      else:
        verse2score[verse] = score

  summed_score2verse = [(score, verse) for verse, score in verse2score.items()]
  summed_score2verse.sort(reverse=True)

  return summed_score2verse[:10]
  
def get_all_combined(query_text):

  methods = [get_combined_models_results(query_text, get_verse_max_score),
             get_combined_models_results(query_text, get_verse_frequency_score),
             get_combined_models_results(query_text, get_avg_score)]
  
  # to have a constant measurement, scores are defined based on sum of scores
  max_score = [sum([score for score, verse in method]) for method in methods]

  verse2score = {}
  for i in range(3):
    for score, verse in methods[i]:
      final_score = score / max_score[i]
      
      if verse in verse2score:
        verse2score[verse][0] += final_score
        verse2score[verse][1] += 1.0
      else:
        verse2score[verse] = [final_score, 1.0]

  score2verse = []
  for verse, [score, frequency] in verse2score.items():
    score2verse.append((score / frequency, verse))

  score2verse.sort(reverse=True)

  return score2verse[:15]