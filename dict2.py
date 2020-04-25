'''
Assign a dictionary item's value to a variable using a
key that's a string. Then append that value to a list
'''
list_of_ages=[]
info={"first name": "Bob", "second name": "Mark", "age": 56}
age=info["age"]
list_of_ages.append(age)
print(list_of_ages)
'''
Assign a dictionary item's value to a variable
using a key that's a string. Then create a
dictionary that contains only that value.
'''
dict={"name": "Bob", "last name": "Mark", "address": "Parkinson Street"}
value=dict["name"]
new_dict={"my_name": value}
print(new_dict)
'''
Targeting the second item by its key, assign the
second item's value to a variable and display it.
'''
relatives ={"father": "Bob", "mother": "Lucy", "sister": "Rose",}
a_relative = relatives["mother"]
print(a_relative)
# In a single line of code,target the third item and display its value. 
states = {1: "goa", 2: "assam", 3: "sikkim", 4: "kerala"}
print(states[3])
