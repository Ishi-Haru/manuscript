import PyPDF2
import os

pdf_path = r"c:\Users\haruy\Desktop\paper\Nano letters\manuscript\figs\slip_length_summary\paper\AFM Slip Length Measurements for Water at Selected Phyllosilicate Surfaces, .pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(f"Number of pages: {len(reader.pages)}")
    
    # Extract text from all pages
    full_text = ""
    for i in range(len(reader.pages)):
        text = reader.pages[i].extract_text()
        full_text += text + "\n"
    
    # Print full text to analyze
    print(full_text)
