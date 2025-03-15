def get_middle(s):
    n = len(s)
    
    if n == 1:
        return s
    
    if n%2 != 0:# si la longueur de la chaine est impaire
        return s[n//2]

    else: # si la longueur de la chaine est paire
        x = s[n//2-1]
        y = s[n//2]
        return x+y