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


           
