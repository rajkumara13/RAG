import os
from pypdf import PdfReader 

def read_pdf(file_path):  
     if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
     reader=PdfReader(file_path)
     pages=[page.extract_text() for page in reader.pages]
     return pages  
   
"""
pdf_path="D:\clg project\RAG\pdf\Rajkumar1 Ai.pdf"  
read_pdf(pdf_path)
print(read_pdf(pdf_path))
"""