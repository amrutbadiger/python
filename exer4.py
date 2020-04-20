"""
A program to calculate rate of interest.
"""
p=int(input("Enter the principal amount(P):"))
r=float(input("Enter the rate of interest(R):"))
t=int(input("Enter the period(T):"))
i=(p*r*t)/100
print("Interest is:",i)
