"""
Bubble sort algorithme permet de trier une liste et ou tableau en comparant deux éléments voisins au sein du tableau
Si l'élément de gauche est plus grand que son voisin de droite, alors je les échange
sinon, rien ne change
et je fais ça jusqu'à la longueur de mon tableau

Finalité : le plus grand élément sera à la fin du tableau, il remonte comme une bulle en haut du tableau en se comparant à chaque tour de boucle à son voisin de droite
quand le plus grand est trié, donc bien placé à la fin, je n'ai plus qu'à vérifier les changements jusqu'à la longueur de mon tableau sans le dernier élément déjà trié
et ce jusqu'à ce que tous mes éléments soient triés dans l'ordre croissant

Ainsi, mes éléments remontent comme une bulle en fonction de du tri

Compléxité : O(n²)
"""


def bubble_sort (arr):
    n = len(arr) #longueur de mon tableau

    # si liste vide ou à 1 élément --> pas besoin de trier et return le tableau directement
    if n<2:
        return arr

    #je boucle sur la longueur de mon array pour appliquer mon bubble sort algo
    for i in range (n):
        is_exchanged = False #réinitialise le statut à False à chaque tour de boucle

        for j in range (n-i-1): #la boucle qui vérifie les changements et les applique à n-i-1 (donc sans les derniers éléments déjà triés à chaque fois)
            if arr[j] > arr[j+1]: #si élément de gauche + grand que élément de droite --> changement
                is_exchanged = True #prouve qu'il y a eu échange entre éléments voisins
                arr[j], arr[j+1] = arr[j+1], arr[j]#échange les éléments de positions


        if is_exchanged == False: # si aucun parcours de boucle et --> pas d'échange et de tri à faire, alors ça veut dire que le tableau est déjà trié
            break

    return arr #retourne le tableau trié
