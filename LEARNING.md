# Day 1

## What I learned

- A class has one responsibility.
- PDFReader should only read PDFs.
- It should return a string.
- Another class should handle chunking.
- Git feature branches let me build features independently and merge them into main safely.

## Questions
- Why do we need overlap between chunks?
- How do embeddings actually work mathematically?git

Why doesn't Chunker accept a PDF file?
- Becasue its job is to split the pdf into chunks not read it

Why do we use split()?
to convert str into list(stry)

Why do we use overlap?
to maintain coneection between two chunks

Why do we return a list instead of one string?
the list is that of diff chunks which makes embedding faster