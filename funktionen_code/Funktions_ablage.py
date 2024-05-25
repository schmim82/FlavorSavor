import streamlit as st
import pandas as pd
import re
from daten_code import Zutaten_daten as zd
import random

DATA_FILE = "test.csv"
DATA_COLUMNS = ['name', 'rezept', 'anzahl']




def csv_reader(csv):
    return pd.read_csv(csv, sep= ";")





#rezepte Listen nach eingaben von Kriterien generieren
def rezepte_L_gen(course_v, herkunft_v, veg_v, df):
    df_kriterien = df[df[course_v]>0]

    if veg_v:
        df_kriterien = df_kriterien[df_kriterien["Vegetarisch"]>0]

    df_kriterien = df_kriterien[df_kriterien[herkunft_v]>0]

    rezepte_pn = df_kriterien["Rezepte"]
    liste = rezepte_pn.tolist()

    return liste



#Ausgabe von Rezepte mit der Liste von Zutaten

def zutaten_ausgabe(rezept, kochbuch, anzahl):
    st.title(rezept)
    st.markdown("\n")

    dictionary = kochbuch[rezept]

    variable = 0
    Zubereitung_text = []

    for key in dictionary:
         

        words = key.split()
        

        if words[0] == "Zubereitung":

            Zubereitung_text.append(dictionary[key])

        else:

            if isinstance(dictionary[key], int) or isinstance(dictionary[key], float):           


                per_vol = (dictionary[key]/4)*anzahl
            

                if len(words) == 1:
                    st.markdown(f" {key} -- {per_vol} gramm")        
                    st.markdown("\n")

                else:
                    st.markdown(f" {key} -- {per_vol}")        
                    st.markdown("\n")
            
            else:
                st.markdown(f" {key} -- {dictionary[key]}")
                st.markdown("\n")


    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")

    for values in Zubereitung_text:
        variable += 1
        
        st.markdown(f"{variable}. {values}")



#Ausgabe von Herkunft_L:

def herkunft_gen(df):

    bekannte_werte = ["Rezepte", "Vorspeise", "Hauptspeise", "Nachspeise", "Vegetarisch"]
    herkunft_L = []

    for spalte in df.columns:
        if spalte not in bekannte_werte:
            herkunft_L.append(spalte)

    return herkunft_L



#einkaufsliste

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
    """Speichere das DataFrame in einer CSV-Datei."""
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

    df = show_dataframe()
    df_kriterien = df[df["name"] == name]
   

    new_data_df = df_kriterien[df["rezept"] != rezept]

    daten_hochladen(new_data_df)




    

def einkaufsliste_erstellen(einkaufsliste, Kochbuch):
    leere_dic = {}

    

    for key in einkaufsliste:
        dictionary = Kochbuch[key]

        anzahl = einkaufsliste[key]

        for key in dictionary:

            words = key.split()
        

            if words[0] != "Zubereitung":

                if key not in leere_dic:

                    if isinstance(dictionary[key], int) or isinstance(dictionary[key], float):
                        leere_dic[key] = dictionary[key] * anzahl

                    else:
                        leere_dic[key] = dictionary[key]

                else:

                    if isinstance(dictionary[key], int) or isinstance(dictionary[key], float):
                        leere_dic[key] = leere_dic[key] + (dictionary[key] * anzahl)

    for key in leere_dic:
        st.markdown(f"{key} -- {leere_dic[key]}")




#random rezept ausgabe

def random_rez(df):
    rez_liste = df["Rezepte"].tolist()
    zufalls_rezept = random.choice(rez_liste)
    return zufalls_rezept


