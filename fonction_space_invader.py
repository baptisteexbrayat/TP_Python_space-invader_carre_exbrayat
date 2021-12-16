import tkinter as tk


class Joueur:
    
    def __init__(self,largueur,longueur,zone_de_jeu):
        self.position_initiale = [(longueur/2)-15,largueur-30,(longueur/2)+15,largueur]
        self.vie = 3
        self.zone_de_jeu = zone_de_jeu
        self.vaisseau = self.zone_de_jeu.create_rectangle(self.position_initiale[0],self.position_initiale[1],self.position_initiale[2],self.position_initiale[3], fill = 'red')

    
    def creation_vaisseau(self):
        return self.vaisseau
    

    def right(self,event):
        self.zone_de_jeu.move(self.vaisseau,10,0)
    
    def left(self,event):
        self.zone_de_jeu.move(self.vaisseau,-10,0)
        
class Alien:
    def __init__(self,largueur,longueur,zone_de_jeu):
        self.position_initiale = [0,0,30,30]
        self.zone_de_jeu = zone_de_jeu
        self.alien = self.zone_de_jeu.create_rectangle(self.position_initiale[0],self.position_initiale[1],self.position_initiale[2],self.position_initiale[3], fill = 'green')
        self.dx = 1
        self.dy = 0

    def creation_alien(self):
        return self.alien
    

   