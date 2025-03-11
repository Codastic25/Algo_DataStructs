def product_fib(_prod): 
    n=0
    while fibonacci(n) * fibonacci(n + 1) < _prod:
        n=n+1
    if (_prod == fibonacci(n)*fibonacci(n+1)):
        resOk = [fibonacci(n), fibonacci(n+1), True]
        return resOk
    else:
        resNotOk = [fibonacci(n), fibonacci(n+1), False]
        return resNotOk
    
#suite de fibonacci en récursif
def fibonacci(n) :
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #solution else pas moi, j'avais fais en récursif mais trop long et trop couteux
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b