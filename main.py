# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:Kirti
# Date:30/01/2026


print("--- Factorial Finder ---\n")
# Write your code here
N = int(input("Enter Number: "))

if N < 0:
    print("Factorial of", -N, "is Not Defined")
else:
    fact = 1
    for i in range(1, N + 1):
        fact *= i
    print("Factorial of", N, "is", fact)




