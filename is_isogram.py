def is_isogram(string):
    #your code here
    #je regarde si ma nouvelle lettre est différente de toutes celles précédentes
    string = string.lower()
    if string == "":#si ma chaine de caractères est vide --> True
        return True
    else :
        for i in range (len(string)) :
            for j in range (i+1, len(string)) :
                if string[i] == string[j]:
                    return False
        return True
            