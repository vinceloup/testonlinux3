#creation de boucle FOR

for i in [1, 2, 5, 7, 8]:
    print(i)
#la boucle affiche chaque nombre un par un, marche aussi avec des lettres
for lettres in 'python ta mere':
    print(lettres)

#on peux ajouter des fonctions dans la boucle
#impression 10 fois de bonjour
for bjr in range(10):
    print('bonjour')


# Creation de boucle while (sexecute tant quune condition est vraie)
#pour dire bonjour 10 fois

bjr2 = 0
while bjr2 <= 10:
    print('bonjour deux')
    bjr2 += 1

#faire en sorte que la boucle ne recommence que tout les 1à secondes
# import time
# while True:
   # print('en cours...')
    # time.sleep(10)





#pour passer a literation suivante du code si on trouve pas ce que lont veux
#on ne veux afficher que les caracteres
liiiste = ['1', '2', 'bonjour', 'trois']
for nombreouchiffre in liiiste:
    if nombreouchiffre.isdigit():
        continue
    print((nombreouchiffre))

#a linverse pour sortir de la boucle quand on a rencontré le bon caractere
liiiste2 = ['1', '2', 'bonjour', 'trois']
for nombreouchiffre2 in liiiste2:
    if nombreouchiffre2.isdigit():
        continue
    print((nombreouchiffre2))




#modifier rapidement une liste avec une boucle
#on veux une liste avec que les nombres positifs

modifboucle = [-5, -4, -10, -100, 1, 4, 8, 9, 10]
nbpositifs = [plus for plus in modifboucle if plus >= 0]
print(nbpositifs)





#boucle pour savoir si une valeur est vraie (ANY) ou si tout est vrai (ALL)
any([False, False, True])
#retourne true
all([False, False, True])
#retourne false



#peux servir pour savoir si tout les fichiers sont bien en jpg
#verif est la fonction pour savoir si cest bien true

fichiers = ['salut.jpg', 'bonjour.jpg', 'bravo.jpg', 'slt.jpg']
all([verif.endswith('.jpg') for verif in fichiers])
#retourne True

# plus d'infos https://www.docstring.fr/glossaire/for/

   # https://www.docstring.fr/glossaire/while/

