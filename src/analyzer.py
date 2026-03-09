import uuid
import time



# Générer les identifiants unique de chaque CV déjà enregistré
def generate_id():
    """
    Génère les iDs des différents CVs 
    """
    return str(uuid.uuid4())


# Validation logique de la date de début et de la date de fin d'une expérience professionnel
def validate_date(cv_list):
    """
    Valide les dates de début et de fin des CVs enregistrés.  
    """
    for item in cv_list:
        for row in item['experience']:
            date_debut = row['debut']
            date_fin = row['fin']
            if date_fin != "Présent":
                str_debut = time.strptime(date_debut, "%Y-%m")
                str_fin = time.strptime(date_fin, "%Y-%m")
                if str_debut > str_fin:
                    raise ValueError(f"{date_debut} est après {date_fin}, ce qui est incorrect.")
    return cv_list

# Partie analyse: analyse des données quantitatifs de chaque CV enregistré
def skills_count(cv_list):
    """
    Affiche le nombre de compétence dans les CVs enregistrés.  
    """
    skill_count = dict()
    for item in cv_list:
        for row in item['competence']:
            if row not in skill_count:
                skill_count[row] = 0
            skill_count[row] += 1
    return (
        f"Top compétences: {skill_count}"
    )

def cities_count(cv_list):
    """
    Affiche le nombre de fois qu'une ville apparait par CVs enregistrés.  
    """
    count_city = dict()
    for item in cv_list:
        city = item['identite']['adresse']['ville']
        if city not in count_city:
            count_city[city] = 0
        count_city[city] += 1
    return (
        f"Villes: {count_city}"
    )

def languages_count(cv_list):
    """
    Affiche le nombre de langue dans chaque CV enregistré.  
    """
    count_language = dict()
    for item in cv_list:
        for lang in item['langue']:
            if lang not in count_language:
                count_language[lang] = 0
            count_language[lang] += 1
    return (
        f"Langues: {count_language}"
    )

def calculate_average_experience(cv_list):
    """
    Calcule la moyenne des expériences de chaque CV enregistrés.  
    """
    total_CV = 0
    total_exp = 0
    for item in cv_list:
        total_CV += 1
        for row in item['experience']:
            total_exp += 1
    
    try:
        
        average = total_exp/0

    except ZeroDivisionError: 

        print("Erreur: Division par zéro")

    except Exception:
        average = total_exp/total_CV 
    

    return (
        f"Total de CV: {total_CV}"
        f"Expériences moyennes : {average}"
    )

# PARTIE générer rapport:
def screen_report(cv_list):
    """
    Affiche la rapport des données statistiques.  
    """
    return (
        "===== CV DATA ANALYSIS ====="
        f"\n{calculate_average_experience(cv_list)}"
        f"\n{skills_count(cv_list)}"
        f"\n{languages_count(cv_list)}"
        f"\n{cities_count(cv_list)}"
    )