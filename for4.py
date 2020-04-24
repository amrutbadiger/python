'''
Code nested for loops. When the outer tuple element is 4
and the inner tuple element is "b" display "ok"
'''
nums=(1, 2, 3, 4, 5, 6, 7,)
strings=("a", "b","c", "d", "e")
for a_number in nums:
    for a_str in strings:
        if a_number == 6 and a_str =="e":
            print("ok")
