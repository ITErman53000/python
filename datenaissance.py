"""
Ecrire un programme demandant l'année de naissance d'un utilisateur.
Par la suite, calculer et afficher son âge à l'aide du calcul "date_actuel - date_naissance = âge.
Exemple: 2003 ? 2022-2003 = 19 ans
"""

# Saisie de la date naissance
date_naissance = int(input("Saisissez votre date de naissance: "))

# Initialisation de la date actuelle (2022)
date_actuel = 2022

# Calcul de son âge, en fonction des deux précédentes variables
age = date_actuel - date_naissance

# Affichage de l'âge
print("Vous avez donc", age,"ans.")