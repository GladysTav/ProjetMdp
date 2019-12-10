import hashlib
from Fonctions import *

class Generation():
    def __init__(self, mdp, login):
        self.mdp = mdp
        self.login = login

    def choix1(self): # OK Xtiti1995
        for i in range(65, 91):
            for j in range(1920, 2000):
                MDPClair = chr(i) + self.login + str(j) # min login année
                TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
                if TestMDP == self.mdp:
                    return MDPClair
        for i in range(97, 123):
            for j in range(1920, 2000):
                MDPClair = chr(i) + self.login + str(j) # maj login année
                TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
                if TestMDP == self.mdp:
                    return MDPClair
        return 0

    def choix2(self): # non ok Faucon30 OK mais pas 123pandas
        # Faucon30 et 123pandas
        MDPClair=""
        fichier = open("dico_animaux.txt", "r", encoding="UTF-8")
        nbligne = 0
        Mot=[]
        while fichier.readline():
            nbligne += 1
        fichier.close()

        fichier = open("dico_animaux.txt", "r", encoding="UTF-8")
        for i in range(0,nbligne-1):
            Mot.append(fichier.readline())
        fichier.close()

        # 1-4 chiffres + animal
        # 1-4 chiffres + maj animal
        # animal + 1-4 chiffres
        # maj animal + 1-4 chiffres
        for a in Mot:
            for j in range(0, 9999):
                MDPClair = a + str(j) # animal nombre
                TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
                if TestMDP == self.mdp:
                    return MDPClair

                MDPClair = str(j) + a # nombre animal
                if a=="pandas":
                    print(MDPClair)
                TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
                if TestMDP == self.mdp:
                    return MDPClair

            Binaire = str(dec2bin(j, len(a)))
            if Binaire[0] == "1":  # Met en majuscule
                a=a[0].upper()+a[1:len(a)-1]
            else:  # met en minuscule
                a=a[0].lower()+a[1:len(a)-1]

            for j in range(0, 9999):
                MDPClair = a + str(j) # animal nombre
                TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
                if TestMDP == self.mdp:
                    return MDPClair

                MDPClair = str(j) + a # nombre animal
                TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
                if TestMDP == self.mdp:
                    return MDPClair
        return 0


    def choix3(self): # OK
        # TaTa et lion
        fichier = open("dico_animaux.txt", "r", encoding="UTF-8")
        nbligne = 0

        while fichier.readline():
            nbligne += 1
        fichier.close()

        fichier = open("dico_animaux.txt", "r", encoding="UTF-8")

        for i in range(0, nbligne): #on passe sur tout les mots

            Mot = list(fichier.readline())
            TailleMot = len(Mot)

            for j in range(0, 2**TailleMot): #on teste toutes les combinaise
                Binaire =str(dec2bin(j, TailleMot))
                for k in range(0, TailleMot): #modifie le mot

                    if Binaire[k] == "1": #Met en majuscule
                        Mot[k]=Mot[k].upper()
                    else: #met en minuscule
                        Mot[k]=Mot[k].lower()

                MDPClair = "".join(Mot)
                TestMDP = hashlib.md5(MDPClair[0:TailleMot-1].encode()).hexdigest()

                if self.mdp == TestMDP:
                    fichier.close()
                    return MDPClair
        fichier.close()

        Mot = self.login
        TailleMot = len(Mot)

        for j in range(0, 2 ** TailleMot):  # on teste toutes les combinaisons
            MDPClair=""
            Binaire = str(dec2bin(j, TailleMot))
            for k in range(0, TailleMot):  # modifie le mot

                if Binaire[k] == "1":  # Met en majuscule
                    MDPClair += Mot[k].upper()
                else:  # met en minuscule
                    MDPClair += Mot[k].lower()

            # print(MDPClair) affiche bien tata - Tata - TaTa
            TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()

            if self.mdp == TestMDP:
                return MDPClair

        return 0

    def choix4(self): # non ok
        # tete0123 et Tuti1234
        Mot = self.login
        for i in range(0,9999):
            MDPClair = Mot + str(('{0:04}'.format(i))) #login + nombre
            TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair

            MDPClair = str('{0:04}'.format(i)) + Mot.capitalize() #nombre + login maj
            TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair

            MDPClair = str('{0:04}'.format(i)) + Mot #nombre + login
            TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair

            MDPClair = Mot.capitalize() + str(('{0:04}'.format(i))) #login maj + nombre
            TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair

        # print(self.login + " : " + self.mdp)
        return 0


    def choix5(self):  # changé toutes les voyelles par un nombre et mis le tout en majuscule
        for j in range(0, 9999):
            MDPClair = self.login + str(j)  # login chiffre
            TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair
        return 0



    def choix6(self): # OK
        # dranacdranac
        fichier = open("dico_animaux.txt", "r", encoding="UTF-8")
        nbligne = 0
        while fichier.readline():
            nbligne += 1
        fichier.close()
        fichier = open("dico_animaux.txt", "r", encoding="UTF-8")

        for i in range(0, nbligne):

            Ani1 = "".join(reversed(fichier.readline().rstrip()))
            for j in range(0, 250):

                MDPClair = Ani1*2
                TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
                if TestMDP == self.mdp:
                    fichier.close()
                    return MDPClair
        fichier.close()

        return 0

    def choix7(self):# OK
        # morsetigre
        fichier = open("dico_animaux.txt", "r", encoding="UTF-8")
        nbligne = 0

        while fichier.readline():
            nbligne += 1
        fichier.close()

        fichier = open("dico_animaux.txt", "r", encoding="UTF-8")
        for i in range(0, 250):
            fichier2 = open("dico_animaux.txt", "r", encoding="UTF-8")
            Ani1 = fichier.readline().rstrip()
            for j in range(0, 250):
                Ani2 = fichier2.readline().rstrip()
                MDPClair = Ani1 + Ani2
                TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
                if TestMDP == self.mdp:
                    fichier.close()
                    fichier2.close()
                    return MDPClair
            fichier2.close()
        fichier.close()

        return 0
