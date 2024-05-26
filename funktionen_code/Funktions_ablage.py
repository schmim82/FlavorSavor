import streamlit as st
import pandas as pd
import re
from daten_code import Zutaten_daten as zd
import random
import os

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

def get_image_list():
    image_dir = os.path.join(os.path.dirname(__file__),"..", 'images')
    return [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('png', 'jpg', 'jpeg', 'gif'))]


 def bild_anzeigen(bild, bilder_liste):
 
    if bild in [os.path.basename(img) for img in bilder_liste]:

        st.image(os.path.join("Funktions_ablage", 'images', bild), use_column_width=True, output_format='PNG')
    else:
        st.markdown("")



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

        elif key == "Bild":
            continue

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

#    bilder_liste = get_image_list()
#    bild = dictionary.get("Bild")

#    if bild:
#        bild_anzeigen(bild,bilder_liste)
        
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

    init_rez()  # Initialisiere oder lade das DataFrame

    # Filtere den DataFrame nach den Kriterien (Name und Rezept)
    df_filtered = st.session_state.df_liste[(st.session_state.df_liste["name"] == name) & (st.session_state.df_liste["rezept"] == rezept)]

    if not df_filtered.empty:
        # Lösche die Zeilen mit den angegebenen Kriterien
        st.session_state.df_liste.drop(df_filtered.index, inplace=True)
        # Speichere den aktualisierten DataFrame in der CSV-Datei
        save_to_csv_rez(st.session_state.df_liste)
        st.success(f' "{rezept}" wurde aus der Einkaufsliste entfernt.')
    else:
        st.warning('Die angegebenen Daten wurden nicht gefunden.')




    

def einkaufsliste_erstellen(einkaufsliste, Kochbuch):
    leere_dic = {}
    leere_dic_2 = {}

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
                        leere_dic[key] += dictionary[key] * anzahl

    for key in leere_dic:
        if isinstance(leere_dic[key], int) or isinstance(leere_dic[key], float):
            leere_dic_2[key] = leere_dic[key]
        else:
            words_2 = key.split()
            if words_2[0] not in leere_dic_2:
                leere_dic_2[words_2[0]] = ""

    for key in leere_dic_2:
        words_3 = key.split()
        if leere_dic_2[key] != "":
            if len(words_3) == 1:
                # Markdown-Text mit Checkbox anzeigen
                checkbox_key = st.checkbox(f"{key} -- {leere_dic_2[key]} gramm")
            else:
                checkbox_key = st.checkbox(f"{key} -- {leere_dic_2[key]}")
        else:
            checkbox_key = st.checkbox(f"{key}")





#random rezept ausgabe

def random_rez(df):
    rez_liste = df["Rezepte"].tolist()
    zufalls_rezept = random.choice(rez_liste)
    return zufalls_rezept


#bilder anzeigen






