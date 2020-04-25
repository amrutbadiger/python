# looping through values and displayin each of them.
bikes={1: "hero", 2: "honda", 3: "tvs", 4: "yamaha"}
for a_bike in bikes.values():
    print(a_bike)
'''
looping through the values of a dictionary ,
test if any value is less than 8 if so,
display "ok" and break the loop.
'''
dict={"a": 34, "b": 23, "c": 45, "d": 7, "e": 33}
for a_value in dict.values():
    if a_value<8:
        print("ok")
        break
'''
Looping through the values in a dictionary,
test if any of the values is equal to "arsenic".
If so, append the value to the poisons list  and break the loop.
'''
poisons=["methane", "gasoline", "petrol"]
acids={1: "citric", 2: "nitric", 3: "sulphur", 4: "arsenic"}
for a_acid in acids.values():
    if a_acid == "arsenic":
        poisons.append(a_acid)
        break
print(poisons)

        
