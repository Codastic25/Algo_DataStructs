def plusMinus(arr):
    # Write your code here
    counterPlus=0
    counterNeg=0
    counterNull=0
    total=len(arr) #pour avoir le nombre d'elements dans ma liste
    
    for elem in arr:
        if elem > 0:
            counterPlus+=1
        elif elem < 0:
            counterNeg+=1
        else :
            counterNull+=1
            
    resPos = counterPlus/total
    resNeg = counterNeg/total
    resNull = counterNull/total
    
    # Affichage avec 6 decimales
    print("{:.6f}".format(resPos))
    print("{:.6f}".format(resNeg))
    print("{:.6f}".format(resNull))
