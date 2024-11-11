##data extraction
import fitz  # PyMuPDF

class PDFExtractor:
    def __init__(self, pdf_path):
        """Initializes the PDFExtractor with the path to the PDF file."""
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)

    def extract_text(self):
        """Extracts all text from the PDF and returns it as a single string."""
        full_text = ""
        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            full_text += page.get_text("text") + "\n"  # Append text of each page
        return full_text

    def close(self):
        """Closes the document to free up resources."""
        self.doc.close()

# # Usage example
# pdf_path = "/content/drive/MyDrive/SJS Transcript Call.pdf"  # Replace with your PDF file path
# pdf_extractor = PDFExtractor(pdf_path)
# pdf_text = pdf_extractor.extract_text()
# pdf_extractor.close()
# print(pdf_text)
