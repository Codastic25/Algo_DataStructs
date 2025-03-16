# Complexité O(n²)

def insertion_sort(arr):
    for i in range(1, len(arr)):  # On commence à 1 et non 0 car le premier élément est déjà "trié"
        key = arr[i]  # Élément à insérer, que l'on nomme cle 
        j = i - 1  # Position avant key, grace a ça on parcourt la partie déjà triée du tableau

        # Déplacer les éléments plus grands vers la droite
        while j >= 0 and arr[j] > key:# on compare key avec les elements deja triés à sa gauche
            arr[j + 1] = arr[j]  # Décalage vers la droite
            j -= 1  # On continue de comparer avec les éléments à gauche

            #cad, on compare key avec l'element deja trié a gauche puis l'element encore a gauche et ainsi de suite jusqu'a placer key a la bonne place par la boucle while plus haut

        # Insérer l'élément à la bonne place
        arr[j + 1] = key  

    return arr

# Exemple d'utilisation
arr = [55,23,89,4,76,456,1,230,569,41,39]
print("Tableau trié :", insertion_sort(arr))
#Tableau trié : [1, 4, 23, 39, 41, 55, 76, 89, 230, 456, 569]
