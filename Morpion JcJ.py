#DEBUT
#On crée le tableau qui contiendra les valeurs du morpion
x = [["▢", "▢", "▢"], ["▢", "▢", "▢"], ["▢", "▢", "▢"]]
#On affiche le tableau avec les numéros correspondants à chaques cases
print("\033[1;33;40m\nVoici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
print(x[0][0], " ", x[0][1], " ", x[0][2], "   1   2   3")
print(x[1][0], " ", x[1][1], " ", x[1][2], "   4   5   6")
print(x[2][0], " ", x[2][1], " ", x[2][2], "   7   8   9")

#On crée la fonction morpion qui prendra en compte le tour du joueur et de la machine, ainsi que l'affichage de fin de partie et demander si le joueur veut rejouer
def morpion(turn, nbtour): 
    #Si c'est le tour du joueur 1
    if turn == "J1" :
        #Demander la case que le joueur veut changer et prendre sa valeur dans la variable "choix"
        choix = input("J1 : Insérer la case que vous voulez changer : ")
        #Conditions pour faire correspondre l'entrée du joueur avec la case correspondante, uniquement si elle est vide
        #Ligne 1
        if choix == "1" and x[0][0] == "▢":
            x[0][0] = "⊛"
        elif choix == "2" and x[0][1] == "▢":
            x[0][1] = "⊛"
        elif choix == "3" and x[0][2] == "▢":
            x[0][2] = "⊛"

        #Ligne 2
        elif choix == "4" and x[1][0] == "▢":
            x[1][0] = "⊛"
        elif choix == "5" and x[1][1] == "▢":
            x[1][1] = "⊛"
        elif choix == "6" and x[1][2] == "▢":
            x[1][2] = "⊛"

        #Ligne 3
        elif choix == "7" and x[2][0] == "▢":
            x[2][0] = "⊛"
        elif choix == "8" and x[2][1] == "▢":
            x[2][1] = "⊛"
        elif choix == "9" and x[2][2] == "▢":
            x[2][2] = "⊛"

        #Sinon afficher le message d'erreur et renvoyer le joueur au choix de la case
        else :
            print("Erreur : La case sélectionnée est soit déjà pleine soit inexistante !")
            morpion(turn, nbtour)

        #Afficher le tableau après que le joueur ait joué
        print("\033[1;33;40m\nVoici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
        print(x[0][0], " ", x[0][1], " ", x[0][2], "   1   2   3")
        print(x[1][0], " ", x[1][1], " ", x[1][2], "   4   5   6")
        print(x[2][0], " ", x[2][1], " ", x[2][2], "   7   8   9")
        #Incrémenter 1 au nombre de tours
        nbtour = nbtour+1
        #Appeler la fonction "checkIfWin" pour le joueur 1 qui vérifiera si ce joueur a gagné la partie ou non
        checkIfWin("J1", nbtour)

    #Quand c'est le tour du Joueur 2
    elif turn == "J2" :
        #Demander la case que le joueur veut changer et prendre sa valeur dans la variable "choix"
        choix = input("J2 : Insérer la case que vous voulez changer : ")
        #Conditions pour faire correspondre l'entrée du joueur avec la case correspondante, uniquement si elle est vide
        #Ligne 1
        if choix == "1" and x[0][0] == "▢":
            x[0][0] = "✕"
        elif choix == "2" and x[0][1] == "▢":
            x[0][1] = "✕"
        elif choix == "3" and x[0][2] == "▢":
            x[0][2] = "✕"

        #Ligne 2
        elif choix == "4" and x[1][0] == "▢":
            x[1][0] = "✕"
        elif choix == "5" and x[1][1] == "▢":
            x[1][1] = "✕"
        elif choix == "6" and x[1][2] == "▢":
            x[1][2] = "✕"

        #Ligne 3
        elif choix == "7" and x[2][0] == "▢":
            x[2][0] = "✕"
        elif choix == "8" and x[2][1] == "▢":
            x[2][1] = "✕"
        elif choix == "9" and x[2][2] == "▢":
            x[2][2] = "✕"

        #Sinon afficher le message d'erreur et renvoyer le joueur au choix de la case
        else :
            print("Erreur : La case sélectionnée est soit déjà pleine soit inexistante !")
            morpion(turn, nbtour)

        #Afficher le tableau après que le joueur ait joué
        print("\033[1;33;40m\nVoici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
        print(x[0][0], " ", x[0][1], " ", x[0][2], "   1   2   3")
        print(x[1][0], " ", x[1][1], " ", x[1][2], "   4   5   6")
        print(x[2][0], " ", x[2][1], " ", x[2][2], "   7   8   9")
        #Incrémenter 1 au nombre de tours
        nbtour = nbtour+1
        #Appeler la fonction "checkIfWin" pour le joueur 1 qui vérifiera si ce joueur a gagné la partie ou non
        checkIfWin("J2", nbtour)

    #Si ce n'est pas le tour d'un joueur et donc que quelqu'un a gagné la partie ou qu'il y a égalité
    elif turn == "no" :
        #Alors demander au joueur si il veut recommencer et implémenter son choix dans la variable "re"
        re = input("Voulez-vous recommencer ? ")
        #Tant que le choix du joueur "re" est différent de "oui"
        while re != "oui":
            #Si la réponse du joueur est "non"
            if re == "non" :
                #Alors afficher un message d'au revoir et terminer le code (return ne fonctionne pas pour dieu ne sait quelle raison)
                print("Au revoir !")
                exit()
            #Si le choix du joueur est "oui"
            elif re == "oui" :
                #Afficher un message de bonne chance
                print("Bonne chance !")
                #Réinitialiser le tableau du morpion
                x[0][0] = "▢"
                x[0][1] = "▢"
                x[0][2] = "▢"
                x[1][0] = "▢"
                x[1][1] = "▢"
                x[1][2] = "▢"
                x[2][0] = "▢"
                x[2][1] = "▢"
                x[2][2] = "▢"
                #Afficher le tableau vide avec toute les coordonées correspondantes aux cases
                print("\033[1;33;40m\nVoici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
                print(x[0][0], " ", x[0][1], " ", x[0][2], "   1   2   3")
                print(x[1][0], " ", x[1][1], " ", x[1][2], "   4   5   6")
                print(x[2][0], " ", x[2][1], " ", x[2][2], "   7   8   9")
                #Réinitialiser le nombre de tours
                nbtour = 0
                #Appeler la fonction "morpion" avec comme paramètre le joueur dont c'est le tour
                morpion("J1", nbtour)
            #Sinon
            else :
                #Alors afficher un message d'erreur et redemander le choix du joueur
                re = input("Réponse incorrecte. Voulez-vous recommencer ? ")

#Créer une fonction "checkIfWin" qui vérifier si un joueur a gagné ou pas à chaque tour
def checkIfWin(turn, nbtour):
    #Si c'est le tour du joueur 1
    if turn == "J1" :
        #Si une des trois lignes comprant 3 cercles
        #Alors le joueur 1 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        if x[0][0] == "⊛"  and x[0][1] == "⊛"  and x[0][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[1][0] == "⊛"  and x[1][1] == "⊛"  and x[1][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[2][0] == "⊛"  and x[2][1] == "⊛"  and x[2][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        #Si une des trois colonnes comprant 3 cercles
        #Alors le joueur 1 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        elif x[0][0] == "⊛"  and x[1][0] == "⊛"  and x[2][0] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[0][1] == "⊛"  and x[1][1] == "⊛"  and x[2][1] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[0][2] == "⊛"  and x[1][2] == "⊛"  and x[2][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        #Si une des deux diagonales comprant 3 cercles
        #Alors le joueur 1 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        elif x[0][0] == "⊛"  and x[1][1] == "⊛"  and x[2][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[0][2] == "⊛"  and x[1][1] == "⊛"  and x[2][0] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        #Si le tour est le neuvième et donc après avoir vérifier si le joueur a gagné
        elif nbtour == 9 :
            #Alors afficher l'égalité et renvoyer la fonction morpion avec la fin de match comme condition
            print("Egalité")
            morpion("no", nbtour)
        #Sinon
        else :
            #Alors renvoyer la fonction morpion avec le joueur dont c'est le tour
            morpion("J2", nbtour)

    #Si c'est le tour du joueur 2
    elif turn == "J2" :
        #Si une des trois lignes comprant 3 cercles
        #Alors le joueur 1 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        if x[0][0] == "✕"  and x[0][1] == "✕"  and x[0][2] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        elif x[1][0] == "✕"  and x[1][1] == "✕"  and x[1][2] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        elif x[2][0] == "✕"  and x[2][1] == "✕"  and x[2][2] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        #Si une des trois colonnes comprant 3 cercles
        #Alors le joueur 1 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        elif x[0][0] == "✕"  and x[1][0] == "✕"  and x[2][0] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        if x[0][1] == "✕"  and x[1][1] == "✕"  and x[2][1] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        elif x[0][2] == "✕"  and x[1][2] == "✕"  and x[2][2] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        #Si une des deux diagonales comprant 3 cercles
        #Alors le joueur 1 gagne et on renvoie la fonction morpion avec la fin de match comme condition après afficher que le joueur a gagné
        elif x[0][0] == "✕"  and x[1][1] == "✕"  and x[2][2] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        elif x[0][2] == "✕"  and x[1][1] == "✕"  and x[2][0] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        #Si le tour est le neuvième et donc après avoir vérifier si le joueur a gagné
        elif nbtour == 9 :
            #Alors afficher l'égalité et renvoyer la fonction morpion avec la fin de match comme condition
            print("Egalité")
            morpion("no", nbtour)
        #Sinon
        else :
            #Alors renvoyer la fonction morpion avec le joueur dont c'est le tour
            morpion("J1", nbtour)

#Appeler la fonction morpion au tour 0 avec le joueur qui commence
morpion("J1", 0)
#FIN