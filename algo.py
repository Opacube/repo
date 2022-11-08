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
