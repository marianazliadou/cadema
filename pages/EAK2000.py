import streamlit as st
import math
import pandas as pd 
import pyarrow as pa
import pyarrow.lib as _lib
import numpy as np
from streamlit.cursor import make_delta_path 
from funkEAK import acd,MR, ΔV_CD, Vb, Vc

st.set_page_config(
  page_title="ΕΑΚ2000", initial_sidebar_state="expanded")

st.markdown('<style>h2{color: black;}</style>', unsafe_allow_html=True)
st.markdown("## <h2><u>Ικανοτικός σχεδιασμός στον ΕΑΚ2000</u></h2>", unsafe_allow_html=True)

with st.sidebar:
    epilogi = st.selectbox(
        "Επιλέξτε τον σχεδιασμό που θέλετε:",
        ("Ικανοτικός σχεδιασμός σε διάτμηση", "Ικανοτικός σχεδιασμός στους κόμβους"),
    )

if epilogi == "Ικανοτικός σχεδιασμός σε διάτμηση":
    with st.sidebar:
        elegxos = st.selectbox(
            "Επιλέξτε τον έλεγχο σχεδιασμού:", ("Δοκός", "Υποστυλώματα")
        )
        if elegxos == "Δοκός":    
          st.link_button("ΕΡΓΑΣΙΑ", "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=92")
          st.link_button("ΕΑΚ2000", "https://oasp.gr/userfiles/EAK2000.pdf#page=195")
        else:
          st.link_button("ΕΡΓΑΣΙΑ", "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=92")
          st.link_button("ΕΑΚ2000", "https://oasp.gr/userfiles/EAK2000.pdf#page=195")


