def f(x):
    response = 0
    for i in range(1000): 
        response += 1
        # 1000

    for i in range(x):
        response += x
        # x

    for i in range(x):
        for j in range(x):
            response += 1
            response += 1
            # x * x = x^2 = 2x^2
    
    return response # 1002 + x + 2x^2