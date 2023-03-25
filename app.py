import streamlit as st
import os
from linkedin_api import Linkedin
import spacy
import en_core_web_sm
from spacy.matcher import Matcher
import PyPDF2
import openai

# Set up Streamlit interface
st.set_page_config(page_title='Profile and Resume Analyzer', page_icon=':clipboard:', layout='wide')

st.title('Profile and Resume Analyzer')

# Authenticate with LinkedIn API
def authenticate_linkedin(client_id, client_secret):
    if client_id and client_secret:
        try:
            api = Linkedin(client_id, client_secret)
            return api
        except:
            st.sidebar.error('Failed to authenticate with LinkedIn API using client ID and client secret. Please check your credentials.')
    else:
        st.sidebar.error('Please set the LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET environment variables.')
        st.sidebar.text_input('Enter your LinkedIn client ID', value=client_id)
        st.sidebar.text_input('Enter your LinkedIn client secret', value=client_secret)

# Extract text from LinkedIn PDF profile
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ''
    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    return text

# Analyze text using Spacy
def analyze_text(text):
    nlp = en_core_web_sm.load()
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    pattern1 = [{'LOWER': 'improve'}, {'POS': 'ADP'}, {'POS': 'NOUN'}]
    pattern2 = [{'LOWER': 'add'}, {'POS': 'NOUN'}, {'POS': 'ADP'}, {'POS': 'NOUN'}]
    matcher.add('Improvement', [pattern1, pattern2])
    matches = matcher(doc)
    suggestions = []
    if matches:
        for match_id, start, end in matches:
            suggestion = doc[start:end].text
            suggestions.append(suggestion)
    return doc, suggestions

# Generate summary and recommendations using OpenAI
def generate_summary_and_recommendations(text):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    summary = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Please summarize the following text:\n{text}",
        temperature=0.5,
        max_tokens=100
    ).choices[0].text.strip()
    recommendations = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Please provide recommendations for improvement based on the following text:\n{text}",
        temperature=0.5,
        max_tokens=200
    ).choices[0].text.strip()
    return summary, recommendations

# Get LinkedIn API authentication from environment variables
client_id = os.getenv('LINKEDIN_CLIENT_ID')
client_secret = os.getenv('LINKEDIN_CLIENT_SECRET')

# Authenticate with LinkedIn API
api = authenticate_linkedin(client_id, client_secret)

# Get profile URL from user
st.sidebar.title('Profile URL')
profile_url = st.sidebar.text_input('Enter your LinkedIn profile URL')

if profile_url:
    # Extract profile data using LinkedIn API
    profile = api.get_profile(profile_url=profile_url)
    
    # Analyze profile using Spacy
    doc_profile, suggestions_profile = analyze_text(profile['summary'])
    
    # Analyze profile using Spacy
    nlp = en_core_web_sm.load()
    doc = nlp(profile['summary'])
    
    # Identify areas for improvement using Spacy Matcher
    matcher = Matcher(nlp.vocab)
    pattern1 = [{'LOWER': 'improve'}, {'POS': 'ADP'}, {'POS': 'NOUN'}]
    pattern2 = [{'LOWER': 'add'}, {'POS': 'NOUN'}, {'POS': 'ADP'}, {'POS': 'NOUN'}]
    matcher.add('Improvement', [pattern1, pattern2])
    matches = matcher(doc)
    
    # Display summary and suggestions
    st.write('**Summary:**')
    st.write(profile['summary'])
    
    if matches:
        st.write('**Suggestions:**')
        for match_id, start, end in matches:
            suggestion = doc[start:end].text
            st.write(suggestion)
    else:
        st.write('**No suggestions. Your profile looks great!**')
        
# Get resume file from user
st.sidebar.title('Resume Upload')
resume_file = st.sidebar.file_uploader('Upload your resume in PDF format', type='pdf')

if resume_file:
    # Extract text from PDF file
    resume_text = extract_text_from_pdf(resume_file)
    
    # Analyze text using Spacy
    doc_resume, suggestions_resume = analyze_text(resume_text)
    
    # Generate summary and recommendations using OpenAI
    summary, recommendations = generate_summary_and_recommendations(resume_text)
    
    # Display summary and suggestions
    st.write('**Summary:**')
    st.write(summary)
    
    st.write('**Recommendations:**')
    st.write(recommendations)
    
    if suggestions_resume:
        st.write('**Suggestions:**')
        for suggestion in suggestions_resume:
            st.write(suggestion)
    else:
        st.write('**No further suggestions. Your resume looks great!**')
else:
    st.write('Please upload a PDF file of your resume to continue.')
