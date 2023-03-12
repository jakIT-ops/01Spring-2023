text=['Introduction to NLP','It is likely to be useful, to people ','Machine learning is the new electrcity', 'R is good langauage','I like this book','I want more books like this']
#convert list to dataframe
import pandas as pd
df = pd.DataFrame({'tweet':text})
print(df)

df['tweet'].apply(lambda x: str(TextBlob(x).correct()))

from textblob import TextBlob
df['tweet'].apply(lambda x: str(TextBlob(x).correct()))

print(spell(u'mussage'))
print(spell(u'sirvice'))
