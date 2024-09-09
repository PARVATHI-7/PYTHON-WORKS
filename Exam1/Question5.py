# write a program to print sum of digit
# sample  input=462=>4+6=10
# sample  input=476=>4+6=10
# note:do not consider prime numbers when you count the sum of digits

number = int(input("enter the  number:"))
sum = 0
for i in range(2,number):
    digit = number%10
    if(digit%i!=0):
        sum = sum+digit
    number = number//10
print(sum)

