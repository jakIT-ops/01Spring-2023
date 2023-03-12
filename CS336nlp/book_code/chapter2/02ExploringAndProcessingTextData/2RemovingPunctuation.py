text=['This is introduction to NLP','It is likely to be useful, to people ','Machine learning is the new electrcity', 'There would be less hype aroun AI and more action going forward','python is the best tool!','R is good langauage', 'I like this book','I want more books like this']
#convert list to dataframe

import pandas as pd
import string
df = pd.DataFrame({'tweet':text})
print(df)

import re
s = "I. like. This book!"
s1 = re.sub(r'[^\w\s]',",s)
s1


s = "I. like. This book!"
for c in string.punctuation:
      s= s.replace(c,"")
s
