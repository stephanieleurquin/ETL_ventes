📊 ETL_ventes
Description

ETL_ventes est un script Python qui automatise le traitement des données de ventes selon le principe ETL (Extract, Transform, Load).

Fonctionnement

📥 Extract : lecture du fichier ventes.csv

🔄 Transform : nettoyage des données et calcul du total (Prix × Quantite)

📤 Load : création d’un nouveau fichier ventes_clean.csv prêt pour analyse

Technologies utilisées

Python

Pandas

Comment exécuter le script

Placer ventes.csv dans le même dossier que ETL_ventes.py

Ouvrir l’invite de commandes

Lancer :

python ETL_ventes.py

Un fichier ventes_clean.csv sera automatiquement généré.