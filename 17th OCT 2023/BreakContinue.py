# break

"""counter = 1
while counter <= 10:
    print(counter)
    if counter >= 5:
        break
        counter = counter + 1"""

#continue
for counter in range(1, 10):
    if counter == 5:
        break
    print(counter)
print("For loop is finished")
