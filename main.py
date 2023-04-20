
from random import randint
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
#import PIL as pil
#from PIL import ImageTk

def aide():
        
        regles_jeu = tk.Toplevel()
        regles_jeu.geometry("800x300")
        regles_jeu.title("Regles du jeu")
        zone_texte1 = tk.Label (regles_jeu, text = "Le jeu du pendu est un jeu de devinettes où un joueur doit deviner un mot en proposant des lettres. Voici les règles de base du jeu :")
        zone_texte2= tk.Label (regles_jeu, text = "1. Le joueur doit deviner le mot en proposant des lettres une à une.")
        zone_texte3 = tk.Label (regles_jeu, text = "2. Si une lettre proposée est dans le mot, elle est révélée dans le mot.")
        zone_texte4= tk.Label (regles_jeu, text = "3. Si une lettre proposée n'est pas dans le mot, un élément est ajouté au dessin du pendu.")
        zone_texte5 = tk.Label (regles_jeu, text = "4. Le joueur a un nombre limité de propositions avant que le dessin ne soit complété (10 erreurs sont autorisées).")
        zone_texte6 = tk.Label (regles_jeu, text = "5. Si le joueur devine le mot avant que le dessin ne soit complété, il gagne. Sinon, il perd.")
        zone_texte1.grid(sticky="nw")
        zone_texte2.grid(sticky="nw")
        zone_texte3.grid(sticky="nw")
        zone_texte4.grid(sticky="nw")
        zone_texte5.grid(sticky="nw")
        zone_texte6.grid(sticky="nw")
        boutton_compris=tk.Button(regles_jeu, text="J'ai compris", command= regles_jeu.destroy)
        boutton_compris.grid(sticky="s")

        regles_jeu.mainloop

def parse_line( ligne , sep, colonne, type) :
    li = ligne.split(sep)
    if type == "int" :
        return(int(li[colonne]))
    elif type == "str" :
        return(li[colonne])
mote=""
chrge = False

jeu = False

fenetre_menu = tk.Tk()
fenetre_menu.geometry("800x500+400+200")
fenetre_menu.grid_columnconfigure(0, weight=1)
fenetre_menu.grid_columnconfigure(1, weight=1)
fenetre_menu.grid_columnconfigure(2, weight=1)
fenetre_menu.grid_columnconfigure(3, weight=1)
fenetre_menu.grid_rowconfigure(1, weight=1)
fenetre_menu.grid_rowconfigure(2, weight=1)
fenetre_menu.grid_rowconfigure(3, weight=1)
fenetre_menu.grid_rowconfigure(4, weight=1)
fenetre_menu.grid_rowconfigure(5, weight=1)
font_label = font.Font(size=20)
font_bouton = font.Font(size=15)
font_label2 = font.Font(size=16)
difficulte = 0

def je(n = None):
    global difficulte
    if n != 1:
        global jeu
        jeu = True
        difficulte=scroller.get()
    fenetre_menu.destroy()

def charger():
    global mote
    global score
    global chrge
    chrge = True
    path = "C:/Users/Administrateur/Desktop/save.csv"
    mode = "r"
    csv_save = open(path, mode)
    ligne = csv_save.readline()
    mote = parse_line(ligne, ",", 0, "str")
    score = parse_line(ligne, ",", 1, "int")
    csv_save.close()
    je()

def mots(liste):
    element = randint(0,len(liste)-1)
    mot = liste[element]
    return mot


score = 0
Label_1 = tk.Label(fenetre_menu, text="Jeu du Pendu", fg = "black")
Label_1['font'] = font_label
Label_2 = tk.Label(fenetre_menu, text="Choisis ta difficulté :")
Label_2['font'] = font_label2

#image=ImageTk.PhotoImage(Image.open("pendu.jpg") )
#label_photo=tk.Label(fenetre_menu,img=image)

scroller=tk.Scale(fenetre_menu ,from_=0, to=8, orient="horizontal")


