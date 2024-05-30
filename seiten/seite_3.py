import streamlit as st
import pandas as pd

def seite_3():
    def csv_reader(csv):
        return pd.read_csv(csv, sep=";")

    Rezepte_dataframe = csv_reader("Rezepte_dataframe.csv")
    rez_liste = Rezepte_dataframe["Rezepte"].tolist()
    rez_liste.sort()  # Liste alphabetisch sortieren
    rez_liste.insert(0, "--")

    # Initialisieren Sie den Session State für die Selectbox, falls nicht vorhanden
    if 'selected_rezept' not in st.session_state:
        st.session_state.selected_rezept = "--"
    
    if 'random_rezept' not in st.session_state:
        st.session_state.random_rezept = None

    # Selectbox für Rezepte
    input_rezept = st.sidebar.selectbox("Rezept suchen", rez_liste, index=rez_liste.index(st.session_state.selected_rezept))
    
    # Slider für Personenanzahl
    personenanzahl = st.sidebar.slider("Wähle die Personenanzahl aus", 1, 10, 2)
    
    # Button für zufälliges Rezept
    random_checkbox = st.sidebar.button("Random Rezept")

    # Wenn der Random-Button gedrückt wird, setze ein zufälliges Rezept und setze die Selectbox zurück
    if random_checkbox:
        st.session_state.random_rezept = fa.random_rez(Rezepte_dataframe)
        st.session_state.selected_rezept = "--"
        fa.zutaten_ausgabe(st.session_state.random_rezept, zd.Kochbuch, personenanzahl)
    # Wenn der Selectbox-Eintrag geändert wird und es nicht das zufällige Rezept ist
    elif input_rezept != "--":
        st.session_state.random_rezept = None  # Reset random recipe
        st.session_state.selected_rezept = input_rezept
        fa.zutaten_ausgabe(input_rezept, zd.Kochbuch, personenanzahl)

    # Falls noch ein zufälliges Rezept gesetzt ist, Ausgabe der Zutaten dafür
    if st.session_state.random_rezept:
        fa.zutaten_ausgabe(st.session_state.random_rezept, zd.Kochbuch, personenanzahl)

    DATA_FILE = "test.csv"
    DATA_COLUMNS = ['Name', 'Rezept', 'Anzahl']

    fa.init_rez()

    Liste_button = st.sidebar.button("Zur Einkaufsliste hinzufügen")
    if Liste_button:
        user_name = fa.get_current_username()
        fa.rezepte_hinzufügen(user_name, st.session_state.random_rezept or input_rezept, personenanzahl)

    favoriten_button = st.sidebar.button(":hearts: Favorit")
    if favoriten_button:
        fa.init_rez_f()
        user_name = fa.get_current_username()
        fa.rezepte_hinzufügen_f(user_name, st.session_state.random_rezept or input_rezept)

# Zum Testen der Funktion können Sie `seite_3` einfach aufrufen:
# seite_3()
