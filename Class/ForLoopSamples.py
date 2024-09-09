# 8/7/24

#  fibonacci series- previous no + current no
# 0 1 1 2 3 5 8 13 21 34 55................

# previous=0
# current=1
# print(f"{previous},{current}",end=" , ")
# for i in range(1,11):
#     next=previous+current
#     previous=current
#     current=next 
#     print(next,end=" , ")

#  read a number and check whether it is fibonacci number or not
# num=int(input("enter a number:"))
# previous=0
# current=1
# isFibo=False #just set cheyth vekya,ithine ann flag set cheyya enn parayunath
# next=previous+current
# while next<=num:
#     next=previous+current
#     previous=current
#     current =next
#     if(next==num): #kodutha numberum nextum same anki fibo ann so true
#         isFibo=True
#         break #anki pinne munnote povenda so break
# print(isFibo)


# print next fibonacci number

number=int(input("enter a number"))
previous=0
current=1
next=previous+current




   