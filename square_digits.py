import math

def square_digits(num):
    final_test = []
    x = str(num)
    for elem in x:
        elem = int(elem) ** 2# je monte chaque element au carre
        final_test.append(elem)
    final_str = "".join(str(x) for x in final_test)
    final_int = int(final_str)
        
        
    return final_int
        