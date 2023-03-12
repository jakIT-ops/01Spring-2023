import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Initialize Porter Stemmer
ps = PorterStemmer()

# Sample input text
input_text = "Stemming is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form—generally a written word form."

# текстийг токенчлох
tokens = word_tokenize(input_text)

# stopwords авахгүй.
# the, and, of, in, is = эдгээр үгс нь хэлэнд түгээмэл хэрэглэгддэг боловч бие даан утга агуулаагүй үгс юм.
filtered_words = [word for word in tokens if word.lower() not in stopwords.words('english')]

# Стемминг хийх 
stemmed_words = [ps.stem(word) for word in filtered_words]

print("Оролтын текст: \n", input_text)
print("\nstopwors хийсэн текст: \n", filtered_words)
print("\nСтемминг текст: \n", stemmed_words)

"""
Stemming гэдэг нь урвуу буюу үүсмэл үгсийг үндсэн болон язгуур хэлбэрт нь оруулах үйл явц юм. Жишээлбэл, "running" ба "ran" гэсэн үгсийн төгсгөлд хоёулаа "run" үндсэн хэлбэр гарч ирнэ. Шинжилгээнд зориулж текстийг хялбарчлахын тулд stemming нь ихэвчлэн (NLP) -д ашиглагддаг.

Stemming алгоритмууд нь үгийн утгыг өөрчилдөг дагаваруудыг арилгах замаар ажилладаг. Жишээ нь, "talks" гэдэг үгийг "-s" дагаварыг хасснаар "talk" гэсэн үгийн үндэс болно. Үүний нэгэн адил "jumping" гэдэг үг нь "-ing" гэсэн дагаварыг хассанаар "jump" гэсэн үндэстэй болно.

NLP-д Porter stemming алгоритм, Snowball stemming алгоритм зэрэг олон янзын алгоритм, арга техникийг ашигладаг.

Stemming нь үргэлж төгс байдаггүй, заримдаа буруу stemming үүсгэдэг. Гэсэн хэдий ч энэ нь боловсруулалт, дүн шинжилгээ хийх шаардлагатай өвөрмөц үгсийн тоог багасгахад тусалдаг тул text classification, information retrieval, neural network, зэрэг олон NLP програмуудад ашиглагддаг
"""
