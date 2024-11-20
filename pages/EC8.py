import streamlit as st
from funkEK8 import (
    SMRc_ar_t,
    SMRc_ar_a,
    SMRc_de_t,
    SMRc_de_a,
    SMRb_ar_t,
    SMRb_ar_a,
    SMRb_de_t,
    SMRb_de_a,
    SMRc_a_t,
    SMRb_a_t,
    SMRc_a_a,
    SMRb_a_a,
    SMRc_k_t,
    SMRb_k_t,
    SMRc_k_a,
    SMRb_k_a,
    Mid_b,
    Mid_s,
    Vd_B,
    Vd_b,
    Vd_b1,
    Vd_b2,
    DV,
    VEd_t_ar,
    VEd_t_de,
    VEd_a_de,
    VEd_a_ar,
    Vd_C,
    Vd_c,
    Vd_c1,
    Vd_c2,
    SMRc_th,
    SMRc_ar,
    SMRb_th,
    SMRb_ar,
    SMRc_eks_th,
    SMRc_eks_arn,
    SMRb_g_ar,
    SMRb_g_de,
    SMRc_g_an,
    SMRc_g_kat,
    Mid_bu,
)

st.set_page_config(
    page_title="ΕΥΡΩΚΩΔΙΚΑΣ 8", initial_sidebar_state="expanded"
)

