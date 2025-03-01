def get_count(sentence):
    cpt=0
    for letter in sentence:
        if (letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u"):
            cpt=cpt+1
            
    return cpt