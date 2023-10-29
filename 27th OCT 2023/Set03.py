t=("TheTestingAcademy","for","TheTestingAcademy")
print("\nSet with the use of Tuple: ")
print(set(t))

set1={1,2,3,4,5}
set2={3,4,5,6,7,8}
set_union=set1.union(set2)
print(set_union)
set_intersection=set1.intersection(set2)
set_intersection=set2.intersection(set1)
print(set_intersection)
set_diffrence=set2.difference(set1)
print(set_diffrence)

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
subset = set2.issubset(set1)
print(subset)

set1=set(["Testing", "for", "Testing"])
print(set1)
