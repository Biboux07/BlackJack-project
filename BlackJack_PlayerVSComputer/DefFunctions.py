#importations
import random

#define the list
Cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

#define functions
def Rcard():
    card = random.choice(Cards)
    return card

def Sum(initial, Numcard):
    final = initial + Numcard
    return final

def Verif(final):
    if final == 21 :
        Dif = 0
    
    if  final != 21 :
        Dif = 21 - final
    return Dif


def results (a, b):
    

    #Cas normaux 2 numbres positifs (trouver le plus proche)
    if a > b :
        i = 1

    if a < b :
        i = 2


    #Une valeur est positive et une negative

    if a <= 21 and b > 21 :
        i = 1
        
    

    if a > 21 and b <= 21 :
        i = 2
        
    #Egalité

    if a == b :
        i = 0
        
    #Cas normaux (trouver le plus proche)

    
    #Imprimer le résultat
    
    if i == 1 :
        print("YOU WIN!")
    
    if i == 2 :
        print("YOU LOST!")
        
    if i == 0 :
        print("TIE!")

    
    return i

    




#i = Rcard()
#print(i)

#k = Sum(10, 5)
#print(k)

#y = Verif(17)
#print(0)

#k = CPUchoice()
#print(k)

#print("YOU WIN!")
#print("WINNER: Player 1")