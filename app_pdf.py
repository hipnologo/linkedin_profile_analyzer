import streamlit as st
import os
import spacy
import en_core_web_sm
from spacy.matcher import Matcher
import PyPDF2

# Set up Streamlit interface
st.set_page_config(page_title='Resume Analyzer', page_icon=':clipboard:', layout='wide')

st.title('Resume Analyzer')

# Get resume file from user
resume_file = st.file_uploader('Upload your resume in PDF format', type='pdf')

if resume_file:
    # Read PDF file and extract text
    pdf_reader = PyPDF2.PdfReader(resume_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):  # range(pdf_reader.getNumPages()):
        page = pdf_reader.pages[page_num] #pdf_reader.getPage(page_num)
        text += page.extract_text()
    
    # Analyze text using Spacy
    nlp = en_core_web_sm.load()
    doc = nlp(text)
    
    # Identify areas for improvement using Spacy Matcher
    matcher = Matcher(nlp.vocab)
    pattern1 = [{'LOWER': 'improve'}, {'POS': 'ADP'}, {'POS': 'NOUN'}]
    pattern2 = [{'LOWER': 'add'}, {'POS': 'NOUN'}, {'POS': 'ADP'}, {'POS': 'NOUN'}]
    matcher.add('Improvement', [pattern1, pattern2])
    matches = matcher(doc)
    
    # Display summary and suggestions
    st.write('**Summary:**')
    st.write(text)
    
    if matches:
        st.write('**Suggestions:**')
        for match_id, start, end in matches:
            suggestion = doc[start:end].text
            st.write(suggestion)
    else:
        st.write('**No suggestions. Your resume looks great!**')
else:
    st.write('Please upload a PDF file of your resume to continue.')

