# find the factorial of a no 
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

input_no=int(input("Enter the no : "))

print(factorial(input_no))