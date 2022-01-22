"""
@author: Baptiste, Paul 3ETI
"""

import tkinter as tk        
from random import randint
import os
import tkinter.font as font
from winsound import SND_ASYNC, SND_FILENAME, SND_LOOP, PlaySound
'''--------------------------------------------------------------------------------------------------------------------'''
musique = PlaySound("musique_amb.wav",SND_FILENAME|SND_ASYNC|SND_LOOP)
'''--------------------------------------------------------------------------------------------------------------------'''
defaite=True
point_joueur=0
vies=3
jeu_en_cours=False
point_par_torpille=100
'''--------------------------------------------------------------------------------------------------------------------'''
hauteur=500
largeur=1200
'''--------------------------------------------------------------------------------------------------------------------'''
#Requin

class Requin:
    hauteur_requin = 40
    largeur_requin = 40
    
    def __init__(self):
        Requin.hauteur_requin = 40
        Requin.largeur_requin = 40
        self.x=largeur/2
        self.y=hauteur-Requin.hauteur_requin-5
        self.vitesse_joueur = 20
        self.apparence=canevas.create_image(self.x,self.y,anchor='center',image=image_requin)
    def affichage(self):
        '''
        Sortie : Image du requin
        But : Créer l'image representant le joueur
        '''
        canevas.coords(self.apparence,self.x,self.y)
    
    

    def mouvement(self,dir):
        '''
        Sortie : Coordonnées du joueur
        But : Effectuer la deplacement du joueur en déplacent l'image du joueur.
        '''
        if self.x>=Requin.largeur_requin and dir==-1:
            self.x+=self.vitesse_joueur*dir
        elif self.x<=largeur-Requin.largeur_requin and dir==1:
            self.x+=self.vitesse_joueur*dir
        self.affichage() 
         
        
projectiles_joueur=[]
   
class Projectile:
    vitesse_projectile = 3
    nombre_de_projectile=0
    
    def __init__(self):
        Projectile.vitesse_projectile = 3
        self.x=requin.x
        self.y=requin.y
        self.apparence=canevas.create_rectangle(self.x , self.y-4 , self.x+5 ,self.y+12 , fill='white')
        self.encours=True
        Projectile.nombre_de_projectile+=1
    def affichage(self):
        '''
        Sortie : Image du projectile
        But : Modifier la position du projectile pour créer son mouvement
        '''
        canevas.coords(self.apparence , self.x , self.y-4 , self.x+5 , self.y+12)
    def mouvement(self):
        '''
        Sortie : Image du projectile
        But : Modifier la position du projectile pour créer son mouvement
        '''
        if self.encours:
            self.y-=Projectile.vitesse_projectile
            self.affichage()
            self.fin_projectile()
            fenetre.after(5,self.mouvement)
    def fin_projectile(self):
        '''
        But : vérifier si le projectile touche une torpille 
        '''
        if self.y<0:
            self.encours=False
            canevas.delete(self.apparence)
            del projectiles_joueur[0]
            Projectile.nombre_de_projectile-=1
        else:
            for i in ennemie:
                if i.vivant:
                    if self.y>=i.y: 
                        if self.y<=i.y+Torpille.hauteur_torpille:
                            if self.x<=i.x+Torpille.largeur_torpille:
                                if self.x>=i.x:
                                    self.elimination()
                                    canevas.delete(i.apparence)
                                    i.vivant=False
                                    scores(point_par_torpille)
                                    win()
    def elimination(self):
        '''
        But : Fait disparaitre le projectile et la torpille touché
        '''
        self.encours=False
        canevas.delete(self.apparence)
        del projectiles_joueur[0]
        Projectile.nombre_de_projectile-=1
        
'''--------------------------------------------------------------------------------------------------------------------'''        
#Torpille

nbre_torpille_par_ligne=10
vitesse_torpille=0.5
        
