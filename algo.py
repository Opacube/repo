#Créer une fonction input qui renvoie un caractère de type string and hasard
#Afficher le caractère
#Si le caractère est égal au caractère à deviner
#Afficher un message de victoire
#Sinon afficher un message de défaite



def input(): #renvoie un caractere de type string au hasard

car = "o" #Créer le caractère gagnant
str = input() #Créer une variable associée au numéro au hasard

if str == car: #Si le caractère au hasard est égal à celui que l'on cherche
    print("Bravo, vous avez gagné !") #Afficher le message de victoire
else : #Sinon
    print("Vous avez perdu !") #Afficher le message de défaite