bouton_aide= tk.Button(fenetre_menu, text="Aide", command=aide, bg="cyan")
bouton_aide['font'] = font_bouton
bouton_aide.grid(sticky="nw")
bouton_jouer = tk.Button(fenetre_menu, text="Jouer", command=lambda : je())
bouton_quitter = tk.Button(fenetre_menu, text="Quitter", command=lambda : je(1))
bouton_charger = tk.Button(fenetre_menu, text="Charger une partie ", command= charger)
bouton_jouer['font'] = font_bouton
bouton_quitter['font'] = font_bouton
bouton_charger['font'] = font_bouton

Label_1.grid(row = 1, column = 1)
bouton_jouer.grid(row = 4, column = 1)
bouton_quitter.grid(row = 5, column = 3)
bouton_charger.grid(row = 0, column = 3)
Label_2.grid(row=5, column=0)
#label_photo.grid(row=1,column=1)
scroller.grid(row=5, column=1)

            
fenetre_menu.mainloop()



while jeu == True:
    LISTE_3_LETTRES = [ "ANE", "AXE", "BEL", "BIP", "CAR", "COL", "COQ", "COR", "COU", "CRI", "GAG", "GAZ", "GEL", "JUS", "NET", "NUL", "VAL", "SKI", "SOT", "TAS", "TIC"]
    
    LISTE_4_LETTRES= ["ETRE", "BEAU", "BETE", "BOXE", "BRUN", "CERF", "CHEZ", "CIRE", "FEMME", "DENT", "DOCK", "DODO", "DRAP", "DUNE", "FAUX", "IBIS", "JAZZ", "JOLI", "JOUE", "KAKI", "LOEO", "LOIN", "LONG", "LUNE", "LYNX", "MINE", "MURE", "OUIE", "OURS", "PION", "RHUM", "ROCK", "SEAU", "TEST", "THYM", "TROU", "TRUC", "USER", "VERT", "YOGA"]
    
    LISTE_5_LETTRES= ["ACCES", "AIMER", "ALOES", "ASSEZ", "AVION", "BALAI", "BANJO", "BARBE", "BONNE", "BRUIT", "BUCHE", "CACHE", "CAPOT", "CARTE", "CHIEN", "CRâNE", "CYCLE", "EBENE", "ESSAI", "GIFLE", "JAMBE", "KOALA", "LIVRE", "LOURD", "MAMAN", "MOULT", "NOEUD", "ORTIE", "PêCHE", "POIRE", "POMME", "POSTE", "PRUNE", "RADAR", "RADIS", "ROBOT", "ROUTE", "RUGBY", "SEUIL", "TAUPE", "TENUE", "TEXTE", "TYRAN", "USUEL", "VALSE"]
    
    LISTE_6_LETTRES= ["ACAJOU", "AGNEAU", "ALARME", "ANANAS", "ANGORA", "ANIMAL","ARCADE", "AVIRON", "BABINE", "BALADE", "BONZAI", "BASSIN", "BILLET", "BOUCHE", "BOUCLE", "BRONZE", "CABANE", "CLOCHE", "CHEQUE", "CIRAGE", "CRAYON", "GARAGE", "GOSPEL", "GOULOT", "GRAMME", "GRELOT", "GUENON", "HOCHET", "HORMIS", "HUMOUR", "HURLER", "JARGON", "LIMITE", "LIONNE", "MENTHE", "OISEAU" , "PODIUM", "POULPE", "POUMON", "PUZZLE", "QUARTZ", "RAPIDE", "SEISME", "TETINE", "TOMATE", "WASABI", "WHISKY", "ZIPPER", "ALGERIE"]
    
    
    LISTE_7_LETTRES= ["ABRITER", "BALLAST", "BARYTON", "BASSINE", "BILLARD", "BRETZEL", "CHARIOT", "CLAIRON", "CORBEAU", "CORTEGE", "CRAPAUD", "DENTIER", "DRAPEAU", "EXEMPLE", "FOURMIS", "GRANDIR", "ICEBERG", "JAVELOT" , "JOURNAL", "JOURNEE", "LOSANGE", "MACADAM", "MONDIAL", "NOTABLE", "OXYGENE", "PANIQUE", "PETROLE", "POTERIE", "POUVOIR",  "SCOOTER", "SENTEUR", "SIFFLET", "SPIRALE", "SUCETTE", "TONNEAU", "TROUSSE", "TUNIQUE", "UKULELE", "VAUTOUR", "ZOZOTER"]
    
    LISTE_8_LETTRES= ["AQUARIUM", "ARAIGNEE", "ARBALETE", "ARCHIPEL", "BANQUISE", "BATTERIE", "BROCANTE", "BROUHAHA", "CAPELINE", "CLAVECIN", "CLOPORTE", "DEBUTANT" , "DIAPASON", "GANGSTER", "GOTHIQUE", "HAUTBOIS", "HERISSON", "LOGICIEL", "OBJECTIF", "PARANOIA", "PARCOURS", "PASTICHE", "QUESTION", "SCARABEE", "SCORPION", "SYMPTOME", "TABOURET", "TOMAHWWK", "TOUJOURS", "TOURISME", "TRIANGLE", "UTOPIQUE", "ZEPPELIN"]
    
    LISTE_9_LETTRES=["ACCORDEON", "ASCENSEUR", "ASCENSION", "ASEPTISER", "AUTOROUTE", "AVALANCHE", "BALALAIKA" , "BILBOQUET", "BOURRICOT", "BRILLANCE", "CABRIOLET", "CONTRARIO", "CORNEMUSE", "DANGEREUX", "EPLUCHAGE", "FEODALITE", "FORTERESSE", "GONDOLIER", "GRAPHIQUE", "HOROSCOPE", "INTREPIDE", "KLAXONNER", "MASCARADE", "METAPHORE", "NARRATEUR", "PERIPETIE", "POPULAIRE", "PRINTEMPS", "QUEMANDER", "TAMBOURIN", "VESTIAIRE", "XYLOPHONE"]
    
    
    LISTE_10_LETTRES=["ACROSTICHE", "APOCALYPSE", "ATTRACTION", "AVENTURIER", "BOUILLOTTE", "CITROUILLE", "CONTROVERSE", "COQUELICOT", "DISSIMULER" , "FLIBUSTIER", "FORESTIERE", "GRENOUILLE", "IMPOSSIBLE", "LABYRINTHE", "MAHARADJAH", "PRUDEMMENT", "QUADRICEPS" , "SOLILOQUER", "SUBJECTIVE"]
    
    LISTE_11_LETTREETPLUS = [ "BACCALAUREAT", "ABRACADABRA", "FRANCOPHILE", "PANDEMONIUM", "CHLOROPHYLLE" , "CONSENTEMENT" , "METALLURGIE" , "METAMORPHOSE", "MONTGOLFIERE", "KALEIDOSCOPE", "CONQUISTADOR", "CONSPIRATEUR", "RHODODENDRON", "QUALIFICATION", "PROTOZOAIRE", "QUADRILATERE", "ZYGOMATIQUE", "SORCELLERIE", "BELLIGERANT"]
    

    liste_liste= [LISTE_3_LETTRES,LISTE_4_LETTRES,LISTE_4_LETTRES,LISTE_6_LETTRES,LISTE_7_LETTRES,LISTE_8_LETTRES,LISTE_9_LETTRES,LISTE_10_LETTRES,LISTE_11_LETTREETPLUS]
    def choisirliste(liste,entier):
       return liste[entier]
    
    
    liste = choisirliste(liste_liste, difficulte)


    if chrge:
        mot = mote
    else:
        mot = mots(liste)

    
    

    
    print(mot)


    def tiret():
        global mot
        affichage=[]
        for i in range(len(mot)):
            affichage.append('*')
        return affichage


    erreur = 0


    def ecrit_les_coords(evt):
        global erreur
        pos_x, pos_y = evt.x, evt.y
        erreur+=1
        print(pos_x,pos_y)


    def deviner_le_mt(mot1):
        global erreur
        mot1 = mot1.upper()
        if mot == mot1:
            messagebox.showinfo(fenetre,message="Vous avez gagné !")
            fenetre.destroy()
        else:
            erreur+=1
            creer_lignes(liste_ligne, erreur, canvas_personnage)



    fenetre = tk.Tk()
    fenetre.title("pendu")
    fenetre.geometry("820x555+400+200")

    mot_pointille = tiret()

    canvas_personnage = tk.Canvas(fenetre, width=500, height=400, bg="cyan")

    lettre_deja_donne = []
    lettre_deja_donne2 = []
    label_erreur = tk.Label(fenetre, text="Vous avez fait "+str(erreur)+" erreur(s)")
    label_lettre_deja_utilise = tk.Label(fenetre, text="Vous n'avez utilisé aucune lettre : ")

    entre = tk.Entry(fenetre,width=10,font = ("helvetica", "10"))

    button_pour_mot = tk.Button(fenetre, text="Deviner le mot ?", command= lambda:deviner_le_mt(entre.get()))

    reussite = 0
    label_score = tk.Label(fenetre, text = "Score : "+str(score))



    def change_label_deja(lett):
        global lettre_deja_donne2
        cdc = ''
        for lettre in lettre_deja_donne2:
            cdc = cdc + lettre + ", " 
        label_lettre_deja_utilise.config(text="Vous avez déjà utilisé les lettres : "+cdc)

    def change_label_erreur():
        global erreur
        global score
        label_erreur.config(text="Vous avez fait "+str(erreur)+" erreur(s)")
        label_score.config(text="Score : "+str(score))
        fenetre.after(10, change_label_erreur)

    change_label_erreur()




    liste_ligne=[[100,400,400,400],[150,400,150,150],[150,150,300,150],[200,150,150,200],[300,150,300,200],[325,250,275,200],[ 300,250,300,300],[300,275,325,275],[275,275,325,275],   [300,300,325,320],[300,300,275,320]]

    def creer_lignes(liste_ligne, index, canevas):
        x1, y1, x2, y2 = liste_ligne[index-1]
        if index != 6:
            canevas.create_line(x1, y1, x2, y2, fill="black")
        else: canevas.create_oval(x1, y1, x2, y2, outline="black")

    #for i in range(len(liste_ligne)):
    #    creer_lignes(liste_ligne, i, canvas_personnage)


    mot_pointille_shw = ""
    for i in range(len(mot_pointille)):
        mot_pointille_shw = ' '+mot_pointille[i]+mot_pointille_shw

    label_pointille = tk.Label(fenetre, text=str(mot_pointille_shw))

    def change_label_pointille(mot):
        mot_pointille_shw = ""
        for i in range(len(mot)):
            mot_pointille_shw = mot_pointille_shw+' '+mot[i]
        label_pointille.config(text=mot_pointille_shw)

    nb_lettre=0
    l_rien=[]
    for i in range(len(mot)):
        if not(mot[i] in l_rien):
            l_rien.append(mot[i])
            nb_lettre+=1

    def rejouer(ent,fen):
        global jeu
        if ent == 1:
            jeu = True
        else: jeu = False
        fen.destroy()

    fenetre.grid_rowconfigure(13, weight=1)


    def sauvegarder():
        global mot
        global score
        path = "C:/Users/Administrateur/Desktop/save.csv"
        mode = "w"
        csv_save = open(path, mode)
        csv_save.write(mot+","+str(score)+"\n")
        csv_save.close()
    
    bouton_save = tk.Button(fenetre, text="Sauvegarder", command=sauvegarder)
    
    def indications():
        global mot
        indice_rand = randint(0,len(mot)-1)
        lettre_rand = mot[indice_rand]
        while lettre_rand in lettre_deja_donne:
            indice_rand = randint(0,len(mot)-1)
            lettre_rand = mot[indice_rand]
        bouton_indication.grid_forget()
        messagebox.showinfo(fenetre,message="Dans le mot, il y a la lettre, "+str(lettre_rand))
        
    bouton_indication = tk.Button(fenetre, command = indications,text="Indice pour le mot")

    def lettre_dans_le_mot_ou_erreur(lettre):
        global mot
        global mot_pointille
        global erreur
        global liste_ligne
        global canvas_personnage
        global reussite
        global lettre_deja_donne
        global nb_lettre
        global score
        if lettre == "A":
            boutonA.grid_forget()
        if lettre == "B":
            boutonB.grid_forget()
        if lettre == "C":
            boutonC.grid_forget()
        if lettre == "D":
            boutonD.grid_forget()
        if lettre == "E":
            boutonE.grid_forget()
        if lettre == "F":
            boutonF.grid_forget()
        if lettre == "G":
            boutonG.grid_forget()
        if lettre == "H":
            boutonH.grid_forget()
        if lettre == "I":
            boutonI.grid_forget()
        if lettre == "J":
            boutonJ.grid_forget()
        if lettre == "K":
            boutonK.grid_forget()
        if lettre == "L":
            boutonL.grid_forget()
        if lettre == "M":
            boutonM.grid_forget()
        if lettre == "N":
            boutonN.grid_forget()
        if lettre == "O":
            boutonO.grid_forget()
        if lettre == "P":
            boutonP.grid_forget()
        if lettre == "Q":
            boutonQ.grid_forget()
        if lettre == "R":
            boutonR.grid_forget()
        if lettre == "S":
            boutonS.grid_forget()
        if lettre == "T":
            boutonT.grid_forget()
        if lettre == "U":
            boutonU.grid_forget()
        if lettre == "V":
            boutonV.grid_forget()
        if lettre == "W":
            boutonW.grid_forget()
        if lettre == "X":
            boutonX.grid_forget()
        if lettre == "Y":
            boutonY.grid_forget()
        if lettre == "Z":
            boutonZ.grid_forget()
        if lettre in mot:
            for i in range(len(mot)):
                if mot[i] == lettre:
                    mot_pointille[i] = lettre
            if not(lettre in lettre_deja_donne2):
                lettre_deja_donne2.append(lettre)
            change_label_deja(lettre)
            #print(mot_pointille)
            if not (lettre in lettre_deja_donne):
                change_label_pointille(mot_pointille)
                reussite += 1
                lettre_deja_donne.append(lettre)
                #print(reussite)
                #print(mot)
        
            if reussite == nb_lettre:
                messagebox.showinfo(fenetre,message="Vous avez gagné !")
                fenetre.destroy()
        
        else:
            
            if not(lettre in lettre_deja_donne2):
                lettre_deja_donne2.append(lettre)
                change_label_deja(lettre)
                erreur +=1
                creer_lignes(liste_ligne, erreur, canvas_personnage)
                score += 1
            if erreur >= 11:
                messagebox.showinfo(fenetre,message="Vous avez perdu !")
                fenetre.destroy()



            
    boutonA=tk.Button(fenetre,text="A",command=lambda : lettre_dans_le_mot_ou_erreur("A"))
    boutonB=tk.Button(fenetre,text="B",command=lambda : lettre_dans_le_mot_ou_erreur("B"))
    boutonC=tk.Button(fenetre,text="C",command=lambda : lettre_dans_le_mot_ou_erreur("C"))
    boutonD=tk.Button(fenetre,text="D",command=lambda : lettre_dans_le_mot_ou_erreur("D"))
    boutonE=tk.Button(fenetre,text="E",command=lambda : lettre_dans_le_mot_ou_erreur("E"))
    boutonF=tk.Button(fenetre,text="F",command=lambda : lettre_dans_le_mot_ou_erreur("F"))
    boutonG=tk.Button(fenetre,text="G",command=lambda : lettre_dans_le_mot_ou_erreur("G"))
    boutonH=tk.Button(fenetre,text="H",command=lambda : lettre_dans_le_mot_ou_erreur("H"))
    boutonI=tk.Button(fenetre,text="I",command=lambda : lettre_dans_le_mot_ou_erreur("I"))
    boutonJ=tk.Button(fenetre,text="J",command=lambda : lettre_dans_le_mot_ou_erreur("J"))
    boutonK=tk.Button(fenetre,text="K",command=lambda : lettre_dans_le_mot_ou_erreur("K"))
    boutonL=tk.Button(fenetre,text="L",command=lambda : lettre_dans_le_mot_ou_erreur("L"))
    boutonM=tk.Button(fenetre,text="M",command=lambda : lettre_dans_le_mot_ou_erreur("M"))
    boutonN=tk.Button(fenetre,text="N",command=lambda : lettre_dans_le_mot_ou_erreur("N"))
    boutonO=tk.Button(fenetre,text="O",command=lambda : lettre_dans_le_mot_ou_erreur("O"))
    boutonP=tk.Button(fenetre,text="P",command=lambda : lettre_dans_le_mot_ou_erreur("P"))
    boutonQ=tk.Button(fenetre,text="Q",command=lambda : lettre_dans_le_mot_ou_erreur("Q"))
    boutonR=tk.Button(fenetre,text="R",command=lambda : lettre_dans_le_mot_ou_erreur("R"))
    boutonS=tk.Button(fenetre,text="S",command=lambda : lettre_dans_le_mot_ou_erreur("S"))
    boutonT=tk.Button(fenetre,text="T",command=lambda : lettre_dans_le_mot_ou_erreur("T"))
    boutonU=tk.Button(fenetre,text="U",command=lambda : lettre_dans_le_mot_ou_erreur("U"))
    boutonV=tk.Button(fenetre,text="V",command=lambda : lettre_dans_le_mot_ou_erreur("V"))
    boutonW=tk.Button(fenetre,text="W",command=lambda : lettre_dans_le_mot_ou_erreur("W"))
    boutonX=tk.Button(fenetre,text="X",command=lambda : lettre_dans_le_mot_ou_erreur("X"))
    boutonY=tk.Button(fenetre,text="Y",command=lambda : lettre_dans_le_mot_ou_erreur("Y"))
    boutonZ=tk.Button(fenetre,text="Z",command=lambda : lettre_dans_le_mot_ou_erreur("Z"))

    bouton_quit=tk.Button(fenetre,text='Quitter',command=lambda : fenetre.destroy())
    

    #print(mot_pointille)
    #lettre_dans_le_mot("m")
    #gprint(mot_pointille)


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

  
    boutonA.grid(column=0,row=10)
    boutonB.grid(column=1,row=10)
    boutonC.grid(column=2,row=10)
    boutonD.grid(column=3,row=10)
    boutonE.grid(column=4,row=10)
    boutonF.grid(column=5,row=10)
    boutonG.grid(column=0,row=11)
    boutonH.grid(column=1,row=11)
    boutonI.grid(column=2,row=11)
    boutonJ.grid(column=3,row=11)
    boutonK.grid(column=4,row=11)
    boutonL.grid(column=5,row=11)
    boutonM.grid(column=0,row=12)
    boutonN.grid(column=1,row=12)
    boutonO.grid(column=2,row=12)
    boutonP.grid(column=3,row=12)
    boutonQ.grid(column=4,row=12)
    boutonR.grid(column=5,row=12)
    boutonS.grid(column=0,row=13)
    boutonT.grid(column=1,row=13)
    boutonU.grid(column=2,row=13)
    boutonV.grid(column=3,row=13)
    boutonW.grid(column=4,row=13)
    boutonX.grid(column=5,row=13)
    boutonY.grid(column=2,row=14)
    boutonZ.grid(column=3,row=14) 

    canvas_personnage.grid(row=0, column=0, rowspan=10,columnspan=6)
    label_erreur.grid(row=0,column=7)
    label_pointille.grid(row = 1, column=7)
    label_lettre_deja_utilise.grid(row = 2, column=6, columnspan=3) # il faut griser les lettres utilisées sinon ca sort de la fenetre
    entre.grid(row= 7, column=6)
    bouton_indication.grid(row = 5, column=7)
    button_pour_mot.grid(row= 7, column=7)
    label_score.grid(row=9,column=6)
    bouton_save.grid(row = 9, column=7)
    bouton_quit.grid(row=14,column=10)

    fenetre.resizable(width = False, height = False)

    fenetre.mainloop()
    
    fenetre_fin = tk.Tk() 
    fenetre_fin.geometry("100x100+500+200") 
    fenetre_fin.grid_rowconfigure(1, weight=1)
    fenetre_fin.grid_rowconfigure(2, weight=1)
    bouton_rejouer = tk.Button(fenetre_fin, text='Rejouer ?', command=lambda : rejouer(1,fenetre_fin))
    bouton_quitter = tk.Button(fenetre_fin, text='Quitter ?', command=lambda : rejouer(0,fenetre_fin))
    bouton_rejouer.grid(row=0, column=0)
    bouton_quitter.grid(row=1, column=0)

    fenetre_fin.mainloop()
    #
    # -----------------------------------------------------