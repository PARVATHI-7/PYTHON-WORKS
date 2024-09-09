# how to check the given number is armstrong number
# 153:1^3+5^3+3^3=153 #then the answer and exponential sum are equal ,so it is an armstrong value
# this idea will properly works on 3 digit number
# 1634:1^3+6^3+3^3+4^3=1634

num=int(input("enter a number:"))
total=0
digit_count=len(str(num))
while(num!=0):
    digit=num%10
    exponent=digit**digit_count
    total=total+exponent
    num=num//10
print(total)