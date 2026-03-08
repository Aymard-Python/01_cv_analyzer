# CV Data Analyzer

Mini projet Python permettant d’analyser des CV stockés au format JSON.

## Project Overview
Ce projet analyse un ensemble de CV afin d'extraire des informations utiles comme :
- les compétences les plus fréquentes
- les années d'expérience
- des statistiques générales sur les candidats

Ce projet fait partie d'une **roadmap de 60 jours pour construire progressivement une plateforme de publication de CV en Python.**

---

## Features
- Chargement de données CV depuis un fichier JSON
- Validation des données (Data Validation pur en Python)
- Analyse des compétences
- Statistiques sur l'expérience professionnelle
- Génération d'un rapport résumé

---

## Tech Stack
- Python pur
- JSON
- Data Validation sans librairies externes
- (Pandas prévu pour plus tard, mais non installé actuellement)

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
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md