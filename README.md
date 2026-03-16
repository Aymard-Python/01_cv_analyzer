# CV Data Analyzer

CV Data Analyzer est un mini projet Python permettant d’analyser des CV stockés au format **JSON**.

Le programme valide la structure des CV, extrait les informations importantes et produit des **statistiques sur les profils professionnels**.

Ce projet fait partie d'une **roadmap de 60 jours visant à construire progressivement une plateforme de publication et d’analyse de CV en Python**.

---

# Project Goals

L’objectif du projet est de :

* valider la structure et la qualité des données CV
* extraire les informations clés (compétences, expériences, diplômes, villes…)
* produire des statistiques sur les profils
* générer un rapport d’analyse automatisé

Le projet est conçu comme un **mini pipeline d’analyse de données**.

---

# How to Run the Project

Clone the repository :

```
git clone https://github.com/Aymard-Python/01_cv_analyzer.git
```

Navigate to the project folder :

```
cd 01_cv_analyzer
```

Run the program :

```
python src/main.py
```

---

# Data Processing Pipeline

Le programme suit un pipeline d’analyse en plusieurs étapes :

```
Load JSON Data
      ↓
Validate Data Structure
      ↓
Validate Content
      ↓
Extract Relevant Information
      ↓
Analyze Statistics
      ↓
Generate Analysis Report
```

Ce pipeline permet de transformer un simple dataset de CV en **statistiques exploitables**.

---

# Current Features

Le projet inclut actuellement les fonctionnalités suivantes :

### Data Loading

* Chargement des CV depuis un fichier JSON
* Gestion des erreurs de fichier

Module concerné :

```
loader.py
```

---

### Data Validation

Validation complète des données avant analyse :

* `validate_schema()` : vérifie la structure globale du CV
* `validate_content()` : vérifie la cohérence des données
* `check_required_fields()` : vérifie la présence des champs obligatoires
* `validate_string_list()` : vérifie les valeurs autorisées dans certaines listes
* validation des dates d'expérience

Module concerné :

```
validator.py
```

---

### Data Extraction

Extraction des informations utiles depuis les CV :

* diplômes
* compétences
* entreprises
* postes occupés
* langues
* loisirs
* villes
* dates d’expérience
* durée d’expérience

Module concerné :

```
extractor.py
```

---

### Statistical Analysis

Analyse des données extraites :

* compétences les plus fréquentes
* loisirs les plus fréquents
* postes les plus fréquents
* entreprises les plus présentes
* répartition des villes
* moyenne d’expériences par candidat
* durée moyenne d’expérience

Module concerné :

```
analyzer.py
```

---

# Example Statistics

Le programme peut produire des statistiques comme :

```
Total CV analyzed : 3

Most common skills :
Python : 2
Javascript : 2
SQL : 2

Most common job :
Développeur Web

Cities :
Yaoundé : 2
Douala : 1
```

---

# Project Structure

```
01_cv_analyzer/
│
├── data/
│   └── cvs.json
│
├── src/
│   ├── loader.py
│   ├── validator.py
│   ├── extractor.py
│   ├── analyzer.py
│   ├── report.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Tech Stack

* Python
* JSON
* Data validation en Python pur (sans librairies externes)

Technologies prévues pour les prochaines étapes :

* **Pandas** pour l’analyse avancée
* **Pytest** pour les tests unitaires
* **Typing** pour le typage statique
* **Logging** pour la gestion des logs

---

# Planned Improvements

Améliorations prévues :

### Data Validation

* validation des emails
* validation des numéros de téléphone
* amélioration du contrôle des types de données

### Code Quality

* ajout de tests unitaires avec **pytest**
* ajout du **typing**
* ajout du **logging**

### Data Analysis

* amélioration des statistiques
* analyse des compétences du marché
* analyse des tendances des profils

### Reporting

* génération automatique d’un **rapport d’analyse**
* export des statistiques

---

# Future Vision

Ce projet constitue la **première étape d’une plateforme complète de gestion et d’analyse de CV**, qui pourra inclure :

* publication de CV
* analyse automatique des profils
* statistiques sur les compétences du marché
* recommandation de profils
* tableau de bord de visualisation

---

# Author

Projet réalisé dans le cadre d’une **roadmap personnelle de progression en Python et Data Analysis**.
