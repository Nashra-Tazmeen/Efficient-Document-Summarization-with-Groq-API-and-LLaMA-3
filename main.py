# main.py

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

from Data_extraction import PDFExtractor
from text_chunker import TextChunker
from summarizer import TextSummarizer
from batches import TokenBatcher

def main():
    # Initialize paths and configurations
    API_KEY= os.getenv("API_KEY")
    pdf_path = "SJS Transcript Call.pdf"  # Replace with the actual PDF file path
     # Replace with your Groq API key
    
    

    # Step 1: Extract text from the PDF
    pdf_extractor = PDFExtractor(pdf_path)
    pdf_text = pdf_extractor.extract_text()
    pdf_extractor.close()
    print("Text extracted from PDF.")

    # Step 2: Split text into chunks
    text_chunker = TextChunker(max_words=300)
    text_chunks = text_chunker.split_text_into_chunks(pdf_text)
    print("Text split into chunks.")

    #step3
    token_batcher = TokenBatcher(token_limit=4000)
    batches = token_batcher.create_batches(text_chunks)
    print(f"Created {len(batches)} batches based on token limits.")

    # Step 4: Clean and summarize each batch using Groq API
    text_summarizer = TextSummarizer(API_KEY)
    final_text=""

    for i, batch in enumerate(batches):
    # print(f"Processing Chunk {i+1}...")
        combined_text = "\n".join(batch)
        # print(f"Processing Batch {i + 1}...")
        cleaned_chunk = text_summarizer.clean_text(combined_text)
        if cleaned_chunk :
            final_text += cleaned_chunk + "\n\n"  
        


    final_summary = text_summarizer.clean_text(final_text)


    print("Final Summary:", final_summary)

            
            

if __name__ == "__main__":
    main()
