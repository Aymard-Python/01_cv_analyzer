from loader import reader_cv_json
from validator import validate_schema, validate_content, check_required_fields, validate_string_list, validate_date
from analyzer import generate_id
from extractor import extract

required_experience = ['poste', 'entreprise', 'debut', 'fin', 'points_cles']
required_competence = ['Javascript', 'Python', 'React', 'SQL', 'Gestion', 'Rédaction', 
                       'Meeting', 'Collaboration excellente']

file_name = "../data/cvs.json"

def main(file_name):
    
    data = reader_cv_json(file_name)

    validate_schema(data)
    validate_content(data)
    validate_date(data)

    for item in data:
        experience = item['experience']
        competence = item['competence']
        for exp in experience:
            check_required_fields(exp, required_experience, context="experience")
        
        validate_string_list(competence, required_competence, 'competence', 'id')

    report = extract(data)
    print(report)


if __name__ == "__main__":
    main(file_name)