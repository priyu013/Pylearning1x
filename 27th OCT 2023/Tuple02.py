#my_list
my_list=[1,2,3,4,5]
print(my_list)
my_list[2]=76
print(my_list)#means list is mutable-can change the data of list

#Tuple-It is immutable in nature means can not change the its data after creation

car=("hero", "honda", "jeep")
print(car)
#car[2]="scorpio" can not be changed data of tuple
#print(car)
print(len(car))

tuple01=(1,2,3,3,"priyanka")
print(tuple01)

#list can be converted to tuple
list1=[2,3,4,56,6]
tuple02=tuple(list1)
print(tuple02)