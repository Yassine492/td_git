import tkinter as tk

racine = tk.Tk()


Touche_0 = tk.Button(racine, fg="white", bg="black", text ="0", relief="raised", height=4, width=4)
Touche_1 = tk.Button(racine, fg="white", bg="black", text ="1", relief="raised", height=4, width=4)
Touche_2 = tk.Button(racine, fg="white", bg="black", text ="2", relief="raised", height=4, width=4)
Touche_3 = tk.Button(racine, fg="white", bg="black", text ="3", relief="raised", height=4, width=4)
Touche_4 = tk.Button(racine, fg="white", bg="black", text ="4", relief="raised", height=4, width=4)
Touche_5 = tk.Button(racine, fg="white", bg="black", text ="5", relief="raised", height=4, width=4)
Touche_6 = tk.Button(racine, fg="white", bg="black", text ="6", relief="raised", height=4, width=4)
Touche_7 = tk.Button(racine, fg="white", bg="black", text ="7", relief="raised", height=4, width=4)
Touche_8 = tk.Button(racine, fg="white", bg="black", text ="8", relief="raised", height=4, width=4)
Touche_9 = tk.Button(racine, fg="white", bg="black", text ="9", relief="raised", height=4, width=4)
point_virgule = tk.Button(racine, fg="white", bg="black", text =".", relief="raised", height=4, width=4)

plus = tk.Button(racine, fg="white", bg="black", text ="+", relief="raised", height=4, width=4)
moins = tk.Button(racine, fg="white", bg="black", text ="-", relief="raised", height=4, width=4)
fois = tk.Button(racine, fg="white", bg="black", text ="x", relief="raised", height=4, width=4)
divise = tk.Button(racine, fg="white", bg="black", text ="÷", relief="raised", height=4, width=4)

affiche_zone = tk.Label(racine, text="Zone d'affichage", bg="white", relief="groove", width=16)

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
fonctions.grid(row=5,column=0, columnspan=4)

point_virgule.grid(row=4, column=2, sticky="w")
plus.grid(row=1, column=3, sticky="w")
moins.grid(row=2, column=3, sticky="w")
fois.grid(row=3, column=3, sticky="w")
divise.grid(row=4, column=3, sticky="w")

racine.mainloop()