#dokos
    if elegxos == 'Δοκός':
        with st.expander('**Τα αριθμητικά δεδομένα σας**'):
            col1,col2 =st.columns(2)
            with col1:
                st.info('**Δεδομένα δοκού:**')
                lb = st.number_input('Μήκος δοκού $l_b$:', value=5.5, step=0.1, format="%.2f")
            with col2:
                st.info('**Τέμνουσες:**')
                V0b = st.number_input('Τέμνουσα της δοκού $V_{0,_b}$:', value=60.0, step=0.1, format="%.2f")
            st.divider()
            st.info("**Ροπές αντοχής:**")
            col1,col2 =st.columns(2)
            with col1:
                st.success('**Αριστερά:**')
                MRb1_t = st.number_input('**Θετική** ροπή αντοχής $MRb,1^+$:', value=50.0, step=0.1, format="%.2f")
                MRb1_a = st.number_input('**Αρνητική** ροπή αντοχής $MRb,1^-$:',value = - 100.0, step=0.1, format="%.2f")
            with col2:
                st.success('**Δεξιά:**')
                MRb2_t = st.number_input('Για **θετική διεύθυνση** $MRb,2^+$:', value= 80.0, step=0.1, format="%.2f")
                MRb2_a = st.number_input('Για **αρνητική διεύθυνση** $MRb,2^-$:',value = -120.0, step=0.1, format="%.2f")

        st.divider()
        fora = st.selectbox("Επιλέξτε σεισμική φορά ανάλυσης:", ("Θετική →", "Αρνητική ←"))

        st.write("")
        st.subheader("**ΤΕΜΝΟΥΣΕΣ**")
        bubble_style = """
        background-color: #FFC0CB;
        border-radius: 20px;
        padding: 10px;
        box-shadow: 2px 2px 5px grey;
        max-width: 390px;
        """
        st.write('<div style="{}">Οι τέμνουσες των άκρων υπολογίζονται από τον τύπο:</div>'.format(bubble_style), unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown(r'''
                     $$\text{V}_{\text{CD,b}} = \text{V}_{\text{0,b}} + \Delta \text{V}_{\text{CD,b}}$$ 
                    
                    **όπου:**
                    
                    ◹ $$\Delta \text{V}_{\text{CD,b}} = 1.20 \left(\frac{\text{M}_{\text{Rb,}_{1}} + \text{M}_{\text{Rb,}_{2}}}{\text{l}_{\text{b}}} \right)$$''')
        st.write("")

        if fora == 'Θετική →':
            st.info("Για **θετική** σεισμική φορά:", icon="👉🏼")
            col1,col2 =st.columns(2)
            with col1:
                st.markdown(rf'''
                ◹ $$\text{{M}}_{{\text{{Rb,}}_{{1}}}}^+ = {MRb1_t}\, \text{{kNm}}$$''')
            with col2:
                st.markdown(rf'''    
                ◹ $$\text{{M}}_{{\text{{Rb,}}_{{2}}}}^- = {MRb2_a}\, \text{{kNm}}$$''')
     
            ΔVCD_b = ΔV_CD(MRb1_t, abs(MRb2_a), lb)
            ΔVCD_b = round(ΔVCD_b, 2)
            st.write("")
            st.markdown(rf''' 
                 **Άρα:**
                 
                 $$\Delta \text{{V}}_{{\text{{CD,b}}}} = 1.20 \left(\frac{{\text{{M}}_{{\text{{Rb,}}_{{1}}}}^+ + |\text{{M}}_{{\text{{Rb,}}_{{2}}}}^-|}}{{\text{{l}}_{{\text{{b}}}}}} \right) = {ΔVCD_b}\, \text{{kN}}$$''')
            VCD_b = Vb(V0b, ΔVCD_b)
            VCD_b = round(VCD_b, 2)
            st.write("")
            st.success("**Οπότε** η τέμνουσα σχεδιασμού δοκού για **θετική** σεισμική φορά θα είναι: ")
            st.markdown(rf''' 
                 
                 $$\text{{V}}_{{\text{{CD,b}}}} = \text{{V}}_{{\text{{0,b}}}} + \Delta \text{{V}}_{{\text{{CD,b}}}} = {V0b} + {ΔVCD_b} = {VCD_b}\, \text{{kN}}$$
''')

        else:
            st.info("Για **αρνητική** σεισμική φορά:", icon="👈🏼")
            col1,col2 = st.columns(2)
            with col1: 
                st.markdown(rf'''
                ◹ $$\text{{M}}_{{\text{{Rb,}}_{{1}}}}^- = {MRb1_a}\, \text{{kNm}}$$''')
            with col2:
                st.markdown(rf'''
                ◹ $$\text{{M}}_{{\text{{Rb,}}_{{2}}}}^+ = {MRb2_t}\, \text{{kNm}}$$''')
            ΔVCD_b = ΔV_CD(abs(MRb1_a), MRb2_t, lb)
            ΔVCD_b = round(ΔVCD_b, 2)
            st.write("")
            st.markdown(rf''' 
                 **Άρα:**
                 
                 $$\Delta \text{{V}}_{{\text{{CD,b}}}} = 1.20 \left(\frac{{|\text{{M}}_{{\text{{Rb,}}_{{1}}}}^-| + \text{{M}}_{{\text{{Rb,}}_{{2}}}}^+}}{{\text{{l}}_{{\text{{b}}}}}} \right) = {ΔVCD_b}\, \text{{kN}}$$''') 
            VCD_b = Vb(V0b, ΔVCD_b)
            VCD_b= round(VCD_b, 2)
            st.success("**Οπότε** η τέμνουσα σχεδιασμού για **αρνητική** σεισμική φορά θα είναι:")
            st.markdown(rf'''
                 $$\text{{V}}_{{\text{{CD,b}}}} = \text{{V}}_{{\text{{0,b}}}} + \Delta \text{{V}}_{{\text{{CD,b}}}} = {V0b} + {ΔVCD_b} = {VCD_b}\, \text{{kNm}}$$''')

   
#ipoatiloma      
    if elegxos == 'Υποστυλώματα':
        with st.expander('**Τα αριθμητικά δεδομένα σας**'):
            st.info("**Δεδομένα υποστυλώματος:**")
            lc = st.number_input('Μήκος υποστυλώματος $l_c$:', value=6.0, step=0.1, format="%.2f")
            st.divider()
            st.info('**Ροπές αντοχής:**')
            col1,col2 =st.columns(2)
            with col1:
                st.success('**Άνω:**')
                MRc1_t = st.number_input('**Θετική** ροπή αντοχής: $MRc,1^+$', value= 90.0,  step=0.1, format="%.2f")
                MRc1_a = st.number_input('**Αρνητική** ροπή αντοχής $MRc,1^-$',value = - 200.0, step=0.1, format="%.2f")
            with col2:
                st.success("**Κάτω:**")
                MRc2_t = st.number_input('**Θετική** ροπή αντοχής $MRc,2^+$', value= 120.0,  step=0.1, format="%.2f")
                MRc2_a = st.number_input('**Αρνητική** ροπή αντοχής $MRc,2^-$',value = - 250.0, step=0.1, format="%.2f")
  
        st.divider()
        fora = st.selectbox("Επιλέξτε σεισμική φορά ανάλυσης:", ("Θετική →", "Αρνητική ←"))

        st.write("")
        st.subheader("**ΤΕΜΝΟΥΣΕΣ**")
        bubble_style = """
        background-color: #FFC0CB;
        border-radius: 20px;
        padding: 10px;
        box-shadow: 2px 2px 5px grey;
        max-width: 390px;
       """
        st.write('<div style="{}">Οι τέμνουσες των άκρων υπολογίζονται από τον τύπο:</div>'.format(bubble_style), unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown(r'''
        $$\text{V}_{\text{CD,c}} = 1.40 \left(\frac{\text{M}_{\text{Rc,}_{1}} + \text{M}_{\text{Rc,}_{2}}}{\text{l}_{\text{c}}} \right)$$
        ''')
        st.write("")
        if fora == 'Θετική →':
            st.write("Όπου για **θετική** σεισμική φορά:")
            col1,col2 =st.columns(2)
            with col1:
                st.markdown(rf'''
                ◹ $$\text{{M}}_{{\text{{Rc,}}_{{1}}}}^+ = {MRc1_t}\, \text{{kNm}}$$''')
            with col2:
                st.markdown(rf'''
                ◹ $$\text{{M}}_{{\text{{Rc,}}_{{2}}}}^- = {MRc2_a}\, \text{{kNm}}$$''')
       
            VCD_c = Vc(MRc1_t, abs(MRc2_a),lc)
            VCD_c = round(VCD_c,2)
            st.success('**Αρα** η τέμνουσα σχεδιασμού για **θετική** σεισμική φορά θα είναι:')
            st.markdown(rf'''
            $$\text{{V}}_{{\text{{CD,c}}}} = 1.40 \left(\frac{{\text{{M}}_{{\text{{Rb,}}_{{1}}}}^+ + |\text{{M}}_{{\text{{Rb,}}_{{2}}}}^-|}}{{\text{{l}}_{{\text{{c}}}}}} \right) = {VCD_c}\, \text{{kN}}$$''')
        else:
            st.write("Όπου για **αρνητική** σεισμική φορά:")
            col1,col2 =st.columns(2)
            with col1:
                st.markdown(rf'''
                ◹ $$\text{{M}}_{{\text{{Rc,}}_{{1}}}}^- = {MRc1_a}\, \text{{kNm}}$$''')
            with col2:
                st.markdown(rf'''
                ◹ $$\text{{M}}_{{\text{{Rc,}}_{{2}}}}^+ = {MRc2_t}\, \text{{kNm}}$$''')
       
            VCD_c = Vc(abs(MRc1_a), MRc2_t,lc)
            VCD_c = round(VCD_c, 2)
            st.success('**Αρα** η τέμνουσα σχεδιασμού για **αρνητική** σεισμική φορά θα είναι:')
            st.markdown(rf'''
$$\text{{V}}_{{\text{{CD,c}}}} = 1.40 \left(\frac{{|\text{{M}}_{{\text{{Rb,}}_{{1}}}}^-| + \text{{M}}_{{\text{{Rb,}}_{{2}}}}^+}}{{\text{{l}}_{{\text{{c}}}}}} \right) = {VCD_c}\, \text{{kN}}$$''')
  

elif epilogi == 'Ικανοτικός σχεδιασμός στους κόμβους':
    with st.sidebar:
          st.link_button("ΕΡΓΑΣΙΑ", "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=92")
          st.link_button("ΕΑΚ2000", "https://oasp.gr/userfiles/EAK2000.pdf#page=121")

    with st.expander('**Τα αριθμητικά δεδομένα σας**'):
            st.info("**Δεδομένα κόμβου:**")
            grd = st.number_input('Συντελεστής $γ_{Rd}$:', value = 1.40, step =0.1, format ='%.3f')
            SMRd = st.number_input('Άθροισμα τελικών **ροπών αντοχής** των δοκών $ΣM_{Rd}$:', value =100.0, step=0.1, format='%.2f')
            SMEb = st.number_input('**Άθροισμα ροπών** $ΣΜ_{Ed}$:', value = 50.0, step=0.1, format='%.2f')
            st.divider()
            st.info('**Ροπές σεισμού:**')
            MEc_t = st.number_input('**Θετική** σεισμική φροά $MΕc^+$', value= 200.0,  step=0.1, format="%.2f")
            MEc_a = st.number_input('**Αρνητική** σεισιμική φορά $MΕc^-$',value = - 100.0, step=0.1, format="%.2f")
           
  
    st.divider()
    fora = st.selectbox("Επιλέξτε σεισμική φορά ανάλυσης:", ("Θετική →", "Αρνητική ←"))

    st.subheader("**ΥΠΟΣΤΥΛΩΜΑΤΑ**")
    bubble_style = """
    background-color: #FFC0CB;
    border-radius: 20px;
    padding: 10px;
    box-shadow: 2px 2px 5px grey;
    max-width: 360px;
    """
    st.write('<div style="{}">Οι ροπές των άκρων των υποστυλωμάτων υπολογίζονται από τον τύπο:</div>'.format(bubble_style), unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.markdown(r'''
                $$\text{M}_{\text{CD,c}} = \text{a}_{\text{CD}} \text{M}_{\text{Ec}}$$
                
                **όπου:**

                $$\text{a}_{\text{CD}} = \text{γ}_{\text{Rd}} \dfrac{\text{ΣM}_\text{Rd}}{|\text{ΣM}_\text{Eb}|}$$
    ''')

    st.write("")
    acd_t = acd(grd, SMRd, SMEb)
    acd_t = round(acd_t,2)
    if acd_t > 1:
        st.markdown(rf'''
                    **Άρα:**
                    $$\text{{α}}_\text{{CD}} = \text{{γ}}_{{\text{{Rd}}}} \dfrac{{\text{{ΣM}}_\text{{Rd}}}}{{|\text{{ΣM}}_\text{{Eb}}|}} = {acd_t}$$
                    ''')
        if fora == 'Θετική →' and abs(MEc_t) > abs(SMEb):
            st.info("Για **θετική** σεισμική φορά:", icon="👉🏼")
            st.markdown(rf''' → Επειδή ισύχει $$|\text{{ME}}_\text{{c}}^+| > |\text{{ΣΜ}}_\text{{b}}|:$$''')
            MCD_t = 1.40 * MEc_t
            st.markdown(rf'''                                                         
                     $$\text{{M}}_{{\text{{CD,c}}}}^+ = 1.40 \text{{M}}_{{\text{{Ec}}}}^+ = 1.40 * {MEc_t:.2f} = {MCD_t:.2f}\, \text{{kNm}}$$ ''')
        elif fora =='Θετική →':
            st.info("Για **θετική** σεισμική φορά:", icon="👉🏼")
            MCD1_t = MR(acd_t, MEc_t)
            MCD1_t = round(MCD1_t,1)
            st.markdown(rf'''                                                         
                    $$\text{{M}}_{{\text{{CD,c}}}}^+ = \text{{a}}_{{\text{{CD}}}} \text{{M}}_{{\text{{Ec}}}}^+ = {acd_t} * {MEc_t:.2f} = {MCD1_t}\, \text{{kNm}}$$ ''')
        elif fora == 'Αρνητική ←' and abs(MEc_a) > abs(SMEb):
            st.info("Για **αρνητική** σεισμική φορά:", icon="👈🏼")
            st.markdown(rf''' → Επειδή ισύχει $$|\text{{ME}}_\text{{c}}^-| > |\text{{ΣΜ}}_\text{{b}}|:$$''')
            MCD_a = 1.40 * MEc_a
            st.markdown(rf'''                                                         
                    $$\text{{M}}_{{\text{{CD,c}}}}^- = 1.40 \text{{M}}_{{\text{{Ec}}}}^- = 1.40 * ({MEc_a:.2f}) = {MCD_a:.2f}\, \text{{kNm}}$$ ''')
        elif fora == 'Αρνητική ←':
            st.info("Για **αρνητική** σεισμική φορά:", icon="👈🏼")
            MCD1_a = MR(acd_t, MEc_a)
            MCD1_a = round(MCD1_a,1)
            st.markdown(rf'''$$\text{{M}}_{{\text{{CD,c}}}}^- = \text{{a}}_{{\text{{CD}}}} \text{{M}}_{{\text{{Ec}}}}^- = {acd_t} * ({MEc_a:.2f}) = {MCD1_a}\, \text{{kNm}}$$ ''')
   
    elif acd_t <= 1:
        acd1 =1
        st.markdown(rf'''
                    **Άρα:**
                    $$\text{{α}}_\text{{CD}} = \text{{γ}}_{{\text{{Rd}}}} \dfrac{{\text{{ΣM}}_\text{{Rd}}}}{{|\text{{ΣM}}_\text{{Eb}}|}} = {acd1}$$''')
        if fora == 'Θετική →' and abs(MEc_t) > abs(SMEb):
            st.info("Για **θετική** σεισμική φορά:", icon="👉🏼")
            st.markdown(rf''' → Επειδή ισύχει $$|\text{{ME}}_\text{{c}}^+| > |\text{{ΣΜ}}_\text{{b}}|:$$''')
            MCD_t = 1.40 * MEc_t
            st.markdown(rf'''                                                         
                     $$\text{{M}}_{{\text{{CD,c}}}}^+ = 1.40 \text{{M}}_{{\text{{Ec}}}}^+ = 1.40 * {MEc_t:.2f} = {MCD_t:.2f}\, \text{{kNm}}$$ ''')
        elif fora =='Θετική →':
            st.info("Για **θετική** σεισμική φορά:", icon="👉🏼")
            MCD1_t = MR(acd1, MEc_t)
            MCD1_t = round(MCD1_t,1)
            st.markdown(rf'''                                                         
                    $$\text{{M}}_{{\text{{CD,c}}}}^+ = \text{{a}}_{{\text{{CD}}}} \text{{M}}_{{\text{{Ec}}}}^+ = {acd1} * {MEc_t:.2f} = {MCD1_t}\, \text{{kNm}}$$ ''')
        elif fora == 'Αρνητική ←' and abs(MEc_a) > abs(SMEb):
            st.info("Για **αρνητική** σεισμική φορά:", icon="👈🏼")
            st.markdown(rf''' → Επειδή ισύχει $$|\text{{ME}}_\text{{c}}^-| > |\text{{ΣΜ}}_\text{{b}}|:$$''')
            MCD_a = 1.40 * MEc_a
            st.markdown(rf'''                                                         
                    $$\text{{M}}_{{\text{{CD,c}}}}^- = 1.40 \text{{M}}_{{\text{{Ec}}}}^- = 1.40 * ({MEc_a:.2f}) = {MCD_a:.2f}\, \text{{kNm}}$$ ''')
        elif fora == 'Αρνητική ←':
            st.info("Για **αρνητική** σεισμική φορά:", icon="👈🏼")
            MCD1_a = MR(acd1, MEc_a)
            MCD1_a = round(MCD1_a,1)
            st.markdown(rf'''$$\text{{M}}_{{\text{{CD,c}}}}^- = \text{{a}}_{{\text{{CD}}}} \text{{M}}_{{\text{{Ec}}}}^- = {acd1} * ({MEc_a:.2f}) = {MCD1_a}\, \text{{kNm}}$$ ''')
   
        
    