# GlobalDocs AI: International Information Management System

**Architect:** Mohammed Afwan M A  
**Role:** Senior Information Architect (Portfolio Project)

## 📌 Project Overview
GlobalDocs AI is a production-grade ecosystem designed to solve the "Dark Data" problem in international organizations. It transforms unstructured regulatory PDFs into structured, machine-readable XML archives and provides an AI-powered semantic search interface.

## 🛠️ The Technical Pipeline
1. **Data Mining (NLP):** Uses `spaCy` to extract Geopolitical Entities (Countries) and metadata from raw PDFs.
2. **Long-Term Preservation (XML):** Converts extracted data into **Akoma Ntoso-style XML** to ensure platform-agnostic readability for 50+ years.
3. **Quality Governance:** A automated QC Auditor script that flags low-confidence metadata for human review.
4. **Semantic Discovery:** Uses **Sentence-Transformers** and **FAISS** to enable searching by *meaning* rather than just keywords.

## 🚀 Key Skills Demonstrated
* **Information Architecture:** Designing schemas for long-term data survival.
* **Natural Language Processing:** Entity extraction and vector embeddings.
* **Business Analysis:** Creation of BRDs, UAT plans, and stakeholder training modules.
* **Python Engineering:** Building a modular ETL (Extract, Transform, Load) pipeline.

## 📂 Project Structure
- `/raw_documents`: Source PDFs (WTO Trade Reviews).
- `/processed_xml`: Structured XML repository.
- `miner.py`: The extraction engine.
- `xml_converter.py`: The preservation script.
- `semantic_engine.py`: The AI search brain.
- `Project_Documentation.pdf`: The Business & Strategic alignment docs.