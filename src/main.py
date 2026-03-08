import json
import uuid
import time

value = [
    'id',
    'identite',
    'experience',
    'competence',
    'langue',
    'loisir', 
]
VALUE = ['age', 'telephone', 'email', 'titre', 'profil', 'points_cles']
KEY_ADRESS = ['rue', 'ville']
KEY_EXPERIENCE = ['poste', 'entreprise', 'debut', 'fin', 'points_cles']
POINT_CLES = ['Développement API REST', 'Optimisation de la base de données', 
              'Gestion du personnel', 'Planning journalier du personnel']
COMPETENCE = ['Javascript', 'Python', 'React', 'SQL', 'Gestion', 
              'Rédaction', 'Meeting', 'Collaboration excellente']
ADRESS = 'adresse'
NAME = 'nom'

# Fonction d'exécution des fonctionnalités 
def main(file_name):
    data = reader_cv_json(file_name)
    validate_keys_format_json(value, data, str)
    validate_keys_identity(data, VALUE, str)
    validate_keys_experience(data, KEY_EXPERIENCE, str)
    validate_name(data, str)
    validate_keys_adress(data, KEY_ADRESS, str)
    validate_keys_skill(data, COMPETENCE, str)
    validate_date(data)
    report = screen_report(data)
    return report

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

# Générer les identifiants unique de chaque CV déjà enregistré
def generate_id():
    """
    Génère les iDs des différents CVs 
    """
    return str(uuid.uuid4())


# Partie validation: validation des données de chaque CV enregistré 
def validate_keys_format_json(value, cv_list, type_field=str):
    """
    Valide les CVs enregistrés et le contenu de ces CVs. 
    """
    if not isinstance(cv_list, list):
        raise ValueError("Le CV ci-après ne correspond pas au format demandé.")
    if not all(isinstance(item, dict) for item in cv_list):
        raise ValueError("Les champs de ce CV ne correspondent pas au format demandé.")
    
    for item in cv_list:
        if value not in item:
            raise ValueError("Ce champ ou ces champs sont introuvables dans le CV.")
        for line in item[value]:
            if not isinstance(line, type_field):
                raise ValueError("Ce champ n'est pas une chaîne de caractère.")
            raise ValueError("Ce champ n'est pas une liste.")
    return cv_list

# Valider la valeur nom de identité
def validate_name(cv_list, type_f=str):
    """
    Valide le champ nom dans la partie identité des CVs enregistrés. 
    """
    for item in cv_list:
        if NAME not in item['identite']:
            raise ValueError(f"Le champ {NAME} n'est pas présent dans le CV.")
        names = item['identite'][NAME]
        names = names.strip()
        if not isinstance(names, type_f):
            raise ValueError(f"Le champ {names} doit être une chaîne de caractère.")
        if not names:
            raise ValueError(f"Le champ {names} doit être rempli.")
        if len(names) <= 2:
            raise ValueError(f"Le champ {names} est très court.")
    return cv_list

def validate_keys_identity(cv_list, VALUE, type_f=int):
    """
    Valide les champs restants dans la partie identité des CVs enregistrés. 
    """
    for item in cv_list:
        if VALUE not in item['identite']:
            raise ValueError(f"Ce champ {VALUE} n'exite pas dans le CV enregistré")
        
        for VALUE in item['identite']:
            if not isinstance(item['identite'][VALUE], type_f):
                raise ValueError(f"Le champ {VALUE} ne correspond pas au format du CV enregistré")
    return cv_list

def validate_keys_adress(cv_list, KEY_ADRESS, type_field=str):
    """
    Valide les champs de l'adresse dans les CVs enregistrés. 
    """
    for item in cv_list:    
        if KEY_ADRESS not in item['identite'][ADRESS]:
            raise ValueError(f"Le champ {KEY_ADRESS} n'esxite pas dans les CVs enregistrés.")
        if not all(isinstance(row, type_field) for row in item['identite'][ADRESS]):
            raise ValueError(f"Le champ {KEY_ADRESS} ne correspond pas au format qui se trouve dans les CVs enregistrés.")
    return cv_list

def validate_keys_experience(cv_list, KEY_EXPERIENCE, type_f=str):
    """
    Valide les champs de la partie expérience dans les CVs enregistrés. 
    """
    for item in cv_list:
        for exp in item['experience']:
            if not isinstance(exp, type_f):
                raise ValueError("Le champ ne correspond pas au format demandé dans les CVs enregistrés.")
            if KEY_EXPERIENCE not in exp:
                raise ValueError(f"Le champ {KEY_EXPERIENCE} n'exite pas dans les CVs enregistrés.")
            if not isinstance(exp[KEY_EXPERIENCE], type_f):
                raise ValueError(f"Le champ {KEY_EXPERIENCE} n'est pas valide.")
                
            if POINT_CLES not in exp['points_cles']:
                raise ValueError(f"Le champ {POINT_CLES} n'existe pas dans les CVs enregistrés.")
            if not all(isinstance(row, type_f) for row in exp['points_cles']):
                raise ValueError(f"Le champ {POINT_CLES} ne respecte pas le format demandé dans les CVs enregistrés.")
    return cv_list

def validate_keys_skill(cv_list, COMPETENCE, type_f=str):
    """
    Valide les champs de la partie compétence des CVs enregistrés.  
    """
    for item in cv_list:
        if COMPETENCE == '' or COMPETENCE == ' ':
            raise ValueError("Le champ ne doit pas être vide.")
        for COMPETENCE in item['competence']:
            if not isinstance(COMPETENCE, type_f):
                raise ValueError(f"Le champ {COMPETENCE} ne respecte pas le format demandé dans les CVs enregistrés.")
    return cv_list

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
        city = item['identite'][ADRESS]['ville']
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