from src.pdf_reader import PDFReader
from src.chunker import Chunker

reader = PDFReader("articles/sample.pdf")
text = reader.extract_text()

chunker = Chunker(chunk_size=300, overlap=50)
chunks = chunker.chunk(text)

print(f"Total chunks: {len(chunks)}")
print("\nFirst chunk:\n")
print(chunks[0])