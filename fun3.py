
'''
Code a function that has two parameters, both of them numbers.
Assign a default value to each parameter. The function does an
arithmetic operation using the two numbers and displays the result.
Call the function without passing arguments.
'''
def divider(first_num=100,second_num=2):
  result=first_num/second_num
  print(result)
divider()

products = ["mugs", "buckets", "chairs", "clips"]
qtys = [12, 48, 60, 144]
def show_level(first_list = products, second_list = qtys, first_index = 0, second_index = 0):
  product = first_list[first_index]
  qty = str(second_list[second_index])
  info_to_show = product + ": " + qty
  print (info_to_show)
show_level()
show_level(first_index=3,second_index=3)# revising the fun call to display another value.

def full_name(last_name="Singh", first_name="Raj"):
    assemble_name=first_name + " " + last_name
    print(assemble_name)
full_name()
full_name(first_name="Ajay")# assigning a default value to a parameter.
    
