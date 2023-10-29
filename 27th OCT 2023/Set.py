#Set-  Set is an unordered collection of data types that is iterable, immutable and has no duplicate elements.
# Creating a Set with a List of Numbers
# Creating a Set
# Adding element and tuple to the Set.
# Access Set
# Removing elements from Set.
# Deletion of elements in a Set.
#Frozen sets
#Python frozen sets are immutable and have methods/operators that don't modify the set.
#Union
#Intersection.
#Diff, SubSet

#initial blank set
set1=set()
print(set1)

set2=set("priya")
print(set2)

set3 = {1, 1,2, 2,3, 4, 5, 5, 4}
print(set3)
print(type(set3))

#set3[1]=3
#print(set3) error-set is immutable in nature

set4=set([1,2,3,4,5,66,3,4,5])
print(set4)