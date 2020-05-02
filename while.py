# coding a while loop.
'''
Code a while loop. As long as x is less
than or equal to 10, display x then add 2 to it.
'''
x = 0
while x<=10:
  print(x)
  x+=2
'''
As long as the counter is less than the length of list_of_names,append an element
of list_of_names to second_list_of_names.Then increment the counter. (Use the counter
as the index ofeach element as you loop through list_of_names.)Display second_list_of_names.
'''
list_of_names=["Ajay", "Raj", "Jay", "Dev", "Sid", "Bob"]
second_list_of_names=[]
counter=0
while counter<len(list_of_names):
    second_list_of_names.append(list_of_names[counter])
    counter+=1
print(second_list_of_names)
