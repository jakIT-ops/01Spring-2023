Text = "I am learning NLP"

#Import textblob
from textblob import TextBlob

#For unigram : Use n = 1
TextBlob(Text).ngrams(1)

#For Bigram : For bigrams, use n = 2
TextBlob(Text).ngrams(2)
[WordList(['I', 'am']),
WordList(['am', 'learning']),
WordList(['learning', 'NLP'])]

#importing the function
from sklearn.feature_extraction.text import CountVectorizer
# Text
text = ["I love NLP and I will learn NLP in 2month "]
# create the transform
vectorizer = CountVectorizer(ngram_range=(2,2))
# tokenizing
vectorizer.fit(text)
# encode document
vector = vectorizer.transform(text)
# summarize & generating output
print(vectorizer.vocabulary_)
print(vector.toarray())
