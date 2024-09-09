# read a number print sum of digit
# digit = 543
# output:5+4+3=12

num=int(input("enter a number:"))
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit
    num=num//10

print(sum)