# Using function as variables.
'''
In a single line display the result returned by the first
function divided bythe result returned bythe second function.
Provide two numbers as positionalarguments for each function.
'''
def divide_numbers(first_number, second_number):
  return first_number / second_number
def calc_leftover(first_number, second_number):
  return first_number % second_number
print(divide_numbers(20,5)/calc_leftover(5,3))
'''
Call the function, providing three positional arguments. The first argument is
the name of the list,The second argument is the the index number of the element
to increment. The third argument is a math expression,Display the changed element.
'''
list_of_numbers = [12, 24, 36]
def increment_list_element(list_name, index_of_element, how_much_to_add):
  list_name[index_of_element] += how_much_to_add
increment_list_element(list_of_numbers,0,9/3)
print(list_of_numbers[0])
