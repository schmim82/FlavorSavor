import streamlit as st
import pandas as pd

from daten_code import Zutaten_daten as zd
from funktionen_code import Funktions_ablage as fa









def seite_2():




    st.title("Einkaufsliste")



    username = fa.get_current_username()
    
df = fa.show_dataframe()

    st.dataframe(df)


    st.sidebar.subheader("Die Rezepte in deiner Einkaufsliste sind:")

    df_persönlich = df[df["name"] == username]

    pers_L = df_persönlich["rezept"].tolist()
    pers_L_anz = df_persönlich["anzahl"].tolist()

     

    
    for item1, item2 in zip(pers_L, pers_L_anz):
        st.sidebar.markdown(f"{item1} für {item2} Personen")






    einkaufsdic = {}
    variable = 0
    
    for item in pers_L:
        einkaufsdic[item] = pers_L_anz[variable]

        variable += 1 

    fa.einkaufsliste_erstellen(einkaufsdic, zd.Kochbuch)


    

    rezept_zum_entfernen = st.sidebar.selectbox("Wähle Rezept zum entfernen aus", pers_L)
    entfern_button = st.sidebar.button("entfernen")

    if entfern_button:
        fa.rezept_entfernen(username, rezept_zum_entfernen)


        df = fa.show_dataframe()

   






