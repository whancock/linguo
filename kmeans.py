# https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-3-more-fun-with-word-vectors


from sklearn.cluster import KMeans
from gensim.models import Word2Vec


model = Word2Vec.load_word2vec_format('./models/text8.model.bin', binary=True)



def cluster_vec(words, num_clusters=2):

	kmeans_clustering = KMeans( n_clusters = num_clusters )
	idx = kmeans_clustering.fit_predict( model[list(words)] )

	print(words)
	print(idx)




cluster_vec(['horse', 'pig', 'dog', 'cat', 'mouse', 'moose'])