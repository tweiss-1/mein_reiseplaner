import streamlit as st
import pandas as pd

# Konfiguration der Seite
st.set_page_config(page_title="Reise-Planer", page_icon="✈️")

st.title("✈️ Smart Trip Planner")
st.write("Berechne, wie lange dein Budget in deiner Traumstadt reicht!")

# --- SEITENLEISTE (Eingaben) ---
st.sidebar.header("Reise-Details")
stadt = st.sidebar.selectbox("Wohin soll es gehen?", ["Berlin", "Paris", "London", "Tokio", "New York"])
budget = st.sidebar.number_input("Gesamtbudget (€)", min_value=100, value=1000, step=50)
stil = st.sidebar.radio("Reisestil", ["Backpacker (günstig)", "Standard", "Luxus"])

# --- DATEN (Durchschnittskosten pro Tag) ---
# In einer echten App könnten diese Daten aus einer Datenbank kommen
preise = {
    "Berlin": {"Backpacker": 50, "Standard": 100, "Luxus": 250},
    "Paris": {"Backpacker": 70, "Standard": 140, "Luxus": 350},
    "London": {"Backpacker": 80, "Standard": 160, "Luxus": 400},
    "Tokio": {"Backpacker": 60, "Standard": 130, "Luxus": 300},
    "New York": {"Backpacker": 100, "Standard": 200, "Luxus": 500}
}

# --- BERECHNUNG ---
tageskosten = preise[stadt][stil]
tage_moeglich = int(budget / tageskosten)

# --- ANZEIGE ---
st.header(f"Dein Trip nach {stadt}")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Mögliche Reisedauer", value=f"{tage_moeglich} Tage")
with col2:
    st.metric(label="Kosten pro Tag", value=f"{tageskosten} €")

# Ein kleiner visueller Check
if tage_moeglich > 0:
    st.info(f"Mit {budget} € kannst du {tage_moeglich} Tage in {stadt} als {stil} verbringen.")
    
    # Visualisierung der Budgetverteilung (Beispielgrafik)
    st.subheader("Budget-Aufteilung (Schätzung)")
    anteile = pd.DataFrame({
        "Kategorie": ["Unterkunft", "Verpflegung", "Aktivitäten"],
        "Anteil (€)": [tageskosten*0.5, tageskosten*0.3, tageskosten*0.2]
    })
    st.bar_chart(data=anteile, x="Kategorie", y="Anteil (€)")
else:
    st.error("Dein Budget ist leider zu niedrig für diesen Reisestil in dieser Stadt.")

if st.button("Reise planen!"):
    st.balloons()
