import streamlit as st
import pandas as pd

from daten_code import Zutaten_daten as zd
from funktionen_code import Funktions_ablage as fa


def seite_3():

   def csv_reader(csv):
        return pd.read_csv(csv, sep= ";")

   Rezepte_dataframe = csv_reader("Rezepte_dataframe.csv")

   personenanzahl = st.sidebar.slider("Wähle die Personenanzahl aus", 1, 10, 2)


   random_checkbox = st.sidebar.button("Random Rezept")
   if random_checkbox:
      st.session_state.random_rezept = fa.random_rez(Rezepte_dataframe)
      fa.zutaten_ausgabe(st.session_state.random_rezept, zd.Kochbuch, personenanzahl)

        

    

        




