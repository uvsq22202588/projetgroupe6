# FICHIER DU GROUPE AMINA, ANDREA, LENNY, RASSIM, JEU DU PENDU
# --------------------------------------

from random import randint
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

jeu = False

fenetre_menu = tk.Tk()
messagebox.showinfo(fenetre_menu,message="Si vous êtes sur mac, il est possible que l'affichage soit un peu moche du style tout noir")
fenetre_menu.geometry("800x500+400+200")
fenetre_menu.grid_columnconfigure(0, weight=1)
fenetre_menu.grid_columnconfigure(1, weight=1)
fenetre_menu.grid_columnconfigure(2, weight=1)
fenetre_menu.grid_columnconfigure(3, weight=1)
fenetre_menu.grid_rowconfigure(1, weight=1)
fenetre_menu.grid_rowconfigure(2, weight=1)
fenetre_menu.grid_rowconfigure(3, weight=1)
fenetre_menu.grid_rowconfigure(4, weight=1)
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

Label_1 = tk.Label(fenetre_menu, text="Jeu du Pendu", fg = "black")
Label_1['font'] = font_label
Label_2 = tk.Label(fenetre_menu, text="difficulté :")
Label_2['font'] = font_label2

scroller=tk.Scale(fenetre_menu ,from_=0, to=8, orient="horizontal")


bouton_jouer = tk.Button(fenetre_menu, text="Jouer", command=lambda : je())
bouton_quitter = tk.Button(fenetre_menu, text="Quitter", command=lambda : je(1))
bouton_jouer['font'] = font_bouton
bouton_quitter['font'] = font_bouton

Label_1.grid(row = 1, column = 1)
bouton_jouer.grid(row = 2, column = 1)
bouton_quitter.grid(row = 3, column = 1)
Label_2.grid(row=4, column=0)
scroller.grid(row=4, column=1)

            
fenetre_menu.mainloop()



