# fibonacci series
# 0 1   1 2 3 5 8 13 21

# previous=0
# current=1
# print(f"{previous},{current}",end=", ")
# for i in range(1,11):
#     next=previous+current
#     print(f"{next}",end=",")
#     previous=current
    
#     current=next


# read a number and print it is fibonacci or not
# int=34

num=int(input("enter a number:"))
previous=0
current=1
isFibo=False
next=previous+current
while(next<=num):
    next=previous+current
    previous=current
    current=next
    if next ==num:
        isFibo=True
        break
print(isFibo)