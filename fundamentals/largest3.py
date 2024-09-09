# read three numbers from user num1,num2,num3
# print largest among the three numbers

# program
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))
if(num1>num2 and num1>num3):
    print(num1,"is the largest")
elif(num2>num3):
    print(num2,"is the largest")
else:
    print(num3,"is the largest")
