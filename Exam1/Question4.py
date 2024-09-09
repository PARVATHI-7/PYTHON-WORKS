# write a program to print sum of digit
# sample  input=5234=>5+2+3+4
# sample  input=1334=>1+3+3+4
# sample  input=1213=>2+3
# note:do not consider one when you count the sum of digits

number=int(input("enter a number:"))
sum=0
while(number!=0):
    digit = num%10
    if(digit!=1):
        sum = sum+digit
    number= number//10
print(sum)

print(f"sum of digit is={sum}")