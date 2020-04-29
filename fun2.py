# another way to pass information .
def names_of_couples(husband_name,wife_name):
    print("The names of the couples are "+ husband_name +" " + "and "+ wife_name)
names_of_couples(husband_name="Raj",wife_name="Sanjana")
'''
Code a function that has two keyword parameters,
first_name and last_name.The function displays the
concatenation of first_name plus a string that's just a space plus last_name.
Call the function, assigning your first and last names to the keywords.
'''
def full_name(first_name,last_name):
  print(first_name+" "+last_name)
full_name(first_name="Raj",last_name="Singh")
'''
Code the function It targets the element within the
list within the dictionary. Then it displays the targeted name.
'''
def call(dictionary,list_name,index_no):
  target=(dictionary[list_name][index_no])
  print(target)
members = {
  "adults": ["Rakesh", "Sanjay", "Sunil"],
  "children": ["Pappu","Raju", "Sandy"],
}
# First code the function call on line 12.
call(members,"children",1)
