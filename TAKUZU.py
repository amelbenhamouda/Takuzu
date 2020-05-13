"""  Auteurs: BEN HAMOUDA Amel et PERRAY Sophie
     Groupe de TD: d
     Groupes de TP: 4 et 5
     Date de création: 2015/2016
     Description: Jeu TAKUZU
"""
from upemtk import *
import time

#################
### FONCTIONS ###
#################

def cree_case_graphique(nb): 
	"""Crée une grille en fonction du nombre de case que posséde le 
	   tazuzu par ligne(nb).
	"""
	i=0
	while i<400:
		cmpt=0
		while cmpt<400:
			rectangle(cmpt, i, cmpt+400/nb, i+400/nb)
			cmpt=cmpt+400/nb
		i=i+400/nb

def charger_grille_graphique(grille): 
	"""Charge dans une liste de liste les chiffres qui apparaitront dans 
	   la grille du takuzu à  réssoudre à  partir d'un fichier mis en 
	   argument(grille).
	"""
	fichier=open(grille, "r")
	grille_fichier=fichier.readlines()
	fichier.close()
	takuzu_debut=[]
	# Fait de chaque chaine de caractére, qui correspond à une ligne 
	# dans le texte téléchargé, un liste et enléve le /n qui se trouve à la fin.
	for ligne in grille_fichier: 
		ligne=list(ligne)
		ligne.pop()
		takuzu_debut.append(ligne)
	# Transforme tous les 0 et les 1 qui se trouve en str en int.
	for lst in takuzu_debut: 
		for i in range(len(lst)):
			if lst[i]=="0":
				lst[i]=0
			if lst[i]=="1":
				lst[i]=1
	return takuzu_debut