class Torpille:
    descente_torpille=20
    nombre_de_torpille=0
    def __init__(self):
        Torpille.largeur_torpille = 14
        Torpille.nombre_de_torpille += 1
        Torpille.hauteur_torpille = 36
        Torpille.y=50 #premiere ligne de torpille
        Torpille.descente_torpille = 20
        self.ecart_torpille = 10
        self.nombre_de_torpille=Torpille.nombre_de_torpille
        self.vivant=True
        self.x=self.nombre_de_torpille*(self.ecart_torpille+Torpille.largeur_torpille)
        Torpille.dir=1
        Torpille.vitesse=vitesse_torpille
    def creation(self):
        '''
        Sortie : image de la torpille
        But : Créer l'image qui va representer la torpille
        '''
        self.apparence=canevas.create_image(self.x,self.y,anchor='nw',image=image_torpille)
    def affichage(self):
        '''
        Sortie : coordonnée de la torpille
        But : Recuperer les coordonnée de chaque la torpille
        '''
        canevas.coords(self.apparence,self.x,self.y)

projectile_torpille=[]                  
class Projectile_torpille:
    
    def __init__(self,i):
        self.x=ennemie[i].x
        self.y=ennemie[i].y
        self.apparence=canevas.create_rectangle(self.x , self.y-4 , self.x ,self.y+12 , fill='black')
        self.encours=True
        self.mouvement()
    def affichage(self):
        '''
        Sortie : liste des coordonnées du projectile
        But : Connaitre la position du projectile
        '''
        canevas.coords(self.apparence , self.x , self.y-4 , self.x ,self.y+12)
    def mouvement(self):
        '''
        Sortie : Image du projectile
        But : Modifier la position du projectile pour créer son mouvement
        '''
        if self.encours:
            self.y+=Projectile.vitesse_projectile
            self.affichage()
            self.fin_projectile()
            fenetre.after(10,self.mouvement)
    def fin_projectile(self):
        '''
        But : vérifie et eleve une vie si le projectile touche le vaisseau ou une defence. Les detruit si leurs nombre devient nulle
        '''
        global Vies
        if self.y>hauteur:
            self.encours=False
            canevas.delete(self.apparence)
            del projectile_torpille[0]
        if self.y>=requin.y-5 :
            if self.y<=requin.y+5 : 
                if self.x<=requin.x+Requin.largeur_requin/2 :
                    if self.x>=requin.x-Requin.largeur_requin/2 :
                        self.encours=False
                        canevas.delete(self.apparence)
                        del projectile_torpille[0]
                        Vies-=1
                        affichage_vies(Vies)
                        if Vies==0:
                            game_over()
        else:
            for i in Defences:
                if i.durabilite>0 :
                    if self.x>=i.x :
                        if self.x<=i.x+Protections.largeur : 
                            if self.y>=Protections.y :
                                if self.y<=Protections.y+Protections.hauteur_protections:
                                    i.protection_touche()
                                    self.encours=False
                                    canevas.delete(self.apparence)
                                    del projectile_torpille[0]       
    
def mouvement_torpille():
    '''
    But : Gerer le mouvement de déplacement des torpilles
    '''
    global ennemie
    if jeu_en_cours:
        L=[i.vivant for i in ennemie]
        if True in L:
            i=L.index(True)
            L.reverse()
            j=L.index(True)
            if (ennemie[-j-1].x+Torpille.largeur_torpille>=largeur and Torpille.dir==1) or\
            (ennemie[i].x-Torpille.largeur_torpille<=0 and Torpille.dir==-1):
                Torpille.dir*=-1
                Torpille.y+=Torpille.descente_torpille
                if Torpille.y+Torpille.hauteur_torpille/2>=Protections.y:
                    game_over()
            for i in ennemie:
                i.x+=Torpille.vitesse*Torpille.dir
                i.affichage()  
            fenetre.after(5,mouvement_torpille)
            
def projectile_des_torpilles():
    '''
    But : Gerer les projectiles des torpilles
    '''
    global ennemie,projectile_torpille 
    if jeu_en_cours:
        L=[i.vivant for i in ennemie]
        i=randint(0,len(ennemie)-1)
        if L[i]:
            projectile_torpille.append(Projectile_torpille(i))
            fenetre.after(randint(200,300),projectile_des_torpilles)
        else:
            fenetre.after(1,projectile_des_torpilles)

def suppr_projectile():
    
    '''
    But : Supprimer tout les projectiles restant quand la partie est fini
    '''
    for i in projectiles_joueur:
        i.encours=False
    for i in projectile_torpille:
        i.encours=False          
'''--------------------------------------------------------------------------------------------------------------------'''                     
#Protections

