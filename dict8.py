# looping through key-value pairs.
dict={"a": 1, "b": 2, "c": 3, 4: "d"}
for a, b in dict.items():
    print(a) # to display the keys.
# to display the values.
dict={"ram":23, "bob": 24, 56: "sid", 78: "ok"}
for a,b in dict.items():
    print(b)
'''
Loop through the keys and values of a dictionary.
If you find an item that has the same key and value,
display "weird" and break the loop.
'''
x={12: "two", 45: "four", 34: "three", 55: 55}
for y,z in x.items():
    if y==z:
        print("weird")
        break
'''
Loop through the dict for both keys and values.
Display both of them with a message written .
'''
nums={"one": "ek", "two": "do", "three": "teen", "four": "char"}
for english, hindi in nums.items():
    print("The Hindi word for "+ english+" "+"is "+hindi)
    
