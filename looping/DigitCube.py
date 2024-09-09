# read a program to extract sum of cube of each digit
# digit=543
# how it works=5^3+4^3+3^3

num=int(input("enter a number:"))
sum=0
while(num!=0):
    digit=num%10
    exponent=digit**3
    sum=sum+exponent
    num=num//10

print(sum)