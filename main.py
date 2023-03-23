# FICHIER DU GROUPE AMINE, LENNY RASSIM, JEU DU PENDU
# --------------------------------------
# PARTIE LENNY
import tkinter as tk


def pixel_noir(evt):
    pos_x, pos_y = evt.x, evt.y
    print(pos_x,pos_y)


fenetre = tk.Tk()
fenetre.title("pendu")
fenetre.geometry("900x700")
mot = "motteste"
mot_pointille = ["_"]*len(mot)
erreur = 0

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
            tk.messagebox.M
        erreur +=1
        

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

canvas_personnage.bind("<Button-1>",pixel_noir)


canvas_personnage.grid(row=0, column=0, rowspan=9, columnspan=3)
fenetre.mainloop()
#
# -----------------------------------------------------