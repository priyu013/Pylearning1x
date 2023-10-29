tuple03 = tuple(["priya", "k"])
print(tuple03)
print(tuple03[0])
print(tuple03[1])

# Convert tuple to List
my_tuple=(1,23,4,5)
print(list(my_tuple))

# Merging Tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)


x = 10
a, b = 23, 34  # This is multiple value assign
q, w, e = (45, 56, 78)  # tuple assigned to multiple variables
print(q)
print(w)
print(e)

#Nested tuple

Hero1=("Salman","Shahrukh", "Ranbir")
Hero2=("Akshay","Vicky","Ranveer")
Team=(Hero1,Hero2)
print(Team)
print(len(Team))
print(Team[0])
print(Team[1])
print(Team[0][0])
print(Team[1][2])

#search in Tuple
cities=("lko","delhi","mumbai","Up")
print("delhi" in cities)
print("mp" in cities)