if jeu == True:
    LISTE_3_LETTRES = [ "ANE", "AXE", "BEL", "BIP", "CAR", "COL", "COQ", "COR", "COU", "CRI", "GAG", "GAZ", "GEL", "JUS", "NET", "NUL", "VAL", "SKI", "SOT", "TAS", "TIC"]
    
    LISTE_4_LETTRES= ["ETRE", "BEAU", "BETE", "BOXE", "BRUN", "CERF", "CHEZ", "CIRE", "FEMME", "DENT", "DOCK", "DODO", "DRAP", "DUNE", "FAUX", "IBIS", "JAZZ", "JOLI", "JOUE", "KAKI", "LOEO", "LOIN", "LONG", "LUNE", "LYNX", "MINE", "MURE", "OUIE", "OURS", "PION", "RHUM", "ROCK", "SEAU", "TEST", "THYM", "TROU", "TRUC", "USER", "VERT", "YOGA"]
    
    LISTE_5_LETTRES= ["ACCES", "AIMER", "ALOES", "ASSEZ", "AVION", "BALAI", "BANJO", "BARBE", "BONNE", "BRUIT", "BUCHE", "CACHE", "CAPOT", "CARTE", "CHIEN", "CRâNE", "CYCLE", "EBENE", "ESSAI", "GIFLE", "JAMBE", "KOALA", "LIVRE", "LOURD", "MAMAN", "MOULT", "NOEUD", "ORTIE", "PêCHE", "POIRE", "POMME", "POSTE", "PRUNE", "RADAR", "RADIS", "ROBOT", "ROUTE", "RUGBY", "SEUIL", "TAUPE", "TENUE", "TEXTE", "TYRAN", "USUEL", "VALSE"]
    
    LISTE_6_LETTRES= ["ACAJOU", "AGNEAU", "ALARME", "ANANAS", "ANGORA", "ANIMAL"," ARCADE", "AVIRON", "BABINE", "BALADE", "BONZAI", "BASSIN", "BILLET", "BOUCHE", "BOUCLE", "BRONZE", "CABANE", "CLOCHE", "CHEQUE", "CIRAGE", "CRAYON", "GARAGE", "GOSPEL", "GOULOT", "GRAMME", "GRELOT", "GUENON", "HOCHET", "HORMIS", "HUMOUR", "HURLER", "JARGON", "LIMITE", "LIONNE", "MENTHE", "OISEAU" , "PODIUM", "POULPE", "POUMON", "PUZZLE", "QUARTZ", "RAPIDE", "SEISME", "TETINE", "TOMATE", "WASABI", "WHISKY", "ZIPPER", "ALGERIE"]
    
    
    LISTE_7_LETTRES= ["ABRITER", "BALLAST", "BARYTON", "BASSINE", "BILLARD", "BRETZEL", "CHARIOT", "CLAIRON", "CORBEAU", "CORTEGE", "CRAPAUD", "DENTIER", "DRAPEAU", "EXEMPLE", "FOURMIS", "GRANDIR", "ICEBERG", "JAVELOT" , "JOURNAL", "JOURNEE", "LOSANGE", "MACADAM", "MONDIAL", "NOTABLE", "OXYGENE", "PANIQUE", "PETROLE", "POTERIE", "POUVOIR",  "SCOOTER", "SENTEUR", "SIFFLET", "SPIRALE", "SUCETTE", "TONNEAU", "TROUSSE", "TUNIQUE", "UKULELE", "VAUTOUR", "ZOZOTER"]
    
    LISTE_8_LETTRES= ["AQUARIUM", "ARAIGNEE", "ARBALETE", "ARCHIPEL", "BANQUISE", "BATTERIE", "BROCANTE", "BROUHAHA", "CAPELINE", "CLAVECIN", "CLOPORTE", "DEBUTANT" , "DIAPASON", "GANGSTER", "GOTHIQUE", "HAUTBOIS", "HERISSON", "LOGICIEL", "OBJECTIF", "PARANOIA", "PARCOURS", "PASTICHE", "QUESTION", "SCARABEE", "SCORPION", "SYMPTOME", "TABOURET", "TOMAHWWK", "TOUJOURS", "TOURISME", "TRIANGLE", "UTOPIQUE", "ZEPPELIN"]
    
    LISTE_9_LETTRES=["ACCORDEON", "ASCENSEUR", "ASCENSION", "ASEPTISER", "AUTOROUTE", "AVALANCHE", "BALALAIKA" , "BILBOQUET", "BOURRICOT", "BRILLANCE", "CABRIOLET", "CONTRARIO", "CORNEMUSE", "DANGEREUX", "EPLUCHAGE", "FEODALITE", "FORTERESSE", "GONDOLIER", "GRAPHIQUE", "HOROSCOPE", "INTREPIDE", "KLAXONNER", "MASCARADE", "METAPHORE", "NARRATEUR", "PERIPETIE", "POPULAIRE", "PRINTEMPS", "QUEMANDER", "TAMBOURIN", "VESTIAIRE", "XYLOPHONE"]
    
    
    LISTE_10_LETTRES=["ACROSTICHE", "APOCALYPSE", "ATTRACTION", "AVENTURIER", "BOUILLOTTE", "CITROUILLE", "CONTROVERSE", "COQUELICOT", "DISSIMULER" , "FLIBUSTIER", "FORESTIERE", "GRENOUILLE", "IMPOSSIBLE", "LABYRINTHE", "MAHARADJAH", "PRUDEMMENT", "QUADRICEPS" , "SOLILOQUER", "SUBJECTIVE"]
    
    LISTE_11_LETTREETPLUS = [ "BACCALAUREAT", "ABRACADABRA", "FRANCOPHILE", "PANDEMONIUM", "CHLOROPHYLLE" , "CONSENTEMENT" , "METALLURGIE" , "METAMORPHOSE", "MONTGOLFIERE", "KALEIDOSCOPE", "CONQUISTADOR", "CONSPIRATEUR", "RHODODENDRON", "QUALIFICATION", "PROTOZOAIRE", "QUADRILATERE", "ZYGOMATIQUE", "SORCELLERIE", "BELLIGERANT"]
    

    liste_liste= [LISTE_3_LETTRES,LISTE_4_LETTRES,LISTE_4_LETTRES,LISTE_6_LETTRES,LISTE_7_LETTRES,LISTE_8_LETTRES,LISTE_9_LETTRES,LISTE_10_LETTRES,LISTE_11_LETTREETPLUS]
    def choisirliste(liste,entier):
       return liste[entier]
    
    
    liste = choisirliste(liste_liste, difficulte)


    def mots(liste):
        element = randint(0,len(liste)-1)
        mot = liste[element]
        return mot


    mot = mots(liste)
    print(mot)


    def tiret():
        global mot
        affichage=[]
        for i in range(len(mot)):
            affichage.append('_')
        return affichage


    erreur = 0


    def ecrit_les_coords(evt):
        global erreur
        pos_x, pos_y = evt.x, evt.y
        erreur+=1
        print(pos_x,pos_y)



    fenetre = tk.Tk()
    fenetre.title("pendu")
    fenetre.geometry("800x500+400+200")

    mot_pointille = tiret()

    canvas_personnage = tk.Canvas(fenetre, width=500, height=400, bg="cyan")

    lettre_deja_donne = []
    lettre_deja_donne2 = []
    label_erreur = tk.Label(fenetre, text="Vous avez fait "+str(erreur)+" erreur(s)")
    label_lettre_deja_utilise = tk.Label(fenetre, text="Vous n'avez utilisé aucune lettre : ")

    reussite = 0


    def change_label_deja(lett):
        global lettre_deja_donne2
        cdc = ''
        for lettre in lettre_deja_donne2:
            cdc = cdc + lettre + ", " 
        label_lettre_deja_utilise.config(text="Vous avez déjà utilisé les lettres : "+cdc)

    def change_label_erreur():
        global erreur
        label_erreur.config(text="Vous avez fait "+str(erreur)+" erreur(s)")
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



    def lettre_dans_le_mot_ou_erreur(lettre):
        global mot
        global mot_pointille
        global erreur
        global liste_ligne
        global canvas_personnage
        global reussite
        global lettre_deja_donne
        global nb_lettre

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
                print("Faux")
                erreur +=1
                creer_lignes(liste_ligne, erreur, canvas_personnage)
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
    label_pointille.grid(row = 11, column=0)
    label_lettre_deja_utilise.grid(row = 11, column=1, columnspan=3)

    fenetre.mainloop()
    #
    # -----------------------------------------------------
