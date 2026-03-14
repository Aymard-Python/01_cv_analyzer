from datetime import datetime
from dateutil.relativedelta import relativedelta
from validator import validate_schema, validate_content


def extract_info_list(key, extract_list):
    """Permet l'extraction des données listes dans CVs json."""
    extract_list[key] = extract_list.get(key, 0) + 1

def extract_info_dict(key, listes, extract):
    """Permet l'extraction des données listes dictionnaires dans CVs json."""
    liste_dict = listes[key]
    if liste_dict not in extract:
        extract[liste_dict] = 0
    extract[liste_dict] += 1

def extract_dict(key, element, dict_elt, extract):
    list_dict = dict_elt.get(key, {}).get(element)
    if list_dict not in extract:
        extract[list_dict] = 0
    extract[list_dict] += 1

def durees_experience(key_debut, key_fin, row, extract):
    date_str_debut = row[key_debut]
    date_str_fin = row[key_fin]
    date_debut = datetime.strptime(date_str_debut, "%Y-%m")
    date_fin = datetime.strptime(date_str_fin, "%Y-%m")
    diff = relativedelta(date_fin, date_debut)
    duree = diff.years + (diff.months/12)
    extract.append(duree)
    return extract

def new_cv_list(cv_list):
    for item in cv_list:
        for row in item['experience']:
            if row['fin'] == 'Présent':
                row['fin'] = '2026-03'
    return cv_list
            
def extract(cv_list):
    stats = {
        'diplomes':{},
        'competences': {},
        'postes': {},
        'entreprises': {},
        'langues': {},
        'loisirs': {},
        'villes': {},
        'date_debut': {},
        'date_fin': {},
        'duree_experiences': []
    }
    
    for item in cv_list:
        EXPERIENCE = item['experience']
        for exp in EXPERIENCE:
            extract_info_dict('poste', exp, stats['postes'])
            extract_info_dict('entreprise', exp, stats['entreprises'])
            extract_info_dict('debut', exp, stats['date_debut'])
            extract_info_dict('fin', exp, stats['date_fin'])
            durees_experience('debut', 'fin', exp, stats['duree_experiences'])
        
        EDUCATION = item['education']
        for educt in EDUCATION:
            extract_info_dict('diplome', educt, stats['diplomes'])

        COMPETENCE = item['competence']
        for comp in COMPETENCE:
            extract_info_list(comp, stats['competences'])

        LANGUE = item['langue']
        for lang in LANGUE:
            extract_info_list(lang, stats['langues'])

        LOISIR = item['loisir']
        for hobbie in LOISIR:
            extract_info_list(hobbie, stats['loisirs'])

        identity = item['identite']
        extract_dict('adresse', 'ville', identity, stats['villes'])
        
    return stats