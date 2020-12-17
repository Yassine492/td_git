import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

racine = tk.Tk()
racine.config(bg="gray25")

<<<<<<< HEAD
nombre = ""

def ajout(nb):
    """ Permet de faire apparaitre les nombres sur la zone de calcul de la calculatrice, et de faire le calcul plus tard """
    global nombre
    nombre += nb
    affiche_zone["text"] = nombre

#Toutes les fonctions qui vont suivre ne servent juste qu'a rentrer des chiffres pour les calculs

def zero():
    ajout("0") #Les nombres sont ici comme des str mais ils seront repasser en float plus tard pour le calcul

def un():
    ajout("1")

def deux():
    ajout("2")

def trois():
    ajout("3")

def quatre():
    ajout("4")

def cinq():
    ajout("5")

def six():
    ajout("6")

def sept():
    ajout("7")

def huit():
    ajout("8")

def neuf():
    ajout("9")

def point():
    ajout(".")

def supprimer():
    """ Fonction qui va supprimer les données entrée dans la calculatrice """
    global nombre
    nombre = ""
    affiche_zone["text"] = nombre #Permet d'afficher dans la zone d'affichage les nombres choisient

def addition():
    """ Fonction qui va additionner les chiffres de la calulatrice """
    global nombre, op, nombre2
    nombre2 = float(nombre) #Transforme notre nombre en float pour pouvoir effectuer un calcul
    nombre = ""
    op = 1 #Correspond a l'operation une soit l'addition
    affiche_zone["text"] = "+"

def soustraction():
    """ Fonction qui va soustraire les chiffres de la calculatrice """
    global nombre, op, nombre2
    nombre2 = float(nombre)
    nombre = ""
    op = 2 #Correspond a l'operation deux soit la soustraction
    affiche_zone["text"] = "-"

def multiplication():
    """ Fonction qui va multiplier les chiffres de la calculatrice """
    global nombre, op, nombre2
    nombre2 = float(nombre)
    nombre = ""
    op = 3 #Correspond a l'opération trois soit la multiplication
    affiche_zone["text"] = "*"

def division():
    """ Fonction qui va diviser les chiffres de la calculatrice """
    global nombre, op, nombre2
    nombre2 = float(nombre)
    nombre = ""
    op = 4 #Correspond a l'operation quatre soit la division
    affiche_zone["text"] = "/"

def resultat():
    """ Fonction qui va permettre d'afficher le resultat sur la calculatrice """
    global nombre
    nombre = float(nombre)
    if op == 1:
        result = round(nombre2 + nombre, 10)
    if op == 2:
        result = round(nombre2 - nombre, 10)
    if op == 3:
        result = round(nombre2 * nombre, 10)
    if op == 4:
        result = round(nombre2 / nombre, 10)
    affiche_zone["text"] = result
    result = 0
    nombre = str(result)


Touche_0 = tk.Button(racine, fg="white", bg="black", text ="0", relief="raised", height=4, width=4, command=zero)
Touche_1 = tk.Button(racine, fg="white", bg="black", text ="1", relief="raised", height=4, width=4, command=un)
Touche_2 = tk.Button(racine, fg="white", bg="black", text ="2", relief="raised", height=4, width=4, command=deux)
Touche_3 = tk.Button(racine, fg="white", bg="black", text ="3", relief="raised", height=4, width=4, command=trois)
Touche_4 = tk.Button(racine, fg="white", bg="black", text ="4", relief="raised", height=4, width=4, command=quatre)
Touche_5 = tk.Button(racine, fg="white", bg="black", text ="5", relief="raised", height=4, width=4, command=cinq)
Touche_6 = tk.Button(racine, fg="white", bg="black", text ="6", relief="raised", height=4, width=4, command=six)
Touche_7 = tk.Button(racine, fg="white", bg="black", text ="7", relief="raised", height=4, width=4, command=sept)
Touche_8 = tk.Button(racine, fg="white", bg="black", text ="8", relief="raised", height=4, width=4, command=huit)
Touche_9 = tk.Button(racine, fg="white", bg="black", text ="9", relief="raised", height=4, width=4, command=neuf)
point_virgule = tk.Button(racine, fg="white", bg="black", text =".", relief="raised", height=4, width=4, command=point)

plus = tk.Button(racine, fg="white", bg="black", text ="+", relief="raised", height=4, width=4, command=addition)
moins = tk.Button(racine, fg="white", bg="black", text ="-", relief="raised", height=4, width=4, command=soustraction)
fois = tk.Button(racine, fg="white", bg="black", text ="x", relief="raised", height=4, width=4, command=multiplication)
divise = tk.Button(racine, fg="white", bg="black", text ="÷", relief="raised", height=4, width=4, command=division)
supprimer = tk.Button(racine, fg="white", bg="black", text="supp", relief="raised", height=4, width=4, command=supprimer)
resultat = tk.Button(racine, fg="white", bg="black", text="=", relief="raised", height=4, width=4, command=resultat)

affiche_zone = tk.Label(racine, bg="white", relief="groove", width=16)

fonctions = tk.Button(racine, text ="f(x) = x ->", relief="sunken", width=16)

Touche_0.grid(row=4, column=1, sticky="w")
Touche_1.grid(row=1, column=0, sticky="w")
Touche_2.grid(row=1, column=1, sticky="w")
Touche_3.grid(row=1, column=2, sticky="w")
Touche_4.grid(row=2, column=0, sticky="w")
Touche_5.grid(row=2, column=1, sticky="w")
Touche_6.grid(row=2, column=2, sticky="w")
Touche_7.grid(row=3, column=0, sticky="w")
Touche_8.grid(row=3, column=1, sticky="w")
Touche_9.grid(row=3, column=2, sticky="w")

affiche_zone.grid(row=0, column=0, columnspan=4)
fonctions.grid(row=6,column=0, columnspan=4)

point_virgule.grid(row=4, column=2, sticky="w")
plus.grid(row=1, column=3, sticky="w")
moins.grid(row=2, column=3, sticky="w")
fois.grid(row=3, column=3, sticky="w")
divise.grid(row=4, column=3, sticky="w")
supprimer.grid(row=4, column=0, sticky="w")
resultat.grid(row=5, column=3, sticky="w")

racine.mainloop()