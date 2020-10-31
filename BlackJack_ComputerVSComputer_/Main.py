import IA1
import DefFunctions
import IA2


# Actual Main #
numgame = 100000
w1 = 0
w2 = 0
w0 = 0


#Loop

for i in range(0, numgame) :

    #Calculations

    a = IA1.CPUchoice()

    b = IA2.CPUchoice()

    

    #Print the results
    #print ("IA1:", b)
    #print ("IA2:", a)


    #See who is the winner
    k = DefFunctions.results(a, b)

    #Stats
    if k == 1 :
        w2 += 1
    
    if k == 2 :
        w1 += 1
        
    if k == 0 :
        w0 += 1


    #affichage

    #print(i,"/",numgame)



#Finals stats :

#fractions



#Print the results


print("Number of games: ", numgame )
print ("IA1: ", w1)
print ("IA2: ", w2)
print ("TIE: ", w0)