import uuid


# Générer les identifiants unique de chaque CV déjà enregistré
def generate_id():
    """
    Génère les iDs des différents CVs 
    """
    return str(uuid.uuid4())

def top_elements(stats, key):
    element = stats.get(key, {})
    if not element:
        return {}
    top_key = float('-inf')
    for _, k in element.items():
        if k > top_key:
            top_key = k
    top_element = {item: k for item, k in element.items() if k == top_key}
    return top_element

def average_elements(cv_list, key):
    total_counts = 0
    total_cv = len(cv_list)
    if total_cv == 0:
        raise ValueError("Erreur: Division par Zéro impossible")
    for item in cv_list:
        for element in item[key]:
            total_counts += 1
    average_element = total_counts/total_cv
        
    return average_element

def average_years_experience(cv_list, stats):
    years = stats['duree_experiences']
    if not years:
        return 0
    sum_years = sum(years)
        
    total_cv = len(cv_list)
    if total_cv == 0:
        raise ValueError("Erreur: Division par Zéro impossible")

    average_year = sum_years/total_cv
    
    return round(average_year, 2)
