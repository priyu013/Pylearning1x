num1=int(input("Enter the First Number:"))
num2=int(input("Enter the First Number:"))
num3=int(input("Enter the First Number:"))
num4=int(input("Enter the First Number:"))
num5=int(input("Enter the First Number:"))
set1=set()
set1.add(num1)
set1.add(num2)
set1.add(num3)
set1.add(num4)
set1.add(num5)
print(set1)

#----OR-----
num1=int(input("Enter the First Number:"))
num2=int(input("Enter the First Number:"))
num3=int(input("Enter the First Number:"))
num4=int(input("Enter the First Number:"))
num5=int(input("Enter the First Number:"))
list1=list()
"""list1.append(num1)
list1.append(num2)
list1.append(num3)
list1.append(num4)
list1.append(num5)"""
list1.extend([num1,num2,num3,num4,num5])
list12=set(list1)
print(list12)