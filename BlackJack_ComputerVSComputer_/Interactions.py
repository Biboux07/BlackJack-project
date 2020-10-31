#importations

import random
import DefFunctions

#Interaction with the player (Function).

def Interaction():
    

    #1ere carte imposée
    Numfinal = DefFunctions.Rcard()

    print("Your first Card is a:", Numfinal)

    print("Would you like to pick another Card? :")



    #variables
    k = 0
    i = 1


    while (True):

        #Verification du score

        k = DefFunctions.Verif(Numfinal)

        if k <= 0 :
            break


        # demande pour continuer

        choice = (input("y/n :"))

        if choice == "y" :
            Numcard = DefFunctions.Rcard()
            Numfinal += Numcard
            i += 1

            #Show results
            print ("New card:", Numcard)
            print ("Total:", Numfinal)


        if choice == "n" :
            print("Ok we stop!")
            
            break
    

    #print("You took :", i , "cards")
        

    return Numfinal


  
    
#a = Interaction()

#print (a)


