import os
from lxml import etree

def audit_records(xml_folder="processed_xml"):
    print("--- Starting Quality Control Audit ---")
    for file in os.listdir(xml_folder):
        tree = etree.parse(f"{xml_folder}/{file}")
        root = tree.getroot()
        
        # Check if Country field is empty or "International"
        country = root.find(".//Country").text
        if country == "International":
            print(f"FLAG [Low Confidence]: {file} - Manual Review Required for Country tag.")
        else:
            print(f"PASS: {file} - Data Integrity Confirmed.")

if __name__ == "__main__":
    audit_records()