# write a program for a simple calculator
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("choose the options \n 1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Divsion\n")
choice=int(input("enter your choice:"))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
else:
    print(num1/num2)