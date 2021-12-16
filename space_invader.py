import tkinter as tk
import fonction_space_invader as si



pdj = tk.Tk()
pdj.geometry('900x450+400+200')

longueur = 480
largueur = 320
x0 = longueur/2
y0 = largueur
zone_de_jeu = tk.Canvas(pdj, width = longueur, height = largueur, bg='white')
vaisseau_joueur = si.Joueur(largueur,longueur,zone_de_jeu)
vaisseau_joueur.creation_vaisseau()
alien = si.Alien(largueur,longueur,zone_de_jeu)
alien.creation_alien()




zone_de_jeu.pack()

button_quitt = hello = tk.Button(pdj, text = "Quitter", fg = 'red', command = pdj.destroy)
button_quitt.pack(side = 'left', padx = 10, pady = 10)
button_replay = hello = tk.Button(pdj, text = "Rejour", fg = 'red',)
button_replay.pack(side = 'left', padx = 5, pady = 5)

zone_de_jeu.bind_all("<KeyPress-Left>", vaisseau_joueur.left)
zone_de_jeu.bind_all("<KeyPress-Right>", vaisseau_joueur.right)
    
pdj.mainloop()