# Streamlit Libraries
import streamlit as st
# NLP Libraries
from nltk
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob
import re

st.title('Sentiment Predictor')
st.text_area('Input text')
st.button('Analyze')
