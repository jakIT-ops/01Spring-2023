sentences = [['I', 'love', 'nlp'],
                  ['I', 'will', 'learn', 'nlp', 'in', '2','months'],
                  ['nlp', 'is', 'future'],
                  [␇'nlp', 'saves', 'time', 'and', 'solves',
'lot', 'of', 'industry', 'problems'],
                  ['nlp', 'uses', 'machine', 'learning']]

import gensim
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

# training the model
skipgram = Word2Vec(sentences, size =50, window = 3, min_count=1,
sg = 1)
print(skipgram)
# access vector for one word
print(skipgram['nlp'])
print(skipgram['deep'])

# save model
skipgram.save('skipgram.bin')
# load model
skipgram = Word2Vec.load('skipgram.bin')

X = skipgram[skipgram.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(skipgram.wv.vocab)
for i, word in enumerate(words):
       pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()

#import library
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
#Example sentences
sentences = [['I', 'love', 'nlp'],
                   ['I', 'will', 'learn', 'nlp', 'in', '2','months'],
                   ['nlp', 'is', 'future'],
                   [␇'nlp', 'saves', 'time', 'and', 'solves','lot', 'of', 'industry', 'problems'],
                   ['nlp', 'uses', 'machine', 'learning']]

# training the model
cbow = Word2Vec(sentences, size =50, window = 3, min_count=1,sg = 1)
print(cbow)

# access vector for one word
print(cbow['nlp'])
# save model
cbow.save('cbow.bin')
# load model
cbow = Word2Vec.load('cbow.bin')
# T – SNE plot
X = cbow[cbow.wv.vocab]
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(cbow.wv.vocab)
for i, word in enumerate(words):
       pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()




