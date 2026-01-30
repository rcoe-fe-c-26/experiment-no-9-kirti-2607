# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:Kirti
# Date:30/01/2026


print("--- Factorial Finder ---\n")
# Write your code here
N = int(input("Enter Number: "))
a=1
for x in range(1,N+1):
    a *= x
if(N<0):
 print("Factorial of" ,abs(N), "is Not Defined")
else:
   print("Factorial of", N ,"is",a)







