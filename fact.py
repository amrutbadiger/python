"""
A program to know the factorial of a given number
"""
fact=1
n=int(input("Enter a number"))
for i in range(1,n+1):
    fact=fact*i
    print("factorial of",n,"is",fact)
