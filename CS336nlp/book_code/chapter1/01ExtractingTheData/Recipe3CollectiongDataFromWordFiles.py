from docx import Document

# Creating a word file objectdoc
doc = open("./files/doc.docx", "rb")
document = docx.Document(doc)
docu=""
for para in document.paragraphs:
       docu += para.text
#to see the output call docu
print(docu)
