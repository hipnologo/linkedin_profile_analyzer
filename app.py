import streamlit as st
import os
from linkedin_api import Linkedin
import spacy
import en_core_web_sm
from spacy.matcher import Matcher

# Set up Streamlit interface
st.set_page_config(page_title='LinkedIn Profile Analyzer', page_icon=':clipboard:', layout='wide')

st.title('LinkedIn Profile Analyzer')

# Get LinkedIn API authentication from environment variables
email = os.getenv('LINKEDIN_EMAIL')
password = os.getenv('LINKEDIN_PASSWORD')
client_id = os.getenv('LINKEDIN_CLIENT_ID')
client_secret = os.getenv('LINKEDIN_CLIENT_SECRET')

if email and password:
    try:
        # Authenticate with LinkedIn API using email and password
        api = Linkedin(email, password)
        st.sidebar.success('Successfully authenticated with LinkedIn API')
    except:
        st.sidebar.error('Failed to authenticate with LinkedIn API using email and password. Please check your credentials.')
elif client_id and client_secret:
    try:
        # Authenticate with LinkedIn API using client ID and client secret
        api = Linkedin(client_id, client_secret)
        st.sidebar.success('Successfully authenticated with LinkedIn API')
    except:
        st.sidebar.error('Failed to authenticate with LinkedIn API using client ID and client secret. Please check your credentials.')
else:
    st.sidebar.error('Please set the LINKEDIN_EMAIL and LINKEDIN_PASSWORD environment variables or the LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET environment variables.')

# Get LinkedIn profile URL from user
st.sidebar.title('Profile URL')
profile_url = st.sidebar.text_input('Enter your LinkedIn profile URL')

if profile_url:
    # Extract profile data using LinkedIn API
    profile = api.get_profile(profile_url=profile_url)
    
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
