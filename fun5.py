# Dealing with a unknown no. of arguements.
'''
to display each value in turn on a separate line.
Start by displaying the value of the first parameter.
'''
def show(**whatever):
  for x in whatever.values():
    print(x)
show(name="Raj", town="Mumbai")

'''
Code an empty list. Code a function that fills the list
In the function definition include three parameters—two parameters that accept keyword
arguments and a third parameter that accepts optional keyword arguments.
Append each of the first two parameters to the list. Then loop through the
dictionary of optional values and append each of those values to the list. Display the list.
Call the function, providing four keyword arguments.
'''
customers=[]
def fill_customer(name, town, **whatever):
    customers.append(name)
    customers.append(town)
    for value in whatever.values():
        customers.append(value)
        print(customers)
fill_customer(name="Ajay", town="Bengaluru", address="Varthur", mobile="9900470925")
        
