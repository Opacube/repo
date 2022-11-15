x = [["▢", "▢", "▢"], ["▢", "▢", "▢"], ["▢", "▢", "▢"]]
print("\033[1;33;40m\nVoici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
print(x[0][0], " ", x[0][1], " ", x[0][2], "   1   2   3")
print(x[1][0], " ", x[1][1], " ", x[1][2], "   4   5   6")
print(x[2][0], " ", x[2][1], " ", x[2][2], "   7   8   9")

def morpion(turn, nbtour): 

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

    elif turn == "J2" :
        #JOUEUR 2
        choix = input("J2 : Insérer la case que vous voulez changer : ")
        #ligne 1
        if choix == "1" and x[0][0] == "▢":
            x[0][0] = "✕"
        elif choix == "2" and x[0][1] == "▢":
            x[0][1] = "✕"
        elif choix == "3" and x[0][2] == "▢":
            x[0][2] = "✕"

        #ligne 2
        elif choix == "4" and x[1][0] == "▢":
            x[1][0] = "✕"
        elif choix == "5" and x[1][1] == "▢":
            x[1][1] = "✕"
        elif choix == "6" and x[1][2] == "▢":
            x[1][2] = "✕"

        #ligne 3
        elif choix == "7" and x[2][0] == "▢":
            x[2][0] = "✕"
        elif choix == "8" and x[2][1] == "▢":
            x[2][1] = "✕"
        elif choix == "9" and x[2][2] == "▢":
            x[2][2] = "✕"
        else :
            print("Erreur : La case sélectionnée est soit déjà pleine soit inexistante !")
            morpion(turn, nbtour)

        print("\033[1;33;40m\nVoici le tableau du jeu ainsi que les coordonnées de chaque case : \n")
        print(x[0][0], " ", x[0][1], " ", x[0][2], "   1   2   3")
        print(x[1][0], " ", x[1][1], " ", x[1][2], "   4   5   6")
        print(x[2][0], " ", x[2][1], " ", x[2][2], "   7   8   9")
        nbtour = nbtour+1
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