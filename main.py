# FICHIER DU GROUPE AMINA, ANDREA, LENNY, RASSIM, JEU DU PENDU
# --------------------------------------
# PARTIE LENNY
from random import randint

liste = ['aigle','buse','faucon','milan'] # avec les listes d'amina

def mots(liste):
    element = randint(0,len(liste)-1)
    mot = liste[element]
    return mot

mot = mots(liste)

def tiret():
    global mot
    affichage=[]
    for i in range(len(mot)):
        affichage.append('_')
    return affichage

import tkinter as tk

erreur = 0


def ecrit_les_coords(evt):
    global erreur
    pos_x, pos_y = evt.x, evt.y
    erreur+=1
    print(pos_x,pos_y)



fenetre = tk.Tk()
fenetre.title("pendu")
fenetre.geometry("900x700")

mot_pointille = tiret()

label_erreur = tk.Label(fenetre, text="Vous avez fait "+str(erreur)+" erreur(s)")


def change_label_erreur():
    global erreur
    label_erreur.config(text="Vous avez fait "+str(erreur)+" erreur(s)")
    fenetre.after(10, change_label_erreur)

change_label_erreur()

def lettre_dans_le_mot_ou_erreur(lettre):
    global mot
    global mot_pointille
    global erreur
    if lettre in mot:
        for i in range(len(mot)):
            if mot[i] == lettre:
                mot_pointille[i] = lettre
        return True
    else: 
        if erreur >= 12:
            #tk.messagebox.M
          erreur +=1
        
boutonA=tk.Button(fenetre,text="A",command=lettre_dans_le_mot_ou_erreur("A"))
boutonB=tk.Button(fenetre,text="B",command=lettre_dans_le_mot_ou_erreur("B"))
boutonC=tk.Button(fenetre,text="C",command=lettre_dans_le_mot_ou_erreur("C"))
boutonD=tk.Button(fenetre,text="D",command=lettre_dans_le_mot_ou_erreur("D"))
boutonE=tk.Button(fenetre,text="E",command=lettre_dans_le_mot_ou_erreur("E"))
boutonF=tk.Button(fenetre,text="F",command=lettre_dans_le_mot_ou_erreur("F"))
boutonG=tk.Button(fenetre,text="G",command=lettre_dans_le_mot_ou_erreur("G"))
boutonH=tk.Button(fenetre,text="H",command=lettre_dans_le_mot_ou_erreur("H"))
boutonI=tk.Button(fenetre,text="I",command=lettre_dans_le_mot_ou_erreur("I"))
boutonJ=tk.Button(fenetre,text="J",command=lettre_dans_le_mot_ou_erreur("J"))
boutonK=tk.Button(fenetre,text="K",command=lettre_dans_le_mot_ou_erreur("K"))
boutonL=tk.Button(fenetre,text="L",command=lettre_dans_le_mot_ou_erreur("L"))
boutonM=tk.Button(fenetre,text="M",command=lettre_dans_le_mot_ou_erreur("M"))
boutonN=tk.Button(fenetre,text="N",command=lettre_dans_le_mot_ou_erreur("N"))
boutonO=tk.Button(fenetre,text="O",command=lettre_dans_le_mot_ou_erreur("O"))
boutonP=tk.Button(fenetre,text="P",command=lettre_dans_le_mot_ou_erreur("P"))
boutonQ=tk.Button(fenetre,text="Q",command=lettre_dans_le_mot_ou_erreur("Q"))
boutonR=tk.Button(fenetre,text="R",command=lettre_dans_le_mot_ou_erreur("R"))
boutonS=tk.Button(fenetre,text="S",command=lettre_dans_le_mot_ou_erreur("S"))
boutonT=tk.Button(fenetre,text="T",command=lettre_dans_le_mot_ou_erreur("T"))
boutonU=tk.Button(fenetre,text="U",command=lettre_dans_le_mot_ou_erreur("U"))
boutonV=tk.Button(fenetre,text="V",command=lettre_dans_le_mot_ou_erreur("V"))
boutonW=tk.Button(fenetre,text="W",command=lettre_dans_le_mot_ou_erreur("W"))
boutonX=tk.Button(fenetre,text="X",command=lettre_dans_le_mot_ou_erreur("X"))
boutonY=tk.Button(fenetre,text="Y",command=lettre_dans_le_mot_ou_erreur("Y"))
boutonZ=tk.Button(fenetre,text="Z",command=lettre_dans_le_mot_ou_erreur("Z"))

#print(mot_pointille)
#lettre_dans_le_mot("m")
#gprint(mot_pointille)

canvas_personnage = tk.Canvas(fenetre, width=500, height=400, bg="cyan")

#canvas_personnage.create_line(100,400,400,400,fill="black")
#canvas_personnage.create_line(150,400,150,150,fill="black")
#canvas_personnage.create_line(150,150,300,150,fill="black")    
#canvas_personnage.create_line(200,150,150,200,fill="black")
#canvas_personnage.create_line(300,150,300,200,fill="black")
#canvas_personnage.create_oval(325,250,275,200,outline="black") # OVAL
#canvas_personnage.create_line(300,250,300,300,fill="black")
#canvas_personnage.create_line(300,275,325,275,fill="black")
#canvas_personnage.create_line(275,275,325,275,fill="black")
#canvas_personnage.create_line(300,300,325,320,fill="black")
#canvas_personnage.create_line(300,300,275,320,fill="black")

liste_ligne=[[100,400,400,400],[150,400,150,150],[150,150,300,150],[200,150,150,200],[300,150,300,200],[325,250,275,200],[ 300,250,300,300],[300,275,325,275],[275,275,325,275],   [300,300,325,320],[300,300,275,320]]

canvas_personnage.bind("<Button-1>",ecrit_les_coords)


boutonA.grid(column=1,row=0)
boutonB.grid(column=1,row=1)
boutonC.grid(column=1,row=2)
boutonD.grid(column=1,row=3)
boutonE.grid(column=1,row=4)
boutonF.grid(column=1,row=5)
boutonG.grid(column=1,row=6)
boutonH.grid(column=1,row=7)
boutonI.grid(column=1,row=8)
boutonJ.grid(column=1,row=9)
boutonK.grid(column=2,row=0)
boutonL.grid(column=2,row=1)
boutonM.grid(column=2,row=2)
boutonN.grid(column=2,row=3)
boutonO.grid(column=2,row=4)
boutonP.grid(column=2,row=5)
boutonQ.grid(column=2,row=6)
boutonR.grid(column=2,row=7)
boutonS.grid(column=2,row=8)
boutonT.grid(column=2,row=9)
boutonU.grid(column=3,row=0)
boutonV.grid(column=3,row=1)
boutonW.grid(column=3,row=2)
boutonX.grid(column=3,row=3)
boutonY.grid(column=3,row=4)
boutonZ.grid(column=3,row=5) 

canvas_personnage.grid(row=0, column=0, rowspan=10)
label_erreur.grid(row=10,column=0)
fenetre.mainloop()
#
# -----------------------------------------------------