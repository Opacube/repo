#Function
def ticTacToe() :
    x = [["▢", "▢", "▢"], ["▢", "▢", "▢"], ["▢", "▢", "▢"]]

    #Cases
    case = {}
    num = 0
    for i in range (len(x)) :
        for k in range (len(x)):
            case[num] = x[i][k]
            num += 1

    #Choice mode
    player = []
    mode = input("\n\n\n\n\n\n\n\n\n\n\033[1;36;40mWhat do you want to do ? \033[1;31;40m1\033[1;36;40m - JvsJ or \033[1;31;40m2\033[1;36;40m - BvsJ")
    while mode != "1" :
        if mode != "2" :
            print("Invalid choice, please try again")
            mode = input("What do you want to do ? \033[1;31;40m1\033[1;36;40m - JvsJ or \033[1;31;40m2\033[1;36;40m - BvsJ")

        #
        else :
            turnchoice = input("Do you want to start ? (yes/no) ")

            while turnchoice != "yes" :
                if turnchoice != "no" :
                    print("Invalid choice, please try again")
                    turnchoice = input("Do you want to start ? (yes/no) ")

                else :
                    print("The bot will then start !")
                    player.append ("Bot")
                    player.append (input("Who are you ? "))
                    player_choice(player, who, case, mode)
                    return

            else :
                print("You will then start !")
                player.append (input("Who are you ? "))
                player.append ("Bot")
                player_choice(player, who, case, mode)
                return


    else :
        print("\n\n\n\n\n\n\n\n\n\n\033[1;36;40mRemember that player 1 starts")
        player.append (input("Who is player 1 ? "))
        player.append (input("\nWho is player 2 ? "))
        print("\n")
        print("Now\033[1;31;40m", player[0], "\033[1;36;40mwill start and\033[1;31;40m", player[1], "\033[1;36;40mwill play second !")
        print("Good luck !\n\n\n\n\n")

        player_choice(player, who, case, mode)

def player_choice(player, who, case, mode):

    printer(case)

    if mode == "1" :
        print("It's\033[1;31;40m", player[who], "\033[1;36;40m's turn !\n\n\n\n")
        choice = input("Type your choice : ")

        while choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" or (case[int(choice)] == symbol[0] or case[int(choice)] == symbol[1]):
            printer(case)
            print("It's\033[1;31;40m", player[who], "\033[1;36;40m's turn !\n\n\n\n")
            choice = input("This does not correspond to any of the coordinates. Type your choice again : ")

        case[int(choice)] = symbol[who]
        if didWin(player, who, case, symbol) :
            return
        else :

            if who == 1 :
                who -= 1
            else :
                who += 1

            player_choice(player, who, case, mode)

    else :
        print("Bot game")
        return

def printer(case) :
    print("\n\n\n\n\nHere is the Tic-Tac-Toe with its coordinates : \033[1;37;40m")
    print(case[0], " ", case[1], " ", case[2], "   0   1   2")
    print(case[3], " ", case[4], " ", case[5], "   3   4   5")
    print(case[6], " ", case[7], " ", case[8], "   6   7   8 \n\033[1;36;40m")

def didWin(player, who, case, symbol) :
    
    a = False

    if case[0] == symbol[who] and case[1] == symbol[who] and case[2] == symbol[who] :
        a = True
    elif case[3] == symbol[who] and case[4] == symbol[who] and case[5] == symbol[who] :
        a = True
    elif case[6] == symbol[who] and case[7] == symbol[who] and case[8] == symbol[who] :
        a = True

    elif case[0] == symbol[who] and case[3] == symbol[who] and case[6] == symbol[who] :
        a = True
    elif case[1] == symbol[who] and case[4] == symbol[who] and case[7] == symbol[who] :
        a = True
    elif case[2] == symbol[who] and case[5] == symbol[who] and case[8] == symbol[who] :
        a = True

    elif case[0] == symbol[who] and case[4] == symbol[who] and case[8] == symbol[who] :
        a = True
    elif case[2] == symbol[who] and case[4] == symbol[who] and case[6] == symbol[who] :
        a = True

    if a :
        printer(case)
        print("\n\n\n\n\nIt's over !\033[1;31;40m", player[who], "won the game !\033[1;36;40m")
        restartchoice = input("Do you want to restart ? ")
        while a :
            if restartchoice != "yes" :
                if restartchoice == "no" :
                    a = False
                    print("\n\n\n\n\n\n\n\n\n\nSee you next time !")
                    return True
                else :
                    restartchoice = input("Please reply with 'yes' or 'no', do you want to restart ? (yes/no) ")
            else :
                ticTacToe()
    else :
        return

symbol = ["⊛", "✕"]
turn = 0
who = 0

ticTacToe()