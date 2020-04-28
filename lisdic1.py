# To append a new dictionary to a list of dictionaries.
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
print(customers)
a = len(customers)
b = "Ajay"
c = "Singh"
new_dict={
    "cust_id": a,
    "first_name": b,
    "last_name": c,
}
customers.append(new_dict)
print(customers)

    
