#importations ;

import random
import DefFunctions

#CPU Function.

def CPUchoice ():
    #idee d'une liste qui retiens les coups
    #possibilité de connaitre le nombre de coups
    k = 0
    i = 0
    Numfinal = 0
    while (True) :

        if Numfinal <= 14 :
            Numcard = DefFunctions.Rcard()
            Numfinal += Numcard

            i += 1

        if Numfinal >= 20 :
            break

        if Numfinal >=15 and Numfinal <= 19 :
            k = int(random.randrange(0,2))
                
        if k == 0 :
            Numcard = DefFunctions.Rcard()
            Numfinal += Numcard

            i += 1

        if k == 1 or k == 2 :
             break

        

    CPUscore = Numfinal
    return CPUscore


