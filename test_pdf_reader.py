from src.pdf_reader import PDFReader

reader = PDFReader("articles/sample.pdf")
text = reader.extract_text()

print(text[:1000])