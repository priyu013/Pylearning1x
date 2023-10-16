"""1.Write a Python program to calculate the area of a circle given its radius using the formula
area=π×r^2 ( Take pie as 3.140)"""
import math
radius= float(input("enter the radius: \n"))
#area= 3.14*radius*radius
area= math.pi*radius*radius

print(area)

#2.Create a program that takes two numbers as input and prints
#whether the first number is greater than, less than, or equal to the second number.

num1=input("enter first number\n")
num2=input("enter second number\n")
result= "greater than" if num1>num2 else"less than" if num1<num2 else "equal to"
print(f"{num1} is {result} {num2}")

#3.Use the ternary operator to find the maximum of three numbers entered by the user.
num1=input("enter first number\n")
num2=input("enter second number\n")
num3=input("enter third number\n")

max_num= num1 if (num1>num2) and (num1>num3) else(num2 if num2>num3 else num3)
print(f" the maximux of {num1},{num2} and {num3} is : {max_num}")

#4.Develop a Python script that calculates the square and cube of a given number.
number=int(input("Enter the number\n"))
square=number**2
print(square)
cube=number**3
print(cube)