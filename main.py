import streamlit as st
import pandas as pd
import re
from daten_code import Zutaten_daten as zd
from funktionen_code import Funktions_ablage as fa



# Funktionen, welche nach Funktions_ablage.py kopiert werden

def csv_reader(csv):
    return pd.read_csv(csv, sep= ";")






#Code ab hier


Rezepte_dataframe = csv_reader("Rezepte_dataframe.CSV")


#App Design
st.set_page_config(page_title="FlavorSavor")
st.sidebar.title("Flavorsavor")
st.sidebar.subheader("Entdecke die Welt der Kulinarik")

#Kriterien generieren

herkunft_L = fa.herkunft_gen(Rezepte_dataframe)

#Kriterien Angabe
choose_course = st.sidebar.radio("Wähle die gewünschte Mahlzeit aus", zd.Speise_L)
choose_herkunft = st.sidebar.selectbox("Wähle die Herkunft des Gerichts aus", herkunft_L)
vegetarian = st.sidebar.checkbox("Vegetarisch")


#Liste nach Kriterien generieren
rezepte_liste = fa.rezepte_L_gen(choose_course, choose_herkunft, vegetarian, Rezepte_dataframe)

if len(rezepte_liste) == 0:
    st.title("Leider ist kein Gericht mit diesen Kriterien Hinterlegt")


    #Habe noch den fehler, das der Error trotzdem angezeigt wird





def rezept_markdown(rezept):
    st.title(rezept)
    variable = 0
    for item in zd.Kochbuch[rezept]:
        variable += 1
        st.markdwon(variable, item)

        




#Rezept wählen

choose_recipe = st.sidebar.selectbox("Wähle das gewünschte Gericht", rezepte_liste)
personenanzahl = st.sidebar.slider("Wähle die Personenanzahl aus", 1, 10, 2)

fa.zutaten_ausgabe(choose_recipe, zd.Kochbuch, personenanzahl)