def placer_pieces_graphique(nb, lst_lignes, symbole):
	"""Place les chiffres qui se trouvent dans la liste de liste(lst_lignes) 
	   dans la grille de takuzu en fonction du nombre de case que posséde 
	   la gille par ligne(nb) et du symbole choisi pour ésoudre le takuzu(symbole).
	"""
	efface("chiffres")
	# Affiche les 0 et les 1.
	if symbole==1: 
		for y in range(len(lst_lignes)):
			for x in range(len(lst_lignes[y])):
				# Les chiffres que l'utilisateur ne peut pas changer sont affichés en noir.
				if lst_lignes[y][x]==0:
					texte((400/(2*nb))+x*(400/nb), (400/(2*nb))+y*(400/nb), "0", ancrage="center", tag="chiffres") 
				elif lst_lignes[y][x]==1:
					texte((400/(2*nb))+x*(400/nb), (400/(2*nb))+y*(400/nb), "1", ancrage="center", tag="chiffres")
				# Les chiffres que l'utilisateur doit afficher lui même sont affichés en bleu.
				elif lst_lignes[y][x]=="0":
					texte((400/(2*nb))+x*(400/nb), (400/(2*nb))+y*(400/nb), "0", ancrage="center", couleur="blue", tag="chiffres") 
				elif lst_lignes[y][x]=="1":
					texte((400/(2*nb))+x*(400/nb), (400/(2*nb))+y*(400/nb), "1", ancrage="center", couleur="blue", tag="chiffres")
	# Affiche les jetons noirs et blancs.
	elif symbole==2: 
		for y in range(len(lst_lignes)):
			for x in range(len(lst_lignes[y])):
				if lst_lignes[y][x]==0 or lst_lignes[y][x]=="0":
					cercle((400/(2*nb))+x*(400/nb), (400/(2*nb))+y*(400/nb), 400//(4*nb), remplissage="white", tag="chiffres")
				elif lst_lignes[y][x]==1 or lst_lignes[y][x]=="1":
					cercle((400/(2*nb))+x*(400/nb), (400/(2*nb))+y*(400/nb), 400//(4*nb), remplissage="black", tag="chiffres")
	# Affiche les croix et les ronds.
	elif symbole==3: 
		for y in range(len(lst_lignes)):
			for x in range(len(lst_lignes[y])):
				# Les chiffres que l'utilisateur ne peut pas changer sont affichés en noir.
				if lst_lignes[y][x]==0:
					texte((400/(2*nb))+x*(400/nb), (400/(2*nb))+y*(400/nb), "O", ancrage="center", tag="chiffres") 
				elif lst_lignes[y][x]==1:
					texte((400/(2*nb))+x*(400/nb), (400/(2*nb))+y*(400/nb), "X", ancrage="center", tag="chiffres")
				# Les chiffres que l'utilisateur doit afficher lui même sont affichés en bleu.
				elif lst_lignes[y][x]=="0":
					texte((400/(2*nb))+x*(400/nb), (400/(2*nb))+y*(400/nb), "O", ancrage="center", couleur="blue", tag="chiffres") 
				elif lst_lignes[y][x]=="1":
					texte((400/(2*nb))+x*(400/nb), (400/(2*nb))+y*(400/nb), "X", ancrage="center", couleur="blue", tag="chiffres")
	mise_a_jour()

def changement_variable_graphique(x, y, nb, lst_lignes):
	"""Prend les coordonnées de l'endroit où l'utilisateur à cliquée en paramétre 
	   ainsi que le nombre de case par ligne et la liste de liste qui affiche les 
	   chiffres dans le takuzu.
	"""
	ligne=y//(400//nb)
	colonne=x//(400//nb)
	# Change la case sur laquelle l'utilisateur à cliqué en fonction de la valeur 
	# qui y était avait et fait en sorte que les chiffres qui était au début dans 
	# le takuzu ne puisse pas être touché.
	if type(lst_lignes[ligne][colonne])==str: 
		if lst_lignes[ligne][colonne]==" ":
			lst_lignes[ligne][colonne]="0"
		elif lst_lignes[ligne][colonne]=="0":
			lst_lignes[ligne][colonne]="1"
		elif lst_lignes[ligne][colonne]=="1":
			lst_lignes[ligne][colonne]=" "

def conditions_graphique(lst_lignes, lst_colonnes): 
	"""Vérifie toute les conditions du jeux.
	"""
	# Vérifie qu'il y a autant de 1 et de 0 dans chaque ligne et chaque colonne et 
	# qu'il n'y a aucune case vide.
	lstligne=1*lst_lignes
	for ligne in lst_lignes:
		liste=[""]
		nb1=0
		nb0=0
		for colonne in ligne :
			if colonne==" ":
				return False
			liste.append(colonne)
			if str(colonne)=="1":
				nb1=nb1+1
			if str(colonne)=="0":
				nb0=nb0+1
		if nb0!=nb1:
			return False
	# Vérifie qu'il n'y est pas trois zero ou trois un les uns à côté des autres 
	# dans une ligne.
	i=0
	while i<len(lst_lignes): 
		cmpt=0
		while cmpt<(len(lst_lignes[i])-2):
			if lst_lignes[i][cmpt]==lst_lignes[i][cmpt+1]==lst_lignes[i][cmpt+2]:
				return False
			cmpt=cmpt+1
		i=i+1
	# Vérifie qu'il n'y est pas trois zero ou trois un les uns à côté des autres 
	# dans une colonne.
	i=0
	while i<len(lst_colonnes): 
		cmpt=0
		while cmpt<(len(lst_colonnes[i])-2):
			if lst_colonnes[i][cmpt]==lst_colonnes[i][cmpt+1]==lst_colonnes[i][cmpt+2]:
				return False
			cmpt=cmpt+1
		i=i+1
	# Vérifie qu'aucune ligne n'est identique à une autre.
	i=0
	while i<(len(lst_lignes)-1): 
		if lst_lignes[i]==lst_lignes[i+1]:
			return False
		i=i+1
	# Vérifie qu'aucune colonne n'est identique à une autre.
	i=0
	while i<(len(lst_colonnes)-1): 
		if lst_colonnes[i] == lst_colonnes[i+1]:
			return False
		i=i+1
	return True

def cree_colonnes(lst_lignes): 
	""" Crée une liste de colonne à  partir d'une liste de ligne.
	"""
	fin=[]
	i=0
	while i<len(lst_lignes[0]):
		n=[lst_lignes[0][i]]
		cmpt=1
		while cmpt<len(lst_lignes):
			n.append(lst_lignes[cmpt][i])
			cmpt=cmpt+1
		fin.append(n)
		i=i+1
	return fin

def conditions_terminal(nb,liste_lignes,liste_colonnes):
	"""Vérifie que toute les conditions du jeux sont bonnes.
	"""
	# LIGNE
	# Vérifie qu'il y est autant de un que de zéro sur une même ligne.
	for compt in range (0,nb): 
		occurence0 = liste_lignes[compt].count("0")
		# Vérifie le nombre de zero.
		if occurence0 != nb / 2 : 
			return False
		occurence1 = liste_lignes[compt].count("1")
		# Vérifie le nombre de un.
		if occurence1 != nb / 2 : 
			return False
	# Vérifie qu'il n'y est pas trois un ou trois zéro les un à côté des autres.
	for i in range(0,len(liste_lignes)): 
		for c in range(1,len(liste_lignes[i])//2,2):
			if liste_lignes[i][c]==liste_lignes[i][c+2]==liste_lignes[i][c+4]:
				return False
	# Vérifie qu'aucune ligne n'est identique à  une autre.
	c=0
	while c < (len(liste_lignes)-1):  
		occurence=liste_lignes.count(liste_lignes[c])
		if occurence != 1 :
			return False
		c=c+1
	# COLONNE
	# Vérifie qu'il y est autant de un que de zéro sur une même colonne.
	for compt in range (1,nb,2): 
		occurence0 = liste_colonnes[compt].count("0")
		# Vérifie le nombre de zero.
		if occurence0 != nb / 2 : 
			return False
		occurence1 = liste_colonnes[compt].count("1")
		# Vérifie le nombre de un.
		if occurence1 != nb / 2 : 
			return False
	# Vérifie qu'il n'y est pas trois un ou trois zéro les un à côté des autres.
	for i in range(1,len(liste_colonnes),2): 
		for c in range(0,len(liste_colonnes[i])//2):
			if liste_colonnes[i][c]==liste_colonnes[i][c+1]==liste_colonnes[i][c+2]:
				return False
	# Vérifie qu'aucune colonne n'est identique à  une autre.
	c=1
	while c < (len(liste_colonnes)-1):  
		occurence=liste_colonnes.count(liste_colonnes[c])
		if occurence != 1 :
			return False
		c=c+2
	return True

def  charger_grille_terminal(grille):
	"""Permet d'afficher ce qui se trouve dans le fichier texte, dans une liste.
	"""
	fichier=open(grille, "r")
	grille=fichier.readlines()
	fichier.close()
	return grille

def grille_terminal(nb): 
	"""Permet d'afficher la grille sur le terminal grâce à une liste de liste.
	"""
	# Avant d'afficher la grille on insert d'abord des lignes (|) dans la liste de liste, 
	# pour permettre de bien visualiser la grille.
	if nb == 4 :
		emplacement= charger_grille_terminal("grille4.txt")
		i=0
		while i<nb:
			emplacement[i]="|"+str(emplacement[i][0])+"|"+str(emplacement[i][1])+"|"+str(emplacement[i][2])+"|"+str(emplacement[i][3])+"|"
			i=i+1
	elif nb == 6 :
		emplacement= charger_grille_terminal("grille6.txt")
		i=0
		while i<nb:
			emplacement[i]="|"+str(emplacement[i][0])+"|"+str(emplacement[i][1])+"|"+str(emplacement[i][2])+"|"+str(emplacement[i][3])+"|"+str(emplacement[i][4])+"|"+str(emplacement[i][5])+"|"
			i=i+1
	elif nb == 8 :
		emplacement= charger_grille_terminal("grille8.txt")
		i=0
		while i<nb:
			emplacement[i]="|"+str(emplacement[i][0])+"|"+str(emplacement[i][1])+"|"+str(emplacement[i][2])+"|"+str(emplacement[i][3])+"|"+str(emplacement[i][4])+"|"+str(emplacement[i][5])+"|"+str(emplacement[i][6])+"|"+str(emplacement[i][7])+"|"
			i=i+1
	elif nb == 10 :
		emplacement= charger_grille_terminal("grille10.txt")
		i=0
		while i<nb:
			emplacement[i]="|"+str(emplacement[i][0])+"|"+str(emplacement[i][1])+"|"+str(emplacement[i][2])+"|"+str(emplacement[i][3])+"|"+str(emplacement[i][4])+"|"+str(emplacement[i][5])+"|"+str(emplacement[i][6])+"|"+str(emplacement[i][7])+"|"+str(emplacement[i][8])+"|"+str(emplacement[i][9])+"|"
			i=i+1
	# Affiche la liste de liste en forme de tableau.
	cmpt=0
	while cmpt<len(emplacement):
		ligne=emplacement[cmpt]
		print(ligne)
		cmpt=cmpt+1
	return emplacement

def changement_variable_terminal(ligne,colonne,nb,liste_lignes): 
	"""Permet de modifier ce qui se trouve dans la liste de liste 
	   (sauf ce qui sont bloquée).
	"""
	for n in range(len(liste_lignes)) :
		# On met en type list pour permettre la modification.
		liste_lignes[n]=list(liste_lignes[n]) 
	ajout = input("Entrez une valeur 0 ou 1: ")
	# On bloque les coups illégaux, pour que l'utilisateur ne met pas autre chose que 0 ou 1.
	while ajout != "0" and  ajout != "1": 
		print("On ne peut mettre que des 0 ou des 1")
		ajout = input("Entrez une valeur 0 ou 1: ")
	# On ajoute la saisie dans la liste de liste.
	liste_lignes[int(ligne)][2*int(colonne)+1]=ajout 
	# On remet la liste de liste en liste de chaine de caractére pour que les conditions
	# puisse être vérifiées.
	for i in liste_lignes: 
		i="".join(i)
		print(i)

###########################
### PROGRAMME PRINCIPAL ###
###########################

# Demande à l'utilisateur le niveau voulu pour le jeu.
nb=int(input("Entrez le nombre de cases voulues sur une ligne(4, 6, 8, 10): ")) 
while not(nb==4 or nb==6 or nb==8 or nb==10):
    nb=int(input("Choisissez 4, 6, 8 ou 10: "))
choix=input("Vous souhaitez jouer au Takuzu en mode terminal(tapez T) ou en mode graphique(tapez G): ")
# On bloque les coups illégaux, pour que l'utilisateur ne puisse pas choisir autre chose que 
# le mode terminal ou le mode graphique.
while not(choix=="g" or choix=="G" or choix=="t" or choix=="T"): 
    choix=input("Tapez T pour le mode terminal ou G pour le mode graphique: ")

if choix=="g" or choix=="G":
    print("Voulez-vous résoudre le takuzu avec:")
    print("1:des 0 et des 1")
    print("2:des jetons noirs et blancs")
    print("3:des cercle et des croix")
    symbole=int(input("Entrez votre choix: "))
    while not(symbole==1 or symbole==2 or symbole==3):
        symbole=int(input("Choisissez 1, 2 ou 3: "))
    # Crée une fenêtre de 400 sur 400.
    cree_fenetre(400, 400) 
    # Crée les cases pour le takuzu dans la fenêtre en fonction du niveau choisi.
    cree_case_graphique(nb) 
    # Charge dans une liste de liste la grille correspondante au niveau choisi.
    if nb==4: 
        grille="grille4.txt"
    elif nb==6:
        grille="grille6.txt"
    elif nb==8:
        grille="grille8.txt"
    elif nb==10:
        grille="grille10.txt"
    lst_lignes=charger_grille_graphique(grille)
    # Affiche dans la fenêtre la liste de liste, ne comprenant que des int, 
    # correspondant au takuzu à résoudre.
    placer_pieces_graphique(nb, lst_lignes, symbole) 
    # Cré une liste correspondant aux colonnes.
    lst_colonnes=cree_colonnes(lst_lignes) 
    # Tant que les conditions ne sont pas correctes le programmes continu.
    while not(conditions_graphique(lst_lignes, lst_colonnes)): 
		# Donne les coordonnées de l'endroit où l'utilisateur à cliqué.
        (x, y, event)=attente_clic()
        # Change la case sur laquelle l'utilisateur à cliqué. 
        changement_variable_graphique(x, y, nb, lst_lignes) 
        # Place dans la grille les changements qui se sont produits.
        placer_pieces_graphique(nb, lst_lignes, symbole) 
        # Création d'une nouvelle liste de colonnes pour la vérification 
        # des conditions.
        lst_colonnes=cree_colonnes(lst_lignes) 
    time.sleep(0.5)
    efface_tout()
    # Affiche "Bravo" quand le takuzu est complé et bon.
    texte(200, 200, "Bravo!", ancrage="center") 
    attente_clic()
    ferme_fenetre() # Ferme la fenêtre.

elif choix == "t" or choix == "T":
    # Affiche la grille sans aucune modification.
    liste_lignes=grille_terminal(nb)
    print("Pour indiquer une case une case il suffit de donner un chiffre pour la ligne et la colonne en partent de 0")
    print("Par exemple, la case (1,2) correspond Ã Â  la deuxiÃ¨me case de la premiÃ¨re ligne")
    while True:
        # Demande l'indice de la ligne et de la colonne Ã Â  l'utilisateur.
        ligne=input("Entrer la ligne dans laquelle se trouve la case souhaitez (chiffre): ")
        colonne=input("Entrer la colonne dans laquelle se trouve la case souhaitez (chiffre): ")
        # Vérifie les coordonnées pour empêcher les coups illégaux.
        if nb == 4:
            while ((ligne=="0" and colonne=="1") or (ligne=="0" and colonne=="3") or (ligne=="1" and colonne=="2") or 
                   (ligne=="2" and colonne=="1") or (ligne=="3" and colonne=="0") or (ligne=="3" and colonne=="1") or 
                   (ligne=="3" and colonne=="3") or (ligne==" " or colonne==" ") or (ligne=="" or colonne=="") or 
                   (ligne>"3" or colonne>"3")):
               print("Cette case ne peut pas être modifier, ou bien elle est inéxistente")
               ligne=input("Entrer la ligne dans laquelle se trouve la case souhaitez (chiffre): ")
               colonne=input("Entrer la colonne dans laquelle se trouve la case souhaitez (chiffre): ")
        if nb == 6 :
            while  ((ligne=="0" and colonne=="0") or (ligne=="0" and colonne=="4") or (ligne=="1" and colonne=="0") or 
                    (ligne=="1" and colonne=="3") or (ligne=="2" and colonne=="3") or (ligne=="2" and colonne=="5") or 
                    (ligne=="3" and colonne=="0") or (ligne=="3" and colonne=="1") or (ligne=="3" and colonne=="2") or 
                    (ligne=="3" and colonne=="3") or (ligne=="4" and colonne=="2") or (ligne=="4" and colonne=="3") or
                    (ligne=="4" and colonne=="4") or (ligne=="4" and colonne=="5") or (ligne=="5" and colonne=="3") or 
                    (ligne=="5" and colonne=="5") or (ligne==" " or colonne==" ") or (ligne=="" or colonne=="") or 
                    (ligne>"5" or colonne>"5")):
                print("Cette case ne peut pas être modifier, ou bien elle est inéxistante")
                ligne=input("Entrer la ligne dans laquelle se trouve la case souhaitez (chiffre): ")
                colonne=input("Entrer la colonne dans laquelle se trouve la case souhaitez (chiffre): ")
        if nb == 8:
            while ((ligne=="0" and colonne=="1") or (ligne=="0" and colonne=="7") or (ligne=="1" and colonne=="6") or 
                   (ligne=="2" and colonne=="1") or (ligne=="2" and colonne=="3") or (ligne=="2" and colonne=="6") or 
                   (ligne=="3" and colonne=="1") or (ligne=="3" and colonne=="6") or (ligne=="4" and colonne=="1") or 
                   (ligne=="4" and colonne=="7") or (ligne=="5" and colonne=="0") or (ligne=="5" and colonne=="1") or 
                   (ligne=="5" and colonne=="2") or (ligne=="5" and colonne=="3") or (ligne=="5" and colonne=="4") or 
                   (ligne=="5" and colonne=="5") or (ligne=="5" and colonne=="6") or (ligne=="6" and colonne=="4") or 
                   (ligne=="7" and colonne=="4") or (ligne=="7" and colonne=="6") or (ligne=="7" and colonne=="7") or 
                   (ligne=="" or colonne=="") or (ligne==" " or colonne==" ") or(ligne>"7" or colonne>"7")):
                print("Cette case ne peut pas être modifier, ou bien elle est inéxistante")
                ligne=input("Entrer la ligne dans laquelle se trouve la case souhaitez (chiffre): ")
                colonne=input("Entrer la colonne dans laquelle se trouve la case souhaitez (chiffre): ")
        if nb == 10:
            while ((i=="0" and j=="2") or (i=="0" and j=="7") or (i=="0" and j=="8") or (i=="1" and j=="0") or 
                   (i=="1" and j=="2") or (i=="1" and j=="4") or (i=="1" and j=="6") or (i=="1" and j=="7") or 
                   (i=="2" and j=="0") or (i=="2" and j=="8") or (i=="3" and j=="0") or (i=="3" and j=="3") or
                   (i=="3" and j=="5") or (i=="3" and j=="8") or (i=="4" and j=="3") or (i=="4" and j=="9") or 
                   (i=="5" and j=="0") or (i=="5" and j=="1") or (i=="5" and j=="4") or (i=="6" and j=="2") or 
                   (i=="6" and j=="4") or (i=="6" and j=="5") or (i=="6" and j=="7") or (i=="6" and j=="9") or
                   (i=="7" and j=="0") or (i=="7" and j=="7") or (i=="7" and j=="9") or (i=="9" and j=="0") or 
                   (i=="9" and j=="1") or (i=="9" and j=="5") or (i==" " or j==" ") or (i=="" or j=="") or 
                   (i>"9" or j>"9")):
                print("Cette case ne peut pas être modifier, ou bien elle est inéxistante")
                i=input("Entrer la ligne dans laquelle se trouve la case souhaitez (chiffre): ")
                j=input("Entrer la colonne dans laquelle se trouve la case souhaitez (chiffre): ")
        print("La case choisie est :",(ligne,colonne))
        print(" ")
        liste_colonnes=cree_colonnes(liste_lignes)
        # Affichage de la grille.
        changement_variable_terminal(ligne,colonne,nb,liste_lignes)
        verification=conditions_terminal(nb,liste_lignes,liste_colonnes)
        # Permet d'arrêter le programme si les conditions sont bonnes et
        # bien sûr si la grille est finie.
        if verification==True :
           print("Gagner!!!")
           break
