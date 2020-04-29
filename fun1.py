# passing information to the function.
def color_check(primary_colors, color_to_check):
  for a_primary_color in primary_colors:
    if color_to_check==a_primary_color:
      print("It's a primary color.")
      break
# Ask the user to enter a color. Assign it to a variable.
color_entered=input("Enter a color: ")
# Here's the tuple:
primary_colors = ("yellow", "red", "blue")
'''
Call the function, passing the tuple name and the variable
containing the user's color choice.(primary_colors, color_entered)
'''
color_check(primary_colors, color_entered)
'''
Code a function that has two parameters. If the
values of the two arguments are the same, display "same"
'''
x=24
y=24
def compare(x,y):
    if x==y:
        print("same")
compare(x,y)
'''
call the function, passing the variables sales_total and tax_rate as arguments.
Code the function. It calculates the tax on a sales total and displays a message.
The function's two parameters are the total and the tax rate.
Calculate the tax by multiplying the two parameters.
Convert the result of the multiplication to a string.
Display the concatenation of "The tax is " and the tax string.
'''
def cal_tax(total,rate):
  tax = total*rate
  tax_as_string=str(tax)
  print("The tax is "+tax_as_string)
sales_total = 100
tax_rate = .03
cal_tax(sales_total, tax_rate)
