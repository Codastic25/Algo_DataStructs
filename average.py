def find_average(numbers):
    # your code here
    if len(numbers) == 0:
        return 0
    
    else:
        cpt=0
        for elem in numbers :
            cpt = elem+cpt
        return cpt/len(numbers)