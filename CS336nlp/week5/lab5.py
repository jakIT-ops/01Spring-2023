
def generate_ngrams(text, n):
    words = text.split()
    ngrams = []
    
    for i in range(len(words) - n + 1):
        ngram = " ".join(words[i:i+n])
        ngrams.append(ngram)
    
    return ngrams

text = "The quick brown fox jumps over the lazy dog."
print("text: ", text)
print("Trigrams: ", generate_ngrams(text, 3))
print("Biggrams: ", generate_ngrams(text, 2))
print("Unigrams: ", generate_ngrams(text, 1))

"""
NLP-д N-грам нь тухайн текстийн N залгаа дараалал бөгөөд ихэвчлэн үг боловч тэмдэгт байж болно.
N-1 үгсийг өгсөн өгүүлбэрийн дараагийн үгийг таамаглдаг. Энэ тохиолдолд N-граммыг хэлний загварыг сургах функц болгон ашигладаг бөгөөд загвар нь дараагийн хамгийн их магадлалтай үгийг таамаглахад N-грам бүрийн давтамжийг ашигладаг.
"""



