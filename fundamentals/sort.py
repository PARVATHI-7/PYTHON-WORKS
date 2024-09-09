# read three numbers from the user num1,num2,num3
# print these three numbers in sorted order

# program
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if(num1<=num2<=num3):
    sorted_numbers=[num1,num2,num3]
elif(num1<=num3<=num2):
    sorted_numbers=[num1,num3,num2]
elif(num2<=num1<=num3):
    sorted_numbers=[num2,num1,num3]
elif(num2<=num3<=num1):
    sorted_numbers=[num2,num3,num1]
elif(num3<=num1<=num2):
    sorted_numbers=[num3,num1,num2]
else:
    sorted_numbers=[num3,num2,num1]

    
print("the numbers in sorted order are:",sorted_numbers)




    
