'''
Assign different Booleans to two variables.Assign 0 to a third variable.
As long as the two Boolean variables have different values, increment the third
variable by 1 and make the first Boolean variable equal to the second Boolean variable.
Display the third variable.
'''
first_flag=True
second_flag=False
number=0
while first_flag!=second_flag:
  number+=1
  first_flag=second_flag
print(number)
# Loop through the dictionary. When a value is True, display its key.
dict = {1: True, 4: True, 10: True, 100: False, 200: True}
for key, values in dict.items():
  if values==True:
    print(key)
