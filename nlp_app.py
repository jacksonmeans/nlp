# Streamlit Libraries
import streamlit as st
# NLP Libraries
import nltk
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob
import re

st.title('Sentiment Predictor')
text = st.text_area('Input text')
if st.button('Analyze'):
  #Keeping only Text and digits
  text = re.sub(r"[^A-Za-z0-9]", " ", text)
  #Removes Whitespaces
  text = re.sub(r"\'s", " ", text)
  # Removing Links if any
  text = re.sub(r"http\S+", " link ", text)
  # Removes Punctuations and Numbers
  text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
  # Splitting Text
  text = text.split()
  # Lemmatizer
  lemmatizer = WordNetLemmatizer()
  lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
  text = " ".join(lemmatized_words)
  blob = TextBlob(text)
  sentiment_score = blob.sentiment.polarity
  if sentiment_score > 0:
      custom_emoji = ':blush:'
      st.success('Happy : {}'.format(custom_emoji))
  elif sentiment_score < 0:
      custom_emoji = ':disappointed:'
      st.warning('Sad : {}'.format(custom_emoji))
  else:
      custom_emoji = ':confused:'
      st.info('Confused : {}'.format(custom_emoji))
  st.success("Polarity Score is: {}".format(sentiment_score))
