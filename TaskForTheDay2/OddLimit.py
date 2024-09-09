# read start_limit and end_limit from the user and using for loop print all the odd numbers from start_limit to end_limit.

start_limit=int(input("enter the starting number:"))
end_limit=int(input("enter the endding limit:"))
for i in range(start_limit,end_limit):
    if i%2 !=0:
        print(i)