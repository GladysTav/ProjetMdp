from tkinter import *
from tkinter import filedialog


class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.nb_clic = 0
        self.filename=""

        Frame1 = Frame(fenetre)
        Frame1.pack(side=TOP,padx=5,pady=5)

        Frame2 = Frame(fenetre)
        Frame2.pack(padx=20, pady=10, anchor="w",side=LEFT)

        Frame4 = Frame(fenetre)
        Frame4.pack(side=RIGHT)

        Frame3 = Frame(fenetre)
        Frame3.pack(padx=5, pady=10, anchor="w",side=BOTTOM)

        # Création de nos widgets
        self.login = Label(Frame1, text="Login : ")
        self.login.pack(side="left")

        self.Ilogin = Entry(Frame1)
        self.Ilogin.pack(side="left", padx=10)

        self.Imdp = Entry(Frame1)
        self.Imdp.pack(side="right")

        self.mdp = Label(Frame1, text="Password : ")
        self.mdp.pack(side="right", padx=10)

        self.labelNb = Label(Frame4, text="Nombres ajoutés : ").pack()
        self.entryNb = Entry(Frame4)
        self.entryNb.pack()
        # self.fichier = Button(Frame4, text="Fichier de mots", command=self.selectFile).pack()


        """
             Trois d'entre eux utilisent des règles simples basées sur leur nom,
            avec optionnellement des nombres rajoutés (maximum 4) .
             Un a mis une lettre devant son nom, avant de rajouter à la fin son année de naissance.
            (Choix1)
             Les autres aiment les animaux et ont dérivés leurs mots de passe de ceux-ci. (Choix2)
             L'un est classique, (Choix3)
             d'autres ont rajoutés des nombres devant ou derrière (max 3), et mis la première lettre ou
            pas en majuscule. (Choix4)
             Un autre est plus complexe : il a changé toutes les voyelles par un nombre et mis le tout
            en majuscule. (ChoiX5)
             Le suivant a pris le nom d'un animal, l'a mis à l'envers, et l'a dédoublé. (Choix6)
             Le dernier a seulement concaténé 2 animaux...(Choix7)
        """

        self.choix = IntVar()
        bouton1 = Radiobutton(Frame2, text="Nom + nombres rajoutés", variable=self.choix, value=1)
        bouton2 = Radiobutton(Frame2, text="Lettre + nom + année", variable=self.choix, value=2)
        bouton3 = Radiobutton(Frame2, text="Dérivé d'animal", variable=self.choix, value=3)
        bouton4 = Radiobutton(Frame2, text="\'Classique\'", variable=self.choix, value=4)
        bouton5 = Radiobutton(Frame2, text="Nombres devant ou derrière + maj optionnelle", variable=self.choix, value=5)
        bouton6 = Radiobutton(Frame2, text="Voyelles -> nombres, reste en majuscule", variable=self.choix, value=6)
        bouton7 = Radiobutton(Frame2, text="Animal à l'envers et dédoublé", variable=self.choix, value=7)
        bouton8 = Radiobutton(Frame2, text="Concaténation de 2 animaux", variable=self.choix, value=8)

        bouton1.pack(anchor="w")
        bouton2.pack(anchor="w")
        bouton3.pack(anchor="w")
        bouton4.pack(anchor="w")
        bouton5.pack(anchor="w")
        bouton6.pack(anchor="w")
        bouton7.pack(anchor="w")
        bouton8.pack(anchor="w")

        self.Search = Button(Frame2, text="Chercher", command=self.search)
        self.Search.pack()

        self.result = Label(Frame2, text="Résultat : ")
        self.result.pack(anchor="w", padx=15, pady=5)
        self.res = Label(Frame2, text="")
        self.res.pack(anchor="e")

        self.bouton_quitter = Button(Frame3, text="Quitter", command=self.quit)
        self.bouton_quitter.pack()

    def cliquer(self):
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

    def search(self):
        self.res["text"]=(str(self.choix.get()))+" - "+str(self.entryNb.get())

    def selectFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("text files", "*.txt"), ("all files", "*.*")))


interface = Interface(Tk())

interface.mainloop()
interface.destroy()
