from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from lxml import etree

# 1. Load the "Translator" (The AI model)
model = SentenceTransformer('all-MiniLM-L6-v2')

def build_semantic_index(xml_folder="processed_xml"):
    documents = []
    file_names = []
    
    for file in os.listdir(xml_folder):
        tree = etree.parse(f"{xml_folder}/{file}")
        text = tree.find(".//Body").text
        documents.append(text)
        file_names.append(file)

    # 2. Convert Text to Vectors (Math)
    embeddings = model.encode(documents)
    dimension = embeddings.shape[1]
    
    # 3. Initialize FAISS Index
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    
    return index, file_names

def search_index(query, index, file_names, top_k=1):
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), top_k)
    
    print(f"\nResults for search: '{query}'")
    for i in range(top_k):
        print(f"Top Match: {file_names[indices[0][i]]} (Distance: {distances[0][i]:.4f})")

if __name__ == "__main__":
    idx, files = build_semantic_index()
    search_index("agricultural policy and cereals", idx, files)
    