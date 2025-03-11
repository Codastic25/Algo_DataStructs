import math

def count_bits(n):

    #conversion en bit et compteur de 1

    cpt = 0
    if (n==0):
        cpt = 0
        return cpt
    
    while (n != 0):
        
    
        if (n%2 != 0):
            #1
            cpt = cpt+1
            n = n/2
            n = math.floor(n)
        else :
            #0
            n = n/2
            
    #print(bitList)

    
    return cpt