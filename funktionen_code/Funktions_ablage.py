import streamlit as st
import pandas as pd
import re
from daten_code import Zutaten_daten as zd

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