nombre_de_protection = 4
durabilite = 20
class Protections:
    
    nombre=0
    nombre = 4
    largeur = 0
    
    hauteur_protections = 15
    def __init__(self):
        Protections.nombre+=1
        Protections.largeur = 1.5*Requin.largeur_requin
        self.nombre=Protections.nombre
        self.x=largeur*self.nombre/(nombre_de_protection+1)
        Protections.y=hauteur-(Requin.hauteur_requin+40)
        Protections.hauteur_protections = 15
        self.durabilite = durabilite
        self.apparence=canevas.create_rectangle(self.x-18,self.y-8,self.x+Protections.largeur,self.y+Protections.hauteur_protections,width=2,outline='grey',fill='grey')
        self.durabilite_protection=canevas.create_text((self.x+Protections.largeur/2)-9,(self.y+Protections.hauteur_protections/2)-4,text=str(self.durabilite)+" vies",fill='white')
    def protection_touche(self):
        '''
        But : Verifier quand la protection se fait toucher si il lui reste au moins un de durabilité et en enleve un
        '''
        self.durabilite-=1
        if self.durabilite>0:
            if self.durabilite>15 and self.durabilite<=20:
                    canevas.itemconfig(self.durabilite_protection,text=(str(self.durabilite)),fill='green')
            if self.durabilite>10 and self.durabilite<=15:
                    canevas.itemconfig(self.durabilite_protection,text=(str(self.durabilite)),fill='yellow')
            if self.durabilite>5 and self.durabilite<=10:
                    canevas.itemconfig(self.durabilite_protection,text=(str(self.durabilite)),fill='orange')
            if self.durabilite<=5:
                    canevas.itemconfig(self.durabilite_protection,text=(str(self.durabilite)),fill='red')
    
        else:
            canevas.delete(self.apparence)
            canevas.delete(self.durabilite_protection)
'''--------------------------------------------------------------------------------------------------------------------'''
temps_dir=0
temps_recharge=1    
def assignation_touche_clavier(event):
    '''
    But : assigner les touches du clavier aux diffentes fonctions
    '''
    global temps_dir
    touche=event.keysym
    if touche=='Left':
        requin.mouvement(-1)
    elif touche=='Right':
        requin.mouvement(1)
    elif touche=='space':
        projectile=Projectile()
        projectiles_joueur.append(projectile)
        projectiles_joueur[Projectile.nombre_de_projectile-1].mouvement()
'''--------------------------------------------------------------------------------------------------------------------'''        
def lancer_partie():
    '''
    But : Nettoie le canvas et relance une partie 
    '''
    global ennemie,requin,jeu_en_cours, point_joueur, nombre_de_protection,Vies, Defences,fenetre
    fenetre.geometry("1920x1080")
    boutton_ajout_vie.destroy()
    boutton_retirer_vie.destroy()
    durabilite_protection.destroy()
    boutton_diminuer_vitesse_torpille.destroy()
    boutton_enlever_durabilite_protection.destroy()
    nombre_protection.destroy()
    boutton_ajouter_protection.destroy()
    boutton_ajouter_durabilite_protection.destroy()
    boutton_retirer_protection.destroy()
    boutton_retirer_torpille.destroy()
    boutton_augmenter_vitesse_torpille.destroy()
    boutton_ajout_torpille.destroy()
    vitesse_des_torpilles.destroy()
    nombre_torpille_par_ligne.destroy()
    canevas.grid()
    canevas.create_image(0,0,anchor='nw',image=image_de_fond)
    goal.grid_remove()
    bouton_jouer.grid_remove()
    requin=Requin()
    Protections.nombre=0
    Defences=[Protections() for i in range(nombre_de_protection)]
    jeu_en_cours = True
    Vies=vies
    ennemie=[]
    affichage_vies(Vies)
    Torpille.nombre_de_torpille=0
    
    for i in range(nbre_torpille_par_ligne):
        ennemie.append(Torpille())
        
    for i in ennemie:
        i.creation()
    mouvement_torpille()
    projectile_des_torpilles()
'''--------------------------------------------------------------------------------------------------------------------'''        
def win():
    '''
    But : Verifier qu'il n'y a plus d'ennemies vivant et faire apparaitre la fenetre de victoire
    '''
    gagne=True
    global jeu_en_cours, defaite
    for i in ennemie:
        if i.vivant:
            gagne=False
    if gagne:
        canevas.grid_remove()
        fenetre.geometry('260x75')
        goal.config(text='WIN')
        goal.config(bg='purple')
        goal.grid(row=1,column=1)
        canevas.delete("ALL")
        bouton_jouer.grid()
        bouton_jouer.config(text='Continue')
        Torpille.vitesse=vitesse_torpille
        jeu_en_cours=False
        suppr_projectile()
        defaite=False
