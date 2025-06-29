def factorial(n):
   
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)

sample_number = int(input("Enter a number to calculate its factorial: "))
result = factorial(sample_number)

print(f"The factorial of {sample_number} is: {result}")
