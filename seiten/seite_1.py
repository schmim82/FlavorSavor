import streamlit as st
import pandas as pd

from daten_code import Zutaten_daten as zd
from funktionen_code import Funktions_ablage as fa


def seite_1():
    def csv_reader(csv):
        return pd.read_csv(csv, sep= ";")

    Rezepte_dataframe = csv_reader("Rezepte_dataframe.csv")


    #App Design
    
    st.sidebar.title("Flavorsavor")
    st.sidebar.subheader("Entdecke die Welt der Kulinarik")



    herkunft_L = fa.herkunft_gen(Rezepte_dataframe)


#Kriterien Angabe
    choose_course = st.sidebar.radio("Wähle die gewünschte Mahlzeit aus", zd.Speise_L)
    choose_herkunft = st.sidebar.selectbox("Wähle die Herkunft des Gerichts aus", herkunft_L)
    vegetarian = st.sidebar.checkbox("Vegetarisch")


#Liste nach Kriterien generieren
    rezepte_liste = fa.rezepte_L_gen(choose_course, choose_herkunft, vegetarian, Rezepte_dataframe)

    if len(rezepte_liste) == 0:
        st.title("Leider ist kein Gericht mit diesen Kriterien Hinterlegt")





#Rezept wählen

    choose_recipe = st.sidebar.selectbox("Wähle das gewünschte Gericht", rezepte_liste)
    personenanzahl = st.sidebar.slider("Wähle die Personenanzahl aus", 1, 10, 2)


    
        
    fa.zutaten_ausgabe(choose_recipe, zd.Kochbuch, personenanzahl)






    
    DATA_FILE = "test.csv"
    DATA_COLUMNS = ['name', 'rezept', 'anzahl']
    
    fa.init_rez()

    Liste_button = st.sidebar.button("Zur Einkaufsliste hinzufügen")
    
    if Liste_button:

        user_name = fa.get_current_username()


        fa.rezepte_hinzufügen(user_name, choose_recipe, personenanzahl)


    favoriten_button = st.sidebar.button(":hearts: Favorit")

    if favoriten_button:

        fa.init_rez_f()

        user_name = fa.get_current_username()

        fa.rezepte_hinzufügen_f(user_name, choose_recipe)










