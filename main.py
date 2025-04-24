import streamlit as st
import pandas as pd
import numpy as np
import math  # Importer math pour math.ceil

# Titre de l'application
st.write('# Hello World 👋')

# Champ de texte pour saisir un film préféré
x = st.text_input('🎬 Quel est ton film préféré ?')

# Affiche le film saisi
if x:
    st.write(f"🍿 Ton film préféré est : **{x}**")

# Bouton interactif
if st.button("Clique ici !"):
    st.write("🚀 Tu as cliqué sur le bouton.")

# Titres et mise en forme
st.write("## Ceci est un titre H2")

st.markdown("*Streamlit* est **vraiment** ***génial***.")
st.markdown('''
:red[Streamlit] :orange[peut] :green[écrire] :blue[du texte] :violet[en]
:gray[beaux] :rainbow[couleurs] et :blue-background[mettre en surbrillance].
''')
st.markdown("Voici un bouquet : :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# Exemple de texte multi-ligne
multi = '''Si tu termines une ligne avec deux espaces,  
un retour à la ligne doux est utilisé.

Deux (ou plusieurs) sauts de ligne donnent un retour dur.
'''
st.markdown(multi)

# Lecture d'un fichier CSV (vérifie que le fichier "movies.csv" est dans le même dossier)
try:
    data = pd.read_csv("movies.csv")
    st.write("### 📄 Données du fichier `movies.csv`")
    st.dataframe(data)
except FileNotFoundError:
    st.error("❌ Fichier 'movies.csv' introuvable. Vérifie qu'il est bien dans le dossier.")

# Données aléatoires pour les graphiques
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.write("### 📊 Diagramme en barres")
st.bar_chart(chart_data)

st.write("### 📈 Courbe linéaire")
st.line_chart(chart_data)

# Calculatrice de remboursement de prêt hypothécaire
st.title("Mortgage Repayments Calculator")

st.write("### Input Data")
col1, col2 = st.columns(2)  # Affichage en 2 colonnes
# Valeurs par défaut ou valeurs minimales/maximales
home_value = col1.number_input("Home Value", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)

# Calcul des paiements
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

# Affichage des paiements
total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.write("### Repayments")
col1, col2, col3 = st.columns(3)  # Création de 3 colonnes
col1.metric(label="Monthly Repayments", value=f"${monthly_payment:,.2f}")
col2.metric(label="Total Repayments", value=f"${total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"${total_interest:,.0f}")

# Création du plan de remboursement
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)  # Calcul de l'année du prêt
    schedule.append(
        [
            i,
            monthly_payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            year,
        ]
    )

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

# Affichage du plan de paiement sous forme de graphique
st.write("### Payment Schedule")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df)
