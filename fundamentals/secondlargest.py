# read three numbers from the user num1,num2,num3
# print the second largest number from the three numbers

# program
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if (num1 >= num2 and num1 <= num3) or (num1 >= num3 and num1 <= num2):
    print(num1,"is the second largest")
elif (num2 >= num1 and num2 <= num3) or (num2 >= num3 and num2 <= num1):
    print(num2,"is the second largest")
else:
    print(num3,"is the second largest")



#  same program with diff logic
# num1=int(input("enter the first number:"))
# num2=int(input("enter the second number:"))
# num3=int(input("enter the third number:"))
#  if num1>num2 and num1>num3:
#     if num2>num3:
#         print(num1,num2,num3)
#     else:
#         print(num1,num3,num2)
# elif num2>num1 and num2>num3:
#     if num1>num3:
#         print(num2,num1,num3)
#     else:
#         print(num2,num3,num1)
# elif num3>num1 and num3>num1:
#     if num1>num2:
#         print(num3,num1,num2)
#     else:
#         print(num3,num2,num1)



#  for getting num1 as second largest
#     # num2>num1>num3 or num3>num1>num2

# for getting num2 as second largest
#     # num1>num2>num3 or num1>num2>num1

# for getting num3 as second largest number
# num1>num3>num2 or num2>num3>num1