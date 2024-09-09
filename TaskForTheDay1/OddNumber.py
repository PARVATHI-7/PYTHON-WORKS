#  write a program to print all the odd number from 1 to 100
start=int(input("enter the starting value:"))
end=int(input("enter the ending value:"))
while(start<=end):
    if(start%2 !=0):
        print(start)
    start=start+1


