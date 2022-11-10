import random

rand_list = []

r = random.randrange(3,5)

for i in range(r):
    rand_list.append([(random.randrange(0,r)) for i in range(r)])

for i in range (len(rand_list)):
    print(rand_list[i])

x = 0
y = 1
top = [(x - 1), y]
bottom = [(x + 1), y]
left = [x, (y - 1)]
right = [x, (y + 1)]
if x - 1 >= 0:
    print("Top : ", top)
else :
    print("Top is negative.")
if x + 1 <+ len(rand_list):
    print("Bottom : ", bottom)
else :
    print("Bottom is above the list")
if y - 1 >+ 0:
    print("Left : ", left)
else : print("Left is negative")
if y + 1 <+ len(rand_list):
    print("Right : ", right)

# topnum = rand_list[x - 1][y]
# bottomnum = rand_list[x + 1][y]
# leftnum = rand_list[x][y - 1]
# rightnum = rand_list[x][y + 1]
# if topnum == 1:
#     print("top is present")
# else:
#     print('top is absent')

#random.choice(⬜, ⬛)

#JEU DE LA VIE

#CREER UNE LISTE AVEC ALEATOIREMENT DES 0 ET 1
#AFFICHER CETTE LISTE X FOIS
#SI IL Y A PLUS DE 2 CELLULES ADJASCENTES
    #LA CELLULE MEURT
#SINON
    #ELLE SE REPRODUIT