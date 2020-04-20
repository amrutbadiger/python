"""
A program to know the even number in the given rangeusing for loop.
"""
n=int(input("Enter the range:"))
for i in range(1,n+1):
    if(i%2==0):
        print(i)
