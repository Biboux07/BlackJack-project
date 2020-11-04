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
        w1 += 1
    
    if k == 2 :
        w2 += 1
        
    if k == 0 :
        w0 += 1


    #affichage
    
    #z = (i/numgame)*100
    #print (z)
    #print(i,"/",numgame)

#print(w1)
#print(w2)
#print(w0)


#Resultat en pourcentage:

pourcentage_w1  =  (w1 / numgame) * 100

pourcentage_w2  =  (w2 / numgame) * 100

pourcentage_w0  =  (w0 / numgame) * 100


#Print the results


print("Number of games: ", numgame )
print ("IA1: ", round(pourcentage_w1, 2), "%")
print ("IA2: ", round(pourcentage_w2, 2), "%")
print ("TIE: ", round(pourcentage_w0, 2), "%")
