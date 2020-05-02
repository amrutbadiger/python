# passing information back from them.
'''
Code a function that performs a calculation on its two parameters and passes the result back
Call the function, passing two positional arguments that are integers.
Display the result produced by the function call.
'''
def calc(first_num, second_num):
  return first_num/second_num
print(calc(100,5))
'''
Code a function that will change one of the values in the dict.
The function has three parameters—the name of a dict, a dict key,
and a dict value. The function uses these parameters to change one of the
values in the dict. Then it returns the revised dict.
Call the function, providing three keyword arguments—Display the new dict.
'''
creatures = {
  "cat": "meow",
  "dog": "bow-wow",
  "lion": "glug",
}
def change_sound(dict,animal,sound):
  dict[animal]=sound
  return dict
revised_dict=change_sound(dict=creatures,animal="lion",sound="roar")
print(revised_dict)
