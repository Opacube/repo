#DEBUT
#On crée une fonction ticTacToe
    #On crée un tableau x qui servira d'interface

    #On créer une variable case qui appelera chaque case du morpion avec un numéro correspondant (la première étant 0 et la dernière 8 puisqu'il y a 9 cases)

    #On crée la liste player qui prendra en compte les 2 joueurs du morpion
    #On affiche quel joueur commence
    #On demande le nom du joueur 1
    #On demande le nom du joueur 2
    #On affiche qui de quel joueur commençera

    #On appel la fonction player_choice qui va gérer le fonctionnement du jeu
    #On termine la fonction

#On crée la fonction player_choice qui prendra les valeurs player, who et case

    #On appel la fonction printer

    #On affiche le joueur dont c'est le tour
    #On demande au joueur son choix de case dans la variable choice à l'aide de la fonction input

    #Tant que le choix du joueur est différent d'une des cases du morpion ou que la case est déjà pleine
        #On appel la fonction printer
        #On affiche le joueur dont c'est le tour
        #On redemande au joueur son choix de case dans la variable choice à l'aide de la fonction input avec un message d'erreur

    #On change la case correspondante au choix du joueur avec le symbole assigné à ce joueur
    #Incrémenter 1 à turn
    #Si la fonction didWin est vraie
        #Alors retourner la fonction

    #Sinon
        #Si le joueur est le joueur 1
            #Alors soustraire 1 à la variable who
        #Sinon
            #Alors ajouter 1 à la variable who

        #Appeler la fonction player_choice

#On crée la fonction printer qui prend comme paramètre case
    #Afficher le tableau du morpion

#On crée la fonction didWin qui prend comme paramètres player, who, case et symbol
    
    #On crée le booléen a par défaut sur False

    #On vérifie les 3 lignes, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True

    #On vérifie les 3 colonnes, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True

    #On vérifie les 2 diagonales, si l'une d'entre elles possède le même symbole 3 fois
    #Alors mettre a sur True

    #Sinon si le tour est le neuvième
    #Alors mettre a sur True

    #Si a est sur True et que le tour est le neuvième
        #Alors appeler la fonction printer
        #Afficher le message d'égalité
    #Sinon si a est sur True
        #Alors appeler la fonction printer
        #Afficher le gagnant de la partie
    #Sinon
        #Retourner la fonction
    
    #Demander si on veut recommencer la partie et créer la variable restartchoice qui prend comme valeur notre choix
    #Tant que a est sur True
        #Alors si restart choice est différent de "yes"
            #Alors si restartchoice est différent de "no"
                #Alors mettre a sur False
                #Afficher un message d'au revoir
                #Renvoyer la fonction avec comme résultat True
            #Sinon
                #Alors redemander si on veut recommencer la partie et créer la variable restartchoice qui prend comme valeur notre choix
        #Sinon
            #Alors appeler la fonction ticTacToe

#On crée la liste symbol qui prendra les deux symboles du jeu
#On crée la variable turn définie sur 0 qui définiera quel tour est en cours
#On crée la variable who définie sur 0 qui définiera le joueur dont c'est le tour de jouer

#On appele la fonction ticTacToe
#FIN