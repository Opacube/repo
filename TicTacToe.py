x = [["▢", "▢", "▢"], ["▢", "▢", "▢"], ["▢", "▢", "▢"]]
print("\033[1;33;40m\nVoici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
print(x[0][0], " ", x[0][1], " ", x[0][2], "   1   2   3")
print(x[1][0], " ", x[1][1], " ", x[1][2], "   4   5   6")
print(x[2][0], " ", x[2][1], " ", x[2][2], "   7   8   9")

def morpion(turn, nbtour): 
    #Quand c'est le tour du joueur 1
    if turn == "J1" :
        choix = input("J1 : Insérer la case que vous voulez changer : ")
        #ligne 1
        if choix == "1" and x[0][0] == "▢":
            x[0][0] = "⊛"
        elif choix == "2" and x[0][1] == "▢":
            x[0][1] = "⊛"
        elif choix == "3" and x[0][2] == "▢":
            x[0][2] = "⊛"

        #ligne 2
        elif choix == "4" and x[1][0] == "▢":
            x[1][0] = "⊛"
        elif choix == "5" and x[1][1] == "▢":
            x[1][1] = "⊛"
        elif choix == "6" and x[1][2] == "▢":
            x[1][2] = "⊛"

        #ligne 3
        elif choix == "7" and x[2][0] == "▢":
            x[2][0] = "⊛"
        elif choix == "8" and x[2][1] == "▢":
            x[2][1] = "⊛"
        elif choix == "9" and x[2][2] == "▢":
            x[2][2] = "⊛"
        else :
            print("Erreur : La case sélectionnée est soit déjà pleine soit inexistante !")
            morpion(turn, nbtour)

        print("\033[1;33;40m\nVoici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
        print(x[0][0], " ", x[0][1], " ", x[0][2], "   1   2   3")
        print(x[1][0], " ", x[1][1], " ", x[1][2], "   4   5   6")
        print(x[2][0], " ", x[2][1], " ", x[2][2], "   7   8   9")
        nbtour = nbtour+1
        checkIfWin("J1", nbtour)
    #Quand c'est le tour du Joueur 2
    elif turn == "J2" :

        verifbot(nbtour)

        #TOUR 1
        if nbtour == 1 :
            if x[1][1] == "▢" :
                x[1][1] = "✕"
                nbtour = nbtour + 1
            else :
                x[0][2] = "✕"
                nbtour = nbtour + 1


        elif nbtour == 3 :
            #COIN HAUT GAUCHE
            if x[0][0] == "⊛" :
                if x[2][1] == "⊛":
                    x[2][0] = "✕"
                    nbtour = nbtour + 1
                elif x[1][2] == "⊛" :
                    x[0][2]
                    nbtour = nbtour + 1
                elif x[2][2] == "⊛" :
                    x[0][1] = "✕"
                    nbtour = nbtour + 1
            #COIN HAUT DROITE
            elif x[0][2] == "⊛" :
                if x[2][1] == "⊛":
                    x[2][2] = "✕"
                    nbtour = nbtour + 1
                elif x[1][0] == "⊛" :
                    x[0][0] = "✕"
                    nbtour = nbtour + 1
                elif x[2][0] == "⊛" :
                    x[0][1] = "✕"
                    nbtour = nbtour + 1
            #COIN BAS GAUCHE
            elif x[2][0] == "⊛" :
                if x[0][1] == "⊛":
                    x[0][0] = "✕"
                    nbtour = nbtour + 1
                elif x[1][2] == "⊛" :
                    x[2][2] = "✕"
                    nbtour = nbtour + 1
                elif x[0][2] == "⊛" :
                    x[2][1] = "✕"
                    nbtour = nbtour + 1
            #COIN BAS DROITE
            elif x[2][2] == "⊛" :
                if x[0][1] == "⊛":
                    x[0][2] = "✕"
                    nbtour = nbtour + 1
                elif x[1][0] == "⊛" :
                    x[2][0] = "✕"
                    nbtour = nbtour + 1
                elif x[0][0] == "⊛" :
                    x[2][1] = "✕"
                    nbtour = nbtour + 1

        #TOUR 2

        print("\033[1;33;40m\nVoici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
        print(x[0][0], " ", x[0][1], " ", x[0][2], "   1   2   3")
        print(x[1][0], " ", x[1][1], " ", x[1][2], "   4   5   6")
        print(x[2][0], " ", x[2][1], " ", x[2][2], "   7   8   9")
        checkIfWin("J2", nbtour)

    elif turn == "no" :
        print("L bozo")
        re = input("Voulez-vous recommencer ? ")
        while re != "oui" and re != "non" :
            re = input("Réponse incorrecte. Voulez-vous recommencer ? ")
        if re == "non" :
            print("Au revoir !")
        else :
            print("Bonne chance !")
            x[0][0] = "▢"
            x[0][1] = "▢"
            x[0][2] = "▢"
            x[1][0] = "▢"
            x[1][1] = "▢"
            x[1][2] = "▢"
            x[2][0] = "▢"
            x[2][1] = "▢"
            x[2][2] = "▢"
            print("\033[1;33;40m\nVoici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
            print(x[0][0], " ", x[0][1], " ", x[0][2], "   1   2   3")
            print(x[1][0], " ", x[1][1], " ", x[1][2], "   4   5   6")
            print(x[2][0], " ", x[2][1], " ", x[2][2], "   7   8   9")
            nbtour = 0
            morpion("J1", nbtour)

def verifbot(nbtour) :
    #Verifier si il y a deux X côte à côte, si oui et que la troisième case est vide, alors placer un X
    #LIGNE 1
    if x[0][0] == "✕" and x[0][1] == "✕" and x[0][2] != "⊛" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][1] == "✕" and x[0][2] == "✕" and x [0][0] != "⊛" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][0] == "✕" and x[0][2] == "✕" and x[0][1] != "⊛" :
        x[0][1] = "✕"
        nbtour = nbtour + 1
        return
    #LIGNE 2
    elif x[1][0] == "✕" and x[1][1] == "✕" and x[1][2] != "⊛" :
        x[1][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "✕" and x[1][2] == "✕" and x [1][0] != "⊛" :
        x[1][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][0] == "✕" and x[1][2] == "✕" and x[1][1] != "⊛" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    #LIGNE 3
    elif x[2][0] == "✕" and x[2][1] == "✕" and x[2][2] != "⊛" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][1] == "✕" and x[2][2] == "✕" and x [2][0] != "⊛" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][0] == "✕" and x[2][2] == "✕" and x[2][1] != "⊛" :
        x[2][1] = "✕"
        nbtour = nbtour + 1
        return
    #COLONNE 1
    elif x[0][0] == "✕" and x[1][0] == "✕" and x[2][0] != "⊛" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][0] == "✕" and x[2][0] == "✕" and x[1][0] != "⊛" :
        x[1][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][0] == "✕" and x[2][0] == "✕" and x[0][0] != "⊛" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    #COLONNE 2
    elif x[0][1] == "✕" and x[1][1] == "✕" and x[2][1] != "⊛" :
        x[2][1] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][1] == "✕" and x[2][1] == "✕" and x[1][1] != "⊛" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "✕" and x[2][1] == "✕" and x[0][1] != "⊛" :
        x[0][1] = "✕"
        nbtour = nbtour + 1
        return
    #COLONNE 3
    elif x[0][2] == "✕" and x[1][2] == "✕" and x[2][2] != "⊛" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][2] == "✕" and x[2][2] == "✕" and x[1][2] != "⊛" :
        x[1][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][2] == "✕" and x[2][2] == "✕" and x[0][2] != "⊛" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    #DIAGONALE 1
    elif x[0][0] == "✕" and x[1][1] == "✕" and x[2][2] != "⊛" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "✕" and x[2][2] == "✕" and x[0][0] != "⊛" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][2] == "✕" and x[0][0] == "✕" and x[1][1] != "⊛" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    #DIAGONALE 2
    elif x[0][2] == "✕" and x[1][1] == "✕" and x[2][0] != "⊛" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "✕" and x[2][0] == "✕" and x[0][2] != "⊛" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][0] == "✕" and x[0][2] == "✕" and x[1][1] != "⊛" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return

    #Verifier si il y a deux O côte à côte, si oui et que la troisième case est vide, alors placer un X
    #LIGNE 1
    elif x[0][0] == "⊛" and x[0][1] == "⊛" and x[0][2] != "✕" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][1] == "⊛" and x[0][2] == "⊛" and x [0][0] != "✕" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][0] == "⊛" and x[0][2] == "⊛" and x[0][1] != "✕" :
        x[0][1] = "✕"
        nbtour = nbtour + 1
        return
    #LIGNE 2
    elif x[1][0] == "⊛" and x[1][1] == "⊛" and x[1][2] != "✕" :
        x[1][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "⊛" and x[1][2] == "⊛" and x [1][0] != "✕" :
        x[1][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][0] == "⊛" and x[1][2] == "⊛" and x[1][1] != "✕" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    #LIGNE 3
    elif x[2][0] == "⊛" and x[2][1] == "⊛" and x[2][2] != "✕" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][1] == "⊛" and x[2][2] == "⊛" and x [2][0] != "✕" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][0] == "⊛" and x[2][2] == "⊛" and x[2][1] != "✕" :
        x[2][1] = "✕"
        nbtour = nbtour + 1
        return
    #COLONNE 1
    elif x[0][0] == "⊛" and x[1][0] == "⊛" and x[2][0] != "✕" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][0] == "⊛" and x[2][0] == "⊛" and x[1][0] != "✕" :
        x[1][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][0] == "⊛" and x[2][0] == "⊛" and x[0][0] != "✕" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    #COLONNE 2
    elif x[0][1] == "⊛" and x[1][1] == "⊛" and x[2][1] != "✕" :
        x[2][1] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][1] == "⊛" and x[2][1] == "⊛" and x[1][1] != "✕" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "⊛" and x[2][1] == "⊛" and x[0][1] != "✕" :
        x[0][1] = "✕"
        nbtour = nbtour + 1
        return
    #COLONNE 3
    elif x[0][2] == "⊛" and x[1][2] == "⊛" and x[2][2] != "✕" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[0][2] == "⊛" and x[2][2] == "⊛" and x[1][2] != "✕" :
        x[1][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][2] == "⊛" and x[2][2] == "⊛" and x[0][2] != "✕" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    #DIAGONALE 1
    elif x[0][0] == "⊛" and x[1][1] == "⊛" and x[2][2] != "✕" :
        x[2][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "⊛" and x[2][2] == "⊛" and x[0][0] != "✕" :
        x[0][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][2] == "⊛" and x[0][0] == "⊛" and x[1][1] != "✕" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    #DIAGONALE 2
    elif x[0][2] == "⊛" and x[1][1] == "⊛" and x[2][0] != "✕" :
        x[2][0] = "✕"
        nbtour = nbtour + 1
        return
    elif x[1][1] == "⊛" and x[2][0] == "⊛" and x[0][2] != "✕" :
        x[0][2] = "✕"
        nbtour = nbtour + 1
        return
    elif x[2][0] == "⊛" and x[0][2] == "⊛" and x[1][1] != "✕" :
        x[1][1] = "✕"
        nbtour = nbtour + 1
        return
    else :
        if x[0][0] == "▢" :
            x[0][0] = "✕"
            nbtour = nbtour + 1
            return
        elif x[0][1] == "▢" :
            x[0][1] = "✕"
            nbtour = nbtour + 1
            return
        elif x[0][2] == "▢" :
            x[0][2] = "✕"
            nbtour = nbtour + 1
            return
        elif x[1][0] == "▢" :
            x[1][0] = "✕"
            nbtour = nbtour + 1
            return
        elif x[1][1] == "▢" :
            x[1][1] = "✕"
            nbtour = nbtour + 1
            return
        elif x[1][2] == "▢" :
            x[1][2] = "✕"
            nbtour = nbtour + 1
            return
        elif x[2][0] == "▢" :
            x[2][0] = "✕"
            nbtour = nbtour + 1
            return
        elif x[2][1] == "▢" :
            x[2][1] = "✕"
            nbtour = nbtour + 1
            return
        elif x[2][2] == "▢" :
            x[2][2] = "✕"
            nbtour = nbtour + 1
            return
        return
    

#Verifier si un joueur a gagné
def checkIfWin(turn, nbtour):
    #JOUEUR 1
    if turn == "J1" :
        #LIGNES
        if x[0][0] == "⊛"  and x[0][1] == "⊛"  and x[0][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[1][0] == "⊛"  and x[1][1] == "⊛"  and x[1][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[2][0] == "⊛"  and x[2][1] == "⊛"  and x[2][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        #COLONNES
        elif x[0][0] == "⊛"  and x[1][0] == "⊛"  and x[2][0] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[0][1] == "⊛"  and x[1][1] == "⊛"  and x[2][1] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[0][2] == "⊛"  and x[1][2] == "⊛"  and x[2][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        #DIAGONALES
        elif x[0][0] == "⊛"  and x[1][1] == "⊛"  and x[2][2] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        elif x[0][2] == "⊛"  and x[1][1] == "⊛"  and x[2][0] == "⊛" :
            print("J1 Wins")
            morpion("no", nbtour)
        #Egalité
        elif nbtour == 9 :
            print("Egalité")
            morpion("no", nbtour)
        else :
            morpion("J2", nbtour)
    #JOUEUR 2
    elif turn == "J2" :
        #LIGNES
        if x[0][0] == "✕"  and x[0][1] == "✕"  and x[0][2] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        elif x[1][0] == "✕"  and x[1][1] == "✕"  and x[1][2] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        elif x[2][0] == "✕"  and x[2][1] == "✕"  and x[2][2] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        #COLONNES
        elif x[0][0] == "✕"  and x[1][0] == "✕"  and x[2][0] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        if x[0][1] == "✕"  and x[1][1] == "✕"  and x[2][1] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        elif x[0][2] == "✕"  and x[1][2] == "✕"  and x[2][2] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        #DIAGONALES
        elif x[0][0] == "✕"  and x[1][1] == "✕"  and x[2][2] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
        elif x[0][2] == "✕"  and x[1][1] == "✕"  and x[2][0] == "✕" :
            print("J2 Wins")
            morpion("no", nbtour)
            #EGALITE
        elif nbtour == 9 :
            print("Egalité")
            morpion("no", nbtour)
        else :
            morpion("J1", nbtour)

morpion("J1", 0)