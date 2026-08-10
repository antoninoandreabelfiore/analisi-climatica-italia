# analisi-climatica-italia
Analisi esplorativa dei dati meteorologici di Milano, Roma e Napoli tramite API (2019-2023).
# 🌦️ Analisi Climatica delle Città Italiane (2019-2023)

## 🎯 Obiettivo del Progetto
Questo progetto analizza i dati meteorologici storici di tre principali città italiane (Milano, Roma, Napoli) negli ultimi 5 anni. L'obiettivo è esplorare le tendenze climatiche, la stagionalità e le differenze geografiche estraendo dati reali e aggiornati.

## 🛠️ Strumenti e Competenze Utilizzate
* **Linguaggio:** Python
* **Raccolta Dati:** API REST (Open-Meteo), libreria `requests`
* **Data Cleaning & Manipolazione:** `pandas` (gestione date, feature engineering)
* **Data Visualization:** `matplotlib`, `seaborn`

## ⚙️ Fasi del Progetto
1. **Data Collection:** Script Python per interrogare l'API di Open-Meteo tramite ciclo iterativo, estraendo temperature e precipitazioni per coordinate geografiche.
2. **Data Cleaning:** Conversione delle date in formato `datetime`, verifica dell'assenza di valori nulli, e creazione di nuove feature analitiche (es. Temperatura Media, Anno, Mese).
3. **Data Visualization (EDA):** Creazione di boxplot, lineplot e barplot per estrarre insight di business/ambientali.

## 📊 Key Insights (Cosa dicono i dati)
* **Escursione Termica:** Milano presenta l'escursione termica annuale più ampia, mentre Napoli mantiene un clima generalmente più mite e costante, come evidenziato dalla distribuzione dei dati nel Boxplot.
* **Stagionalità Costante:** Le tre città seguono una curva di stagionalità identica. Tuttavia, le linee di tendenza non si incrociano mai nel corso dei 5 anni analizzati, confermando una rigida gerarchia termica da Nord a Sud.


## 🚀 Come visualizzare il progetto
Puoi leggere tutto il codice, i commenti passo-passo e visualizzare i grafici generati aprendo il file `.ipynb` presente in questa repository.
