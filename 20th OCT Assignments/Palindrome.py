# Task #1
# Palindrome Checker:
# Create a function that checks if a given string is a palindrome (reads the same forwards and backward).
# 121

"""def reverse_string(input_string):
    reverse_str = ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str

    original_str = "naman"
    rev_str = reverse_string(original_str)
    print(rev_str)

    if original_str == rev_str:
         print("Palindrome")
    else:
         print("Not a Palindrome")"""

def reverse_string(input_string):
    reverse_str = ""
    for c in input_string:
        reverse_str = c + reverse_str
    return reverse_str


original_str = "NAMAN"
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
    print("Palindrome")
else:
    print("It is not")
