num=20
def multiply_by_10(n):
    n*= 10
    num = n
    print("value of num inside the function", num)
    return n
op= multiply_by_10(num)
print(op)
print("value of num outside of function", num)
