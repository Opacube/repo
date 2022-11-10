#DEBUT
#On admet une fonction random qui retourne un chiffre entre 0 et 2 inclus
#On admet une fonction input qui récupère le choix du joueur
#Creer une variable keepPlaying sur Vrai qui permettra de savoir si le joueur veut continuer de jouer
#Creer une variable round pour savoir combien de rounds ont été joués et la définir sur 0
#Creer une variable winJoueur pour savoir combien de parties le joueur a gagné et la définir sur 0
#Creer une variable defaiteJoueur pour savoir combien de parties le joueur a perdu et la définir sur 0

#Creer une fonction pierre feuille ciseaux qui permettra de jouer au jeu

    #Afficher les règles du jeu dont les 3 choix à faire et quel choix l'emporte sur lequel
    #Tant que keepPlaying est sur Vrai
        #Laisser le joueur rentrer son choix grâce à la fonction input et l'implémenter dans la variable choix
            #Si la variable choix comprant le string "pierre"
                #Alors Implémenter 0 dans choixJoueur1
            #Sinon si la variable choix comprant le string "feuille"
                #Alors Implémenter 1 dans choixJoueur1
            #Sinon si la variable choix comprant le string "ciseaux"
                #Alors implémenter 2 dans choixJoueur1
            #Sinon
                #Alors afficher un message indiquant l'utilisateur que la réponse est erronée

        #Executer la fonction random et l'implémenter à la variable choixPC

        #Si la variable choixJoueur1 est de valeur 0
            #Si la variable choixPC est de valeur 0
                #Il y a égalité, on affiche le message d'égalité
            #Si la variable choixPC est de valeur 1
                #L'ordinateur gagne, on affiche le message de défaite et on incrémente 1 à la variable defaiteJoueur
            #Si la variable choixPC est de valeur 1
                #L'ordinateur perd, on affiche le message de victoire et on incrémente 1 à la variable winJoueur 
        
        #Si la variable choixJoueur1 est de valeur 1
            #Si la variable choixPC est de valeur 1
                #Il y a égalité, on affiche le message d'égalité
            #Si la variable choixPC est de valeur 2
                #L'ordinateur gagne, on affiche le message de défaite et on incrémente 1 à la variable defaiteJoueur
            #Si la variable choixPC est de valeur 0
                #L'ordinateur perd, on affiche le message de victoire et on incrémente 1 à la variable winJoueur 

        #Si la variable choixJoueur1 est de valeur 2
            #Si la variable choixPC est de valeur 2
                #Il y a égalité, on affiche le message d'égalité
            #Si la variable choixPC est de valeur 0
                #L'ordinateur gagne, on affiche le message de défaite et on incrémente 1 à la variable defaiteJoueur
            #Si la variable choixPC est de valeur 1
                #L'ordinateur perd, on affiche le message de victoire et on incrémente 1 à la variable winJoueur 

        #Afficher le choix original de l'ordinateur pour informer le joueur
        #Incrémenter 1 à la variable round
    #Demander au joueur si il veut continuer et récupérer son choix avec un input dans keepPlaying
        #Si son choix est oui
            #Alors rappeler la fonction pierre feuille ciseaux
        #Sinon
            #Alors afficher un message d'au revoir avec le résultat final comprenant le nombre de parties gagnées, perdues et de rounds joués
#Fin de la fonction

#Executer la fonction
#FIN



#FIBONACCI
def Fibonacci():
    n1 = 0
    nterms = int(input("Entrez le nombre de termes que vous voulez afficher: "))
    print("OK.")
    n2 = int(input("Entrez la valeur par laquelle vous souhaitez commencer: "))
    print("La suite fibonacci en commençant par " + str(2) + " est :")
    print(n1, ",", n2, end= ", ")

    for i in range(2, nterms):
        exitnum = n1 + n2
    print(exitnum, end= ", ")

    n1 = n2
    n2 = exitnum


import random


#JEU DE LA VIE
def jeuDeLaVie():
    jdlv_list = [random.randint(0,1) for i in range()]

#CREER UNE LISTE AVEC ALEATOIREMENT DES 0 ET 1
#AFFICHER CETTE LISTE X FOIS
#SI IL Y A PLUS DE 2 CELLULES ADJASCENTES
    #LA CELLULE MEURT
#SINON
    #ELLE SE REPRODUIT



#EXERCICE 1
tablo = [0,10, 15, 5, 72, 87, 2, 3, 5, 6, 1, 9, 0] #Creer le premier tableau
tablo2 = [10,210, 315, 45, 572, 687, 72, 83, 95, 106, 111, 129, 130] #Creer le deuxième tableau

stringtablo = str(tablo) #transformer le premier tableau en string
stringtablo2 = str(tablo2) #transformer le deuxieme tableau en string
tablo3 = stringtablo + ', ' + stringtablo2 #combiner les deux tableau avec une virgule entre les deux
print (tablo3) #afficher les deux tableaux ensembles

#EXERCICE 2
#faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere
#avec l'ensembles des occuration d'un chiffre e.g
#la fonction (tableau, 0) doit renvoyer "0, 4, 7" n'hésitez pas à implémenter la premiere fonction
tableau = [0,1,1,1,0,1,1,0,1] #Creation du tableau
def occuration (tableau, occurence): #creation de la fonction occuration
    index = "" #creation de la variable index
    for i in range(len(tableau)): #pour chaque index du tableau
        if tableau[i] == occurence: #si la valeur de l'index du tableau est égal à l'occurence
            index = index + str(i) + ", " #créer le numéro de l'index sur lequelle l'ocurrence à lieu
    return index #fermer la fonction et renvoyer la valeur
print(occuration(tableau, 0)) #afficher la fonction

def occuratione (tableau, x):#Definir une fonction qui prend une liste tableau et une variable x quelconque
    i = 0 #Initialiser i a 0
    chaineResultat = "" #Definir chaineResultat en tant que string vide
    firstTurn = True
    while i < len(tableau) : #Tant que i est inferieur a la longueur de tableau
        if tableau[i] == x:
            if firstTurn:
                chaineResultat = str(i) + ", "
                firstTurn = False
            else :
                chaineResultat = chaineResultat + str(i) + ", " #Alors on assigne a chaineResultat le retour de concatWithComma(chaineResultat, str(i))
        i = i + 1 #On incremente i de 1
    return chaineResultat
print(occuratione(tableau, 0))

#EXERCICE 3
#Faire une fonction afficher un message
def msg(mess): #Creer la fonction msg
    print(mess) #afficher le message désiré
    return #fermer la fonction
msg("Salutations") #appeler la fonction msg avec le message choisit

#EXERCICE 4
#Ecrivez la fonction login (username, password, listUser) qui affiche un message de connexion si le combo mdp/user est bon.

tableauCleVal = {"Cle" : "Valeur"}
tableauCleVal["Cle"] #Renvoie "valeur"

#tel que
listUser = {
    "Alexandre" : "motdepasse",
    "Michel" : "password",
    "Toto" : "12345",
    "JhonDoe" : "azerty"
}

def login(username, password, listUser): #creation de la fonction login
    if listUser[username] == password: #si la clé est égale à la valeur
        print ("Vous vous êtes connecté avec succès !") #affichage d'un message disant que la connexion est autorisée
    else: #sinon
        print("Le mot de passe ou l'utilisateur est incorrect") #affichage d'un message disant que la connexion a échouée
    return #fermer la fonction
