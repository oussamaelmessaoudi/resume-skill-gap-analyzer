from pdfminer.high_level import extract_text
import os
import spacy
import docx2txt

text_from_pdf = extract_text("../assets/Resume.pdf")
nlp = spacy.load("en_core_web_sm")
doc = nlp(text_from_pdf)

for token in doc:
    print(token.text,token.pos_)