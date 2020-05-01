# Mixing positional and keyword arguements.
'''
Code a function with two parameters that have defaults.
The function displays the parameters on separate lines.
Call the function, overriding both defaults.
'''
def greeting(first_value="Hi", second_value="Raj"):
  print(first_value)
  print(second_value)
greeting(first_value="Hello", second_value="Jay")
'''
Code a function that does a math operation on two parameters and
displays the result.Call the function. The first argument is a
positional argument. The second argument is a keyword argument.
'''
def area(length, breadth=10):
  result=length*breadth
  print(result)
area(24,breadth=10)
# To find and display a value of a dictionary by passing an arguement.
customers={
    0: {
        "first name": "Jay",
        "second name": "Dev",
        "address": "Whitefield",
    },
    1: {
        "first name": "Raj",
        "second name": "Roy",
        "address": "Khade Bazar",
    },
    2: {
        "first name": "Sid",
        "second name": "Jack",
        "address": "Lamington Rd.",
    },
}
def find_data(dict, inner_dict, target):
    print(dict[inner_dict][target])
find_data(customers,2,"address")
        
