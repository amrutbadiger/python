"""
A progam to know the largest and smallest number of the given list.
"""
arr=[]
num=int(input("Enter a number:"))
for i in range(num):
    numbers=int(input("Enter different numbers:"))
    arr.append(numbers)

    print("Largest number in the list:",max(arr))
    print("Smallest number in the list:",min(arr))
