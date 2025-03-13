def rotateLeft(d, arr):
    # Write your code here
    n = len(arr)#longueur du tableau
    arr[d:]#reste des elem
    arr[:d]#premiers elem
    
    tmp=arr[:d]
    """
    arr[d:]=tmp
    arr[d:]=arr[:d]
    arr[:d]=tmp
    """
    
    neo_arr = arr[d:] + tmp
    
    return neo_arr
    