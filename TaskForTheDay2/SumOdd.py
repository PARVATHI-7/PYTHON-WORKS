# write a program using for loop to print sum of all odd numbers from 1 to 100

start=1
end=101
sum=0
for odd in range(start,end):
    if odd%2 !=0:
        sum=sum+odd
print(sum)