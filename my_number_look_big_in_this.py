def narcissistic( value ):
    nombreChiffres = len(str(value)) #me donne le nombre de chiffres et donc la puissance
    chaineValue = str(value) #conversion en str
    listValue = list(chaineValue) #conversion du str en list
    numberInLste = list(map(int, listValue)) #conversion des elements str en int
    
    cpt=0
    for elem in numberInLste:
        res = elem**nombreChiffres
        cpt=cpt+res
        if (cpt==value):
            return True
    
    return False # Code away