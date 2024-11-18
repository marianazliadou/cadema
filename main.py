import streamlit as st
import numpy as np
import math
import pandas as pd


st.set_page_config(
    page_title='ΙΚΑΝΟΤΙΚΟΣ ΣΧΕΔΙΑΣΜΟΣ', page_icon="📊", layout="wide", initial_sidebar_state="expanded")
col1, col2 = st.columns(2)
with col1:
    dipae_url = "images/dipae.jpg"
    st.image(dipae_url, width=500)
with col2:
    tei_url = "images/tei.jpg"
    st.image(tei_url, width=500)
st.markdown("<p style='text-align: center;'>Μαρία Ναζλιάδου</p>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Νοέμβριος 2024</p>",
            unsafe_allow_html=True)
st.divider()

st.write("")
st.markdown("""<h2 style='color: #2F4F4F; font-size: 50px; text-align: center;'><u>ΙΚΑΝΟΤΙΚΟΣ ΣΧΕΔΙΑΣΜΟΣ</u></h2>""", unsafe_allow_html=True)

st.write("")
st.markdown("""<div style=
  "background-color: #008B8B;
   padding: 3px;
   border-radius: 20px;"><p style="color: #F8F8FF; font-size: 20px; text-align: center;">Ικανοτικός σχεδιασμός σε διάτμηση</p></div>""", unsafe_allow_html=True)
diatmisi_url = "images/FLOW1.jpg"
st.image(diatmisi_url,  use_column_width=True)
st.write("")
st.write("")
st.markdown("""<div style=
  "background-color: #008B8B;
   padding: 3px;
   border-radius: 20px;"><p style="color: #F8F8FF; font-size: 20px; text-align: center;">Ικανοτικός σχεδιασμός σε κόμβο</p></div>""", unsafe_allow_html=True)
komvos_url = "images/FLOW2.jpg"
st.image(komvos_url,  use_column_width=True)
