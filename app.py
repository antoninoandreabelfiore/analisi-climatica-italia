import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

# 1. Configurazione della pagina Web
st.set_page_config(page_title="Meteo Dashboard", page_icon="🌦️", layout="wide")
st.title("🌦️ Dashboard Climatica Italiana (2019-2023)")
st.markdown("Esplora i dati meteorologici di **Milano**, **Roma** e **Napoli** in modo interattivo.")


# 2. Funzione per scaricare e pulire i dati (con Cache per non ripetere il download!)
@st.cache_data
def carica_dati():
    citta = {
        "Milano": {"lat": 45.46, "lon": 9.19},
        "Roma": {"lat": 41.90, "lon": 12.49},
        "Napoli": {"lat": 40.85, "lon": 14.26}
    }
    url = "https://archive-api.open-meteo.com/v1/archive"
    tutti_i_dati = []

    for nome_citta, coordinate in citta.items():
        parametri = {
            "latitude": coordinate["lat"],
            "longitude": coordinate["lon"],
            "start_date": "2019-01-01",
            "end_date": "2023-12-31",
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
            "timezone": "Europe/Berlin"
        }
        risposta = requests.get(url, params=parametri)
        if risposta.status_code == 200:
            df_temp = pd.DataFrame(risposta.json()['daily'])
            df_temp['citta'] = nome_citta
            tutti_i_dati.append(df_temp)
            time.sleep(0.5)

    df = pd.concat(tutti_i_dati, ignore_index=True)

    # Pulizia dati (La nostra Fase 3)
    df = df.rename(columns={
        'time': 'data', 'temperature_2m_max': 'temp_max',
        'temperature_2m_min': 'temp_min', 'precipitation_sum': 'precipitazioni_mm'
    })
    df['data'] = pd.to_datetime(df['data'])
    df['temp_media'] = (df['temp_max'] + df['temp_min']) / 2
    df['anno'] = df['data'].dt.year
    df['mese'] = df['data'].dt.month

    return df


# Mostriamo un messaggio di caricamento mentre scarica i dati la prima volta
con_spinner = st.spinner("Scaricamento dati dall'API di Open-Meteo in corso...")
with con_spinner:
    df_pulito = carica_dati()

# 3. INTERATTIVITÀ: Creiamo una barra laterale per i filtri
st.sidebar.header("Filtra i Dati")
citta_selezionata = st.sidebar.selectbox("Seleziona una città", df_pulito['citta'].unique())
anno_selezionato = st.sidebar.slider("Seleziona l'anno", 2019, 2023, 2023)

# Filtriamo il dataframe in base alle scelte dell'utente
df_filtrato = df_pulito[(df_pulito['citta'] == citta_selezionata) & (df_pulito['anno'] == anno_selezionato)]

# 4. VISUALIZZAZIONE: Creiamo il layout della pagina
st.subheader(f"Statistiche per {citta_selezionata} nel {anno_selezionato}")

# Metriche rapide in alto (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura Massima Registrata", f"{df_filtrato['temp_max'].max()} °C")
col2.metric("Temperatura Minima Registrata", f"{df_filtrato['temp_min'].min()} °C")
col3.metric("Precipitazioni Totali Annuali", f"{df_filtrato['precipitazioni_mm'].sum():.1f} mm")

st.divider()  # Linea di separazione

# Grafico
st.subheader("Andamento delle Temperature Medie")
fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(x='data', y='temp_media', data=df_filtrato, ax=ax, color='#1f77b4')
plt.title(f"Temperature a {citta_selezionata} ({anno_selezionato})")
plt.xlabel("Data")
plt.ylabel("Temp Media (°C)")
st.pyplot(fig)  # Comando Streamlit per mostrare un grafico Matplotlib!

# Mostriamo anche la tabella dati grezza (nascosta in un menu a tendina)
with st.expander("Mostra il Dataset filtrato"):
    st.dataframe(df_filtrato)