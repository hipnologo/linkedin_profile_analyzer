import streamlit as st
import os
import spacy
import en_core_web_sm
from spacy.matcher import Matcher
import PyPDF2
import openai

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set up Streamlit interface
st.set_page_config(page_title='Resume Analyzer', page_icon=':clipboard:', layout='wide')

st.title('Resume Analyzer')

# Get resume file from user
resume_file = st.file_uploader('Upload your resume in PDF format', type='pdf')

if resume_file:
    # Read PDF file and extract text
    pdf_reader = PyPDF2.PdfReader(resume_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)): #range(pdf_reader.getNumPages()):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    
    # Generate summary using OpenAI API
    summary = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Please summarize the following text:\n{text}",
        temperature=0.5,
        max_tokens=100
    ).choices[0].text.strip()
    
    # Generate recommendations using OpenAI API
    recommendations = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Please provide recommendations for improvement based on the following text:\n{text}",
        temperature=0.5,
        max_tokens=200
    ).choices[0].text.strip()
    
    # Display summary and recommendations
    st.write('**Summary:**')
    st.write(summary)
    
    st.write('**Recommendations:**')
    st.write(recommendations)
else:
    st.write('Please upload a PDF file of your resume to continue.')

