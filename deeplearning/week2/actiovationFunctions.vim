Хиймэл мэдрэлийн сүлжээнд нейрон бүрийн гаралтад шугаман бус байдлыг нэвтрүүлэхийн тулд идэвхжүүлэх функцийг ашигладаг. 
Мэдрэлийн сүлжээнд түгээмэл хэрэглэгддэг идэвхжүүлэх функцууд энд байна. 

* `Сигмоид:` Сигмоид идэвхжүүлэх функц нь аливаа оролтыг 0 ба 1-ийн мужид буулгадаг бөгөөд үүнийг магадлал гэж тайлбарлаж болно. 

* `ReLU (Rectified Linear Unit):` ReLU идэвхжүүлэх функц нь сөрөг утгыг тэгээр сольж, нийлэлтийг хурдасгадаг. 

* `Tanh (Hyperbolic Tangent):` tanh идэвхжүүлэх функц нь ямар ч оролтыг -1 ба 1-ийн мужид буулгадаг. 

* `Leaky ReLU:` ReLU идэвхжүүлэх функцийн сайжруулсан хувилбар нь сөрөг утгуудын хувьд бага зэрэг градиент хийх боломжийг олгодог. 

* `Softmax:` Softmax идэвхжүүлэх функц нь оролтын багцыг K боломжит гаралт дээр магадлалын хуваарилалтад буулгадаг. 

* `ELU (Exponential Linear Unit):` ELU идэвхжүүлэх функц нь сөрөг утгыг оролтын шугаман функцээр сольдог бөгөөд энэ нь алга болох градиент асуудлыг багасгахад тусалдаг. 

Идэвхжүүлэх функцийг сонгох нь таны шийдэх гэж буй асуудлын төрөл болон мэдрэлийн сүлжээний архитектураас хамаарна гэдгийг анхаарах нь чухал юм.

### Output types

| Output Type | Output Distribution | Output Layer | Cost Function |
| :---------- | ------------------- | ------------ | ------------: |
| Binary | Bernoulli | Sigmoid | Binary cross-entropy |
| Discrets | Multinoulli | softmax | Discrete cross-entropy |
| Continuous | Gaussion | Linear | Gaussion cross-entropy |
| Continuous | Mixture of Gaussion | Mixture Density | Cross-entropy | 
| Continuous | Arbitrary | See part Gan VAE, FVBN | Various |

### Activation functions nn linear or non-linear 

1. Linear Activation functions: Шугаман идэвхжүүлэлтийн функцууд нь оролттой пропорциональ гаралтыг үүсгэдэг идэвхжүүлэх функцууд юм. Шугаман идэвхжүүлэлтийн функцуудын жишээнд таних функц ба шугаман Шулуутгагч функц орно. Шугаман идэвхжүүлэлтийн функцууд нь хэрэгжүүлэхэд хялбар бөгөөд тооцооллын хувьд үр ашигтай боловч оролт ба гаралтын хооронд шугаман бус хамаарал байдаг нарийн төвөгтэй асуудлуудад тохиромжгүй байж болно.

2. Non-linear Activation functions: Шугаман бус идэвхжүүлэх функцууд нь оролттой пропорциональ бус гаралт үүсгэдэг идэвхжүүлэх функцууд юм. Шугаман бус идэвхжүүлэх функцуудын жишээнд sigmoid, tanh, ReLU, softmax орно. Шугаман бус идэвхжүүлэлтийн функцууд нь шугаман бус байдлыг сүлжээнд нэвтрүүлж, оролт ба гаралтын хоорондох нарийн төвөгтэй харилцааг загварчлах боломжийг олгодог учраас чухал юм.

Ерөнхийдөө шугаман бус идэвхжүүлэлтийн функцийг шугаман идэвхжүүлэлтийн функцээс илүүд үздэг, учир нь тэдгээр нь мэдрэлийн сүлжээнд нарийн төвөгтэй харилцааг загварчлах, өгөгдөл дэх шугаман бус хэв маягийг авах боломжийг олгодог. Үүний үр дүнд олон төрлийн хэрэглээнд илүү сайн гүйцэтгэл, нарийвчлал сайжирна.

