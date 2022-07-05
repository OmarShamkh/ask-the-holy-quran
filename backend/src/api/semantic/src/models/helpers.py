# from pyarabic.araby import tokenize

# stopwords = []
# def get_stopwords():
#   # prepare/read stopwords
#   stopwords = open("./data/external/stopwords_list.txt").readlines()

#   # remove /n from each stopword
#   stopwords = [word[:-1] for word in stopwords]
  
#   # convert list to set, to enhance searching
#   stopwords = set(stopwords)
#   return stopwords


# def get_meaningful_words_length(text):
#   tokens = tokenize(text)

#   cnt = 0
#   for term in tokens:
#     if term not in stopwords:
#       cnt += 1
      
#   return cnt
