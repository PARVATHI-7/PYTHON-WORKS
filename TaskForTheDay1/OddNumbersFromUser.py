# read start_limit and end_limit from the user and print all the odd numbers from the start_limit and end_limit
start_limit=int(input("enter the starting value:"))
end_limit=int(input("enter the ending value:"))
while(start_limit<=end_limit):
    if(start_limit%2 !=0):
        print(start_limit)
    start_limit=start_limit+1