st.markdown("<style>h2{color: black;}</style>", unsafe_allow_html=True)
st.markdown("## <u>Ικανοτικός σχεδιασμός στον Ευρωκώδικα 8</u>", unsafe_allow_html=True)

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
            st.link_button(
                "ΕΡΓΑΣΙΑ",
                "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=92",
            )
            st.link_button(
                "ΕΥΡΩΚΩΔΙΚΑΣ 8",
                "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=92",
            )
            st.page_link("pages/info.py", label="Σχεδιασμός δοκού", icon="🪄")
        else:
            st.link_button(
                "ΕΡΓΑΣΙΑ",
                "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=92",
            )
            st.link_button(
                "ΕΥΡΩΚΩΔΙΚΑΣ 8",
                "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=93",
            )
            st.page_link("pages/info.py", label="Σχεδιασμός υποστυλώματος", icon="🔗")

    # TAMPLO - dokos
    if elegxos == "Δοκός":
        katask = st.selectbox("Τι κατηγορία πλαστιμότητας έχουμε;", ("ΚΠΜ", "ΚΠΥ"))
        if katask == "ΚΠΜ":
            grd = 1.0
            st.write("Ο συντελεστής $γ_{Rd}$ είναι:", grd)
        else:
            grd = 1.2
            st.write("Ο συντελεστής $γ_{Rd}$ είναι:", grd)

        with st.expander("**Τα αριθμητικά δεδομένα σας**"):
            st.info("**Δεδομένα δοκού:**")
            lcl = st.number_input("**Μήκος δοκού:** $L_cl$", value=5.5, step=0.1, format="%.3f")
            V0_i = st.number_input("**Τέμνουσα κατακόρυφου φορτίου:** $V_{0,i}$", value=50.0, step=0.1, format="%.2f")
            col1, col2_3, col4 = st.columns([1, 2, 1])
            with col1:
                ar_dokos = st.checkbox("Αριστερή δοκός")
                if ar_dokos:
                    st.error("**Ροπές αντοχής αριστερής δοκού:**")
                    MRb1l_a = st.number_input(
                        "**Αρνητική** ροπή αντοχής $M_{{Rb,1left}}^-$:", value=-100.0, step=0.1, format="%.2f"
                    )
                    MRb1l_t = st.number_input(
                        "**Θετική** ροπή αντοχής $MRb,1_{left}^+$:", value=50.0, step=0.1, format="%.2f"
                    )
                else:
                    st.write("")
                ar_upost = st.checkbox("Αριστερό υποστύλωμα", value=True)
                if ar_upost:
                    st.divider()
                    st.info("**Ροπές αντοχής αριστερού υποστυλώματος:**")
                    arupost_an = st.checkbox("Άνω")
                    if arupost_an:
                      st.error("**Άνω:**")
                      MRc_1a = st.number_input(
                          "**Αρνητική** ροπή αντοχής: $MRc,1^-$:", value=-250.0, step=0.1, format="%.2f"
                      )
                      MRc_1t = st.number_input(
                          "**Θετική** ροπή αντοχής: $MRc,1^+$:", value=500.0, step=0.1, format="%.2f"
                      )
                    else:
                        st.write("")
                    arupost_kat = st.checkbox("Κάτω", value=True)
                    if arupost_kat:
                      st.error("**Κάτω:**")
                      MRc_2a = st.number_input(
                          "**Αρνητική** ροπή αντοχής: $MRc,2^-$:", value=-300.0, step=0.1, format="%.2f"
                      )
                      MRc_2t = st.number_input(
                          "**Θετική** ροπή αντοχής: $MRc,2^+$:", value=600.0, step=0.1, format="%.2f"
                      )
                    else:
                        st.write("")
                else:
                    st.write("")

            with col2_3:
                st.info("**Ροπές αντοχής δοκού**")
                col1, col2 = st.columns(2)
                with col1:
                    st.success("**Αριστερά:**")
                    MRb_1a = st.number_input(
                        "**Αρνητική** ροπή αντοχής: $MRb,1^-$:", value=-150.0, step=0.1, format="%.2f"
                    )
                    MRb_1t = st.number_input(
                        "**Θετική** ροπή αντοχής: $MRb,1^+$:", value=300.0, step=0.1, format="%.2f"
                    )
                with col2:
                    st.success("**Δεξιά:**")
                    MRb_2a = st.number_input(
                        "**Αρνητική** ροπή αντοχής: $MRb,2^-$:", value=-200.0, step=0.1, format="%.2f"
                    )
                    MRb_2t = st.number_input(
                        "**Θετική** ροπή αντοχής: $MRb,2^+$:", value=400.0, step=0.1, format="%.2f"
                    )

            with col4:
                de_dokos = st.checkbox("Δεξιά δοκός")
                if de_dokos:
                    st.error("**Ροπές αντοχής δεξιάς δοκού:**")
                    MRb2r_a = st.number_input(
                        "**Αρνητική** ροπή αντοχής $MRb,2_{right}^-$:", value=-200.0, step=0.1, format="%.2f"
                    )
                    MRb2r_t = st.number_input(
                        "**Θετική** ροπή αντοχής $MRb,2_{right}^+$:", value=100.0, step=0.1, format="%.2f"
                    )
                else:
                    st.write("")
                de_upost = st.checkbox("Δεξιό υποστύλωμα")
                if de_upost:
                    st.divider()
                    st.info("**Ροπές αντοχής δεξιού υποστυλώματος:**")
                    deupost_an = st.checkbox("Άνω:")
                    if deupost_an:
                      st.error("**Άνω:**")
                      MRc_3a = st.number_input(
                          "**Αρνητική** ροπή αντοχής: $MRc,3^-$:", value=-350.0, step=0.1, format="%.2f"
                      )
                      MRc_3t = st.number_input(
                          "**Θετική** ροπή αντοχής: $MRc,3^+$:", value=700.0, step=0.1, format="%.2f"
                      )
                    else:
                        st.write("")
                    deupost_kat = st.checkbox("Κάτω:")
                    if deupost_kat:
                      st.error("**Κάτω:**")
                      MRc_4a = st.number_input(
                          "**Αρνητική** ροπή αντοχής: $MRc,4^-$:", value=-100.0, step=0.1, format="%.2f"
                      )
                      MRc_4t = st.number_input(
                          "**Θετική** ροπή αντοχής: $MRc,4^+$:", value=200.0, step=0.1, format="%.2f"
                      )
                    else:
                        st.write("")
                else:
                    st.write("")

        st.write("")
        dokos_url = "images/dokos.jpg"
        st.image(dokos_url, caption="Eυρωκώδικας 8", use_column_width=True)

        st.divider()
        fora = st.selectbox("Επιλέξτε σεισμική φορά ανάλυσης:", ("Θετική", "Αρνητική"))

        MRb1l_a = MRb1l_a if "MRb1l_a" in locals() else 0
        MRb1l_t = MRb1l_t if "MRb1l_t" in locals() else 0
        MRc_1a = MRc_1a if "MRc_1a" in locals() else 0
        MRc_1t = MRc_1t if "MRc_1t" in locals() else 0
        MRc_2a = MRc_2a if "MRc_2a" in locals() else 0
        MRc_2t = MRc_2t if "MRc_2t" in locals() else 0
        MRb2r_a = MRb2r_a if "MRb2r_a" in locals() else 0
        MRb2r_t = MRb2r_t if "MRb2r_t" in locals() else 0
        MRc_3a = MRc_3a if "MRc_3a" in locals() else 0
        MRc_3t = MRc_3t if "MRc_3t" in locals() else 0
        MRc_4a = MRc_4a if "MRc_4a" in locals() else 0
        MRc_4t = MRc_4t if "MRc_4t" in locals() else 0

        if ar_dokos:
          MRb1l_a = MRb1l_a 
          MRb1l_t = MRb1l_t 
        elif de_dokos:
          MRb2r_a = MRb2r_a 
          MRb2r_t = MRb2r_t        
        else:
            MRb1l_a = 0
            MRb1l_t = 0
            MRb2r_a = 0
            MRb2r_t = 0

        if fora == "Θετική":
            SMRb_ar = SMRb_ar_t(MRb1l_a, MRb_1t)
            SMRb_ar = round(SMRb_ar, 2)
            SMRc_ar = SMRc_ar_t(MRc_1a, MRc_2t)
            SMRc_ar = round(SMRc_ar,2)
            SMRb_de = SMRb_de_t(MRb2r_t, MRb_2a)
            SMRb_de = round(SMRb_de, 2)
            SMRc_de = SMRc_de_t(MRc_3a, MRc_4t)
            SMRc_de = round(SMRc_de,2)
        else:
            SMRb_ar = SMRb_ar_a(MRb1l_t, MRb_1a)
            SMRb_ar = round(SMRb_ar, 2)
            SMRc_ar = SMRc_ar_a(MRc_1t, MRc_2a)
            SMRc_ar = round(SMRc_ar,2)
            SMRb_de = SMRb_de_a(MRb2r_a, MRb_2t)
            SMRb_de = round(SMRb_de, 2)
            SMRc_de = SMRc_de_a(MRc_3t, MRc_4a)
            SMRc_de = round(SMRc_de,2)

        st.subheader("**ΡΟΠΕΣ**")
        bubble_style = """
        background-color: #FFC0CB;
        border-radius: 20px;
        padding: 10px;
        box-shadow: 2px 2px 5px grey;
        max-width: 405px;
    """
        st.write(
            '<div style="{}">Οι ροπές των άκρων υπολογίζονται από τον γενικό τύπο:</div>'.format(
                bubble_style
            ),
            unsafe_allow_html=True,
        )
        st.write("")
        st.write("")
        st.markdown(r"""
      $$\text{M}_{\text{i,d}} = \gamma_{\text{Rd}}  \text{M}_{\text{Rb,i}} \min\left(1, \dfrac{\sum \text{M}_{\text{Rc}}}{\sum \text{M}_{\text{Rb}}}\right)$$
      """)

        st.write("")
        tab1, tab2 = st.tabs(["Αριστερά", "Δεξιά"])
        with tab1:
            if SMRb_ar > SMRc_ar:
                st.markdown(rf"""
        Επειδή: $$\sum \text{{M}}_{{\text{{Rb,αρ}}}} = {SMRb_ar}\, \text{{kNm}} > \sum \text{{M}}_{{\text{{Rc,αρ}}}} = {SMRc_ar}\, \text{{kNm}}$$, ο τύπος θα πάρει την μορφή:
        
        **⇒** $$\text{{M}}_{{\text{{i,d}}}} = \gamma_{{\text{{Rd}}}} \text{{M}}_{{\text{{Rb,i}}}} \dfrac{{\sum \text{{M}}_{{\text{{Rc,αρ}}}}}}{{\sum \text{{M}}_{{\text{{Rb,αρ}}}}}}$$
        """)
                
                if fora == 'Θετική':
                  col1, col2 = st.columns([1,10])
                  with col2:
                     dokos_thetiko_aristera_url = "images/dokos_thetiko_aristera.jpg"
                     st.image(dokos_thetiko_aristera_url, caption="Φορά των ροπών που συντρέχουν στο άκρο της αριστερής δοκού για θετική σεισμική φορά.", width=460)

                  M1dt = Mid_b(grd, MRb_1t, SMRc_ar, SMRb_ar)
                  M1dt = round(M1dt, 2)
                  st.markdown(
                    rf""" Έτσι, η ροπή στο **αριστερό άκρο για θετική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{1,d}}}}^+ = {M1dt}\, \text{{kNm}}$$""") 
                else:
                    col1,col2 = st.columns([1,10])
                    with col2:
                     dokos_arnitiko_aristera_url = "images/dokos_arnitiko_aristera.jpg"
                     st.image(dokos_arnitiko_aristera_url, caption="Φορά των ροπών που συντρέχουν στο άκρο της αριστερής δοκού για αρνητική σεισμική φορά.", width=500)

                    M1da = Mid_b(grd, MRb_1a, SMRc_ar, SMRb_ar)
                    M1da = round(M1da, 2)
                    st.markdown(
                    rf""" Έτσι, η ροπή στο **αριστερό άκρο για αρνητική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{1,d}}}}^- = {M1da}\, \text{{kNm}}$$"""
                )

            elif SMRb_ar <= SMRc_ar:
                st.markdown(rf""" Επειδή: $$\sum \text{{M}}_{{\text{{Rb,αρ}}}}= {SMRb_ar}\, \text{{kNm}} \leq \sum \text{{M}}_{{\text{{Rc,αρ}}}} = {SMRc_ar}\, \text{{kNm}}$$, ο τύπος θα πάρει την μορφή:                     
        **⇒** $$\text{{M}}_{{\text{{i,d}}}} = \gamma_{{\text{{Rd}}}} \text{{M}}_{{\text{{Rb,i}}}}$$""")
                
                if fora == 'Θετική':
                  col1, col2 = st.columns([1,10])
                  with col2:
                     dokos_thetiko_aristera_url = "images/dokos_thetiko_aristera.jpg"
                     st.image(dokos_thetiko_aristera_url, caption="Φορά των ροπών που συντρέχουν στο άκρο της αριστερής δοκού για θετική σεισμική φορά.", width=460)
                  
                  M1dtt = Mid_s(grd, MRb_1t)
                  M1dtt = round(M1dtt, 2)
                  st.markdown(
                    rf""" Έτσι η ροπή στο **αριστερό άκρο για θετική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{1,d}}}}^+ = {M1dtt}\, \text{{kNm}}$$""")
                  
                else:
                    col1,col2 = st.columns([1,10])
                    with col2:
                     dokos_arnitiko_aristera_url = "images/dokos_arnitiko_aristera.jpg"
                     st.image(dokos_arnitiko_aristera_url, caption="Φορά των ροπών που συντρέχουν στο άκρο της αριστερής δοκού για αρνητική σεισμική φορά.", width=500)
                  
                    M1daa = Mid_s(grd, MRb_1a)
                    M1daa = round(M1daa, 2)
                    st.markdown(
                    rf""" Έτσι, η ροπή στο **αριστερό άκρο για αρνητική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{1,d}}}}^- = {M1daa}\,\text{{kNm}}$$"""
                )

        with tab2:
            if SMRb_de > SMRc_de:
                st.markdown(rf""" 
        Επειδή: $$\sum \text{{M}}_{{\text{{Rb,δεξ}}}} = {SMRb_de}\, \text{{kNm}} > \sum \text{{M}}_{{\text{{Rc,δεξ}}}} = {SMRc_de}\, \text{{kNm}}$$, ο τύπος θα πάρει την μορφή:
        
        **⇒** $$\text{{M}}_{{\text{{i,d}}}} = \gamma_{{\text{{Rd}}}} \text{{M}}_{{\text{{Rb,i}}}} \dfrac{{\sum \text{{M}}_{{\text{{Rc,δεξ}}}}}} {{\sum \text{{M}}_{{\text{{Rb,δεξ}}}}}}$$
        """)
                if fora == 'Θετική':
                  col1, col2 = st.columns([1,10])
                  with col2:
                     dokos_thetiko_deksia_url = "images/dokos_thetiko_deksia.jpg"
                     st.image(dokos_thetiko_deksia_url, caption="Φορά των ροπών που συντρέχουν στο άκρο της δεξιάς δοκού για θετική σεισμική φορά.", width=460)
                  M2da = Mid_b(grd, MRb_2a, SMRc_de, SMRb_de)
                  M2da = round(M2da, 2)
                  st.markdown(
                  rf""" Έτσι, η ροπή στο **δεξιό άκρο για θετική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{2,d}}}}^- = {M2da}\, \text{{kNm}}$$"""
                )
                
                else:
                  col1,col2 = st.columns([1,10])
                  with col2:
                     dokos_arnitiko_deksia_url = "images/dokos_arnitiko_deksia.jpg"
                     st.image(dokos_arnitiko_deksia_url, caption="Φορά των ροπών που συντρέχουν στο άκρο της δεξιάς δοκού για αρνητική σεισμική φορά.", width=500)
                  M2dt = Mid_b(grd, MRb_2t, SMRc_de, SMRb_de)
                  M2dt = round(M2dt, 2)
                  st.markdown(
                    rf""" Έτσι, η ροπή στο **δεξιό άκρο για αρνητική σεισμική φορά** θα είναι ίση: $$\text{{M}}_{{\text{{2,d}}}}^+ = {M2dt}\,\text{{kNm}}$$""")
                    

            elif SMRb_de <= SMRc_de:
                st.markdown(rf"""
          Επειδή: $$\sum \text{{M}}_{{\text{{Rb,δεξ}}}} = {SMRb_de}\, \text{{kNm}} \leq \sum \text{{M}}_{{\text{{Rc,δεξ}}}} = {SMRc_de}\, \text{{kNm}}$$, ο τύπος θα πάρει την μορφή:
        
        **⇒** $$\text{{M}}_{{\text{{i,d}}}} = \gamma_{{\text{{Rd}}}} \text{{M}}_{{\text{{Rb,i}}}}$$        
        """)
                if fora == 'Θετική':
                  col1, col2 = st.columns([1,10])
                  with col2:
                     dokos_thetiko_deksia_url = "images/dokos_thetiko_deksia.jpg"
                     st.image(dokos_thetiko_deksia_url, caption="Φορά των ροπών που συντρέχουν στο άκρο της δεξιάς δοκού για θετική σεισμική φορά.", width=460)
                  M2daa = Mid_s(grd, MRb_2a)
                  M2daa = round(M2daa, 2)
                  st.markdown(
                  rf""" Έτσι, η ροπή στο **δεξιό άκρο για θετική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{2,d}}}}^- = {M2daa}\, \text{{kNm}}$$"""
                )
                else:
                  col1,col2 = st.columns([1,10])
                  with col2:
                     dokos_arnitiko_deksia_url = "images/dokos_arnitiko_deksia.jpg"
                     st.image(dokos_arnitiko_deksia_url, caption="Φορά των ροπών που συντρέχουν στο άκρο της δεξιάς δοκού για αρνητική σεισμική φορά.", width=500)
                  M2dtt = Mid_s(grd, MRb_2t)
                  M2dtt = round(M2dtt, 2)
                  st.markdown(
                    rf""" Έτσι, η ροπή στο **δεξιό άκρο για αρνητική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{2,d}}}}^+ = {M2dtt}\, \text{{kNm}}$$""")
                    

        st.divider()
        st.subheader("**ΤΕΜΝΟΥΣΕΣ**")
        bubble_style = """
        background-color: #FFC0CB;
        border-radius: 20px;
        padding: 10px;
        box-shadow: 2px 2px 5px grey;
        max-width: 690px;
    """
        st.write(
            '<div style="{}">Η γενική μορφή των σχέσεων υπολογισμού των τεμνουσών σχεδιασμού των υποστυλωμάτων είναι:</div>'.format(
                bubble_style
            ),
            unsafe_allow_html=True,
        )

        st.write("")
        st.write("")
        st.markdown(r"""
    $$\text{max} \text{V}_{\text{d}_\text{(x)}} = \frac{\gamma_{\text{Rd}} \times \left[\text{M}_{\text{Rb,}_{1}}^- \times \min \left(1, \left(\frac{\sum \text{M}_{\text{Rc,}{\text{αρ}}}}{\sum \text{M}_{\text{Rb,}{\text{αρ}}}}\right)_1\right) + \text{M}_{\text{Rb,}_{2}}^+ \times \min \left(1, \left(\frac{\sum \text{M}_{\text{Rc,}{\text{δεξ}}}}{\sum \text{M}_{\text{Rb,}{\text{δεξ}}}}\right)_2\right) \right]}{\text{L}_{\text{cl}}} + \text{V}_{{\text{G}+{\text{ψ}_2}{\text{Q}_o}}_\text{(x)}}$$
      """)

        st.write("")
        st.markdown(r"""
   $$\text{min} \text{V}_{\text{d}_\text{(x)}} = - \frac{\gamma_{\text{Rd}} \times \left[\text{M}_{\text{Rb,}_{1}}^+ \times \min \left(1, \left(\frac{\sum \text{M}_{\text{Rc,}{\text{αρ}}}}{\sum \text{M}_{\text{Rb,}{\text{αρ}}}}\right)_1\right) + \text{M}_{\text{Rb,}_{2}}^- \times \min \left(1, \left(\frac{\sum \text{M}_{\text{Rc,}{\text{δεξ}}}}{\sum \text{M}_{\text{Rb,}{\text{δεξ}}}}\right)_2\right)\right]}{\text{L}_{\text{cl}}} + \text{V}_{{\text{G}+{\text{ψ}_2}{\text{Q}_o}}_\text{(x)}}$$
  """)
        st.markdown(
            """ <style>.dashed-line {
    border-top: 1px dashed #555;
    margin-top: 10px;
    margin-bottom: 20px;
    border-width: 2px;}</style><div class="dashed-line"></div>""",
            unsafe_allow_html=True,
        )

        st.write("")
        if SMRb_ar > SMRc_ar and SMRb_de > SMRc_de:
            st.markdown(
                rf""" ▧ Επειδή: $$\sum \text{{M}}_{{\text{{Rb,αρ}}}} = {SMRb_ar}\, \text{{kNm}} > \sum \text{{M}}_{{\text{{Rc,αρ}}}} = {SMRc_ar}\, \text{{kNm και}} \sum \text{{M}}_{{\text{{Rb,δεξ}}}} = {SMRb_de}\, \text{{kNm}} > \sum \text{{M}}_{{\text{{Rc,δεξ}}}} = {SMRc_de}\, \text{{kNm}}$$"""
            )
            st.write("")

            st.markdown(r"""   
        $$\text{max} \text{V}_{\text{d}_\text{(x)}} = \dfrac{ \gamma_{\text{Rd}} \times \left[ \left( \text{M}_{\text{Rb,}_{1}}^{-} \times \dfrac{\sum \text{M}_{\text{Rc,αρ}}}{\sum \text{M}_{\text{Rb,αρ}}} \right) + \left( \text{M}_{\text{Rb,}_{2}}^{+} \times \dfrac{\sum \text{M}_{\text{Rc,δεξ}}}{\sum \text{M}_{\text{Rb,δεξ}}} \right) \right] }{\text{L}_{\text{cl}}} + \text{V}_{\text{G}+{\text{ψ}_2}{\text{Q}_o}_\text{(x)}}$$ 
        
        **και**
        
        $$\text{min} \text{V}_{\text{d}_\text{(x)}} = - \dfrac{ \gamma_{\text{Rd}} \times \left[ \left( \text{M}_{\text{Rb,}_{1}}^{+} \times \dfrac{\sum \text{M}_{\text{Rc,αρ}}}{\sum \text{M}_{\text{Rb,αρ}}} \right) + \left( \text{M}_{\text{Rb,}_{2}}^{-} \times \dfrac{\sum \text{M}_{\text{Rc,δεξ}}}{\sum \text{M}_{\text{Rb,δεξ}}} \right) \right] }{\text{L}_{\text{cl}}} + \text{V}_{\text{G}+{\text{ψ}_2}{\text{Q}_o}_\text{(x)}}$$ 
        
        **Άρα:**
        """)
            maxVd_x = Vd_B(
                grd, MRb_1a, SMRc_ar, SMRb_ar, MRb_2t, SMRc_de, SMRb_de, lcl, V0_i
            )
            minVd_x = Vd_B(
                grd, MRb_1t, SMRc_ar, SMRb_ar, MRb_2a, SMRc_de, SMRb_de, lcl, V0_i
            )
            maxVd_x = round(maxVd_x, 2)
            minVd_x = round(minVd_x, 2)
            st.markdown(
                rf""" **⁛** Η **μέγιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{max}} \text{{V}}_{{\text{{d}}_\text{{(x)}}}} = {maxVd_x}\, \text{{kN}}$$ και η **ελάχιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{min}} \text{{V}}_{{\text{{d}}_\text{{(x)}}}} = {-minVd_x}\, \text{{kN}}$$"""
            )

        elif SMRb_ar > SMRc_ar and SMRb_de <= SMRc_de:
            st.markdown(rf"""
      ▧ Επειδή $$\sum \text{{M}}_{{\text{{Rb,αρ}}}} = {SMRb_ar}\, \text{{kNm}} > \sum \text{{M}}_{{\text{{Rc,αρ}}}} = {SMRc_ar}\, \text{{kNm και}} \sum \text{{M}}_{{\text{{Rb,δεξ}}}} = {SMRb_de}\, \text{{kNm}} \leq \sum \text{{M}}_{{\text{{Rc,δεξ}}}} = {SMRc_de}\, \text{{kNm}}$$""")
            st.write("")

            st.markdown(r"""
      $$\text{max} \text{V}_{\text{d}_\text{(x)}} = \frac{ \gamma_{\text{Rd}} \times \left[ \left( \text{M}_{\text{Rb,}_{1}}^{-} \times \frac{\sum \text{M}_{\text{Rc,αρ}}}{\sum \text{M}_{\text{Rb,αρ}}} \right) + \text{M}_{\text{Rb,}_{2}}^{+} \right] }{\text{L}_{\text{cl}}} + \text{V}_{\text{G} + {\text{ψ}_2}{\text{Q}_o}_\text{(x)}}$$

      **και**

      $$\text{min} \text{V}_{\text{d}_\text{(x)}} = - \frac{ \gamma_{\text{Rd}} \times \left[ \left( \text{M}_{\text{Rb,}_{1}}^{+} \times \frac{\sum \text{M}_{\text{Rc,αρ}}}{\sum \text{M}_{\text{Rb,αρ}}} \right) + \text{M}_{\text{Rb,}_{2}}^{-} \right] }{\text{L}_{\text{cl}}} + \text{V}_{\text{G} + {\text{ψ}_2}{\text{Q}_o}_\text{(x)}}$$

      **Άρα:**   
      """)
            maxVd_x = Vd_b1(grd, MRb_1a, SMRc_ar, SMRb_ar, MRb_2t, lcl, V0_i)
            minVd_x = Vd_b1(grd, MRb_1t, SMRc_ar, SMRb_ar, MRb_2a, lcl, V0_i)
            maxVd_x = round(maxVd_x, 2)
            minVd_x = round(minVd_x, 2)
            st.markdown(
                rf""" **⁛** Η **μέγιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{max}} \text{{V}}_{{\text{{d}}_\text{{(x)}}}} = {maxVd_x}, \text{{kN}}$$ και η **ελάχιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{min}} \text{{V}}_{{\text{{d}}_\text{{(x)}}}} = {-minVd_x}\, \text{{kN}}$$"""
            )

        elif SMRb_ar <= SMRc_ar and SMRb_de > SMRc_de:
            st.markdown(rf"""
      ▧ Επειδή $$\sum \text{{M}}_{{\text{{Rb,αρ}}}} = {SMRb_ar}\, \text{{kNm}} \leq \sum \text{{M}}_{{\text{{Rc,αρ}}}} = {SMRc_ar}\, \text{{kNm και}} \sum \text{{M}}_{{\text{{Rb,δεξ}}}} = {SMRb_de}\, \text{{kNm}} > \sum \text{{M}}_{{\text{{Rc,δεξ}}}} = {SMRc_de}\, \text{{kNm}}$$""")

            st.write("")

            st.markdown(r"""
      $$\text{max} \text{V}_{\text{d}_\text{(x)}} = \dfrac{ \gamma_{\text{Rd}} \times \left[ \text{M}_{\text{Rb,}_{1}}^{-} + \left( \text{M}_{\text{Rb,}_{2}}^{+} \times \dfrac{\sum \text{M}_{\text{Rc,δεξ}}}{\sum \text{M}_{\text{Rb,δεξ}}} \right) \right] }{\text{L}_{\text{cl}}} + \text{V}_{\text{G} + {\text{ψ}_2}{\text{Q}_o}_\text{(x)}}$$  

      **και**

      $$\text{min} \text{V}_{\text{d}_\text{(x)}} = - \dfrac{ \gamma_{\text{Rd}} \times \left[ \text{M}_{\text{Rb,}_{1}}^{+} + \left( \text{M}_{\text{Rb,}_{2}}^{-} \times \dfrac{\sum \text{M}_{\text{Rc,δεξ}}}{\sum \text{M}_{\text{Rb,δεξ}}} \right) \right] }{\text{L}_{\text{cl}}} + \text{V}_{\text{G} + {\text{ψ}_2}{\text{Q}_o}_\text{(x)}}$$  

      **Άρα:**   
      """)
            maxVd_x = Vd_b2(grd, MRb_1a, MRb_2t, SMRc_de, SMRb_de, lcl, V0_i)
            minVd_x = Vd_b2(grd, MRb_1t, MRb_2a, SMRc_de, SMRb_de, lcl, V0_i)
            maxVd_x = round(maxVd_x, 2)
            minVd_x = round(minVd_x, 2)
            st.markdown(
                rf""" **⁛** Η **μέγιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{max}} \text{{V}}_{{\text{{d}}_\text{{(x)}}}} = {maxVd_x}\, \text{{kN}}$$ και η **ελάχιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{min}} \text{{V}}_{{\text{{d}}_\text{{(x)}}}} = {-minVd_x}\, \text{{kN}}$$"""
            )

        elif SMRb_ar <= SMRc_ar and SMRb_de <= SMRc_de:
            st.markdown(rf"""
      ▧ Επειδή $$\sum{{\text{{M}}}}_{{\text{{Rb,αρ}}}} = {SMRb_ar}\, \text{{kNm}} \leq \sum \text{{M}}_{{\text{{Rc,αρ}}}} = {SMRc_ar}\, \text{{kNm και}} \sum \text{{M}}_{{\text{{Rb,δεξ}}}} = {SMRb_de}\, \text{{kNm}} \leq \sum \text{{M}}_{{\text{{Rc,δεξ}}}} = {SMRc_de}\, \text{{kNm}}$$""")
            st.write("")

            st.markdown(r"""
        $$\text{max} \text{V}_{\text{d}_\text{(x)}} = \gamma_{\text{Rd}} \times \frac{(\text{\text{M}}_{\text{Rb,}_{1}}^{-} + \text{\text{M}}_{\text{Rb,}_{2}}^{+})}{\text{L}_{\text{cl}}} + \text{V}_{\text{G}+{\text{ψ}_2}{\text{Q}_o}_\text{(x)}}$$

        **και**

        $$\text{min} \text{V}_{\text{d}_\text{(x)}} =  \gamma_{\text{Rd}} \times \frac{(\text{M}_{\text{Rb,}_{1}}^{+} + \text{M}_{\text{Rb,}_{2}}^{-})}{\text{L}_{\text{cl}}} + \text{V}_{\text{G}+{\text{ψ}_2}{\text{Q}_o}_\text{(x)}}$$

        **Άρα:**       
      """)
            maxVd_x = Vd_b(grd, MRb_1a, MRb_2t, lcl, V0_i)
            maxVd_x = round(maxVd_x, 2)

            minVd_x = Vd_b(grd, MRb_1t, MRb_2a, lcl, V0_i)
            minVd_x = round(minVd_x, 2)
            st.markdown(
                rf""" **⁛** Η **μέγιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{max}} \text{{V}}_{{\text{{d}}_\text{{(x)}}}} = {maxVd_x}\, \text{{kN}}$$ και η **ελάχιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{min}} \text{{V}}_{{\text{{d}}_\text{{(x)}}}} = {-minVd_x}\, \text{{kN}}$$"""
            )

        st.divider()
        st.subheader("**ΤΕΜΝΟΥΣΕΣ ΚΡΙΣΙΜΩΝ ΠΕΡΙΟΧΩΝ**")
        st.write("▧ Λόγω της παραπάνω ανήσωσης έχουμε:")
        st.info("**Τέμνουσε ροπών:**")
        if SMRb_ar > SMRc_ar and SMRb_de > SMRc_de and fora == 'Θετική':
            DVmax1 = DV(M1dt, M2da, lcl)
            DVmax1 = round(DVmax1, 2)
            st.markdown(rf"""
      **⁛** Για **θετική σεισμική φορά οι τέμνουσες ροπών** θα είναι:
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overrightarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overrightarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} =  {DVmax1}\, \text{{kN}}$$""")
            st.info("**Τέμνουσες σχεδιασμού:**")
            VEdar1 = VEd_t_ar(V0_i, DVmax1)
            VEdar1 = round(VEdar1, 2)
            VEdde1 = VEd_t_de(V0_i, DVmax1)
            VEdde1 = round(VEdde1, 2)
            st.markdown(rf"""
      **⁛** Για το **αριστερό άκρο οι τέμνουσες σχεδιασμού** θα είναι:
      $$\text{{V}}_{{\text{{Ed,αρ}}}} = \text{{V}}_{{\text{{0,i}}}} + \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdar1}\, \text{{kN}}$$ και για το **δεξιό άκρο** θα είναι: $$\text{{V}}_{{\text{{Ed,δεξ}}}} = - \text{{V}}_{{\text{{0,i}}}} + \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdde1}\, \text{{kN}}$$
      """)

        elif SMRb_ar > SMRc_ar and SMRb_de > SMRc_de and fora == 'Αρνητική':
            DVmin1 = DV(M1da, M2dt, lcl)
            DVmin1 = round(DVmin1, 2)
            st.markdown(rf"""
      **⁛** Για **αρνητική σεισμική φορά οι τέμνουσες ροπών** θα είναι:
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overleftarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overleftarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {-DVmin1}\, \text{{kN}}$$
      """)
            st.info("**Τέμνουσες σχεδιασμού:**")
            VEdar1 = VEd_a_ar(V0_i, DVmin1)
            VEdar1 = round(VEdar1, 2)
            VEdde1 = VEd_a_de(V0_i, DVmin1)
            VEdde1 = round(VEdde1, 2)
            st.markdown(rf"""
      **⁛** Για το **αριστερό άκρο οι τέμνουσες ροπών** θα είναι:
         $$\text{{V}}_{{\text{{Ed,αρ}}}} = \text{{V}}_{{\text{{0,i}}}} - \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdar1}\, \text{{kN}}$$ και για το **δεξιό άκρο** θα είναι: $$\text{{V}}_{{\text{{Ed,δεξ}}}} =  - \text{{V}}_{{\text{{0,i}}}} - \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdde1}\, \text{{kN}}$$
      """)
            
        elif SMRb_ar > SMRc_ar and SMRb_de <= SMRc_de and fora == 'Θετική':
            DVmax2 = DV(M1dt, M2daa, lcl)
            DVmax2 = round(DVmax2, 2)
            st.markdown(rf"""
      **⁛** Για **θετική σεισμική φορά οι τέμνουσες ροπών** θα είναι:
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overrightarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overrightarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {DVmax2}\, \text{{kN}}$$""")

            st.info("**Τέμνουσες σχεδιασμού:**")
            VEdar2 = VEd_t_ar(V0_i, DVmax2)
            VEdar2 = round(VEdar2, 2)
            VEdde2 = VEd_t_de(V0_i, DVmax2)
            VEdde2 = round(VEdde2, 2)
            st.markdown(rf"""
      **⁛** Για το **αριστερό άκρο οι τέμνουσες σχεδιασμού** θα είναι:
      $$\text{{V}}_{{\text{{Ed,αρ}}}} =  \text{{V}}_{{\text{{0,i}}}} - \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdar2}\, \text{{kN}}$$ και για το **δεξιό άκρο** θα είναι: $$\text{{V}}_{{\text{{Ed,δεξ}}}} = - \text{{V}}_{{\text{{0,i}}}} + \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdde2}\, \text{{kN}}$$
      """)

        elif SMRb_ar > SMRc_ar and SMRb_de <= SMRc_de and fora == 'Αρνητική':
            DVmin2 = DV(M1da, M2dtt, lcl)
            DVmin2 = round(DVmin2, 2)
            st.markdown(rf"""
      **⁛** Για **αρνητική σεισμική φορά οι τέμνουσες ροπών** θα είναι:
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overleftarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overleftarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {-DVmin2}\, \text{{kN}}$$
      """)

            st.info("**Τέμνουσες σχεδιασμού:**")
            VEdar2 = VEd_a_ar(V0_i, DVmin2)
            VEdar2 = round(VEdar2, 2)
            VEdde2 = VEd_a_de(V0_i, DVmin2)
            VEdde2 = round(VEdde2, 2)
            st.markdown(rf"""
      **⁛** Για το **αριστερό άκρο οι τέμνουσες σχεδιασμού** θα είναι:
      $$\text{{V}}_{{\text{{Ed,αρ}}}} = - \text{{V}}_{{\text{{0,i}}}} - \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdar2}\, \text{{kN}}$$ και για το **δεξιό άκρο** θα είναι: $$\text{{V}}_{{\text{{Ed,δεξ}}}} = - \text{{V}}_{{\text{{0,i}}}} - \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdde2}\, \text{{kN}}$$
      """)

        elif SMRb_ar <= SMRc_ar and SMRb_de > SMRc_de and fora == 'Θετική':
            DVmax3 = DV(M1dtt, M2da, lcl)
            DVmax3 = round(DVmax3, 2)
            st.markdown(rf"""
      **⁛** Για **θετική σεισμική φορά οι τέμνουσες ροπών** θα είναι:
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overrightarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overrightarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {DVmax3}\, \text{{kN}}$$""")

            st.info("**Τέμνουσες σχεδιασμού:**")
            VEdar3 = VEd_t_ar(V0_i, DVmax3)
            VEdar3 = round(VEdar3, 2)
            VEdde3 = VEd_t_de(V0_i, DVmax3)
            VEdde3 = round(VEdde3, 2)
            st.markdown(rf"""
      **⁛** Για το **αριστερό άκρο οι τέμνουσες σχεδιασμού** θα είναι:
      $$\text{{V}}_{{\text{{Ed,αρ}}}} =  \text{{V}}_{{\text{{0,i}}}} + \Delta \text{{V}}_{{\text{{Ed,max,i}}}} = {VEdar3}\, \text{{kN}}$$ και για το **δεξιό άκρο** θα είναι: $$\text{{V}}_{{\text{{Ed,δεξ}}}} = - \text{{V}}_{{\text{{0,i}}}} + \Delta \text{{V}}_{{\text{{Ed,max,i}}}} = {VEdde3}\, \text{{kN}}$$
      """)
      
        elif SMRb_ar <= SMRc_ar and SMRb_de > SMRc_de and fora == 'Αρνητική':
            DVmin3 = DV(M1daa, M2dt, lcl)
            DVmin3 = round(DVmin3, 2)
            st.markdown(rf"""
      **⁛** Για **αρνητική σεισμική φορά οι τέμνουσες ροπών** θα είναι:
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overleftarrow{{\text{{M}}}}_{{\text{{1,d}}}} +   \overleftarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {-DVmin3}\, \text{{kN}}$$
    """)
            st.info("**Τέμνουσες σχεδιασμού:**")
            VEdar3 = VEd_a_ar(V0_i, DVmin3)
            VEdar3 = round(VEdar3, 2)
            VEdde3 = VEd_a_de(V0_i, DVmin3)
            VEdde3 = round(VEdde3, 2)
            st.markdown(rf"""
      **⁛** Για το **αριστερό άκρο οι τέμνουσες σχεδιασμού** θα είναι:
      $$\text{{V}}_{{\text{{Ed,αρ}}}} = \text{{V}}_{{\text{{0,i}}}} - \Delta \text{{V}}_{{\text{{Ed,min,i}}}} = {VEdar3}\, \text{{kN}}$$ και για το **δεξιό άκρο** θα είναι: $$\text{{V}}_{{\text{{Ed,δεξ}}}} =  - \text{{V}}_{{\text{{0,i}}}} - \Delta \text{{V}}_{{\text{{Ed,min,i}}}} = {VEdde3}\, \text{{kN}}$$
      """)

        elif SMRb_ar <= SMRc_ar and SMRb_de <= SMRc_de and fora =='Θετική':
            DVmax4 = DV(M1dtt, M2daa, lcl)
            DVmax4 = round(DVmax4, 2)
            st.markdown(rf"""
        **⁛** Για **θετική σεισμική φορά οι τέμνουσες ροπών** θα είναι:
        $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overrightarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overrightarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {DVmax4}\, \text{{kN}}$$""")
            
            st.info("**Τέμνουσες σχεδιασμού:**")
            VEdar4 = VEd_t_ar(V0_i, DVmax4)
            VEdar4 = round(VEdar4, 2)
            VEdde4 = VEd_t_de(V0_i, DVmax4)
            VEdde4 = round(VEdde4, 2)
            st.markdown(rf"""
      **⁛** Για το **αριστερό άκρο οι τέμνουσες σχεδιασμού** θα είναι:
      $$\text{{V}}_{{\text{{Ed,αρ}}}} = \text{{V}}_{{\text{{0,i}}}} + \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdar4}\, \text{{kN}}$$ και για το **δεξιό άκρο** θα είναι: $$\text{{V}}_{{\text{{Ed,δεξ}}}} = - \text{{V}}_{{\text{{0,i}}}} + \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdde4}\, \text{{kN}}$$
      """)

        elif SMRb_ar <= SMRc_ar and SMRb_de <= SMRc_de and fora =='Αρνητική':
            DVmin4 = DV(M1daa, M2dtt, lcl)
            DVmin4 = round(DVmin4, 2)
            st.markdown(rf"""
        **⁛** Για **αρνητική σεισμική φορά οι τέμνουσες ροπών** θα είναι:
        $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overleftarrow{{\text{{M}}}}_{{\text{{1,d}}}} +   \overleftarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {-DVmin4}\, \text{{kN}}$$
      """)
            st.info("**Τέμνουσες σχεδιασμού:**")
            VEdar4 = VEd_a_ar(V0_i, DVmin4)
            VEdar4 = round(VEdar4, 2)
            VEdde4 = VEd_a_de(V0_i, DVmin4)
            VEdde4 = round(VEdde4, 2)
            st.markdown(rf"""
      **⁛** Για το **αριστερό άκρο οι τέμνουσες σχεδιασμού** θα είναι:
      $$\text{{V}}_{{\text{{Ed,αρ}}}} = \text{{V}}_{{\text{{0,i}}}} - \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdar4}\, \text{{kN}}$$ και για το **δεξιό άκρο** θα είναι: $$\text{{V}}_{{\text{{Ed,δεξ}}}} = - \text{{V}}_{{\text{{0,i}}}} - \Delta \text{{V}}_{{\text{{Ed,i}}}} = {VEdde4}\, \text{{kN}}$$
      """)

    # TAMPLO - ypostyloma
    else:
        katask = st.selectbox("Τι κατηγορία πλαστιμότητας έχουμε;", ("ΚΠΜ", "ΚΠΥ"))
        if katask == "ΚΠΜ":
            grd = 1.1
            st.write("Ο συντελεστής $γ_{Rd}$ είναι:", grd)
        else:
            grd = 1.3
            st.write("Ο συντελεστής $γ_{Rd}$ είναι:", grd)

        with st.expander("**Τα αριθμητικά δεδομένα σας**"):
            st.info("**Δεδομένα υποστυλώματος**")
            lcl = st.number_input("**Μήκος δοκού:** $l_{cl}$", value=5.5, step=0.1, format="%.1f")
            col1, col2_3, col4 = st.columns([1, 2, 1])
            with col1:
                an_upost = st.checkbox("Άνω υποστύλωμα")
                if an_upost:
                    st.error("**Ροπές αντοχής άνω υποστυλώματος:**")
                    MRc1o_a = st.number_input(
                        "**Αρνητική** ροπή αντοχής $MRc,1_{over}^-$:", value=-10.0, step=0.1, format="%.1f"
                    )
                    MRc1o_t = st.number_input(
                        "**Θετική** ροπή αντοχής $MRc,1_{over}^+$:", value=10.0, step=0.1, format="%.1f"
                    )
                else:
                    st.write("")
                an_dokos = st.checkbox("Άνω δοκός", value=True)
                if an_dokos:
                    st.divider()
                    st.info("**Ροπές αντοχής δοκών:**")
                    andokos_de = st.checkbox("Δεξιά", value=True)
                    if andokos_de:
                      st.error("**Δεξιά:**")
                      MRb_1a = st.number_input(
                          "**Αρνητική** ροπή αντοχής: $MRb,1^-$:", value=-250.0, step=0.1, format="%.1f"
                      )
                      MRb_1t = st.number_input(
                          "**Θετική** ροπή αντοχής: $MRb,1^+$:", value=500.0, step=0.1, format="%.1f"
                      )
                    else:
                        st.write("")
                    andokos_ar = st.checkbox("Αριστερά")
                    if andokos_ar:
                      st.error("**Αριστερά:**")
                      MRb_2a = st.number_input(
                          "**Αρνητική** ροπή αντοχής: $MRb,2^-$:", value=-300.0, step=0.1, format="%.1f"
                      )
                      MRb_2t = st.number_input(
                          "**Θετική** ροπή αντοχής: $MRb,2^+$:", value=600.0, step=0.1, format="%.1f"
                      )
                    else:
                        st.write("")
                else:
                    st.write("")

            with col2_3:
                st.info("**Ροπές αντοχής υποστυλώματος:**")
                col1, col2 = st.columns(2)
                with col1:
                    st.success("**Άνω:**")
                    MRc_1a = st.number_input(
                        "**Αρνητική** ροπή αντοχής $MRc,1^-$:", value=-250.0, step=0.1, format="%.1f"
                    )
                    MRc_1t = st.number_input(
                        "**Θετική** ροπή αντοχής $MRc,1^+$:", value=500.0, step=0.1, format="%.1f"
                    )
                with col2:
                    st.success("**Κάτω:**")
                    MRc_2a = st.number_input(
                        "**Αρνητική** ροπή αντοχής $MRc,2^-$:", value=-300.0, step=0.1, format="%.1f"
                    )
                    MRc_2t = st.number_input(
                        "**Θετική** ροπή αντοχής $MRc,2^+$:", value=600.0, step=0.1, format="%.1f"
                    )

            with col4:
                kat_upost = st.checkbox("Κάτω υποστύλωμα")
                if kat_upost:
                    st.error("**Ροπές αντοχής κάτω υποστυλώματος:**")
                    MRc2u_a = st.number_input(
                        "**Αρνητική** ροπή αντοχής $MRc,2_{under}^-$:", value=-100.0, step=0.1, format="%.1f"
                    )
                    MRc2u_t = st.number_input(
                        "**Θετική** ροπή αντοχής $MRc,2_{under}^+$:", value=200.0, step=0.1, format="%.1f"
                    )
                else:
                    st.write("")
                kat_dokos = st.checkbox("Κάτω δοκός")
                if kat_dokos:
                    st.divider()
                    st.info("**Ροπές αντοχής δοκών:**")
                    kdokos_de = st.checkbox("Δεξιά:")
                    if kdokos_de:
                      st.error("**Δεξιά:**")
                      MRb_3a = st.number_input(
                          "**Αρνητική** ροπή αντοχής: $MRb,3^-$:", value=-100.0, step=0.1, format="%.1f"
                      )
                      MRb_3t = st.number_input(
                          "**Θετική** ροπή αντοχής: $MRb,3^+$:", value=200.0, step=0.1, format="%.1f"
                      )
                    else: st.write("")
                    katdokos_ar = st.checkbox("Αριστερά:")
                    if katdokos_ar:
                      st.error("**Αριστερά:**")
                      MRb_4a = st.number_input(
                          "**Αρνητική** ροπή αντοχής: $MRb,4^-$:", value=-50.0, step=0.1, format="%.1f"
                      )
                      MRb_4t = st.number_input(
                          "**Θετική** ροπή αντοχής: $MRb,4^+$:", value=100.0, step=0.1, format="%.1f"
                      )
                    else:
                        st.write("")
                else:
                    st.write("")

        st.write("")
        ipostil_url = "images/ipostil.jpg"
        col1, col2, col3 = st.columns([1, 1, 5])
        with col3:
          st.image(ipostil_url, caption="Ευρωκώδικας 8", width=380)

        st.divider()
        fora = st.selectbox("Επιλέξτε σεισμική φορά ανάλυσης:", ("Θετική", "Αρνητική"))

        MRc1o_a = MRc1o_a if "MRc1o_a" in locals() else 0
        MRc1o_t = MRc1o_t if "MRc1o_t" in locals() else 0
        MRb_1a = MRb_1a if "MRb_1a" in locals() else 0
        MRb_1t = MRb_1t if "MRb_1t" in locals() else 0
        MRb_2a = MRb_2a if "MRb_2a" in locals() else 0
        MRb_2t = MRb_2t if "MRb_2t" in locals() else 0
        MRc2u_a = MRc2u_a if "MRc2u_a" in locals() else 0
        MRc2u_t = MRc2u_t if "MRc2u_t" in locals() else 0
        MRb_3a = MRb_3a if "MRb_3a" in locals() else 0
        MRb_3t = MRb_3t if "MRb_3t" in locals() else 0
        MRb_4a = MRb_4a if "MRb_4a" in locals() else 0
        MRb_4t = MRb_4t if "MRb_4t" in locals() else 0

        if an_upost:
            MRc1o_a = MRc1o_a 
            MRc1o_t = MRc1o_t 
        elif kat_upost:
            MRc2u_a = MRc2u_a 
            MRc2u_t = MRc2u_t 
        else:
            MRc1o_a = 0
            MRc1o_t = 0
            MRc2u_a = 0
            MRc2u_t = 0

        if fora == "Θετική":
            SMRb_a = SMRb_a_t(MRb_2a, MRb_1t)
            SMRb_a = round(SMRb_a, 2)
            SMRc_a = SMRc_a_t(MRc_1t, MRc1o_a)
            SMRc_a = round(SMRc_a, 2)
            SMRb_k = SMRb_k_t(MRb_3t, MRb_4a)
            SMRb_k = round(SMRb_k, 2)
            SMRc_k = SMRc_k_t(MRc_2a, MRc2u_t)
            SMRc_k = round(SMRc_k,2)
        else:
            SMRb_a = SMRb_a_a(MRb_2t, MRb_1a)
            SMRb_a = round(SMRb_a,2)
            SMRc_a = SMRc_a_a(MRc_1a, MRc1o_t)
            SMRc_a = round(SMRc_a,2)
            SMRb_k = SMRb_k_a(MRb_3a, MRb_4t)
            SMRb_k = round(SMRb_k,2)
            SMRc_k = SMRc_k_a(MRc_2t, MRc2u_a)
            SMRc_k = round(SMRc_k,2)

        st.subheader("**ΡΟΠΕΣ**")
        bubble_style = """
        background-color: #FFC0CB;
        border-radius: 20px;
        padding: 10px;
        box-shadow: 2px 2px 5px grey;
        max-width: 365px;
    """
        st.write(
            '<div style="{}">Οι ροπές των άκρων υπολογίζονται από τον τύπο:</div>'.format(
                bubble_style
            ),
            unsafe_allow_html=True,
        )

        st.write("")
        st.markdown(r"""
      $$\text{{M}}_{\text{i,c}} = \gamma_{\text{Rd}} \text{{M}}_{\text{Rc,i}} \min\left(1, \dfrac{\sum \text{{M}}_{\text{Rb}}}{\sum \text{{M}}_{\text{Rc}}}\right)$$
          """)

        st.write("")
        tab1, tab2 = st.tabs(["Άνω", "Κάτω"])
        with tab1:
            if SMRb_a < SMRc_a:
                st.markdown(rf"""
        ▧ Επειδή: $$\sum \text{{M}}_{{\text{{Rb,άνω}}}} = {SMRb_a}\, \text{{kNm}} < \sum \text{{M}}_{{\text{{Rc,άνω}}}} = {SMRc_a}\, \text{{kNm}}$$ ο τύπος θα πάρει την μορφή
        
        **⇒** $$\text{{M}}_{{\text{{i,d}}}} = \gamma_{{\text{{Rd}}}} \text{{M}}_{{\text{{Rc,i}}}} \dfrac{{\sum \text{{M}}_{{\text{{Rb,άνω}}}}}}{{\sum \text{{M}}_{{\text{{Rc,άνω}}}}}}$$
        """)
                if fora == 'Θετική':
                  col1, col2 = st.columns([1,8])
                  with col2:
                     ipostil_a_th_url = "images/ipostil_ano_thetiko.jpg"
                     st.image(ipostil_a_th_url, caption="Φορά των ροπών που συντρέχουν στο άνω άκρο του υποστυλώματος για θετική σεισμική φορά.", width=440)
                  M1dt = Mid_bu(grd, MRc_1t, SMRb_a, SMRc_a)
                  M1dt = round(M1dt, 2)
                  st.markdown(
                    rf""" Έτσι η ροπή στο **άνω άκρο για θετική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{1,d}}}}^+ = {M1dt}\, \text{{kNm}}$$""")
                else:
                  col1,col2 = st.columns([1,9])
                  with col2:
                     ipostil_a_ar_url = "images/ipostil_ano_arnitiko.jpg"
                     st.image(ipostil_a_ar_url, caption="Φορά των ροπών που συντρέχουν στο άνω άκρο του υποστυλώματος για αρνητική σεισμική φορά.", width=440)
                  M1da = Mid_bu(grd, MRc_1a, SMRb_a, SMRc_a)
                  M1da = round(M1da, 2)
                  st.markdown(
                    rf""" Έτσι η ροπή στο **άνω άκρο για αρνητική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{1,d}}}}^- = {M1da}\, \text{{kNm}}$$"""
                )
            elif SMRb_a >= SMRc_a:
                st.markdown(rf"""
        ▧ Επειδή: $$\sum \text{{M}}_{{\text{{Rb,άνω}}}} = {SMRb_a}\, \text{{kNm}} \geq \sum \text{{M}}_{{\text{{Rc,άνω}}}} = {SMRc_a}\, \text{{kNm}}$$ ο τύπος θα πάρει την μορφή
        
        **⇒** $$\text{{M}}_{{\text{{i,d}}}} = \gamma_{{\text{{Rd}}}} \text{{M}}_{{\text{{Rc,i}}}}$$  
        """)
                if fora == 'Θετική':
                  col1, col2 = st.columns([1,8])
                  with col2:
                     ipostil_a_th_url = "images/ipostil_ano_thetiko.jpg"
                     st.image(ipostil_a_th_url, caption="Φορά των ροπών που συντρέχουν στο άνω άκρο του υποστυλώματος για θετική σεισμική φορά.", width=440)
                  M1dtt = Mid_s(grd, MRc_1t)
                  M1dtt = round(M1dtt, 2)
                  st.markdown(
                    rf""" Έτσι η ροπή στο **άνω άκρο για θετική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{1,d}}}}^+ = {M1dtt}\, \text{{kNm}}$$""")
                else:
                  col1,col2 = st.columns([1,9])
                  with col2:
                     ipostil_a_ar_url = "images/ipostil_ano_arnitiko.jpg"
                     st.image(ipostil_a_ar_url, caption="Φορά των ροπών που συντρέχουν στο άνω άκρο του υποστυλώματος για αρνητική σεισμική φορά.", width=440)
                  M1daa = Mid_s(grd, MRc_1a)
                  M1daa = round(M1daa, 2)
                  st.markdown(
                    rf""" Έτσι η ροπή στο **άνω άκρο για αρνητική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{1,d}}}}^- = {M1daa}\, \text{{kNm}}$$"""
                )
        with tab2:
            if SMRb_k < SMRc_k:
                st.markdown(rf""" 
        ▧ Επειδή: $$\sum \text{{M}}_{{\text{{Rb,κάτω}}}} = {SMRb_k}\, \text{{kNm}} < \sum \text{{M}}_{{\text{{Rc,κάτω}}}} = {SMRc_k}\, \text{{kNm}}$$ ο τύπος θα πάρει την μορφή
        
        **⇒** $$\text{{M}}_{{\text{{i,d}}}} = \gamma_{{\text{{Rd}}}} \text{{M}}_{{\text{{Rc,i}}}} \dfrac{{\sum \text{{M}}_{{\text{{Rb,κάτω}}}}}}{{\sum \text{{M}}_{{\text{{Rc,κάτω}}}}}}$$
    """)
                if fora == 'Θετική':
                  col1, col2 = st.columns([1,10])
                  with col2:
                     ipostil_k_th_url = "images/ipostil_kato_thetiko.jpg"
                     st.image(ipostil_k_th_url, caption="Φορά των ροπών που συντρέχουν στο κάτω άκρο του υποστυλώματος για θετική σεισμική φορά.", width=440)
                  M2da = Mid_bu(grd, MRc_2a, SMRb_k, SMRc_k)
                  M2da = round(M2da, 2)
                  st.markdown(
                    rf""" Έτσι η ροπή στο **κάτω άκρο για θετική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{2,d}}}}^- = {M2da}\, \text{{kNm}}$$""")
                else:
                  col1,col2 = st.columns([1,10])
                  with col2:
                     ipostil_k_ar_url = "images/ipostil_kato_arnitiko.jpg"
                     st.image(ipostil_k_ar_url, caption="Φορά των ροπών που συντρέχουν στο κάτω άκρο του υποστυλώματος για αρνητική σεισμική φορά.", width=440)
                  M2dt = Mid_bu(grd, MRc_2t, SMRb_k, SMRc_k)
                  M2dt = round(M2dt, 2)
                  st.markdown(
                    rf""" Έτσι η ροπή στο **κάτω άκρο για αρνητική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{2,d}}}}^+ = {M2dt}\, \text{{kNm}}$$"""
                )
            elif SMRb_k >= SMRc_k:
                st.markdown(rf""" 
        ▧ Επειδή: $$\sum \text{{M}}_{{\text{{Rb,κάτω}}}} = {SMRb_k}\, \text{{kNm}} \geq \sum \text{{M}}_{{\text{{Rc,κάτω}}}} = {SMRc_k}\, \text{{kNm}}$$ ο τύπος θα πάρει την μορφή 
        
        **⇒** $$\text{{M}}_{{\text{{i,d}}}} = \gamma_{{\text{{Rd}}}} \text{{M}}_{{\text{{Rc,i}}}}$$
        """)
                if fora == 'Θετική':
                  col1, col2 = st.columns([1,10])
                  with col2:
                     upost_thetiki_kato_url = "images/upost_thetiki_kato.jpg"
                     st.image(upost_thetiki_kato_url, caption="Φορά των ροπών που συντρέχουν στο κάτω άκρο του υποστυλώματος για θετική σεισμική φορά.", width=550)
                  M2daa = Mid_s(grd, MRc_2a)
                  M2daa = round(M2daa, 2)
                  st.markdown(
                    rf""" Έτσι η ροπή στο **άνω άκρο για θετική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{2,d}}}}^- = {M2daa}\, \text{{kNm}}$$""")
                else:
                  col1,col2 = st.columns([1,10])
                  with col2:
                     upost_arnitiko_kato_url = "images/upost_arnitiko_kato.jpg"
                     st.image(upost_arnitiko_kato_url, caption="Φορά των ροπών που συντρέχουν στο κάτω άκρο του υποστυλώματος για αρνητική σεισμική φορά.", width=550)
                  M2dtt = Mid_s(grd, MRc_2t)
                  M2dtt = round(M2dtt, 2)
                  st.markdown(
                    rf""" Έτσι η ροπή στο **άνω άκρο για αρνητική σεισμική φορά** θα είναι: $$\text{{M}}_{{\text{{2,d}}}}^+ = {M2dtt}\, \text{{kNm}}$$"""
                )

        st.divider()
        st.subheader("**ΤΕΜΝΟΥΣΕΣ**")
        bubble_style = """
      background-color: #FFC0CB;
      border-radius: 20px;
      padding: 10px;
      box-shadow: 2px 2px 5px grey;
      max-width: 690px;
      """
        st.write(
            '<div style="{}">Η γενική μορφή των σχέσεων υπολογισμού των τεμνουσών σχεδιασμού των υποστυλωμάτων είναι:</div>'.format(
                bubble_style
            ),
            unsafe_allow_html=True,
        )
        st.write("")
        st.write("")

        st.markdown(r"""
      $$\text{max } \text{V}_{\text{d}_\text{(y)}} =  \dfrac{\gamma_{\text{Rd}} \times \left[\text{M}_{\text{Rc,}_{1}}^+ \times \min \left(1, \left(\frac{\sum \text{M}_{\text{Rb,άνω}}}{\sum \text{{M}}_{\text{Rc,άνω}}}\right)_1\right) + \text{{M}}_{\text{Rc,}_{2}}^- \times \min \left(1, \left(\frac{\sum \text{{M}}_{\text{Rb,κάτω}}}{\sum \text{M}_{\text{Rc,κάτω}}}\right)_2\right)\right]}{\text{L}_{\text{cl}}}$$

        """)
        st.write("")
        st.markdown(r"""
     $$\text{min } \text{V}_{\text{d}_\text{(y)}} =  \dfrac{\gamma_{\text{Rd}} \times \left[\text{M}_{\text{Rc,}_{1}}^- \times \min \left(1, \left(\frac{\sum \text{M}_{\text{Rb,άνω}}}{\sum \text{M}_{\text{Rc,άνω}}}\right)_1\right) + \text{M}_{\text{Rc,}_{2}}^+ \times \min \left(1, \left(\frac{\sum \text{M}_{\text{Rb,κάτω}}}{\sum \text{M}_{\text{Rc,κάτω}}}\right)_2\right)\right]}{\text{L}_{\text{cl}}}$$""")

        st.markdown(
            """ <style>.dashed-line {
    border-top: 7px dashed #555;
    margin-top: 10px;
    margin-bottom: 10px;
    border-width: 2px;}</style><div class="dashed-line"></div>""",
            unsafe_allow_html=True,
        )
        st.write("")

        if SMRb_a >= SMRc_a and SMRb_k >= SMRc_k:
            st.markdown(rf"""
      ▧ Επειδή $$\sum \text{{M}}_{{\text{{Rb,άνω}}}} = {SMRb_a}\, \text{{kNm}} \geq \sum \text{{M}}_{{\text{{Rc,άνω}}}} = {SMRc_a}\, \text{{kNm}}$$ και $$\sum \text{{M}}_{{\text{{Rb,κάτω}}}} = {SMRb_k}\, \text{{kNm}} \geq \sum \text{{M}}_{{\text{{Rc,κάτω}}}} = {SMRc_k}\, \text{{kNm}}$$""")
            st.write("")

            st.markdown(r"""
      $$\text{max} \text{V}_{\text{d}_\text{(y)}} = \gamma_{\text{\text{Rd}}} \times \dfrac{( \text{M}_{\text{Rc,}_{1}}^{+} + \text{M}_{\text{Rc,}_{2}}^{-} )}{\text{L}_{\text{cl}}}$$

      **και**

      $$\text{min} \text{V}_{\text{d}_\text{(y)}} = \gamma_{\text{Rd}} \times \dfrac{( \text{M}_{\text{Rc,}_{1}}^{-} + \text{M}_{\text{Rc,}_{2}}^{+} )}{\text{L}_{\text{cl}}}$$

      **Άρα:**
      """)
            maxVd_y = Vd_c(grd, MRc_1t, MRc_2a, lcl)
            maxVd_y = round(maxVd_y, 2)
            minVd_y = Vd_c(grd, MRc_1a, MRc_2t, lcl)
            minVd_y = round(minVd_y, 2)

            st.markdown(rf""" 
      **⁛** Η **μέγιστη τέμνουσα σχεδιασμού του υπσοτυλώματος** θα είναι: $$\text{{max}} \text{{V}}_{{\text{{d}}_\text{{(y)}}}} = {maxVd_y}\, \text{{kN}}$$ και η **ελάχιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{min}} \text{{V}}_{{\text{{d}}_\text{{(y)}}}} = {- minVd_y}\, \text{{kN}}$$""")

        elif SMRb_a < SMRc_a and SMRb_k < SMRc_k:
            st.markdown(rf"""
      ▧ Επειδή $$\sum \text{{M}}_{{\text{{Rb,άνω}}}} = {SMRb_a}\, \text{{kNm}} < \sum \text{{M}}_{{\text{{Rc,άνω}}}} = {SMRc_a}\, \text{{kNm}}$$ και $$\sum \text{{M}}_{{\text{{Rb,κάτω}}}} = {SMRb_k}\, \text{{kNm}} < \sum \text{{M}}_{{\text{{Rc,κάτω}}}} = {SMRc_k}\, \text{{kNm}}$$
      """)
            st.write("")

            st.markdown(r"""
      $$\text{maxV}_{\text{d}_\text{(y)}} = \dfrac{\gamma_{\text{Rd}} \times \left( \text{M}_{\text{Rc,}_{1}}^+ \times \dfrac{\sum \text{M}_{\text{Rb,άνω}}}{\sum \text{M}_{\text{Rc,άνω}}} \right) + \left( \text{M}_{\text{Rc,}_{2}}^- \times \dfrac{\sum \text{M}_{\text{Rb,κάτω}}}{\sum \text{M}_{\text{Rc,κάτω}}} \right)}{\text{L}_{\text{cl}}}$$

      **και**

      $$\text{minV}_{\text{d}_\text{(y)}} = \dfrac{\gamma_{\text{Rd}} \times \left( \text{M}_{\text{Rc,}_{1}}^{-} \times \dfrac{\sum \text{M}_{\text{Rb,άνω}}}{\sum \text{M}_{\text{Rc,άνω}}} \right) + \left( \text{M}_{\text{Rc,}_{2}}^{+} \times \dfrac{\sum \text{M}_{\text{Rb,κάτω}}}{\sum \text{M}_{\text{Rc,κάτω}}} \right)}{\text{L}_{\text{cl}}}$$

      **Άρα:**
      """)
            
            maxVd_y = Vd_C(grd, MRc_1t, MRc_2a, SMRc_a, SMRb_a, SMRc_k, SMRb_k, lcl)
            maxVd_y = round(maxVd_y, 2)
            minVd_y = Vd_C(grd, MRc_1a, MRc_2t, SMRc_a, SMRb_a, SMRc_k, SMRb_k, lcl)
            minVd_y = round(minVd_y, 2)


            st.markdown(rf"""
      **⁛** Η **μέγιστη τέμνουσα σχεδιασμού του υπσοτυλώματος** θα είναι: $$\text{{max}} \text{{V}}_{{\text{{d}}_\text{{(y)}}}} = {maxVd_y}\, \text{{kN}}$$ και η **ελάχιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{min}} \text{{V}}_{{\text{{d}}_\text{{(y)}}}} = {minVd_y}\, \text{{kN}}$$""")

        elif SMRb_a < SMRc_a and SMRb_k >= SMRc_k:
            st.markdown(rf"""
      ▧ Επειδή $$\sum \text{{M}}_{{\text{{Rb,άνω}}}} = {SMRb_a}\, \text{{kNm}} < \sum \text{{M}}_{{\text{{Rc,άνω}}}} = {SMRc_a}\, \text{{kNm}}$$ και $$\sum \text{{M}}_{{\text{{Rb,κάτω}}}} = {SMRb_k}\, \text{{kNm}} \geq \sum \text{{M}}_{{\text{{Rc,κάτω}}}} = {SMRc_k}\, \text{{kNm}}$$
      """)
            st.write("")

            st.markdown(r"""
      $$\text{maxV}_{\text{d}_\text{(y)}} = \dfrac{\gamma_{\text{Rd}} \times \left( (\text{M}_{\text{Rc,}_{1}}^{+} \times \dfrac{\sum \text{M}_{\text{Rb,άνω}}}{\sum \text{M}_{\text{Rc,άνω}}}) + \text{M}_{\text{Rc,}_{2}}^- \right)}{\text{L}_{\text{cl}}}$$

      **και**

      $$\text{minV}_{\text{d}_\text{(y)}} = \dfrac{\gamma_{\text{Rd}} \times \left( (\text{M}_{\text{Rc,}_{1}}^- \times \dfrac{\sum \text{M}_{\text{Rb,άνω}}}{\sum \text{M}_{\text{Rc,άνω}}}) + \text{M}_{\text{Rc,}_{2}}^+ \right)}{\text{L}_{\text{cl}}}$$

      **Άρα:**
      """)
            maxVd_y = Vd_c1(grd, MRc_1t, MRc_2a, SMRb_a, SMRc_a, lcl)
            maxVd_y = round(maxVd_y, 2)
            minVd_y = Vd_c1(grd, MRc_1a, MRc_2t, SMRb_a, SMRc_a, lcl)
            minVd_y = round(minVd_y, 2)
            st.markdown(rf"""
      **⁛** Η **μέγιστη τέμνουσα σχεδιασμού του υπσοτυλώματος** θα είναι: $$\text{{max}} \text{{V}}_{{\text{{d}}_\text{{(y)}}}} = {maxVd_y}\, \text{{kN}}$$ και η **ελάχιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{min}} \text{{V}}_{{\text{{d}}_\text{{(y)}}}} = {minVd_y}\, \text{{kN}}$$""")

        elif SMRb_a >= SMRc_a and SMRb_k < SMRc_k:
            st.markdown(rf"""
      ▧ Επειδή $$\sum \text{{M}}_{{\text{{Rb,άνω}}}} = {SMRb_a}\, \text{{kNm}} \geq \sum \text{{M}}_{{\text{{Rc,άνω}}}} = {SMRc_a}\, \text{{kNm}}$$ και $$\sum \text{{M}}_{{\text{{Rb,κάτω}}}} = {SMRb_k}\, \text{{kNm}} < \sum \text{{M}}_{{\text{{Rc,κάτω}}}} = {SMRc_k}\, \text{{kNm}}$$
      """)
            st.write("")

            st.markdown(r"""
      $$\text{max} \text{V}_{\text{d}_\text{(y)}} = \dfrac{\gamma_{\text{Rd}} \times \left( \text{M}_{\text{Rc,}_{1}}^+ + ( \text{M}_{\text{Rc,}_{2}}^- \times \dfrac{\sum \text{M}_{\text{Rb,κάτω}}}{\sum \text{M}_{\text{Rc,κάτω}}}) \right)}{\text{L}_{\text{cl}}}$$

      **και**

      $$\text{min} \text{V}_{\text{d}_\text{(y)}} = \dfrac{\gamma_{\text{Rd}} \times \left( \text{M}_{\text{Rc,}_{1}}^- + (\text{M}_{\text{Rc,}_{2}}^+ \times \dfrac{\sum \text{M}_{\text{Rb,κάτω}}}{\sum \text{M}_{\text{Rc,κάτω}}}) \right)}{\text{L}_{\text{cl}}}$$

      **Άρα:**     
      """)
            maxVd_y = Vd_c2(grd, MRc_1t, MRc_2a, SMRb_k, SMRc_k, lcl)
            maxVd_y = round(maxVd_y, 2)
            minVd_y = Vd_c2(grd, MRc_1a, MRc_2t, SMRb_k, SMRc_k, lcl)
            minVd_y = round(minVd_y, 2)
            st.markdown(rf"""
      **⁛** Η **μέγιστη τέμνουσα σχεδιασμού του υπσοτυλώματος** θα είναι: $$\text{{max}} \text{{V}}_{{\text{{d}}_\text{{(y)}}}} = {maxVd_y}\, \text{{kN}}$$ και η **ελάχιστη τέμνουσα σχεδιασμού του υποστυλώματος** θα είναι: $$\text{{min}} \text{{V}}_{{\text{{d}}_\text{{(y)}}}} = {minVd_y}\, \text{{kN}}$$
      """)

        st.divider()
        st.subheader("**ΤΕΜΝΟΥΣΕΣ ΚΡΙΣΙΜΩΝ ΠΕΡΙΟΧΩΝ**")
        st.write(
            "▧ Λόγω της παραπάνω ανήσωσης και της **απουσίας της τέμνουσας κατακόρυφου φορτίου** έχουμε:"
        )
        st.info("**Τέμνουσες ροπών και σχεδιασμού:**")
        if SMRb_a >= SMRc_a and SMRb_k >= SMRc_k and fora == 'Θετική':
            DVmax1 = DV(M1dtt, M2daa, lcl)
            DVmax1 = round(DVmax1, 2)
            st.markdown(rf"""
      **⁛** Για **θετική σεισμική φορά οι τέμνουσες** θα είναι:
      
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overrightarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overrightarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} =  {DVmax1}\,\text{{kN}} = \text{{V}}_{{\text{{Ed}}}} $$""")
        
        elif SMRb_a >= SMRc_a and SMRb_k >= SMRc_k and fora == 'Αρνητική':
            DVmin1 = DV(M1daa, M2dtt, lcl)
            Dvmin1 = round(DVmin1, 2)
            st.markdown(rf"""
      **⁛** Για **αρνητική σεισμική φορά οι τέμνουσες** θα είναι:
      
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overleftarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overleftarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {-DVmin1}\, \text{{kN}} = \text{{V}}_{{\text{{Ed}}}}$$""")

        elif SMRb_a < SMRc_a and SMRb_k < SMRc_k and fora == 'Θετική':
            DVmax2 = DV(M1dt, M2da, lcl)
            DVmax2 = round(DVmax2, 2)
            st.markdown(rf"""
      **⁛** Για **θετική σεισμική φορά οι τέμνουσες** θα είναι:
      
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overrightarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overrightarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {DVmax2}\,\text{{kN}} = \text{{V}}_{{\text{{Ed}}}}$$""")
       
        elif SMRb_a < SMRc_a and SMRb_k < SMRc_k and fora == 'Αρνητική':
            DVmin2 = DV(M1da, M2dt, lcl)
            DVmin2 = round(DVmin2, 2)
            st.markdown(rf"""
      **⁛** Για **αρνητική σεισμική φορά οι τέμνουσες** θα είναι:
    
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overleftarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overleftarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {-DVmin2}\, \text{{kN}} = \text{{V}}_{{\text{{Ed}}}}$$""")

        elif SMRb_a >= SMRc_a and SMRb_k < SMRc_k and fora == 'Θετική':
            DVmax3 = DV(M1dtt, M2da, lcl)
            DVmax3 = round(DVmax3, 2)
            st.markdown(rf"""
    **⁛** Για **θετική σεισμική φορά οι τέμνουσες** θα είναι:
    
    $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overrightarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overrightarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {DVmax3}\,\text{{kN}} = \text{{V}}_{{\text{{Ed}}}}$$""")
    
        elif SMRb_a >= SMRc_a and SMRb_k < SMRc_k and fora == 'Αρνητική':
            DVmin3 = DV(M1daa, M2dt, lcl)
            DVmin3 = round(DVmin3, 2)
            st.markdown(rf"""
    **⁛** Για **αρνητική σεισμική φορά οι τέμνουσες** θα είναι:
    
    $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overleftarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overleftarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {-DVmin3}\, \text{{kN}} = \text{{V}}_{{\text{{Ed,}}}}$$""")

        elif SMRb_a < SMRc_a and SMRb_k >= SMRc_k and fora == 'Θετική':
            DVmax4 = DV(M1dt, M2daa, lcl)
            DVmax4 = round(DVmax4, 2)
            st.markdown(rf"""
      **⁛** Για **θετική σεισμική φορά οι τέμνουσες** θα είναι:
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overrightarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overrightarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {DVmax4}\,\text{{kN}} = \text{{V}}_{{\text{{Ed}}}}$$""")

        elif SMRb_a < SMRc_a and SMRb_k >= SMRc_k and fora == 'Αρνητική':
            DVmin4 = DV(M1da, M2dtt, lcl)
            DVmin4 = round(DVmin4, 2)
            st.markdown(rf"""
      **⁛** Για **αρνητική σεισμική φορά οι τέμνουσες** θα είναι:
      
      $$\Delta \text{{V}}_{{\text{{Ed,i}}}} = \dfrac{{(\overleftarrow{{\text{{M}}}}_{{\text{{1,d}}}} + \overleftarrow{{\text{{M}}}}_{{\text{{2,d}}}})}}{{\text{{L}}_{{\text{{cl}}}}}} = {-DVmin4}\, \text{{kN}} = \text{{V}}_{{\text{{Ed}}}}$$""")


