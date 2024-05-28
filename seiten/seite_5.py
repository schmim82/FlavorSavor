import streamlit as st
import pandas as pd

from daten_code import Zutaten_daten as zd
from funktionen_code import Funktions_ablage as fa


def seite_5():


  st.title("Willkommen bei Flavorsavor")
  st.header("Entdecke die Kunst der Kulinarik")
  st.subheader("Mit unserer App tauchst du ein in die vielfältige Welt der internationalen Küche. Egal ob du nach einem bestimmten Land, einer speziellen Mahlzeit, vegetarischen Rezepten suchst oder einfach nicht weißt, was du kochen sollst – Flavorsavor hat für jeden Geschmack das passende Rezept.

Features:
- Rezept Auswahl: Filtere nach Land, Mahlzeit oder vegetarischen Optionen.
- Personalisierte Mengenangaben: Automatische Anpassung der Zutatenmenge basierend auf der Anzahl der Personen.
- Einkaufsliste: Füge Rezepte zur Einkaufsliste hinzu und lass alle Zutaten automatisch addieren. Während dem Einkauf kannst du die Zutaten jeweils abhaken.
- Favoriten: Speichere deine Lieblingsrezepte für schnellen Zugriff.
- Random Rezept: Lass dich inspirieren, wenn du nicht weißt, was du kochen sollst.

Mit FlavorSavor wird Kochen zu einem kulinarischen Erlebnis. Viel Spaß beim Entdecken und Genießen!")
  
