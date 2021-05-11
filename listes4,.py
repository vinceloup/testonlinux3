employes = ['Carlos', 'gisele', 'David', 'David', 'David', 'David', 'David',  'Richard', 'Jean Claude']
resultat = employes.index('David')

print(resultat)

#compte le nombre doccurence dans la liste
compte = employes.count('David')
print(compte)


#enlever un element de la liste
#element sert a afficher la personne en moins
element = employes.pop(-1)
print(employes)
print(element)

#pour vider une liste
employes.clear()
print(employes)


#joindre un element a une liste
employes = ['Carlos', 'gisele', 'David', 'David', 'David', 'David', 'David',  'Richard', 'Jean Claude']
joindre = 'vincent'.join(employes)
print(joindre)


#on peux utiliser en ajoutant un retour a la ligne
employes = ['Carlos', 'gisele', 'David', 'David', 'David', 'David', 'David',  'Richard', 'Jean Claude']
joindre2 = '\n'.join(employes)
print(joindre2)

#on peux utiliser en ajoutant un tiret a la liste, 
#utile pour créer des dossiers
employes = ['Carlos', 'gisele', 'David', 'David', 'David', 'David', 'David',  'Richard', 'Jean Claude']
joindre3 = '_'.join(employes)
print(joindre3)



#Faire une liste à partir d'une chaine de caractere
courses = "riz, pommes, salades, thon, poisson, saumon, beurre, lait"
courses = courses.split()
print(courses)



#Savoir si un éléément se trouve dans la liste
personnes = ['Pierre', 'paul', 'jacques', 'henri']
"paul" in personnes

#Savoir si un éléément se trouve dans la liste et le suppr
if 'paul' in personnes:
    personnes.remove('paul')

print(personnes)


#ajouter un nombre a une liste 
liste5 = [1, 2, 3, 4, 5]
liste5.append(6)
if 6 in liste5:
    print("Le nombre 6 a bien été ajouté à la liste.")


#LISTES IMBRIQUEES ENTRES ELLES
#on veux récupérer python
imbriq = [1, 2, 3, ['python', 'java'], 4, 5]
print(imbriq[3][0])


#ex de recupération de caracteres et de données
langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]

python = langages[0][0]
deux = nombres[1][1][0]
sept = nombres[4][0][0]

print(python)
print(deux)
print(sept)


