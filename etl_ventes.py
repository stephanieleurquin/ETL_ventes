import pandas as pd

# 1️⃣ Lire le CSV

df = pd.read_csv(r"C:\Users\leurq\Documents\ventes.csv")
# 2️⃣ Convertir les colonnes 'Prix' et 'Quantite' en numérique et supprimer les lignes invalides
df["Prix"] = pd.to_numeric(df["Prix"], errors="coerce")
df["Quantite"] = pd.to_numeric(df["Quantite"], errors="coerce")
df = df.dropna(subset=["Prix", "Quantite"])

# 3️⃣ Ajouter une colonne 'Total'
df["Total"] = df["Prix"] * df["Quantite"]

# 4️⃣ Sauvegarder dans un nouveau CSV
df.to_csv(r"C:\Users\leurq\Documents\ventes_clean.csv", index=False)
print("Pipeline ETL terminé ! Fichier 'ventes_clean.csv' créé sur le Bureau.")