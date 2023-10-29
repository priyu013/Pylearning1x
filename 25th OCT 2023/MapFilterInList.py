sq= lambda x: x*x
result= sq(5)
print(result)

#Map function where we will go from item and apply a function
number=[1,2,3,4,5]
#sq_number= [1,2,3,4,5]
sq_number = []

for i in number:
    sq_number.append(sq(i))
print(sq_number)

#Map Function

sq_number2= list(map(lambda x:x*x, number))
print(sq_number2)

sq_number3= list(map(lambda x:x*4, number))
print(sq_number3)

def triple(a):
    return a*3
sq3=list(map(triple,number))
print(sq3)
