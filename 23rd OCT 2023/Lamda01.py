#def sayHello():
    #print("hello")

#sayHello()

#def funWithPara(a):
 #   return a**2
#output=funWithPara(2)
#print(output)

#Lamda Expression
#def doubleOfMe(value):
#return value*2


#output = lambda value:value*2
#print(output(2))

def sayHello(name):
    print("Your name is", name)
    sayHello=lambda name: print("hi my name is" , name)
    sayHello("priyanka")
