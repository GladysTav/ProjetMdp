import hashlib
from Fonctions import *

class Generation():
    def __init__(self, mdp, login):
        self.mdp = mdp
        self.login = login

    def choix1(self):
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

    def choix2(self): #le choix 2 est pas encore fait
        voyelles = ["a","e","i","o","u"]
        fichier = open("dico_animaux.txt", "r", encoding="UTF-8")
        nbligne = 0

        while fichier.readline():
            nbligne += 1
        fichier.close()

        fichier = open("dico_animaux.txt", "r", encoding="UTF-8")
        for i in range(0,250):
            Mot = list(fichier.readline())

        return 0


    def choix3(self):

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

    def choix4(self):

        Mot = self.login
        for i in range(0,1000):
            MDPClair = Mot + str(('{0:01}'.format(i)))
            TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair

            MDPClair2 = str('{0:01}'.format(i)) + Mot.capitalize()
            TestMDP = hashlib.md5(MDPClair2.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair2

            MDPClair3 = str('{0:01}'.format(i)) + Mot
            TestMDP = hashlib.md5(MDPClair3.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair3

            MDPClair5 = Mot.capitalize() + str(('{0:01}'.format(i)))
            TestMDP = hashlib.md5(MDPClair5.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair5

            MDPClair4 = str(('{0:01}'.format(i))) + Mot.capitalize() + str(('{0:01}'.format(i)))
            TestMDP = hashlib.md5(MDPClair5.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair4

            MDPClair6 = str(('{0:01}'.format(i))) + Mot + str(('{0:01}'.format(i)))
            TestMDP = hashlib.md5(MDPClair5.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair6


        # print(self.login + " : " + self.mdp)
        return 0


    def choix5(self):  #nom+nombres
        for j in range(0, 9999):
            MDPClair = self.login + str(j)  # login chiffre
            TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()
            if TestMDP == self.mdp:
                return MDPClair
        return 0



    def choix6(self):

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

    def choix7(self):
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
