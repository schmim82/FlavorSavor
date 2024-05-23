import streamlit as st
import pandas as pd

from daten_code import Zutaten_daten as zd
from funktionen_code import Funktions_ablage as fa


def seite_3():


   random_checkbox = st.sidebar.button("Random Rezept")
   if random_checkbox:
      st.session_state.random_rezept = fa.random_rez(Rezepte_dataframe)
      fa.zutaten_ausgabe(st.session_state.random_rezept, zd.Kochbuch, personenanzahl)

        

    

        




