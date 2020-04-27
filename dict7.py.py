# loop thru the keys of a dict and display them.
dict={1: "jio", 2: "airtel", 3: "vodafone", 4: "idea"}
for a_dict in dict.keys():
    print(a_dict)
# loop thru the keys of a dict.append the value of each key to a list& display them.
alpha=[]
a ={"a": 1, "b": 2, "c": 3, "d": 4}
for b in a.keys():
    alpha.append(b)
    print(alpha)
# loop thru the keys if value of key is >=99 display ok and break the loop.
nums={23: "arm", 32: "waist", 22: "age", 99: "year", 31: "day"}
for a_num in nums.keys():
    if a_num >=99:
        print("ok")
        break
#loop thru the keys and display the values of the dict. store the keys in a variable
dict={1: "jio", 2: "airtel", 3: "vodafone", 4: "idea"}
for a_dict in dict.keys():
    print(dict[a_dict])
# loop thru a dict. Add each key-value pair in it to another dict and display it.
b={}
a ={"a": 1, "b": 2, "c": 3, "d": 4}
for c in a.keys():
    b[c]=a[c]
    print(b)

    
    
