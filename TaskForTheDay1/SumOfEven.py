# write a program to print sum of all even numbers from 1 to 100

start=int(input("enter the starting value:"))
end=int(input("enter the ending value:"))
sum=0
while(start<=end):
    if(start%2==0):
        sum=sum+start
    start=start+1
print(sum)