import fitz # PyMuPDF
import spacy
import os

nlp = spacy.load("en_core_web_sm")

def mine_document(pdf_path):
    doc = fitz.open(pdf_path)
    text = " ".join([page.get_text() for page in doc])
    
    # NLP Data Mining for Entities
    spacy_doc = nlp(text[:2000]) # Scan first 2000 chars for metadata
    countries = [ent.text for ent in spacy_doc.ents if ent.label_ == "GPE"]
    
    return {
        "title": os.path.basename(pdf_path),
        "country": countries[0] if countries else "International",
        "content": text
    }

# Execute
# print(mine_document("path/to/your/trade_doc.pdf"))
# --- ADD THIS TO THE BOTTOM OF miner.py ---

if __name__ == "__main__":
    # Path to your documents folder
    folder_path = "raw_documents"
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found!")
    else:
        # Loop through every file in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".pdf"):
                path = os.path.join(folder_path, filename)
                print(f"\n--- Mining Document: {filename} ---")
                
                # Call our mining function
                result = mine_document(path)
                
                # Print the mined metadata
                print(f"Mined Country: {result['country']}")
                print(f"Content Length: {len(result['content'])} characters")