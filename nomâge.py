"""
Ecrire un programme demandant le nom et l'âge d'un utilisateur.
Par la suite, afficher un message comportant le nom, puis l'âge saisis par l'utilisateur.
Exemple: Bonjour IT-Erman, tu as 67 ans.
"""

# Saisie du nom
nom = input("Saisissez votre nom: ")

# Saisie de l'âge
age = int(input("Saisissez votre âge: "))

# Affichage du message comportant le nom + l'âge.
print("Bonjour",nom,". Tu as", age, "ans.")