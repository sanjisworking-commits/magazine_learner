class Chunker:
    def __init__(self, chunk_size=500, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text):
        words = text.split()
        chunks = []

        step = self.chunk_size - self.overlap

        for start in range(0, len(words), step):
            end = start + self.chunk_size
            chunk_words = words[start:end]
            chunk_text = " ".join(chunk_words)

            chunks.append(chunk_text)

        return chunks