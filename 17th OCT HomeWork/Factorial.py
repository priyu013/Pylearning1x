number= int(input("enter number: \n"))
if number <0:
    print("factorial not possible \n")
else:
    fact = 1
    for i in range(1, number+1):
        fact = fact*i
print("fact is " , fact)