class PDFParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        import fitz  # PyMuPDF
        document = fitz.open(self.file_path)
        text = ""
        for page in document:
            text += page.get_text()
        document.close()
        return text

    def chunk_text(self, text, chunk_size=1000, overlap=100):
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start += chunk_size - overlap
        return chunks

    def parse(self):
        text = self.extract_text()
        return self.chunk_text(text)