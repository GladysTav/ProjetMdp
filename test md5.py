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
    print(mdp[0] + " : ") # 1 2 3 6 7 OK
    print("1. "+str(motdepasse.choix1()))
    print("2. "+str(motdepasse.choix2()))
    print("3. "+str(motdepasse.choix3()))
    print("4. "+str(motdepasse.choix4()))
    print("5. "+str(motdepasse.choix5()))
    print("6. "+str(motdepasse.choix6()))
    print("7. "+str(motdepasse.choix7()))
    print()
fichier.close()
