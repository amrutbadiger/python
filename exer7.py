"""
A program to know the odd numbers in the given range using for loop.
"""
n=int(input("Enter the range:"))
for i in range(1,n+1):
    if(i%2!=0):
        print("Odd numbers:",i)
