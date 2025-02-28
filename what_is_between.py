def between(a,b):
    # good luck
    completeList = [a,b]
    while (a!=b):
        a=a+1
        completeList.append(a)
        completeList.sort()
    #suppression du dernier element qui apparait deux fois
    completeList.pop()
        
    return completeList
    