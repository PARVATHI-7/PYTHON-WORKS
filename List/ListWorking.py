# class list - in python it represents all in form of list 
# collections :

#  1)   def append()-used to add a new member to a list,then 
#       the added element will be always at the end of the list 

# num=[1,2,3,4]  # add element to a list #num is the name of class - list
# num.append(5)
# print(num)

#  2)   def insert()-used to add an element,and it can be done at any location 
#       ie,not at the end of the list 
#       syntax:num.insert(index,num to be inserted) [index starts from 0,1,2,3......]

# num=[1,2,3,4]
# num.insert(1,6)
# print(num)

#  3)   def count()-to check how many times an element is used in the list
#       allows duplicates

# num=[1,2,2,3,4,2,5]
# print(num.count(2))


#  4)   def pop()- this function will remove the last element of the list and returns it

# num=[1,2,3,4]
# print(num.pop()) and also it can be remove by provideing index
# print(num.pop(2))

#  5)   def remove()-here element will be removed and then the list is returned
#       list.remove(element),removes the first occurent element that is present on the list.

# num=[1,2,2,3,4]
# num.remove(2)
# print(num)

#  6)def.extend()-need to add more than 2 elements to a list

# num=[1,2,3,4,5]
# num.extend([6,8,9,10])
# print(num)

