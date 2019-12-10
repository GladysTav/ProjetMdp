fichier = open("dico_animaux.txt", "r", encoding="UTF-8")
fichier2 = open("dico_animaux.txt", "r", encoding="UTF-8")

nbligneF1 = 0

while fichier.readline():
    nbligneF1 += 1
fichier.close()
fichier = open("dico_animaux.txt", "r", encoding="UTF-8")

for i in range(0, nbligneF1):

    part1 = fichier.readline().rstrip()
    for j in range(0, nbligneF1):

        part2 = fichier2.readline().rstrip()
        MDPClair = part1 + part2
        TestMDP = hashlib.md5(MDPClair.encode()).hexdigest()

        if TestMDP == mdp:
            fichier.close()
            fichier2.close()
            print(MDPClair)
fichier.close()
fichier2.close()