import streamlit as st 
import numpy as np 
import math
import pandas as pd 




st.set_page_config(
  page_title = 'ΙΚΑΝΟΤΙΚΟΣ ΣΧΕΔΙΑΣΜΟΣ', page_icon="📊", layout="wide", initial_sidebar_state="expanded")
col1,col2 = st.columns(2)
with col1:
  dipae_url = "images/dipae.jpg"
  st.image(dipae_url, use_column_width=True )
with col2:
  tei_url = "images/tei.jpg"
  st.image(tei_url, use_column_width=True)
st.markdown("<p style='text-align: center;'>Μαρία Ναζίάδου</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Νοέμβριος 2024</p>", unsafe_allow_html=True)
st.divider()

st.write("")
st.markdown("""<h2 style='color: #2F4F4F; font-size: 50px; text-align: center;'><u>ΙΚΑΝΟΤΙΚΟΣ ΣΧΕΔΙΑΣΜΟΣ</u></h2>""",unsafe_allow_html=True)
st.markdown("""<h2 style='color: #191970; font-size: 24px;'>▫ <u>Διαφορές υπολογισμού ικανοτικού σχεδιασμού ανάμεσα στον Ευρωκώδικα 8 και στον ΕΑΚ2000.</u>""",unsafe_allow_html=True)
st.write("")
st.markdown("""<div style=
  "background-color: #008B8B;
   padding: 3px;
   border-radius: 20px;"><p style="color: #F8F8FF; font-size: 20px; text-align: center;">Ικανοτικός σχεδιασμός σε διάτμηση</p></div>""", unsafe_allow_html=True)
diatmisi_url = "images/FLOW1.jpg"
st.image(diatmisi_url,  use_column_width=True)
st.write("▷ Η διαφορά υπολογισμού του **ικανοτικού σχεδιασμού σε διάτμηση**, ανάμεσα στον Ευρωκώδικα 8 και το ΕΑΚ 2000 είναι ότι, **οι υπολογισμοί του Ευρωκώδικα 8  συμπεριλαμβάνουν και τις ροπές αντοχής των γειτονικών δομικών στοιχείων** (π.χ. αριστερή δοκός ή/και άνω υποστύλωμα), ενώ στον **ΕΑΚ2000 οι υπολογισμοί γίνονται μόνο με τις ροπές αντοχής της κύριας δοκού ή υποστυλώματος.**")
st.write("")
st.write("")
st.write("")
st.markdown("""<div style=
  "background-color: #008B8B;
   padding: 3px;
   border-radius: 20px;"><p style="color: #F8F8FF; font-size: 20px; text-align: center;">Ικανοτικός σχεδιασμός σε κόμβο</p></div>""", unsafe_allow_html=True)
komvos_url = "images/FLOW2.jpg"
st.image(komvos_url,  use_column_width=True)

st.write("▷ Η διαφορά υπολογισμού του **ικανοτικού σχεδιασμού σε κόμβο, ανάμεσα στον Ευρωκώδικα 8 και στον ΕΑΚ2000 είναι:**")
st.write("1. Στον Ευρωκώδικα 8 ο κόμβος χωρίζεται σε 3 τύπους: **α. τον εσωτερικό κόμβο, β. τον εξωτερικό κόμβο, γ. τον γωνιακό κόμβο**, ενώ στον ΕΑΚ2000 όχι.")
st.markdown(rf'''2. Η ροή των υπολογισμών στον Ευρωκώδικα 8 καταλήγει στην **ανισότητα $$\sum \text{{Μ}}_\text{{Rc}} \geq 1.3 \sum \text{{M}}_\text{{Rb}}$$**, ενώ στον ΕΑΚ2000 καταλήγει στις **ροπές αντοχής των άκρων του υποστυλώματος.**''')





