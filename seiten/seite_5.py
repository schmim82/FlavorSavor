import streamlit as st
import pandas as pd

from daten_code import Zutaten_daten as zd
from funktionen_code import Funktions_ablage as fa


def seite_5():


  st.title("Willkommen bei Flavorsavor")
  st.header("Entdecke die Kunst der Kulinarik")

  st.markdown("Mit unserer App tauchst du ein in die vielfältige Welt der internationalen Küche. Egal ob du nach einem bestimmten Land, einer speziellen Mahlzeit, vegetarischen Rezepten suchst oder einfach nicht weißt, was du kochen sollst – Flavorsavor hat für jeden Geschmack das passende Rezept.")
  st.markdown("\n")
  st.markdown("Features:")
  st.markdown("- Rezept Auswahl: Filtere nach Land, Mahlzeit oder vegetarischen Optionen.")
  st.markdown("- Personalisierte Mengenangaben: Automatische Anpassung der Zutatenmenge basierend auf der Anzahl der Personen.")
  st.markdown("- Einkaufsliste: Füge Rezepte zur Einkaufsliste hinzu und lass alle Zutaten automatisch addieren. Während dem Einkauf kannst du die Zutaten jeweils abhaken.")
  st.markdown("- Favoriten: Speichere deine Lieblingsrezepte für schnellen Zugriff.")
  st.markdown("- Random Rezept: Lass dich inspirieren, wenn du nicht weißt, was du kochen sollst.")
  st.markdown("Mit FlavorSavor wird Kochen zu einem kulinarischen Erlebnis. Viel Spaß beim Entdecken und Genießen!")
  fa.logo_anzeigen("logo.png", "Ja")









  
