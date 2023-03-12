#Import libraries
import nltk
from textblob import TextBlob
#Extract noun
blob = TextBlob("John is learning natural language processing")
for np in blob.noun_phrases:
    print(np)
