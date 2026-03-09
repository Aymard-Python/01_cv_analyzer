# CV Data Analyzer

Mini projet Python permettant d’analyser des CV stockés au format JSON.

L’objectif du projet est d’extraire des informations utiles à partir de données de CV afin de produire des statistiques et préparer une future plateforme de publication et d’analyse de profils professionnels.

---

# How to Run the Project

Clone the repository :

git clone https://github.com/Aymard-Python/01_cv_analyzer.git

Navigate to the project folder :

cd 01_cv_analyzer

Run the program :

python src/main.py

---

# Project Overview

Ce projet analyse un ensemble de CV afin d'extraire des informations utiles comme :

- les compétences les plus fréquentes
- les loisirs les plus fréquents
- le nombre d’expériences par candidat
- les années d'expérience
- des statistiques générales sur les candidats

Ce projet fait partie d'une **roadmap de 60 jours visant à construire progressivement une plateforme de publication et d’analyse de CV en Python.**

---

# Current Features

Le projet contient actuellement des fonctions de **chargement et de validation des données** :

- Chargement des CV depuis un fichier JSON
- `validate_schema` : vérifie la structure globale du CV
- `validate_content` : vérifie la validité des données
- `check_required_fields` : vérifie la présence des champs obligatoires
- `validate_string_list` : vérifie les valeurs autorisées dans certaines listes

validator.py → contient les fonctions de validation des données CV (validate_schema, validate_content, etc.)

Ces validations permettent de s’assurer que les données analysées sont cohérentes avant d’effectuer des statistiques.

---

# Planned Features

Fonctionnalités prévues pour les prochaines étapes :

### Validation des données
- validation des emails
- validation des numéros de téléphone
- amélioration du contrôle des types de données

### Qualité du code
- ajout de tests unitaires avec **pytest**
- ajout du typage avec **typing**
- ajout du **logging**

### Analyse des données
- analyse des compétences
- calcul des compétences les plus fréquentes
- analyse des loisirs les plus fréquents
- calcul du nombre d’expériences par candidat
- calcul des années d’expérience

### Statistiques globales
- statistiques générales sur les candidats
- génération d’un rapport résumé

---

# Tech Stack

- Python
- JSON
- Data Validation en Python pur (sans librairies externes)

Prévu pour les étapes futures :

- Pandas (analyse avancée)
- Pytest (tests unitaires)

---

## Project Structure

01_cv_analyzer/
│
├── data/
│   └── cvs.json
│
├── src/
│   ├── loader.py
│   ├── analyzer.py
│   ├── validator.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md

---

# Future Vision

Ce projet constitue la **première étape d’une plateforme complète de gestion et d’analyse de CV**, 
qui pourra inclure :

- publication de CV
- analyse automatique des profils
- statistiques sur les compétences du marché
- recommandation de profils

---