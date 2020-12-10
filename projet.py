import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

racine = tk.Tk()
racine.config(bg="gray25")

operande = "" # operande en cours
result = 0 # resultat des operations

def Number(a):
    """Prend en entree un argument qui est un chiffre de 0 a 9 ou un point decimal ajoute cet argurment a la chaine nombre pour pouvoir afficher des nombres a la fois entiers et decimaux"""
    global operande
    operande += a
    affiche_zone.config(text=float(operande))
def Reset():
    """Reinitialise l'affichage et les variables pour recommencer un nouveau calcul"""
    global result
    global operande
    operande = ""
    result = 0
    affiche_zone.config(text="")

def Square():
    x = np.linspace(0, 20, 100)
    plt.plot(x, np.square(x))
    plt.show()
def SquareRoot():
    x = np.linspace(0, 20, 500)
    plt.plot(x, np.sqrt(x))
    plt.show()
def Logarithm():
    x = np.linspace(1, 20, 500)
    plt.plot(x, np.log(x))
    plt.show()
def Exponential():
    x = np.linspace(0, 20, 500)
    plt.plot(x, np.exp(x))
    plt.show()

# boutons de numeros de 0 a 9
Touche_0 = tk.Button(racine, fg="white", bg="black", text ="0", relief="raised", width=2, command=lambda: Number("0"))
Touche_1 = tk.Button(racine, fg="white", bg="black", text ="1", relief="raised", width=2, command=lambda: Number("1"))
Touche_2 = tk.Button(racine, fg="white", bg="black", text ="2", relief="raised", width=2, command=lambda: Number("2"))
Touche_3 = tk.Button(racine, fg="white", bg="black", text ="3", relief="raised", width=2, command=lambda: Number("3"))
Touche_4 = tk.Button(racine, fg="white", bg="black", text ="4", relief="raised", width=2, command=lambda: Number("4"))
Touche_5 = tk.Button(racine, fg="white", bg="black", text ="5", relief="raised", width=2, command=lambda: Number("5"))
Touche_6 = tk.Button(racine, fg="white", bg="black", text ="6", relief="raised", width=2, command=lambda: Number("6"))
Touche_7 = tk.Button(racine, fg="white", bg="black", text ="7", relief="raised", width=2, command=lambda: Number("7"))
Touche_8 = tk.Button(racine, fg="white", bg="black", text ="8", relief="raised", width=2, command=lambda: Number("8"))
Touche_9 = tk.Button(racine, fg="white", bg="black", text ="9", relief="raised", width=2, command=lambda: Number("9"))
# boutons operateurs
plus = tk.Button(racine, fg="white", bg="black", text ="+", relief="raised", width=2)
moins = tk.Button(racine, fg="white", bg="black", text ="-", relief="raised", width=2)
fois = tk.Button(racine, fg="white", bg="black", text ="*", relief="raised", width=2)
divise = tk.Button(racine, fg="white", bg="black", text ="/", relief="raised", width=2)
# Effacer
erase = tk.Button(racine, fg="white", bg="black", text ="E", relief="raised", width=2, command=Reset)
# nombres flottants
point_virgule = tk.Button(racine, fg="white", bg="black", text =".", relief="raised", width=2, command=lambda: Number("."))
# Resultat
total = tk.Button(racine, fg="white", bg="black", text ="=", relief="raised", width=2)
# Zone de calcul
affiche_zone = tk.Label(racine, text="Zone d'affichage", bg="white", relief="groove", width=16)
# trace des courbes  des fonctions
fonction_carre = tk.Button(racine, text ="x -> x^2", fg="white", bg="black", command=Square)
fonction_racine_carre = tk.Button(racine, text ="x -> sqrt(x)" , fg="white", bg="black", command=SquareRoot)
fonction_logarithme = tk.Button(racine, text ="x -> log(x)", fg="white", bg="black", command=Logarithm)
fonction_exponentielle = tk.Button(racine, text ="x -> exp(x)", fg="white", bg="black", command=Exponential)


# boutons de numeros de 0 a 9
Touche_0.grid(row=4, column=1)
Touche_1.grid(row=1, column=0)
Touche_2.grid(row=1, column=1)
Touche_3.grid(row=1, column=2)
Touche_4.grid(row=2, column=0)
Touche_5.grid(row=2, column=1)
Touche_6.grid(row=2, column=2)
Touche_7.grid(row=3, column=0)
Touche_8.grid(row=3, column=1)
Touche_9.grid(row=3, column=2)
# Zone de calcul
affiche_zone.grid(row=0, column=0, columnspan=5)
# nombres flottants
point_virgule.grid(row=4, column=2)
# boutons operateurs
plus.grid(row=1, column=3)
moins.grid(row=2, column=3)
fois.grid(row=3, column=3)
divise.grid(row=4, column=3)
# Resultat
total.grid(row=4, column=0)
# Effacer
erase.grid(row=0, column=4, rowspan=4)
# trace des courbes  des fonctions
fonction_carre.grid(row=5,column=0)
fonction_racine_carre.grid(row=5,column=1)
fonction_logarithme.grid(row=5,column=2)
fonction_exponentielle.grid(row=5,column=3)

racine.mainloop()