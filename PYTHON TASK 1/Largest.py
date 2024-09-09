# write a program to determine largest of three numbers
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if num1>num2 and num1>num3:
    print("Num1 is the largest number")
elif num2>num3:
    print("Num2 is the largest")
else:
    print("Num3 is the largest")
