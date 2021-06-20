#---------------------------------------------#
# Ley de la suma

# Crecimiento lineal
def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n+n) = O(2n) = O(n) 

# Crecimiento exponencial
def f(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

# O(n) + O(n*n) = O(n+n) = O(n + n^2) = O(n^2) 

#---------------------------------------------#
# Ley de la multiplicación

# Crecimiento exponencial
def f(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

# O(n) O(n) = O(nn) = O(n^2) 

#---------------------------------------------#
#Recursividad múltiple
 
def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

# O(2^n)