import time

required = {
    '_fields': ['id', 'identite', 'experience', 'competence', 'education', 'langue', 'loisir'],
    '_experience': ['poste', 'entreprise', 'debut', 'fin', 'points_cles'],
    '_education': ['diplome', 'institution', 'annee'],
    '_identity': ['nom', 'age', 'adresse', 'titre', 'telephone', 'email', 'profil'],
    '_competence': ['Javascript', 'Python', 'React', 'SQL', 'Gestion', 'Rédaction', 'Meeting', 'Collaboration excellente'],
    '_language': ['FR', 'EN'],
    '_hobbies': ['Photographie', 'Musique', 'Sport', 'Lecture']
}

def validate_schema(cv_list):
    """Valide la structure et les types des CVs."""
    ## Validation du type de chaque clé dans chaque CV.
    if not isinstance(cv_list, list):
        raise ValueError("Le format de ce CV n'est pas correct.")
    if not all(isinstance(item, dict) for item in cv_list):
        raise ValueError("Tous ces champs doivent être des dictionnaires.")
        
    for item in cv_list:
        if 'id'not in item:
            raise ValueError("La clé id est inexistant d'où l'erreur de validation.")
            
     # Validation des données globales des CVs 
        check_required_fields(item, required['_fields'], context=f"du CV {item['id']}")
    
        Identity = item['identite']
        
        for key_list in ['competence', 'langue', 'loisir']:
            if not isinstance(item[key_list], list):
                raise ValueError(f"Erreur dans le CV avec id = {item['id']}: {key_list} doit être une liste.")
            if not all(isinstance(key_str, str) for key_str in item[key_list]):
                raise ValueError(f"Erreur dans le CV avec id = {item['id']}: {key_list} doit être une chaîne de caractère.")
                
        for key_li in ['experience', 'education']:
            if not isinstance(item[key_li], list):
                raise ValueError(f"Erreur dans le CV avec id = {item['id']}: {key_li} doit être une liste.")
            if not all(isinstance(key_dict, dict) for key_dict in item[key_li]):
                raise ValueError(f"Erreur dans le CV avec id = {item['id']}: {key_li} doit être un dictionnaire.")
        for experience in item['experience']:
            if not isinstance(experience['points_cles'], list):
                raise ValueError(f"Erreur dans le CV avec id = {item['id']}: points_cles doit être liste.")
            if not all(isinstance(exp, str) for exp in experience['points_cles']):
                raise ValueError(f"Erreur dans le CV avec id = {item['id']}: l'élément doit être une chaîne de caractère.")
                
        if not isinstance(item['id'], str):
            raise ValueError(f"Erreur dans le CV avec id = {item['id']}: La clé {'id'} doit être une chaîne de caractère.")
            
        if not isinstance(Identity, dict):
            raise ValueError(f"Erreur dans le CV avec id = {item['id']}: La clé {'identite'} ne respecte pas le format d'un dictionnaire.")
        for key_st in ['nom', 'titre', 'telephone', 'email', 'profil']:
            if not isinstance(Identity[key_st], str):
                raise ValueError(f"Erreur dans le CV avec id = {item['id']}: Chacun des éléments de la clé identité doit être une chaîne de caractère.")
        if not isinstance(Identity['age'], int):
            raise ValueError(f"Erreur dans le CV avec id = {item['id']}: l'âge doit être un entier.")
        if not isinstance(Identity['adresse'], dict):
            raise ValueError(f"Erreur dans le CV avec id = {item['id']}: l'adresse doit être un dictionnaire.")
        for key_ad in ['rue', 'ville']:
            if not isinstance(Identity['adresse'][key_ad], str):
                raise ValueError(f"Erreur dans le CV avec id = {item['id']}: la clé {key_ad} de l'élément adresse doit être une chaîne de caractère.")
    return cv_list

def validate_content(cv_list):
    
    for item in cv_list:
        EXPERIENCE = item['experience']
        EDUCATION = item['education']
        IDENTITY = item['identite']
        LOISIR = item['loisir']
        COMPETENCE = item['competence']
        LANGUE = item['langue']

        # Validation des données de la clé education dans les CVs
        for education in EDUCATION:
            check_required_fields(education, required['_education'], context=f"education du CV {item['id']}")

         # Validation des données de la clé experience dans les CVs
        for experience in EXPERIENCE:
            check_required_fields(experience, required['_experience'], context=f"experience du CV {item['id']}")

         # Validation des données de la clé identite dans les CVs
        check_required_fields(IDENTITY, required['_identity'], context=f"identite du CV {item['id']}")
        
         # Valide la longueur de la chaîne de caractère nom dans la clé identite les CVs
        if len(IDENTITY['nom']) < 2:
            raise ValueError(f"Erreur dans le CV avec id = {item['id']}: l'élément nom de la clé identite est très court.")
            
        # Validation des données de la clé competence dans les CVs
        validate_string_list(COMPETENCE, required['_competence'], 'competence', item['id'])

        # Validation des données de la clé langue dans les CVs
        validate_string_list(LANGUE, required['_language'], 'langue', item['id'])

        # Validation des données de la clé loisir dans les CVs
        validate_string_list(LOISIR, required['_hobbies'], 'loisir', item['id'])
                
    return cv_list 

def validate_date(cv_list):
    for item in cv_list:
        identity = item['identite']
        experience = item['experience']
        education = item['education']

        for line in education:
            check_required_fields(line, required['_education'], context="education")
            year_str = line['annee']
            try:
                year = time.strptime(year_str, "%Y")
            except ValueError:
                raise ValueError(
                        f"Erreur CV de {identity['nom']}: Mauvais format de l'année {year_str}."
                        f"Format attendu: YYYY"   
                    )
                
        for row in experience:
            check_required_fields(row, required['_experience'], context="experience")
            date_debut_str = row['debut']
            date_fin_str = row['fin']

            try:
                date_debut = time.strptime(date_debut_str, "%Y-%m")
                date_fin = time.strptime(date_fin_str, "%Y-%m")
            except ValueError:
                raise ValueError(
                    f"Erreur CV de {identity['nom']}: Mauvais format de date "
                    f"(début: {date_debut_str}, fin: {date_fin_str}). Format attendu: YYYY-MM."
                )

            if date_debut > date_fin:
                raise ValueError(
                    f"Erreur dans le CV de {identity['nom']}: La date de début" 
                    f"{date_debut_str} ne doit pas être supérieur à la date de fin {date_fin_str}."
                )
    
    return cv_list

def check_required_fields(data, required_keys, context=""):
    """
    Permet de vérifier l'existance des clés et le contenu de 
    leur valeur dans les CVs. 
    """
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Erreur dans la clé {context}: la clé {key} est manquante.")
        if not data[key]:
            raise ValueError(f"Erreur dans la clé {context}: {key} est vide.")
        
def validate_string_list(values, allowed_values, field_name, cv_id):
    """
    Permet de vérifier que les valeurs des clés ou des éléments de 
    chaque clé dans les CVs ne sont pas vides. 
    """
    for val in values:
        if not val:
            raise ValueError(f"Erreur dans le CV  {cv_id}: Une valeur dans {field_name} {val} est vide.")
        if val not in allowed_values:
            raise ValueError(f"Erreur dans le CV {cv_id}: La valeur {val} est non reconnu.")