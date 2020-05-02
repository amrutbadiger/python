
gnum = 200

def  add_nums(num1, num2, *others):
    print(others, type(others))
    print(others[0])
    num = 100
    result = gnum + num + num1 + num2

    return result

def print_range(num):
    for i in range(num):
        print(i, "-->", i*i, i*i*i)
    print("=====")


res1 = add_nums(2,3, 33,44,5)
print(res1)

res2 = add_nums(1000, 3245)
print(res2)

print_range(5)
print_range(3)
