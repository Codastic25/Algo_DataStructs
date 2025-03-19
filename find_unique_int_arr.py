"""
def find_uniq(arr):
    # your code here
    for elem in arr:
        if arr.count(elem) == 1:
            n = elem
            return n # n: unique number in the array
        
    #complexite trop grande pour de trop grands nombres
    solution intrenet ci dessous car la solution ci dessus est time out
"""

def find_uniq(arr):
    a, b = set(arr)  # Récupère les deux valeurs distinctes
    return a if arr.count(a) == 1 else b

