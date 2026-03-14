from analyzer import top_elements, average_elements, average_years_experience

def generate_report(stats, cv_list):

    total_cv = len(cv_list)
    top_competences = top_elements(stats, 'competences')
    top_postes = top_elements(stats, 'postes')
    top_entreprises = top_elements(stats, 'entreprises')
    top_loisirs = top_elements(stats, 'loisirs')
    average_competence = average_elements(cv_list, 'competence')
    average_experience = average_elements(cv_list, 'experience')
    average_year_experience = average_years_experience(cv_list, stats)
    compagnies = stats['entreprises']
    villes = stats['villes']
    education = stats['diplomes']
    

    with open('../data/analysis_report.txt', 'w', encoding='utf-8') as f:
        f.write("=========== CV ANALYSIS REPORT ===========\n\n")
        
        f.write(f"Total CV analysés : {total_cv}\n")
        f.write(f"Années d'expériences moyenne : {average_year_experience} ans\n")
        f.write(f"Moyenne de compétences: {average_competence}\n")
        f.write(f"Moyenne d'expériences: {average_experience}\n")
        f.write("================================================\n\n")
        f.write("Top compétences :\n")
        for item, k in top_competences.items():
            f.write(f"{item}: {k}\n")
        f.write("================================================\n\n")
        f.write("Top postes :\n")
        for item, k in top_postes.items():
            f.write(f"{item}: {k}\n")
        f.write("================================================\n\n")
        f.write("Top loisirs :\n")
        for item, k in top_loisirs.items():
            f.write(f"{item}: {k}\n")
        f.write("================================================\n\n")
        f.write("Entreprises :\n")
        for item, k in compagnies.items():
            f.write(f"{item}: {k}\n")
        f.write("================================================\n\n")
        f.write("Niveau d'études :\n")
        for item, k in education.items():
            f.write(f"{item}: {k}\n")
        f.write("================================================\n\n")
        f.write("Villes :\n")
        for item, k in villes.items():
            f.write(f"{item}: {k}\n")
            
    return print("Analysis report generated successfully.")
    