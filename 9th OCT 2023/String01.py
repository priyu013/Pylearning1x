#string= Bunch of character
name = "Priyanka"
name = "priya"
print(name)

#Python strings are immutable in nature, it can't change once created.
#for eg: name[0]="K" It will give error that 'str' object does not support item assignment
#String_functions

#Capitalization Stringfunction- Return copy of string with its first character capitalised.

result= name.capitalize()
print(result)
print(name)

#ID stringFunction- indenty of data or adress reference
print(id(name))
print(id(result))

#Uppercase StringFunction-Resurns all character in Upper case
result2=name.upper()
print(result2)

#Lowercase String Function- Return all charactor in lower case
result3 = name.lower()
print(result3)

# Swapcase() string Functions- eturns a copy of the string with uppercase characters converted to lowercase and vice versa.
name= "PriyaAnk"
print(name.swapcase())

#Title StringFunctions- returns the titlecase version of string, where 1st letter of word would be capital and or sentance
name="hello Priya"
print(name.title())

#Replace String function
text="Hello Bata"
result_rep = text.replace("Bata","priya")
print(result_rep)

#find stringFunctions-Resturns the lowest string of substring in he string
#return -1 if the substring not found

text="hello world"
index= text.find("world")
print(index)
#count() - count the char -
count = text.count("l")
print(count)


#index and len
name  = "Priyanka"
# len -> 1
print(len(name))
# index - 0 to len-1
# p - 0, r - 1, a - 2, m - 3 , 0-4, d -5