# FICHIER DU GROUPE AMINA, ANDREA, LENNY, RASSIM, JEU DU PENDU
# --------------------------------------
# PARTIE LENNY
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
mot = "motteste"
mot_pointille = ["_"]*len(mot)
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

canvas_personnage.bind("<Button-1>",ecrit_les_coords)



canvas_personnage.grid(row=0, column=0, rowspan=9, columnspan=3)
label_erreur.grid(row=10,column=0)
fenetre.mainloop()
#
# -----------------------------------------------------