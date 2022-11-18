#DEBUT
#On admet une fonction random qui retourne un chiffre entre 0 et 2 inclus
#On admet une fonction input qui récupère le choix du joueur
    #Creer une fonction pierre feuille ciseaux qui permettra de jouer au jeu    #Creer une variable round pour savoir combien de rounds ont été joués et la définir sur 0
    #Creer une variable winJoueur pour savoir combien de parties le joueur a gagné et la définir sur 0
    #Creer une variable defaiteJoueur pour savoir combien de parties le joueur a perdu et la définir sur 0
    #Afficher les règles du jeu dont les 3 choix à faire et quel choix l'emporte sur lequel
    #Tant que keepPlaying est sur Vrai
        #Laisser le joueur rentrer son choix grâce à la fonction input et l'implémenter dans la variable choix
            #Si la variable choix comprant le string "pierre"
            #Alors mplémenter 0 dans choixJoueur1
        #Sinon si la variable choix comprant le string "feuille"
            #Alors Implémenter 1 dans choixJoueur1
        #Sinon si la variable choix comprant le string "ciseaux"
            #Alors implémenter 2 dans choixJoueur1

        #Executer la fonction random et l'implémenter à la variable choixPC

        #Si la variable choixJoueur1 est de valeur 0
            #Si la variable choixPC est de valeur 0
                #Il y a égalité, on affiche le message d'égalité
            #Si la variable choixPC est de valeur 1
                #L'ordinateur gagne, on affiche le message de défaite et on incrémente 1 à la variable defaiteJoueur
            #Si la variable choixPC est de valeur 2
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
        #Si son choix est non
            #Alors rajouer la boucle
            #Alors afficher un message d'au revoir avec le résultat final comprenant le nombre de parties gagnées, perdues et de rounds joués
#Fin de la fonction
#Executer la fonction
#FIN