# define a factorial function with one argument called n
def factorial(n):
    # initialite the result variable
    result = 1

    # for in n
    for i in range(n):
        # result is equal him self * i
        result = result * (i + 1)

    # return result
    return result

# define a factorial_recursive function with one argument called n
def factorial_recursive(n):
    # if n equal to 1 retrun n
    if n == 1:
        return n
    # else return n * facatoria_recursive passing n - 1
    else:
        return n * factorial_recursive(n - 1)

print(factorial(2))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
print(factorial(10))

print(factorial_recursive(2))
print(factorial_recursive(4))
print(factorial_recursive(5))
print(factorial_recursive(6))
print(factorial_recursive(7))
print(factorial_recursive(8))
print(factorial_recursive(9))
print(factorial_recursive(10))