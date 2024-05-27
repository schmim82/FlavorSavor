import streamlit as st
import pandas as pd

from daten_code import Zutaten_daten as zd
from funktionen_code import Funktions_ablage as fa




def seite_4():

  st.title("Favoriten")

  username = fa.get_current_username()


  df = fa.show_dataframe_f()
  df_persönlich = df[df["name"] == username]

  st.subheader("Deine lieblings Rezepte sind:")

  pers_L = df_persönlich["rezept"].tolist()
  pers_L.append("alle")


           
  rezept_zum_entfernen = st.sidebar.selectbox("Wähle das Rezept zum entfernen aus", pers_L)
  entfern_button = st.sidebar.button("entfernen")

  if entfern_button:
      fa.rezept_entfernen_f(username, rezept_zum_entfernen)


      df = fa.show_dataframe()


      df_persönlich = df[df["name"] == username]

      pers_L = df_persönlich["rezept"].tolist()


      for item1 in zip(pers_L):
          st.markdown(f"{item1}")

    
  else:
      df = fa.show_dataframe()


      df_persönlich = df[df["name"] == username]

      pers_L = df_persönlich["rezept"].tolist()

      for item1 in zip(pers_L):
          st.markdown(f"{item1}")

