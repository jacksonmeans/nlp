# Streamlit Libraries
import streamlit as st
# NLP Libraries
from nltk
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob
import re

st.title('Sentiment Predictor')
st.text_area('Input text')
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
  lemmatized_words = [lemmatizer.lemmatize(______) for word in text]
      text = " ".join(_________)
  blob = TextBlob(text)
  sentiment_score = blob.sentiment.polarity
  if result > 0:
      custom_emoji = ':blush:'
      st.success('Happy : {}'.format(______))
  elif result < 0:
      custom_emoji = ':disappointed:'
      st.warning('Sad : {}'.format(_____))
  else:
      custom_emoji = ':confused:'
      st.info('Confused : {}'.format(_____))
  st.success("Polarity Score is: {}".format(result))
