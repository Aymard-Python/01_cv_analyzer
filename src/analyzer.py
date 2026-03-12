import uuid


# Générer les identifiants unique de chaque CV déjà enregistré
def generate_id():
    """
    Génère les iDs des différents CVs 
    """
    return str(uuid.uuid4())


