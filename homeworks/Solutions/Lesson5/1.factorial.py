def factorial(n):
    result = 1

    for i in range(n):
        result = result * (i + 1)

    return result

def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

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