'''
A program to create a tuple.adding the elements of a tuple to a list
Concatenating element of two tuples and assigning it to a variable.
'''
a=("a", "b", "c", "d", "e", "f")
b=(1, 2, 3, 4, 5, 6, 7, 8)
print(a) # creating a tupple with strings.
print(b) # creating a tupple with numbers.
print(b[5]) # displayin a specific element of a tupple
# concatenating 2 specific elements of diff tuples and assigning it to a variable.
x = (3, "Hello", "Howdy", "Greetings")
y = ("earth", "sun", "World", "Pluto", 144)
greeting=x[1]+" "+y[2]
print(greeting) 
'''
 To  Code a tuple with three elements that are strings.
Then, in a single line, append the last element to a list.
'''
my_list=["x", "y"]
my_tupple=("a", "b", "c")
my_list.append(my_tupple[2])
print(my_list)
'''
Insert an element of the tuple into the first
position (index 0) in the list. Then display the list
'''
list=[4, 5, 6]
tupple=(1, 2, 3)
list.insert(0,tupple[2])
print(list)