'''--------------------------------------------------------------------------------------------------------------------'''        
def game_over():
    '''
    But : Afficher la fenetre de game over
    '''
    global jeu_en_cours, defaite
    canevas.grid_remove()
    fenetre.geometry('260x75')
    goal.config(text='LOSE')
    goal.config(bg='red')
    goal.grid(row=1,column=1)
    canevas.delete("ALL")
    bouton_jouer.grid()
    bouton_jouer.config(text='REPLAY')
    Torpille.vitesse=vitesse_torpille
    jeu_en_cours=False
    suppr_projectile()
    point_joueur=0
    score.config(text='Score: '+str(point_joueur))
'''--------------------------------------------------------------------------------------------------------------------'''                
def scores(pts):
    '''
    Entrée : int nombre de point
    Sortie : str point du joueur
    But : Afficher les point du joueur au cours de la partie
    '''
    global point_joueur
    point_joueur+=pts
    score.config(text='Score: '+str(point_joueur))
'''--------------------------------------------------------------------------------------------------------------------'''
def affichage_vies(Vies):
    '''
    Entrée : int nombre de vies
    Sortie
    But : Gerer les projectiles des torpilles
    '''
    nombre_vies.config(text='Vies: '+str(Vies))
'''--------------------------------------------------------------------------------------------------------------------'''        
def ajouter_vie():
    '''
    Sortie : str nombre de vie
    But : permet au joueur de s'ajouter des vies
    '''
    global vies
    if vies<30:
        vies+=1
        nombre_vies.config(text='Vies: '+str(vies))
'''--------------------------------------------------------------------------------------------------------------------'''
def retirer_vies():
    '''
    Sortie : str nombre de vie
    But : permet au joueur de s'enlever des vies
    '''
    global vies
    if vies>1:
        vies-=1
        nombre_vies.config(text='Vies: '+str(vies))
'''--------------------------------------------------------------------------------------------------------------------'''    
def ajouter_vitesse():
    '''
    Sortie : str vitesse torpille
    But : permet au joueur de d'ajouter de la vitesse au ennemies
    '''
    global vitesse_torpille
    if vitesse_torpille<10:
        vitesse_torpille+=0.5
        vitesse_des_torpilles.config(text='Vitesse torpilles '+str(vitesse_torpille))
'''--------------------------------------------------------------------------------------------------------------------'''    
def retirer_vitesse():
    '''
    Sortie : str vitesse torpille
    But : permet au joueur de d'enlever de la vitesse au ennemies
    '''
    global vitesse_torpille
    if vitesse_torpille>0.5:
        vitesse_torpille-=0.5
        vitesse_des_torpilles.config(text='Vitesse aliens '+str(vitesse_torpille))
'''--------------------------------------------------------------------------------------------------------------------'''    
def ajouter_torpille():
    '''
    Sortie : str nombre de torpille
    But : permet au joueur d'ajouter des ennemies
    '''
    global nbre_torpille_par_ligne
    if nbre_torpille_par_ligne<25:
        nbre_torpille_par_ligne+=1
        nombre_torpille_par_ligne.config(text='Nombre torpilles sur la ligne: '+str(nbre_torpille_par_ligne))
'''--------------------------------------------------------------------------------------------------------------------'''
def retirer_torpille():
    '''
    Sortie : str nombre de torpille
    But : permet au joueur d'enlever des ennemies
    '''
    global nbre_torpille_par_ligne
    if nbre_torpille_par_ligne>1:
        nbre_torpille_par_ligne-=1
        nombre_torpille_par_ligne.config(text='Nombre aliens sur la ligne: '+str(nbre_torpille_par_ligne))
'''--------------------------------------------------------------------------------------------------------------------'''
def ajouter_durabilite_protection():
    '''
    Sortie : str durabilité des protections
    But : permet au joueur d'ajouter de la durabilités aux protections
    '''
    global durabilite
    if durabilite<20:
        durabilite+=1
        durabilite_protection.config(text="Vies protections: "+str(durabilite))
