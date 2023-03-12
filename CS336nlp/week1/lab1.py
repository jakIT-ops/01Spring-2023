import PyPDF2

# lab 1 pdf унших
# ном дээрх код нь сангийн version тэй зөрөөд байсан учир өөрчилөв.
with open("/home/jakit/01Spring-2023/CS336nlp/week1/1intro.pdf", "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)

    num_pages = len(pdf_reader.pages)

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        print(text)
