'''
A program to pop up elemenrs from one list to another variables.
Also to pop a element from one list and append or insert it to other list.
'''
a=["tom", "bob", "sid", "dick", "bib", "ram", "bhim",]
b=["boy", "girl", "madam", "sir", "mr.", "mrs.",]
print(a)
print(b)
name=a.pop(4)
print(name) # pop an element from a list and assign it to a variable.
b.append(a.pop(5))
print(b) # to pop an element from a list and append it to another.
a.append(b.pop(0))
print(a)
b.insert(2, a.pop(4))
print(b) # to pop an element and insert it in another list.
c = b.pop(5) + " " + "Ramu"
print(c)
'''
Using the keywords append and pop move the first elementof the list a
to the end of the list a .
'''
a.append(a.pop(0))
print(a)
'''
Using minimal code, pop the last element of list b
and append it to list a.
'''
a.append(b.pop())
print(a)
