import streamlit as st
import pandas as pd

from daten_code import Zutaten_daten as zd
from funktionen_code import Funktions_ablage as fa


def get_current_username():
    """Funktion zum Abrufen des aktuellen Benutzernamens."""
    return st.session_state.get('username', None)



def init_github_rez():
    """Initialisiere das GithubContents-Objekt."""
    if 'github' not in st.session_state:
        st.session_state.github = GithubContents(
            st.secrets["github"]["owner"],
            st.secrets["github"]["repo"],
            st.secrets["github"]["token"])
        print("GitHub initialisiert")

def init_rez():
    """Initialisiere oder lade das DataFrame."""
    if 'df_liste' not in st.session_state:
        if st.session_state.github.file_exists(DATA_FILE):
            st.session_state.df_liste = st.session_state.github.read_df(DATA_FILE)
        else:
            st.session_state.df_liste = pd.DataFrame(columns=DATA_COLUMNS)

def save_to_csv_rez(dataframe):

    st.session_state.github.write_df(DATA_FILE, dataframe, "updated CSV")

def daten_hochladen(new_data_df):
    init_github_rez() # Initialisiere das GithubContents-Objekt
    init_rez() # Lade die informationen aus dem GitHub-Datenrepository

# DataFrame aktualisieren
    st.session_state.df_liste = pd.concat([st.session_state.df_liste, new_data_df], ignore_index=True)

# DataFrame in CSV-Datei speichern
    save_to_csv_rez(st.session_state.df_liste)


def show_dataframe():
    dataframe = st.session_state.df_liste
    
    return dataframe









def rezepte_hinzufügen(name, rezept, anzahl):

    
    df = show_dataframe()
    df_kriterien = df[df["name"] == name]
   

    if rezept in df_kriterien["rezept"].values:
        st.markdown("schon vorhanden")

    else:
        new_data = {'name': [name], 'rezept': [rezept], 'anzahl': [anzahl]}
        new_data_df = pd.DataFrame(new_data)

        daten_hochladen(new_data_df)





def rezept_entfernen(name, rezept):

    init_rez()

    if rezept == "alle":
        df_filtered = st.session_state.df_liste[st.session_state.df_liste["name"] == name]

        if not df_filtered.empty:

            st.session_state.df_liste.drop(df_filtered.index, inplace = True)

            save_to_csv_rez(st.session_state.df_liste)
            st.success(f" Alle Rezepte für {name} wurden a us der Einkaufsliste entfernt.")

        else:
            st.warning(f"Keine Rezepte für {name} in der Einkaufsliste gefunden.")

    else:
        df_filtered = st.session_state.df_liste[(st.session_state.df_liste["name"] == name) & (st.session_state.df_liste["rezept"] == rezept)]

        if not df_filtered.empty:
            st.session_state.df_liste.drop(df_filtered.index, inplace=True)
            save_to_csv_rez(st.session_state.df_liste)
            st.success(f"{rezept} wurde aus der Einkaufsliste entfernt.")
        else:
            st.warning(f"Das Rezept {rezept} konnte nicht aus der Einkaufsliste entfernt werden.")





def seite_4():

  st.title("Favoriten)


           
