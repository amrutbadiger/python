'''
Adding and changing elements of a list.
adding elements using append
'''
fruits = ["apple", "banana", "guava"]
print(fruits)
fruits.append("papay")
print(fruits)
fruits.insert(1, "water melon") # using insert to add at a specific place.
print(fruits)
more_fruits=fruits +["grapes", "oranges"] #adding more than 1 ele. and assign to a differnt variable.
print(more_fruits)
more_fruits[5]= "strawberry" # changing the value of element.
print(more_fruits)
