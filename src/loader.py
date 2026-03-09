import json

file_name = "../data/cvs.json"
# Lecture et ouverture des CV déjà enregistré 
def reader_cv_json(file_name):
    """
    Permet d'ouvrir les différents CVs enregistrés.  
    """
    try:
        with open(file_name, 'r', encoding="utf-8") as f:
            cv_list = json.load(f)
            return cv_list
    except FileNotFoundError:
        print(f"Erreur: le fichier {file_name} n'existe pas.")
        return []
    except json.JSONDecodeError:
        print(f'Erreur: le fichier {file_name} est vide ou mal formaté.')
        return []