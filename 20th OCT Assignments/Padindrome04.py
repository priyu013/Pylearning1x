original_str = "Priyanka"

def rev_string(original_str):
    return ''.join(reversed(original_str))

rev_str = rev_string(original_str)
print(rev_str)

if original_str==rev_str:
    print("palindrome")
else:
    print("not a palindrome")
