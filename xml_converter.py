from lxml import etree
import datetime
import os
from miner import mine_document # This connects your miner to the converter

def create_xml_record(mined_data, output_folder="processed_xml"):
    # 1. Create the Root Element
    root = etree.Element("GlobalDoc", version="1.0")
    
    # 2. Add Metadata Header
    metadata = etree.SubElement(root, "Metadata")
    etree.SubElement(metadata, "DocID").text = f"GD-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    etree.SubElement(metadata, "Country").text = mined_data['country']
    etree.SubElement(metadata, "Date").text = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 3. Add the Body Content
    body = etree.SubElement(root, "Body")
    body.text = mined_data['content'][:10000] # Saving first 10k chars
    
    # 4. Save the File
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    file_name = mined_data['title'].replace(".pdf", ".xml")
    tree = etree.ElementTree(root)
    tree.write(f"{output_folder}/{file_name}", pretty_print=True, xml_declaration=True, encoding="UTF-8")
    print(f"Archived to XML: {file_name}")

if __name__ == "__main__":
    folder_path = "raw_documents"
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            path = os.path.join(folder_path, filename)
            data = mine_document(path)
            create_xml_record(data)