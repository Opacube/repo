#DEBUT
#On admet une fonction random qui retourne un chiffre entre 0 et 2 inclus
import random
#On admet une fonction input qui récupère le choix du joueur
def pfc():
    keepPlaying = True
    #Creer une fonction pierre feuille ciseaux qui permettra de jouer au jeu    #Creer une variable round pour savoir combien de rounds ont été joués et la définir sur 0
    round = 0
    #Creer une variable winJoueur pour savoir combien de parties le joueur a gagné et la définir sur 0
    winJoueur = 0
    #Creer une variable defaiteJoueur pour savoir combien de parties le joueur a perdu et la définir sur 0
    defaiteJoueur = 0
    choixPCstr = ""
    #Afficher les règles du jeu dont les 3 choix à faire et quel choix l'emporte sur lequel
    print("Le jeu Pierre Feuille Ciseaux consiste en deux joueurs qui s'affrontent avec 3 choix chacun. \n")
    print("La pierre bat les ciseaux, les ciseaux battent la feuille et la feuille bat la pierre. \n")
    print("Si les deux joueurs font le même choix, c'est match nul ! \n")
    print("Vous jouerez contre l'ordinateur ! Bonne chance !")
    #Tant que keepPlaying est sur Vrai
    while keepPlaying == True :
        #Laisser le joueur rentrer son choix grâce à la fonction input et l'implémenter dans la variable choix
        choix = input("Votre choix : ")
        while choix != "feuille" and choix != "pierre" and choix != "ciseaux" :
            choix = input("Votre réponse est erronée, veuillez réessayer : ")
            #Si la variable choix comprant le string "pierre"
        if choix == "pierre" :
            #Alors mplémenter 0 dans choixJoueur1
            choixJoueur1 = 0
        #Sinon si la variable choix comprant le string "feuille"
        elif choix == "feuille" :
            #Alors Implémenter 1 dans choixJoueur1
            choixJoueur1 = 1
        #Sinon si la variable choix comprant le string "ciseaux"
        elif choix == "ciseaux" :
            #Alors implémenter 2 dans choixJoueur1
            choixJoueur1 = 2

        #Executer la fonction random et l'implémenter à la variable choixPC
        choixPC = random.randint(0,2)

        #Si la variable choixJoueur1 est de valeur 0
        if choixJoueur1 == 0 :
            #Si la variable choixPC est de valeur 0
            if choixPC == 0 :
                #Il y a égalité, on affiche le message d'égalité
                print("Egalité !")
            #Si la variable choixPC est de valeur 1
            if choixPC == 1 :
                #L'ordinateur gagne, on affiche le message de défaite et on incrémente 1 à la variable defaiteJoueur
                print("Vous avez perdu la manche !")
                defaiteJoueur = defaiteJoueur + 1
            #Si la variable choixPC est de valeur 2
            if choixPC == 2 :
                #L'ordinateur perd, on affiche le message de victoire et on incrémente 1 à la variable winJoueur 
                print("Vous avez gagné la manche !")
                winJoueur = winJoueur + 1
        
        #Si la variable choixJoueur1 est de valeur 1
        if choixJoueur1 == 1 :
            #Si la variable choixPC est de valeur 1
            if choixPC == 1 :
                #Il y a égalité, on affiche le message d'égalité
                print("Egalité !")
            #Si la variable choixPC est de valeur 2
            elif choixPC == 2 :
                #L'ordinateur gagne, on affiche le message de défaite et on incrémente 1 à la variable defaiteJoueur
                print("Vous avez perdu la manche !")
                defaiteJoueur = defaiteJoueur + 1
            #Si la variable choixPC est de valeur 0
            elif choixPC == 0 :
                #L'ordinateur perd, on affiche le message de victoire et on incrémente 1 à la variable winJoueur 
                print("Vous avez gagné la manche !")
                winJoueur = winJoueur + 1

        #Si la variable choixJoueur1 est de valeur 2
        if choixJoueur1 == 2 :
            #Si la variable choixPC est de valeur 2
            if choixPC == 2 :
                #Il y a égalité, on affiche le message d'égalité
                print("Egalité !")
            #Si la variable choixPC est de valeur 0
            elif choixPC == 0 :
                #L'ordinateur gagne, on affiche le message de défaite et on incrémente 1 à la variable defaiteJoueur
                print("Vous avez perdu la manche !")
                defaiteJoueur = defaiteJoueur + 1
            #Si la variable choixPC est de valeur 1
            elif choixPC == 1 :
                #L'ordinateur perd, on affiche le message de victoire et on incrémente 1 à la variable winJoueur
                print("Vous avez gagné la manche !")
                winJoueur = winJoueur + 1
            
            if choixPC == 0 :
                choixPCstr = "Pierre"
            elif choixPC == 1 :
                choixPCstr = "Feuille"
            elif choixPC == 2 :
                choixPCstr = "Ciseaux"


        #Afficher le choix original de l'ordinateur pour informer le joueur
        if choixPC == 0 :
            choixPCstr = "Pierre"
        elif choixPC == 1 :
            choixPCstr = "Feuille"
        elif choixPC == 2 :
            choixPCstr = "Ciseaux"
        print("Le choix adverse était :", choixPCstr)
        #Incrémenter 1 à la variable round
        round = round + 1
        #Demander au joueur si il veut continuer et récupérer son choix avec un input dans keepPlaying
        choixJoueur = input("Voulez-vous continuer ? \n")
        #Si son choix est non
        if choixJoueur == "oui" :
            #Alors rajouer la boucle
            keepPlaying = True
        else :
            #Alors afficher un message d'au revoir avec le résultat final comprenant le nombre de parties gagnées, perdues et de rounds joués
            keepPlaying = False
            print("Voici vos résultats finaux : ")
            print("Manches jouées : ", round)
            print("Victoires : ", winJoueur)
            print("Défaites : ", defaiteJoueur)
#Fin de la fonction
pfc()
#Executer la fonction
#FIN


        while choix != 1 and choix != 2 and choix != 3 and choix != 4 and choix != 5 and choix != 6 and choix != 7 and choix != 8 and choix != 9 :