# Task #2
# Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.

# n = 12345
# sum = 15
#user_input=int(input("Enter Digit"))
"""Digit=12345
mod1=Digit%10
print(mod1)
Digit=1234
mod2=Digit%10
print(mod2)
Digit=123
mod3=Digit%10
print(mod3)
Digit=12
mod4=Digit%10
print(mod4)
Digit=1
mod5=Digit%10
print(mod5)
sum=mod1+mod2+mod3+mod4+mod5
print("sum of 12345 is:-", sum)"""

num=int(input("Enter Digit\n"))
sum=0
while num!=0:
    digit= num%10
    sum=sum+digit
    num=int(num/10)
print(sum)