'''--------------------------------------------------------------------------------------------------------------------'''                
def enlever_durabilite_protection():
    '''
    Sortie : str durabilité des protections
    But : permet au joueur d'enlever de la durabilités aux protections
    '''
    global durabilite
    if durabilite>1:
        durabilite-=1
        durabilite_protection.config(text="Vies protections: "+str(durabilite))
'''--------------------------------------------------------------------------------------------------------------------'''
def ajouter_protection():
    '''
    Sortie : str nombre de protection
    But : permet au joueur d'ajouter des protections
    '''
    global nombre_de_protection
    if nombre_de_protection<12:
        nombre_de_protection+=1
        nombre_protection.config(text="Nombre de protections: "+str(nombre_de_protection))
'''--------------------------------------------------------------------------------------------------------------------'''        
def retirer_protection():
    '''
    Sortie : str nombre de protection
    But : permet au joueur d'enlever des protections
    '''
    global nombre_de_protection
    if nombre_de_protection>1:
        nombre_de_protection-=1
        nombre_protection.config(text="Nombre de protections: "+str(nombre_de_protection))
'''--------------------------------------------------------------------------------------------------------------------'''
fenetre = tk.Tk()
'''--------------------------------------------------------------------------------------------------------------------'''
image_requin=tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "requin.gif"))
image_torpille=tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "torpille.gif"))
image_de_fond=tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "fondmarin.gif"))
'''--------------------------------------------------------------------------------------------------------------------'''
fenetre.title("Menu")
fenetre.iconbitmap(os.path.join(os.path.dirname(__file__), "submarine_icon.ico"))
fenetre['bg'] = 'darkcyan'
fenetre.title("SCUBA INVADER")
fenetre.geometry("800x190")
'''--------------------------------------------------------------------------------------------------------------------'''
score=tk.Label(fenetre,text='Score: '+str(point_joueur),bg="cadet blue",font = font.Font(family='Times New Roman',size = 13))
score.grid(row=0,column=3,padx=5,pady=5)
'''--------------------------------------------------------------------------------------------------------------------'''
nombre_vies=tk.Label(fenetre,text="Vies: "+str(vies),font = font.Font(family='Times New Roman',size = 12))
nombre_vies.grid(row=1,column=2,padx=5,pady=5)
nombre_vies.configure(bg='#49A')
'''--------------------------------------------------------------------------------------------------------------------'''
vitesse_des_torpilles=tk.Label(fenetre,text="Vitesse torpilles: "+str(vitesse_torpille),font = font.Font(family='Times New Roman',size = 12))
vitesse_des_torpilles.grid(row=1,column=3,padx=5,pady=5)
vitesse_des_torpilles.configure(bg='#49A')
'''--------------------------------------------------------------------------------------------------------------------'''
nombre_torpille_par_ligne=tk.Label(fenetre,text="Nombre torpilles sur la ligne: "+str(nbre_torpille_par_ligne),font = font.Font(family='Times New Roman',size = 12))
nombre_torpille_par_ligne.grid(row=1,column=4,padx=5,pady=5)
nombre_torpille_par_ligne.configure(bg='#49A')
'''--------------------------------------------------------------------------------------------------------------------'''
durabilite_protection=tk.Label(fenetre,text="Vies protections: "+str(durabilite),font = font.Font(family='Times New Roman',size = 12))
durabilite_protection.grid(row=1,column=5,padx=5,pady=5)
durabilite_protection.configure(bg='#49A')
'''--------------------------------------------------------------------------------------------------------------------'''
nombre_protection=tk.Label(fenetre,text="Nombre de protections: "+str(nombre_de_protection),font = font.Font(family='Times New Roman',size = 12))
nombre_protection.grid(row=1,column=6,padx=5,pady=5)
nombre_protection.configure(bg='#49A')
'''--------------------------------------------------------------------------------------------------------------------'''
canevas=tk.Canvas(fenetre,height=hauteur,width=largeur, bg='black')
canevas.grid(row=2,column=1,columnspan=2,padx=250,pady=50)
canevas.grid_remove()
canevas.focus_set()
canevas.bind('<Key>',assignation_touche_clavier)
'''--------------------------------------------------------------------------------------------------------------------'''
bouton_jouer=tk.Button(fenetre,text='PLAY',font = font.Font(family='Times New Roman',size = 15),relief='ridge', anchor='w',command=lancer_partie)
bouton_jouer.grid(row=0,column=1,padx=10,pady=10)
bouton_jouer.configure(bg='aquamarine')
'''--------------------------------------------------------------------------------------------------------------------'''
bouton_quitter=tk.Button(fenetre,text='LEAVE',font = font.Font(family='Times New Roman',size = 15),relief='ridge', anchor='w',command=fenetre.destroy)
bouton_quitter.grid(row=0,column=6,padx=5,pady=5)
bouton_quitter.configure(bg='medium aquamarine')
'''--------------------------------------------------------------------------------------------------------------------'''
boutton_ajout_vie=tk.Button(fenetre,text='+1 vies',command=ajouter_vie,relief='raised')
boutton_ajout_vie.grid(row=2,column=2,padx=5,pady=5)
boutton_ajout_vie.configure(bg='sky blue')
'''--------------------------------------------------------------------------------------------------------------------'''
boutton_retirer_vie=tk.Button(fenetre,text='-1 vies',command=retirer_vies,relief='raised')
boutton_retirer_vie.grid(row=3,column=2,padx=5,pady=5)
boutton_retirer_vie.configure(bg='sky blue')
'''--------------------------------------------------------------------------------------------------------------------'''
boutton_augmenter_vitesse_torpille=tk.Button(fenetre,text='+0.5 Vitesse torpilles',command=ajouter_vitesse,relief='raised')
boutton_augmenter_vitesse_torpille.grid(row=2,column=3,padx=5,pady=5)
boutton_augmenter_vitesse_torpille.configure(bg='sky blue')
'''--------------------------------------------------------------------------------------------------------------------'''
boutton_diminuer_vitesse_torpille=tk.Button(fenetre,text='-0.5 Vitesse aliens',command=retirer_vitesse,relief='raised')
boutton_diminuer_vitesse_torpille.grid(row=3,column=3,padx=5,pady=5)
boutton_diminuer_vitesse_torpille.configure(bg='sky blue')
'''--------------------------------------------------------------------------------------------------------------------'''
boutton_ajout_torpille=tk.Button(fenetre,text='+1 torpilles',command=ajouter_torpille,relief='raised')
boutton_ajout_torpille.grid(row=2,column=4,padx=5,pady=5)
boutton_ajout_torpille.configure(bg='sky blue')
'''--------------------------------------------------------------------------------------------------------------------'''
boutton_retirer_torpille=tk.Button(fenetre,text='-1 alien',command=retirer_torpille,relief='raised')
boutton_retirer_torpille.grid(row=3,column=4,padx=5,pady=5)
boutton_retirer_torpille.configure(bg='sky blue')
'''--------------------------------------------------------------------------------------------------------------------'''
boutton_ajouter_durabilite_protection=tk.Button(fenetre,text='+1 vies',command=ajouter_durabilite_protection,relief='raised')
boutton_ajouter_durabilite_protection.grid(row=2,column=5,padx=5,pady=5)
boutton_ajouter_durabilite_protection.configure(bg='sky blue')
'''--------------------------------------------------------------------------------------------------------------------'''
boutton_enlever_durabilite_protection=tk.Button(fenetre,text='-1 vies',command=enlever_durabilite_protection,relief='raised')
boutton_enlever_durabilite_protection.grid(row=3,column=5,padx=5,pady=5)
boutton_enlever_durabilite_protection.configure(bg='sky blue')
'''--------------------------------------------------------------------------------------------------------------------'''
boutton_ajouter_protection=tk.Button(fenetre,text='+1 ',command=ajouter_protection,relief='raised')
boutton_ajouter_protection.grid(row=2,column=6,padx=5,pady=5)
boutton_ajouter_protection.configure(bg='sky blue')
'''--------------------------------------------------------------------------------------------------------------------'''
boutton_retirer_protection=tk.Button(fenetre,text='-1',command=retirer_protection,relief='raised')
boutton_retirer_protection.grid(row=3,column=6,padx=5,pady=5)
boutton_retirer_protection.configure(bg='sky blue')
'''--------------------------------------------------------------------------------------------------------------------'''
goal=tk.Label(fenetre)
goal.grid(row=1,column=0)
goal.grid_remove()
'''--------------------------------------------------------------------------------------------------------------------'''
fenetre.mainloop()