# KOMVOUS
if epilogi == "Ικανοτικός σχεδιασμός στους κόμβους":
    with st.sidebar:
        komvos = st.selectbox(
            "Επιλέξτε κόμβο:",
            ["Εσωτερικός κόμβος", "Εξωτερικός κόμβος", "Γωνιακός κόμβος"],
        )

    # SIDEBAR - ESWTWRIKOS
    if komvos == "Εσωτερικός κόμβος":
        with st.sidebar:
            st.link_button(
                "ΕΡΓΑΣΙΑ",
                "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=92",
            )
            st.link_button(
                "ΕΥΡΩΚΩΔΙΚΑΣ 8",
                "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=115",
            )
            st.page_link(
                "pages/info.py", label="Υπολογισμός εσωτερικού κόμβου", icon="🔗"
            )

    # TABLO - ESWTERIKOS
    if komvos == "Εσωτερικός κόμβος":
        with st.expander("**Τα αριθμητικά δεδομένα σας**"):
            col1, col2 = st.columns(2)
            with col1:
                st.info("**Ροπές δοκού:**")
                st.success("**Δεξιά:**")
                MRb1_n = st.number_input(
                    "**Αρνητική** ροπή αντοχής $MRb,1^-$:", value=-100.0, step=0.1, format="%.2f"
                )
                MRb1_p = st.number_input(
                    "**Θετική** ροπή αντοχής $MRb,1^+$:", value=200.0, step=0.1, format="%.2f"
                )
                st.success("**Αριστερά:**")
                MRb2_n = st.number_input(
                    "**Αρνητική** ροπή αντοχής $MRb,2^-$:", value=-350.0, step=0.1, format="%.2f"
                )
                MRb2_p = st.number_input(
                    "**Θετική** ροπή αντοχής $MRb,2^+$:", value=700.0, step=0.1, format="%.2f"
                )
                
            with col2:
                st.info("**Ροπές υποστυλώματος:**")
                st.success("**Άνω:**")
                MRc1_n = st.number_input(
                    "**Αρνητική** ροπή αντοχής $MRc,1^-$:", value=-50.0, step=0.1, format="%.2f"
                )
                MRc1_p = st.number_input(
                    "**Θετική** ροπή αντοχής $MRc,1^+$:", value=100.0, step=0.1, format="%.2f"
                )
                st.success("**Κάτω:**")
                MRc2_n = st.number_input(
                    "**Αρνητική** ροπή αντοχής $MRc,2^-$:", value=-120.0, step=0.1, format="%.2f"
                )
                MRc2_p = st.number_input(
                    "**Θετική** ροπή αντοχής $MRc,2^+$:", value=60.0, step=0.1, format="%.2f"
                )

        st.divider()
        seis_fora =st.selectbox("Επιλέξτε σεισμική φορά ανάλυσης:",['Θετική', 'Αρνητική'])
        if seis_fora == 'Θετική':
            eswterikos_th_url = "images/eswterikos_thetiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 25])
            with col3:
                 st.image(eswterikos_th_url, caption="Θετική φορά εσωτερικού κόμβου.", width=580)
        else:
            eswterikos_ar_url = "images/eswterikos_arnitiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 30])
            with col3:
                 st.image(eswterikos_ar_url, caption="Αρνητική φορά εσωτερικού κόμβου.", width=620)

        st.subheader("**Ροπές αντοχής**")
        st.write("Σύμφωνα με τα παραπάνω δεδομένα σας:")
        st.write("Οι  ροπές αντοχής των **δοκών** για:")

        if seis_fora == 'Θετική':
            col1,col2 = st.columns(2)
            with col1:
                 st.info('**Δεξιά:**')
                 st.markdown(rf"""
        **▧ Θετική** φόρτιση: 
        
        $$\text{{M}}_{{\text{{Rb,}}_{{1}}}}^+ = {MRb1_p:.2f}\, \text{{kNm}}$$""")
                 
            with col2:  
                 st.info("**Αριστερά:**")
                 st.markdown(rf"""
        **▧ Θετική** φόρτιση: 
        $$\text{{M}}_{{\text{{Rb,}}_{{2}}}}^- = {MRb2_n:.2f}\, \text{{kNm}}$$""")   
        else:
            col1,col2 = st.columns(2)
            with col1:
                st.info("**Δεξιά:**")
                st.markdown(rf"""
        **▧ Αρνητική** φόρτιση: 
        
        $$\text{{M}}_{{\text{{Rb,}}_{{1}}}}^- = {MRb1_n:.2f}\, \text{{kNm}}$$""")
                
            with col2:
                 st.info("**Αριστερά:**")
                 st.markdown(rf"""
        **▧ Αρνητική** φόρτιση: 

        $$\text{{M}}_{{\text{{Rb,}}_{{2}}}}^+ = {MRb2_p:.2f}\, \text{{kNm}}$$""")

        st.divider()
        st.write("Οι ροπές αντοχής των **υποστυλωμάτων** για:")
        if seis_fora == 'Θετική':
             col1,col2=st.columns(2)
             with col1:
                 st.info("**Άνω:**")
                 st.markdown(rf"""
        **▧ Θετική** φόρτιση: 

        $$\text{{M}}_{{\text{{Rc,}}_{{1}}}}^+ = {MRc1_p:.2f}\, \text{{kNm}}$$""")
             with col2:
                 st.info("**Κάτω:**")
                 st.markdown(rf"""
        **▧ Θετική** φόρτιση: 

        $$\text{{M}}_{{\text{{Rc,}}_{{2}}}}^- = {MRc2_n:.2f}\, \text{{kNm}}$$""")
        else:
            col1,col2=st.columns(2)
            with col1:
                st.info("**Άνω:**")
                st.markdown(rf"""
        **▧ Αρνητική** φόρτιση: 

        $$\text{{M}}_{{\text{{Rc,}}_{{1}}}}^- = {MRc1_n:.2f}\, \text{{kNm}}$$""")
            with col2:
                st.info("**Κάτω:**")
                st.markdown(rf"""
        **▧ Αρνητική** φόρτιση: 

        $$\text{{M}}_{{\text{{Rc,}}_{{2}}}}^+ = {MRc2_p:.2f}\, \text{{kNm}}$$""")

        st.divider()
        st.info("**Ελεγχος ανισότητας:**")
        if seis_fora == 'Θετική':
             SMRc = SMRc_th(MRc1_p, MRc2_n)
             SMRb = SMRb_th(MRb1_p, MRb2_n)
             st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_\text{{Rc}} = \text{{M}}_{{\text{{Rc,}}_{{1}}}}^+ + \text{{M}}_{{\text{{Rc,}}_{{2}}}}^- = {SMRc:.2f}\, \text{{kNm}}$$"""
        )
             st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_\text{{Rb}} = \text{{M}}_{{\text{{Rb,}}_{{1}}}}^+ + \text{{M}}_{{\text{{Rb,}}_{{2}}}}^- = {SMRb:.2f}\,\text{{kNm}}$$"""
        )
             st.write("")
             if SMRc >= 1.3 * SMRb:
                 st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3*SMRb:.2f}\, \text{{kNm}}$$"""
            )
                 st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
             else:
                 st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \times \sum \text{{M}}_{{\text{{Rb}}}}  → {SMRc:.2f}\, \text{{kNm}} < {1.3*SMRb:.2f}\, \text{{kNmn}}$$"""
            )
                 st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                 st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή τα άκρα των δοκών έχουν αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                 st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")
        else:
             SMRc = SMRc_ar(MRc1_n, MRc2_p)
             SMRb = SMRb_ar(MRb1_n, MRb2_p)
             st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_\text{{Rc}} = \text{{M}}_{{\text{{Rc,}}_{{1}}}}^- + \text{{M}}_{{\text{{Rc,}}_{{2}}}}^+ = {SMRc:.2f}\, \text{{kNm}}$$"""
        )
             st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_\text{{Rb}} = \text{{M}}_{{\text{{Rb,}}_{{1}}}}^- + \text{{M}}_{{\text{{Rb,}}_{{2}}}}^+ = {SMRb:.2f}\,\text{{kNm}}$$"""
        )
             st.write("")
             if SMRc >= 1.3 * SMRb:
                 st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}}  → {SMRc:.2f}\, \text{{kNm}} \geq {1.3*SMRb:.2f}\, \text{{kNm}}$$"""
            )
                 st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
             else:
                 st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \times \sum \text{{M}}_{{\text{{Rb}}}}  → {SMRc:.2f}\, \text{{kNm}} < {1.3*SMRb:.2f}\, \text{{kNm}}$$"""
            )
                 st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                 st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή τα άκρα των δοκών έχουν αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                 st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")


    # SIDEBAR - EKSWTERIKOS
    if komvos == "Εξωτερικός κόμβος":
        with st.sidebar:
            st.link_button(
                "ΕΡΓΑΣΙΑ",
                "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=92",
            )
            st.link_button(
                "ΕΥΡΩΚΩΔΙΚΑΣ 8",
                "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=115",
            )
            st.page_link(
                "pages/info.py", label="Υπολογισμός εξωτερικού κόμβου", icon="🔗"
            )

    # TABLO - EKSWTERIKOS
    if komvos == "Εξωτερικός κόμβος":
        with st.expander("**Τα αριθμητικά δεδομένα σας**"):
            st.info("**Ροπές άνω υποστυλώματος:**")
            MRc1_n = st.number_input(
            "**Αρνητική** ροπή αντοχής $MRc,1^-$:", value=-350.0, step = 0.1, format="%.2f"
            )
            MRc1_p = st.number_input(
            "**Θετική** ροπής αντοχής $MRc,1^+$:", value=500.0, step = 0.1, format="%.2f"
            )

            st.divider()
            col1,col2 = st.columns(2)
            with col1: 
                  ar_d = st.checkbox("**Αριστερή δοκός**")
                  if ar_d:
                    st.info("**Ροπές δοκού:**")
                    MRb1_n = st.number_input(
                    "**Αρνητική** ροπή αντοχής $MRb,1^-$:", value=-100.0, step = 0.1, format="%.2f"
                )
                    MRb1_p = st.number_input(
                    "**Θετική** ροπή αντοχής $MRb,1^+$:", value=200.0, step = 0.1, format="%.2f"
                )
            with col2:
                  de_d = st.checkbox("**Δεξιά δοκός**")
                  if de_d:
                      st.info("**Ροπές δοκού**")
                      MRb2_n = st.number_input(
                    "**Αρνητική** ροπή αντοχής $MRb,2^-$:", value=-400.0, step = 0.1, format="%.2f"
                )
                      MRb2_p = st.number_input(
                    "**Θετική** ροπή αντοχής $MRb,2^+$:", value=600.0, step = 0.1, format="%.2f"
                )

            st.divider()
            st.info("**Ροπές κάτω υποστυλώματος:**")
            MRc2_n = st.number_input(
            "**Αρνητική** ροπή αντχοής $MRc,2^-$:", value=-400.0, step = 0.1, format="%.2f"
            )
            MRc2_p = st.number_input(
            "**Θετική** ροπή αντχοής $MRc,2^+$:", value=200.0, step = 0.1, format="%.2f"
            )
            
        st.divider()
        fora = st.selectbox("Επιλέξτε σεισμική φορά ανάλυσης:", ['Θετική', 'Αρνητική'])

        st.subheader("**Ροπές αντοχής:**")
        st.write("Σύμφωνα με τα παραπάνω δεδομένα σας:")
        if ar_d and de_d and fora == 'Θετική':
            st.error("Πρέπει να επιλέξετε **μια μόνο** δοκό.")
        elif ar_d and de_d and fora == 'Αρνητική':
            st.error("Πρέπει να επιλέξετε **μια μόνο** δοκό.")
        elif ar_d and fora == 'Θετική':
            ekswterikos2_th_url = "images/ekswterikos2_thetiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 50])
            with col3:
                 st.image(ekswterikos2_th_url, caption="Θετική φορά εξωτερικού κόμβου.", width=580)

            st.markdown(rf"""
            Η ροπή αντοχής της **δοκού** για **θετική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rb}}}}^- = {MRb1_n:.2f}\, \text{{kNm}}$$""")
        elif ar_d and fora == 'Αρνητική':
            ekswterikos2_ar_url = "images/ekswterikos2_arnitiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 50])
            with col3:
                 st.image(ekswterikos2_ar_url, caption="Αρνητική φορά εξωτερικού κόμβου.", width=540)

            st.markdown(rf"""
            Η ροπή αντοχής της **δοκού** για **αρνητική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rb}}}}^+ = {MRb1_p:.2f}\, \text{{kNm}}$$""")
        elif de_d and fora =='Θετική':
            ekswterikos2_th_url = "images/ekswterikos2_thetiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 50])
            with col3:
                 st.image(ekswterikos2_th_url, caption="Θετική φορά εξωτερικού κόμβου.", width=540)

            st.markdown(rf"""
            Η ροπή αντοχής της **δοκού** για **θετική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rb}}}}^+ = {MRb2_p:.2f}\, \text{{kNm}}$$""")
        elif de_d and fora == 'Αρνητική':
            ekswterikos2_ar_url = "images/ekswterikos2_arnitiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 50])
            with col3:
                 st.image(ekswterikos2_ar_url, caption="Αρνητική φορά εξωτερικού κόμβου.", width=540)

            st.markdown(rf"""
            Η ροπή αντοχής της **δοκού** για **αρνητική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rb}}}}^- = {MRb2_n:.2f}\, \text{{kNm}}$$""")
        else:
            st.error("Πρέπει να επιλέξετε δοκό.")

        st.divider()
        st.write("Οι ροπές αντοχής του **υποστυλώματος** για:")
        if fora == 'Θετική':
            col1,col2 = st.columns(2)
            with col1:
                st.info("**Άνω:**")
                st.markdown(rf"""
        **▧ Θετική** φόρτιση:
        
        $$\text{{M}}_{{\text{{Rc,}}_{{1}}}}^+ = {MRc1_p:.2f}\, \text{{kNm}}$$""")
            with col2:
                st.info("**Κάτω:**")
                st.markdown(rf"""
        **▧ Θετική** φόρτιση:
        
        $$\text{{M}}_{{\text{{Rc,}}_{{2}}}}^- = {MRc2_n:.2f}\, \text{{kNm}}$$""")
        else:
            col1,col2 = st.columns(2)
            with col1:
                st.info("**Άνω:**")
                st.markdown(rf"""
        **▧ Αρνητική** φόρτιση:

        $$\text{{M}}_{{\text{{Rc,}}_{{1}}}}^- = {MRc1_n:.2f}\, \text{{kNm}}$$""")
            with col2:
                st.info("**Κάτω:**")
                st.markdown(rf"""
        **▧ Αρνητική** φόρτιση:

        $$\text{{M}}_{{\text{{Rc,}}_{{2}}}}^+ = {MRc2_p:.2f}\, \text{{kNm}}$$""")
                
        
        st.divider()
        st.write("")
        st.info("**Ελεγχος ανισότητας:**")
        if fora == 'Θετική' and de_d and ar_d:
            st.error('Πρέπει να επιλέξετε **μια μόνο** δοκό.')
        elif fora == 'Αρνητική' and de_d and ar_d:
            st.error('Πρέπει να επιλέξετε **μια μόνο** δοκό.')
        elif fora == 'Θετική' and de_d:
            SMRc = SMRc_eks_th(MRc1_p, MRc2_n)
            SMRb = MRb2_p
            st.markdown(
                rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc,}}_{{1}}}}^+ + \text{{M}}_{{\text{{Rc,}}_{{2}}}}^- = {SMRc:.2f}\, \text{{kNm}}$$"""
            )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^+ = {SMRb:.2f}\, \text{{kNm}}$$""")
            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

                
        elif fora == 'Θετική' and ar_d:
            SMRc = SMRc_eks_th(MRc1_p, MRc2_n)
            SMRb = abs(MRb1_n)
            st.markdown(
                rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc,}}_{{1}}}}^+ + \text{{M}}_{{\text{{Rc,}}_{{2}}}}^- = {SMRc:.2f}\, \text{{kNm}}$$"""
            )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^- = {SMRb:.2f}\, \text{{kNm}}$$""")
            if SMRc >= 1.3 * SMRb:
                 st.markdown(
                 rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                 st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                 st.markdown(
                 rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}} $"""
            )
                 st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                 st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                 st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        elif fora == 'Αρνητική' and de_d:
            SMRc = SMRc_eks_arn(MRc2_p, MRc1_n)
            SMRb = abs(MRb2_n)
            st.markdown(
                rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc,}}_{{1}}}}^+ + \text{{M}}_{{\text{{Rc,}}_{{1}}}}^- = {SMRc:.2f}\, \text{{kNm}}$$"""
            )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^+ = {SMRb:.2f}\, \text{{kNm}}$$""")
            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}} $$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        elif fora == 'Αρνητική' and ar_d:
            SMRc = SMRc_eks_arn(MRc2_p, MRc1_n)
            SMRb = MRb1_p
            st.markdown(
                rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc,}}_{{1}}}}^+ + \text{{M}}_{{\text{{Rc,}}_{{1}}}}^- = {SMRc:.2f}\, \text{{kNm}}$$"""
            )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^+ = {SMRb:.2f}\, \text{{kNm}}$$""")
            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        else:
            st.error('Πρέπει να επιλέξετε δοκό.')
        
    # SIDEBAR - GWNIAKOS
    if komvos == "Γωνιακός κόμβος":
        with st.sidebar:
            st.link_button(
                "ΕΡΓΑΣΙΑ",
                "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=92",
            )
            st.link_button(
                "ΕΥΡΩΚΩΔΙΚΑΣ 8",
                "https://www.phd.eng.br/wp-content/uploads/2015/02/en.1998.1.2004.pdf#page=115",
            )
            st.page_link(
                "pages/info.py", label="Υπολογισμός γωνιακού κόμβου", icon="🔗"
            )

    # ΤΑBLO - GWNIAKOS
    if komvos == "Γωνιακός κόμβος":
        with st.expander("**Τα αριθμητικά δεδομένα σας**"):
            an_up = st.checkbox("**Άνω υποστύλωμα**")
            if an_up:
                st.info("**Ροπές υποστυλώματος:**")
                MRc1_n = st.number_input(
                    "**Αρνητική** ροπή αντοχής $MRc,1^-$", value=-200.0, step = 0.1, format="%.2f"
                )
                MRc1_p = st.number_input(
                    "**Θετική** ροπή αντοχής $MRc,1^+$", value=120.0, step = 0.1, format="%.2f"
                )
        
            col1, col2= st.columns(2)
            with col1:
                ar_dok = st.checkbox('**Αριστερή δοκός**')
                if ar_dok:
                     st.info("**Ροπές δοκού:**")
                     MRb1_n = st.number_input(
                    "**Αρνητική** ροπή αντοχής $MRb,1^-$:", value=-100.0, step = 0.1, format="%.2f"
                )
                     MRb1_p = st.number_input(
                    "**Θετική** ροπή αντοχής $MRb,1^+$:", value=50.0, step = 0.1, format="%.2f"
                )
            with col2:
                de_dok = st.checkbox("**Δεξιά δοκός**")
                if de_dok:
                    st.info("**Ροπές δοκού:**")
                    MRb2_n = st.number_input(
                    "**Αρνητική** ροπή αντοχής $MRb,2^-$:", value=-400.0, step = 0.1, format="%.2f"
                )
                    MRb2_p = st.number_input(
                    "**Θετική** ροπή αντοχής $MRb,2^+$:", value=200.0, step = 0.1, format="%.2f"
                )
            kat_up = st.checkbox("**Κάτω υποστύλωμα**")
            if kat_up:
                   st.info("**Ροπές υποστυλώματος:**")
                   MRc2_n = st.number_input(
                "**Αρνητική** ροπή αντοχής $MRc,2^-$", value=-50.0, step = 0.1, format="%.2f"
                )
                   MRc2_p = st.number_input(
                "**Θετική** ροπή αντοχής $MRc,2^+$", value=100.0, step = 0.1, format="%.2f"
                )
                            
        st.divider()
        fora = st.selectbox('Επιλέξτε σεισμική φορά ανάλυσης:', ['Θετική', 'Αρνητική'])

        if fora == 'Θετική' and ar_dok and an_up:
            gwniako1_th_url = "images/gwniakos_anoaristera_thetiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 100])
            with col3:
                 st.image(gwniako1_th_url, caption="Θετική φορά γωνιακού κόμβου.", width=540)
        elif fora =='Αρνητική' and ar_dok and an_up:
            gwniako1_ar_url = "images/gwniakos_anoaristera_arnitiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 100])
            with col3:
                 st.image(gwniako1_ar_url, caption="Αρνητική φορά γωνιακού κόμβου.", width=540)
        elif fora == 'Θετική' and ar_dok and kat_up:
            gwniako2_th_url = "images/gwniakos_katoaristera_thetiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 50])
            with col3:
                 st.image(gwniako2_th_url, caption="Θετική φορά γωνιακού κόμβου.", width=420)
        elif fora == 'Αρνητική' and ar_dok and kat_up:
            gwniako2_ar_url = "images/gwniakos_katoaristera_arnitiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 50])
            with col3:
                 st.image(gwniako2_ar_url, caption="Αρνητική φορά γωνιακού κόμβου.", width=420)
        elif fora == 'Θετική' and de_dok and an_up:
            gwniako3_th_url = "images/gwniakos_anodeksia_thetiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 10])
            with col3:
                 st.image(gwniako3_th_url, caption="Θετική φορά γωνιακού κόμβου.", width=420)
        elif fora == 'Αρνητική' and de_dok and an_up:
            gwniako3_ar_url = "images/gwniakos_anodeksia_arnitiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 10])
            with col3:
                 st.image(gwniako3_ar_url, caption="Αρνητική φορά γωνιακού κόμβου.", width=420)
        elif fora == 'Θετική' and de_dok and kat_up:
            gwniako4_th_url = "images/gwniakos_katodeksia_thetiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 10])
            with col3:
                 st.image(gwniako4_th_url, caption="Θετική φορά γωνιακού κόμβου.", width=420)

        elif fora == 'Αρνητική' and de_dok and kat_up:
            gwniako4_ar_url = "images/gwniakos_katodeksia_arnitiko.jpg"
            col1, col2, col3 = st.columns([1, 1, 15])
            with col3:
                 st.image(gwniako4_ar_url, caption="Αρνητική φορά γωνιακού κόμβου.", width=420)

        st.subheader("**Ροπές αντοχής:**")
        st.write("Σύμφωνα με τα παραπάνω δεδομένα σας:")
        if ar_dok and de_dok:
            st.error("Πρέπει να επιλέξετε **μια μόνο** δοκό.")
        elif ar_dok and fora == 'Θετική':
            st.markdown(rf"""
        Η ροπή αντοχής της **δοκού** για **θετική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rb}}}}^- = {MRb1_n:.2f}\, \text{{kNm}}$$""")
        elif ar_dok and fora == 'Αρνητική':
            st.markdown(rf"""
        Η ροπή αντοχής της **δοκού** για **αρνητική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rb}}}}^+ = {MRb1_p:.2f}\, \text{{kNm}}$$""")
        elif de_dok and fora == 'Θετική':
            st.markdown(rf"""
            Η ροπή αντοχής της **δοκού** για **θετική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rb}}}}^+ = {MRb2_p:.2f}\, \text{{kNm}}$$""")
        elif de_dok and fora == 'Αρνητική':
            st.markdown(rf"""
            Η ροπή αντοχής της **δοκού** για **αρνητική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rb}}}}^- = {MRb2_n:.2f}\, \text{{kNm}}$$""")
        else:
            st.error('Πρέπει να επιλέξετε δοκό.')

        st.divider()     
        if an_up and kat_up:
            st.error("Πρέπει να επιλέξετε **ένα μόνο** υποστύλωμα.")
        elif an_up and fora == 'Θετική':
            st.markdown(rf"""
            Η ροπή αντοχής του **υποστυλώματος** για **θετική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rc}}}}^+ = {MRc1_p:.2f}\, \text{{kNm}}$$""")
        elif an_up and fora == 'Αρνητική':
            st.markdown(rf"""
            Η ροπή αντοχής του **υποστυλώματος** για **αρνητική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rc}}}}^- = {MRc1_n:.2f}\, \text{{kNm}}$$""")
        elif kat_up and fora == 'Θετική':
            st.markdown(rf"""
            Η ροπή αντοχής του **υποστυλώματος** για **θετική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rc}}}}^- = {MRc2_n:.2f}\, \text{{kNm}}$$""")
        elif kat_up and fora == 'Αρνητική':
            st.markdown(rf"""
            Η ροπή αντοχής του **υποστυλώματος** για **αρνητική** φόρτιση είναι: $$\text{{M}}_{{\text{{Rc}}}}^+ = {MRc2_p:.2f}\, \text{{kNm}}$$""")
        else:
            st.error('Πρέπει να επιλέξετε υποστύλωμα.')

        st.divider()
        st.info("**Ελεγχος ανισότητας:**")
        if an_up and kat_up and ar_dok and de_dok and fora == 'Θετική':
            st.error("Πρέπει να επιλέξετε **μια μόνο δοκό** και **ένα μονο υποστύλωμα**.")
        elif an_up and kat_up and ar_dok and de_dok and fora == 'Αρνητική':
            st.error("Πρέπει να επιλέξετε **μια μόνο δοκό** και **ένα μονο υποστύλωμα**.")
        elif an_up and kat_up and ar_dok and fora == 'Θετική':
            st.error('Πρέπει να επιλέξετε **ένα μονο υποστύλωμα**.')
        elif an_up and kat_up and ar_dok and fora == 'Αρνητική':
            st.error('Πρέπει να επιλέξετε **ένα μονο υποστύλωμα**.')
        elif an_up and kat_up and de_dok and fora == 'Θετική':
            st.error('Πρέπει να επιλέξετε **ένα μονο υποστύλωμα**.')
        elif an_up and kat_up and de_dok and fora == 'Αρνητική':
            st.error('Πρέπει να επιλέξετε **ένα μονο υποστύλωμα**.')
        elif an_up and ar_dok and de_dok and fora == 'Θετική':
            st.error('Πρέπει να επιλέξετε **μια μόνο δοκό**.')
        elif an_up and ar_dok and de_dok and fora == 'Αρνητική':
            st.error('Πρέπει να επιλέξετε **μια μόνο δοκό**.')
        elif kat_up and ar_dok and de_dok and fora == 'Θετική':
            st.error('Πρέπει να επιλέξετε **μια μόνο δοκό**.')
        elif kat_up and ar_dok and de_dok and fora == 'Αρνητική':
            st.error('Πρέπει να επιλέξετε **μια μόνο δοκό**.')
        elif an_up and kat_up and fora == 'Θετική':
            st.error('Πρέπει να επιλέξετε και **μια δοκό**.')
        elif an_up and kat_up and fora == 'Αρνητική':
            st.error('Πρέπει να επιλέξετε και **μια δοκό**.')
        elif ar_dok and de_dok and fora == 'Θετική':
            st.error('Πρέπει να επιλέξετε και **ένα υποστύλωμα**.')
        elif ar_dok and de_dok and fora == 'Αρνητική':
            st.error('Πρέπει να επιλέξετε και **ένα υποστύλωμα**.')

        elif an_up and ar_dok and fora == 'Θετική':
            SMRc = MRc1_p
            SMRb = abs(MRb1_n)
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc}}}}^+ = {SMRc:.2f}\, \text{{kNm}}$$"""
        )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^- = {SMRb:.2f}\, \text{{kNm}}$$"""
        )
            st.write("")

            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞"
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        elif an_up and ar_dok and fora == 'Αρνητική':
            SMRc = abs(MRc1_n)
            SMRb = MRb1_p
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc}}}}^- = {SMRc:.2f}\, \text{{kNm}}$$"""
        )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^+ = {SMRb:.2f}\, \text{{kNm}}$$"""
        )
            st.write("")

            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        elif an_up and de_dok and fora == 'Θετική':
            SMRc= MRc1_p
            SMRb = MRb2_p
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc}}}}^+ = {SMRc:.2f}\, \text{{kNm}}$$"""
        )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^+ = {SMRb:.2f}\, \text{{kNm}}$$"""
        )
            st.write("")

            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        elif an_up and de_dok and fora == 'Αρνητική':
            SMRc= abs(MRc1_n)
            SMRb = abs(MRb2_n)
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc}}}}^- = {SMRc:.2f}\, \text{{kNm}}$$"""
        )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^- = {SMRb:.2f}\, \text{{kNm}}$$"""
        )
            st.write("")

            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        elif kat_up and ar_dok and fora == 'Θετική':
            SMRc = abs(MRc2_n)
            SMRb = abs(MRb1_n)
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc}}}}^- = {SMRc:.2f}\, \text{{kNm}}$$"""
        )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^- = {SMRb:.2f}\, \text{{kNm}}$$"""
        )
            st.write("")

            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        elif kat_up and ar_dok and fora == 'Αρνητική':
            SMRc = MRc2_p
            SMRb = MRb1_p
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc}}}}^+ = {SMRc:.2f}\, \text{{kNm}}$$"""
        )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^+ = {SMRb:.2f}\, \text{{kNm}}$$"""
        )
            st.write("")

            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        elif kat_up and de_dok and fora == 'Θετική':
            SMRc= abs(MRc2_n)
            SMRb = MRb2_p
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc}}}}^- = {SMRc:.2f}\, \text{{kNm}}$$"""
        )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^+ = {SMRb:.2f}\, \text{{kNm}}$$"""
        )
            st.write("")

            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        elif kat_up and de_dok and fora == 'Αρνητική':
            SMRc= MRc2_p
            SMRb = abs(MRb2_n)
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rc}}}} = \text{{M}}_{{\text{{Rc}}}}^+ = {SMRc:.2f}\, \text{{kNm}}$$"""
        )
            st.markdown(
            rf""" **⇒** $$\sum \text{{M}}_{{\text{{Rb}}}} = \text{{M}}_{{\text{{Rb}}}}^- = {SMRb:.2f}\, \text{{kNm}}$$"""
        )
            st.write("")

            if SMRc >= 1.3 * SMRb:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} \geq 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} \geq {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.success(
                "Η ανισότητα **ικανοποιείται**!", icon="🥳"
            )
            else:
                st.markdown(
                rf""" **Άρα:** $$\sum \text{{M}}_{{\text{{Rc}}}} < 1.3 \sum \text{{M}}_{{\text{{Rb}}}} → {SMRc:.2f}\, \text{{kNm}} < {1.3 * SMRb:.2f}\, \text{{kNm}}$$"""
            )
                st.error(
                "Η ανισότητα **δεν ικανοποιείται**.",
                icon="😞",
            )
                st.error("1. Ελέγξτε τους **λόγους εξάντλησης** (αν δηλαδή το άκρα της δοκού έχει αρκετά περιθώρια αντοχής) ώστε να **μειωθεί αντίστοιχα και ο διαμήκης οπλισμός**.")
                st.error("2. Εάν αποτύχει, τότε θα πρέπει να **αυξηθεί ο διαμήκης οπλισμός του υποστυλώματος**.")

        else:
            st.error('Πρέπει να διαλέξετε **μια δοκό** και **ένα υποστύλωμα**.')