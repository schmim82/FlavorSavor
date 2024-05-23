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

#random
    random_checkbox = st.sidebar.checkbox("Random Rezept")
    if random_checkbox:
        st.session_state.random_rezept = fa.random_rez(Rezepte_dataframe)

        fa.zutaten_ausgabe(st.session_state.random_rezept, zd.Kochbuch, personenanzahl)

    else:
        if "random_rezept" not in st.session_state:
            st.session_state.random_rezept = choose_recipe
        fa.zutaten_ausgabe(st.session_state.random_rezept, zd.Kochbuch, personenanzahl)





    
    DATA_FILE = "test.csv"
    DATA_COLUMNS = ['Name', 'Rezept', 'Anzahl']
    
    fa.init_rez()

    Liste_button = st.sidebar.button("Zur Liste hinzufügen")
    
    if Liste_button:

        user_name = fa.get_current_username()


        fa.rezepte_hinzufügen(user_name, choose_recipe, personenanzahl)









