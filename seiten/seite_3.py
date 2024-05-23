import streamlit as st
import pandas as pd

from daten_code import Zutaten_daten as zd
from funktionen_code import Funktions_ablage as fa


def seite_3():
    def csv_reader(csv):
        return pd.read_csv(csv, sep=";")

    Rezepte_dataframe = csv_reader("Rezepte_dataframe.csv")

    personenanzahl = st.sidebar.slider("Wähle die Personenanzahl aus", 1, 10, 2)

    random_checkbox = st.sidebar.button("Random Rezept")

    # Überprüfen, ob `random_rezept` im Session State ist, sonst initialisieren
    if 'random_rezept' not in st.session_state:
        st.session_state.random_rezept = None

    if random_checkbox:
        st.session_state.random_rezept = fa.random_rez(Rezepte_dataframe)

    # Nur ausgeben, wenn `random_rezept` gesetzt ist
    if st.session_state.random_rezept:
        fa.zutaten_ausgabe(st.session_state.random_rezept, zd.Kochbuch, personenanzahl)


    DATA_FILE = "test.csv"
    DATA_COLUMNS = ['Name', 'Rezept', 'Anzahl']
    
    fa.init_rez()

    Liste_button = st.sidebar.button("Zur Liste hinzufügen")
    
    if Liste_button:

        user_name = fa.get_current_username()


        fa.rezepte_hinzufügen(user_name, st.session_state.random_rezept, personenanzahl)



