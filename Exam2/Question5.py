# given a list
# Numbers=[10,10,20,20,20,21,22,23]
# a)print count of each number

numbers=[10,10,20,20,20,21,22,23]
original=numbers.copy()
list=[]
for i in numbers:
   count=numbers.count(i)
   print(f" {i}={count}")
   while numbers.count(1)>1:
      numbers.remove (i)
for j in original:
    if original.count(j)==1:
        list.append(j)
print(f"list of non repeaing numbers={list})")


