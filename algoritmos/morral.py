
def morral(size, weight, values, n):
    
    if n == 0 or size ==0:
        return 0
    
    if weight[n - 1] > size:
        return morral(size, weight, values, n - 1)

    return max(values[n - 1] + morral(size - weight[n - 1], weight, values, n - 1), morral(size, weight, values, n - 1))

if __name__ == '__main__':
    values = [60, 100, 120]
    weight = [10, 20, 30]
    size = 50
    n = len(values)

    response = morral(size, weight, values, n)
    print(response)