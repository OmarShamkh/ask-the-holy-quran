from gensim.models import KeyedVectors, Word2Vec

# Download ksucca_full_cbow vectors: https://drive.google.com/u/0/uc?id=1rZiOKy71Z_WycxnOG9bwrNoAc4ziGo_n
# or download aravec: https://archive.org/download/full_grams_cbow_300_twitter
# Then, load the vectors directly from the file.

# NOTE: You can use only 1m out of vectors loaded to speed up the model performance
model = KeyedVectors.load_word2vec_format('./data/processed/ksucca_full_cbow.bin', binary=True)


# Pickle the model
model.save("./references/model.pkl")
