import streamlit as st
import pandas as pd
import numpy as np
import requests
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
from pandas.io.json import json_normalize
from streamlit.script_runner import StopException, RerunException


st.title("iFlects")
st.subheader("Welcome to iFlects:  A Sentiment Analysis Web application using Text Classification Algorithms")
st.set_option('deprecation.showfileUploaderEncoding', False)


single_review = st.text_input('Enter Sentence Below:')
count_positive = 0
count_negative = 0
count_neutral = 0



if single_review:
    url = 'http://iflectssentiment.herokuapp.com/classify/?text='+single_review
    r = requests.get(url)
    result = r.json()["text_sentiment"]
    if result=='positive':
        st.write("Positive sentence!")
    elif result=='negative':
       st.write("Negatve sentence!")
    else:
        st.write("Neutral sentence!")
else:
    st.write("Enter some sentence on the textbox.")


