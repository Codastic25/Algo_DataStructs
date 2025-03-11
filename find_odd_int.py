def find_it(seq):
    #on trouve le nombre d'occurrences de chaque nombre dans le tableau
    #return l'element qui a une occurrence impaire
    
    for num in seq: #je parcours les elements de ma liste
        count = seq.count(num)# occurrences de chaque element
        if count%2!=0:
            return num
                
    

