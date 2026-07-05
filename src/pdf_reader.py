
from pypdf import PdfReader

class PDFReader:

    def __init__(self, path):
        self.path = path

    def extract_text(self):

        reader = PdfReader(self.path)

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text
