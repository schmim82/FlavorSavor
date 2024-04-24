import streamlit as st
import pandas as pd
import re
#Rezepte als csv machen --> course, cuisine, recipe, ingrediants, amounts, preparation, vegi/vegan
rezepte_df = pd.read_csv('Kochbuch_App.csv', sep=';')


#Tab design
st.set_page_config(page_title="FlavorSavor", page_icon="🥗", layout="wide")

#App design
st.sidebar.title("FlavorSavor")
st.sidebar.subheader("Endecke die Welt der Kulinarik")

#Wählen Course: Vorspeise, Hauptspeise, Nachspeise --> nur 1 kann gewählt werden
choose_course = st.sidebar.radio("Wähle die gewünschte Mahlzeit aus", rezepte_df["course"].unique())
course_filtered_df = rezepte_df[rezepte_df["course"] == choose_course]

#Wählen Cuisine: italian, chinese, etc. --> mehrere können gewählt werden
choose_cuisine = st.sidebar.selectbox("Wähle die gewünschte/n Küche/n", course_filtered_df["cuisine"].unique())
cuisine_filtered_df = rezepte_df[rezepte_df["cuisine"] == choose_cuisine]

#Wählen: Vegetarisch
not_vegetarian = st.sidebar.checkbox("Vegetarisch")

#Wenn Vegetarisch, werden gewisse Rezepte nicht angezeigt
if not_vegetarian:
    cuisine_filtered_df = cuisine_filtered_df[cuisine_filtered_df['vegetarian'] != 'ja']
    

#Wählen: Rezept
choose_recipe = st.sidebar.selectbox("Wähle das gewünschte Gericht", cuisine_filtered_df['recipe'])
recipe_filtered_df = rezepte_df[rezepte_df["recipe"] == choose_recipe]
st.title(choose_recipe)

#Wählen: Personenanzahl
personenanzahl = st.sidebar.slider("Wähle die Personenanzahl aus", 1, 10, 2)
ingredients = recipe_filtered_df['ingredients']

def scale_mengen(ingredients, personenauswahl):
    scaled_ingredients = []
    for ingredient_list in ingredients.str.split(','):
        for ingredient in ingredient_list:
            match = re.match(r"\s*([\d.,]+)\s*([^\d]+)", ingredient)
            if match:
                num, item = match.groups()
                num = float(num)
                scaled_num = round((num / 4) * personenauswahl, 2)
                scaled_ingredients.append(f"{scaled_num} {item.strip()}")
    return scaled_ingredients

# Funktionsaufruf
scaled_ingredients = scale_mengen(ingredients, personenanzahl)

# Anzeige der skalierten Zutaten
st.subheader(f"Zutaten für {personenanzahl} Personen:")
for ingredient in scaled_ingredients:
    st.write(f"- {ingredient}")

st.header("Zubereitung:")
st.markdown(recipe_filtered_df['preparation'])