from nltk.stem import PorterStemmer
import pandas as pd

text=['I like fishing','I eat fish','There are many fishes in pound']
df = pd.DataFrame({'tweet':text})
# print(df)

# Үг хэллэгийг үндсэн буюу язгуур хэлбэрт нь
# буулгах үйл явц юм. Байгалийн хэлний боловсруулалтад stemming нь ихэвчлэн текст ангилах, мэдээлэл хайх, текст олборлох зэрэг ажлуудад туслах текст өгөгдлийг урьдчилан боловсруулахад ашиглагддаг.

st = PorterStemmer()
df['tweet'][:5].apply(lambda x: " ".join([st.stem(word) for
word in x.split()]))

print(df)