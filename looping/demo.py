# write a program to print multiplication table of 2
# read from user
start=int(input("enter the starting number:"))
end=int(input("enter the ending number:"))
while(start<=end):
    if start%2==0:
        print(start)
    start=start+1
