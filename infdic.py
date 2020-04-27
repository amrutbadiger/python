# to get information out of a list of dictionaries.Display it.
customers =[
    {
        "cust_id": 0,
        "first_name": "Jay",
        "last_name": "Dixit",
    },
    {
        "cust_id": 1,
        "first_name": "Raj",
        "last_name": "Dev",
    },
    {
        "cust_id": 2,
        "first_name": "Ram",
        "last_name": "Sinh",
    },
]
cust=customers[1]
print(cust)
'''
Target one of the dictionaries in the list, loading it into a variable.
Then target a value within that dictionary, loading it into another variable. Display the value.
'''
customers =[
    {
        "cust_id": 0,
        "first_name": "Jay",
        "last_name": "Dixit",
    },
    {
        "cust_id": 1,
        "first_name": "Raj",
        "last_name": "Dev",
    },
    {
        "cust_id": 2,
        "first_name": "Ram",
        "last_name": "Sinh",
    },
]
cust =customers[2]
cust_name=cust["first_name"]
print(cust_name)
