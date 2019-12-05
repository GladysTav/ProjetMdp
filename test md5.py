#1 - 3  - 6 - 7 sont ok
# NOK : 2 - 4 - 5

from Generation import *

fichier = open("passtext.txt", "r", encoding="UTF-8")
nbligne = 0
while fichier.readline(): #on compte nmobre de ligne du fichier d mot de passe
    nbligne += 1
fichier.close()

fichier = open("passtext.txt", "r", encoding="UTF-8")

for i in range (0, nbligne): #on teste tout les mots de passe sur le choix 3
    mdp = fichier.readline().rstrip().split(':')
    motdepasse = Generation(mdp[1], mdp[0])#création de l'objet
    print(mdp[0] + " : " + str(motdepasse.choix7())) #on cherche le mot de passe avec le choix 3
fichier.close()
