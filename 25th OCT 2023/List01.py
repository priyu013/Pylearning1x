#List-collection of diffrent datatypes

my_list=[1,2,3,4,5]
my_list2=[1,True, "hello", 3.3]
print("Initial list: ", my_list)
print("Initial list: ", my_list2)

#indexing
print("Elemnet at index 0 of my_list:", my_list[0])
print("Elemnet at index 1 of my_list2:", my_list2[1])

#Changing element
my_list[1]=20
print("List after changing element at index 1:" , my_list)

#append()-I will add data at the end of list
my_list.append(4)
print("list after appendng 4:", my_list)

#extend()- add all the item of list to another list
my_list.extend([5,6])
print("my list after extending", my_list)

#insert()-Insert an item at specific positon in the list
my_list.insert(1,20)
print("list after inserting the item:", my_list)

#remove()-remove the first occurence of specific item
my_list.remove(4)
print("List after removing the item:", my_list)

#copy()-
my_copy_list=my_list.copy()
print(my_copy_list)

#clear()-remove all the item from the list
my_list.clear()
print("intial list:", my_list)

#sort()- sort the item in the list in ascending order
my_copy_list.sort()
print(my_copy_list)

#reverse()- reverse the order of the item in the list
my_copy_list.reverse()
print(my_copy_list)
#count()-return the no of times a specific item appears in thr list
my_copy_list.count(4)
print(my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])


print(len(my_copy_list))

my_list = my_copy_list.copy()
print(my_list.remove(4))