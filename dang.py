import os
import re
from docx import Document

folder_path = r"D:\PHC  things\Talha & Osama Clinic"
pattern = r"\[(.*?)\]"

results = []

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".docx"):
        file_path = os.path.join(folder_path, filename)

        try:
            doc = Document(file_path)
            for para in doc.paragraphs:
                matches = re.findall(pattern, para.text)
                results.extend(matches)

        except Exception as e:
            print(f"Error reading {filename}: {e}")

# print results
for r in results:
    print(r)

with open("extracted_brackets.txt", "w", encoding="utf-8") as out:
    for r in results:
        out.write(r + "\n")
