import PyPDF2
import os
import sys

# Set output encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = r"c:\Users\haruy\Desktop\paper\Nano letters\manuscript\figs\slip_length_summary\paper"

pdfs = [
    "Vinogradova and Yakubov 2003 - Dynamic Effects on Force Measurements. 2. Lubrication and the Atomic Force Microscope.pdf",
    "Bonaccurso et al. 2002 - Hydrodynamic force measurements - boundary slip of water on hydrophilic surfaces and electrokinetic effects.pdf"
]

for pdf_file in pdfs:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    if os.path.exists(pdf_path):
        print(f"\n{'='*80}")
        print(f"File: {pdf_file}")
        print(f"{'='*80}")
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                print(f"Number of pages: {len(reader.pages)}")
                
                # Extract text from all pages
                full_text = ""
                for i in range(len(reader.pages)):
                    try:
                        text = reader.pages[i].extract_text()
                        full_text += text + "\n"
                    except Exception as e:
                        print(f"  Error extracting page {i+1}: {e}")
                
                # Print full text to analyze
                print(full_text)
        except Exception as e:
            print(f"Error reading PDF: {e}")
    else:
        print(f"File not found: {pdf_path}")
