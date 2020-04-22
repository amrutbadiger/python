'''
A code to display eliminating ambiguity.
ex.1 to force this order.1st mul 2 by 4, then mul the result by 4 & then add 2.
'''
a = ((2*4)*4)+2
b= (2*4)*(4+2) # to mul 2 by 4 then add 4 & 2 and then mul the 1st and 2nd res.
# ex2. div 5 by 7 then sub 1 from 4 and then mul 1st and 2nd res.
x=(5/7)*(4-1)
y=5/(7*(4-1)) # 1st sub 1 from 4 then div the red by 7 and then div 2nd res by 5.
z=((5/7)*4)-1 # div 5 by 7 then mul the res by 4 and then sub 1.
print(a)
print(b)
print(x)
print(y)
print(z)
