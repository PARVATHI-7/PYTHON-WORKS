# program to check number is palindrome

number=int(input("enter a number:"))
result=0
while(number!=0):
    digit=number%10
    result=result*10+digit
    number=number//10
print(result)
# or 

# print("palindrome" if result==original else "not palindrome")