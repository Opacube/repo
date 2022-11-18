#DEBUT
#On crée une fonction ticTacToe
def ticTacToe() :
    #On crée un tableau x qui servira d'interface
    x = [["▢", "▢", "▢"], ["▢", "▢", "▢"], ["▢", "▢", "▢"]]

    #On créer une variable case qui appelera chaque case du morpion avec un numéro correspondant (la première étant 0 et la dernière 8 puisqu'il y a 9 cases)
    case = {}
    num = 0
    for i in range (len(x)) :
        for k in range (len(x)):
            case[num] = x[i][k]
            num += 1

    #On crée la liste player qui prendra en compte les 2 joueurs du morpion
    player = []
    #On affiche quel joueur commence
    print("\n\n\n\n\n\n\n\n\n\n\033[1;36;40mRemember that player 1 starts")
    #On demande le nom du joueur 1
    player.append (input("Who is player 1 ? "))
    #On demande le nom du joueur 2
    player.append (input("\nWho is player 2 ? "))
    print("\n")
    #On affiche qui de quel joueur commençera
    print("Now\033[1;31;40m", player[0], "\033[1;36;40mwill start and\033[1;31;40m", player[1], "\033[1;36;40mwill play second !")
    print("Good luck !\n\n\n\n\n")

    #On appel la fonction player_choice qui va gérer le fonctionnement du jeu
    player_choice(player, who, case, turn)
    #On termine la fonction
    return

#On crée la fonction player_choice qui prendra les valeurs player, who et case
def player_choice(player, who, case, turn):

    #On appel la fonction printer
    printer(case)

    #On affiche le joueur dont c'est le tour
    print("It's\033[1;31;40m", player[who], "\033[1;36;40m's turn !\n\n\n\n")
    #On demande au joueur son choix de case dans la variable choice à l'aide de la fonction input
    choice = input("Type your choice : ")

    #Tant que le choix du joueur est différent d'une des cases du morpion ou que la case est déjà pleine
    while choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" or (case[int(choice)] == symbol[0] or case[int(choice)] == symbol[1]):
        #On appel la fonction printer
        printer(case)
        #On affiche le joueur dont c'est le tour
        print("It's\033[1;31;40m", player[who], "\033[1;36;40m's turn !\n\n\n\n")
        #On redemande au joueur son choix de case dans la variable choice à l'aide de la fonction input avec un message d'erreur
        choice = input("This does not correspond to any of the coordinates. Type your choice again : ")

    #On change la case correspondante au choix du joueur avec le symbole assigné à ce joueur
    case[int(choice)] = symbol[who]
    #Incrémenter 1 à turn
    turn += 1
    #Si la fonction didWin est vraie
    if didWin(player, who, case, symbol, turn) :
        #Alors retourner la fonction
        return

    #Sinon
    else :
        #Si le joueur est le joueur 1
        if who == 1 :
            #Alors soustraire 1 à la variable who
            who -= 1
        #Sinon
        else :
            #Alors ajouter 1 à la variable who
            who += 1

        #Appeler la fonction player_choice
        player_choice(player, who, case, turn)

#On crée la fonction printer qui prend comme paramètre case
def printer(case) :
    #Afficher le tableau du morpion
    print("\n\n\n\n\nHere is the Tic-Tac-Toe with its coordinates : \033[1;37;40m")
    print(case[0], " ", case[1], " ", case[2], "   0   1   2")
    print(case[3], " ", case[4], " ", case[5], "   3   4   5")
    print(case[6], " ", case[7], " ", case[8], "   6   7   8 \n\033[1;36;40m")

#On crée la fonction didWin qui prend comme paramètres player, who, case et symbol
def didWin(player, who, case, symbol, turn) :
    
    #On crée le booléen a par défaut sur False
    a = False

    #On vérifie les 3 lignes, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True
    if case[0] == symbol[who] and case[1] == symbol[who] and case[2] == symbol[who] :
        a = True
    elif case[3] == symbol[who] and case[4] == symbol[who] and case[5] == symbol[who] :
        a = True
    elif case[6] == symbol[who] and case[7] == symbol[who] and case[8] == symbol[who] :
        a = True

    #On vérifie les 3 colonnes, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True
    elif case[0] == symbol[who] and case[3] == symbol[who] and case[6] == symbol[who] :
        a = True
    elif case[1] == symbol[who] and case[4] == symbol[who] and case[7] == symbol[who] :
        a = True
    elif case[2] == symbol[who] and case[5] == symbol[who] and case[8] == symbol[who] :
        a = True

    #On vérifie les 2 diagonales, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True
    elif case[0] == symbol[who] and case[4] == symbol[who] and case[8] == symbol[who] :
        a = True
    elif case[2] == symbol[who] and case[4] == symbol[who] and case[6] == symbol[who] :
        a = True
    #Sinon si le tour est le neuvième
    #Alors mettre a sur True
    elif turn == 9 :
        a = True

    #Si a est sur True et que le tour est le neuvième
    if a and turn == 9:
        #Alors appeler la fonction printer
        printer(case)
        #Afficher le message d'égalité
        print("\n\n\n\n\nIt's over ! It's a tie !\033[1;36;40m")
    #Sinon si a est sur True
    elif a :
        #Alors appeler la fonction printer
        printer(case)
        #Afficher le gagnant de la partie
        print("\n\n\n\n\nIt's over !\033[1;31;40m", player[who], "won the game !\033[1;36;40m")
    #Sinon
    else :
        #Retourner la fonction
        return
    
    #Demander si on veut recommencer la partie et créer la variable restartchoice qui prend comme valeur notre choix
    restartchoice = input("Do you want to restart ? ")
    #Tant que a est sur True
    while a :
        #Alors si restart choice est différent de "yes"
        if restartchoice != "yes" :
            #Alors si restartchoice est différent de "no"
            if restartchoice == "no" :
                #Alors mettre a sur False
                a = False
                #Afficher un message d'au revoir
                print("\n\n\n\n\n\n\n\n\n\nSee you next time !")
                #Renvoyer la fonction avec comme résultat True
                return True
            #Sinon
            else :
                #Alors redemander si on veut recommencer la partie et créer la variable restartchoice qui prend comme valeur notre choix
                restartchoice = input("Please reply with 'yes' or 'no', do you want to restart ? (yes/no) ")
        #Sinon
        else :
            #Alors appeler la fonction ticTacToe
            ticTacToe()

#On crée la liste symbol qui prendra les deux symboles du jeu
symbol = ["⊛", "✕"]
#On crée la variable turn définie sur 0 qui définiera quel tour est en cours
turn = 0
#On crée la variable who définie sur 0 qui définiera le joueur dont c'est le tour de jouer
who = 0

#On appele la fonction ticTacToe
ticTacToe()
#FIN