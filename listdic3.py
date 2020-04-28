# to get information from a list within a dictionary.
specs ={
    "colors":["green", "blue", "yellow", "purple"],
}
if "blue" in specs["colors"]:
    print("0k")
if "orange" in specs["colors"]:
    print("yes")
else:
    print("no")

if "black" in specs["colors"]:
    print("first")
elif "purple" in specs["colors"]:
    print("second")
etails = {
  "nickname": "Mick",
  "married": "yes",
  "careers": ["firefighter", "mathematician", "rock star"],
}
'''
Test whether a particular career is in the list.
If so, display "yes". If not, display "no".
'''

details = {
  "nickname": "Mick",
  "married": "yes",
  "careers": ["firefighter", "mathematician", "rock star"],
}
if "engineer" in details["careers"]:
    print("yes")
else:
    print("no")

# If he is married and has "rock star" in his career list, display "perfect".
if details["married"]=="yes" and "rock star" in details["careers"]:
    print("perfect")

