import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title = "Noten", page_icon = "🏫", layout="wide")

st.title("Noten Rechner")



# Listen initialisieren oder aus dem Cache laden
list_names = ["Mathe Noten", "Physik Noten", "Englisch Noten", "Biologie Noten"]
selected_list_name = st.selectbox("Wähle ein Fach aus:", list_names)

if selected_list_name not in st.session_state:
    st.session_state[selected_list_name] = []

# Eingabe einer Zahl
new_number = st.number_input("Gib eine Note ein und drücke Enter, um sie dem Fach hinzuzufügen:", value=0.0)

if st.button("Hinzufügen"):
    # Hinzufügen der neuen Zahl zur ausgewählten Liste
    st.session_state[selected_list_name].append(new_number)
    st.success(f"Die Zahl {new_number} wurde erfolgreich zur {selected_list_name} hinzugefügt!")

# Alle Listen anzeigen


for list_name in list_names:
    st.write(f"Aktuelle {list_name}:", st.session_state[list_name])

    


# Alle Listen in ein Dictionary sammeln und auf die gleiche Länge bringen
max_length = max(len(st.session_state[list_name]) for list_name in list_names)
data = {list_name: st.session_state[list_name] + [np.nan] * (max_length - len(st.session_state[list_name])) for list_name in list_names}

# DataFrame erstellen
df = pd.DataFrame(data)

# DataFrame anzeigen
st.write("Noten in DataFrame:")
st.write(df)

st.sidebar.line_chart(df)







