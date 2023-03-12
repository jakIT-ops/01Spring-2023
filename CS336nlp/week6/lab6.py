import numpy as np
import nltk
from nltk import bigrams
import itertools
import pandas as pd

def co_occurrence_matrix(corpus):
    vocab = set(corpus)
    vocab = list(vocab)
    vocab_to_index = {word: i for i, word in enumerate(vocab)}
    # Create bigrams from all words in corpus
    bi_grams = list(bigrams(corpus))
    # Frequency distribution of bigrams ((word1, word2), num_occurrences)
    bigram_freq = nltk.FreqDist(bi_grams).most_common(len(bi_grams))
    # Initialise co-occurrence matrix
    # co_occurrence_matrix[current][previous]
    co_occurrence_matrix = np.zeros((len(vocab), len(vocab)))
    # Loop through the bigrams taking the current and previous word,
    # and the number of occurrences of the bigram.
    for bigram in bigram_freq:
        current = bigram[0][1]
        previous = bigram[0][0]
        count = bigram[1]
        pos_current = vocab_to_index[current]
        pos_previous = vocab_to_index[previous]
        co_occurrence_matrix[pos_current][pos_previous] = count
    co_occurrence_matrix = np.matrix(co_occurrence_matrix)
    # return the matrix and the index
    return co_occurrence_matrix, vocab_to_index

sentences = [['I', 'love', 'nlp'],
             ['I', 'love', 'to', 'learn'],
             ['nlp', 'is', 'future'],
             ['nlp', 'is', 'cool']]

merged = list(itertools.chain.from_iterable(sentences))
matrix = co_occurrence_matrix(merged)

CoMatrixFinal = pd.DataFrame(matrix[0], index=matrix[1], columns=matrix[1])
print(CoMatrixFinal)

"""
Дээрх код нь корпусыг (өгүүлбэрийн жагсаалт) оролт болгон авч, корпус дахь бүх үгсээс биграмм үүсгэж, биграммын давтамжийн тархалтыг тооцож, нүд бүр (i, j) i үгийн контекст цонхонд j үг хэдэн удаа гарч ирэхийг заана. Функц нь корпус дахь үг бүрийг матриц дахь харгалзах индекст нь буулгах матрицыг буцаана.

DataFrame-ийн мөр, баганын шошго нь корпус доторх үгс бөгөөд нүд тус бүрийн оруулгууд нь корпусын контекст цонхонд харгалзах мөр, баганын үгийн хамт тохиолдох тоог илэрхийлнэ.
"""

"""
NLP-д co_occurance_matrix бий болгох нь корпус дахь үг бүр корпус дахь бусад үг бүрийн тогтмол контекст цонхонд гарч ирэх тоог тоолох явдал юм. Контекст цонхыг зорилтот үгийн зүүн эсвэл баруун талд байгаа тогтмол тооны үг гэж тодорхойлж болно. Үүссэн матриц нь үг тус бүрийн корпус дахь бусад үгтэй хамт тохиолдох давтамжийг харуулдаг бөгөөд үгсийн хоорондын ижил төстэй байдал эсвэл хамаарлын хэмжүүр болгон ашиглаж болно"""





















































