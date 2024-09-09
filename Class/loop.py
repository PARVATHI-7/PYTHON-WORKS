# 4/7/24

# digit ne extract cheyan vendi => digit=num%10
# digit ne seperate akan vendi => num=num//10


# print multiplication table for a number
# number=2
# 1*2=2,2*2=4.......10*2=20
# num=2
# for i in range(1,9):
#     print(f"{i}*{num}={i*num}")


# wap to find factorial for a number
# eg:4!=1x2x3x4
 
# num=int(input("enter a number:"))
# factor=1
# for i in range(1,num+1):
#     factor=factor*i
# print(f"{factor}")

# power range:
# 2=>24[2+22]
# 3=>369[3+33+333]
# 4=>4936[4+44+444+4444]

# number=int(input("enter a number:"))
# pattern=0
# for i in range(1,number+1):
#     pattern=pattern*10+number
#     print(pattern)


# write a program to check the given number is palindrome or not
# 121 is a palnindromic number,123 is not a palindromic number
# num=int(input("enter a number:"))
# result=0
# while (num!=0):
#     digit=num%10
#     result=result*10+digit
#     num=num//10
# print(f" it is a palindrome {result}")

# this prgm shows both palindrome and not palindrome
# num=int(input("enter a number:"))
# result=0
# original =num
# while(num!=0):
#     digit=num%10
#     result=result*10+digit
#     num=num//10
# print("palindrome" if result==original else "it is not palindrome")

# powerranger
# num=int(input("enter a number:"))
# pattern=0
# for i in range(1,num+1):
#     pattern=pattern*10+num
#     print(pattern)

# prime number = chela numbers use cheyth divide cheythal 0 verila agnathe numbersann prime number
# 7 => 1,7 [2,3,4,5,6 vech 7 ne divide cheyan pattila so it s a prime number]
# 9 => 1,9 [2,,3,4,5,6,7,8]
# 11 => 1,11 [numbers vech competely divisible  alla]
# if a number need to be prime number it should be divisible by 1 and that particular number
# if n is a prime number then (1,n)  =>2,,,,,,, n-1

# num=7 #loop will works from 2,3,4,5,6
# isPrime= True # assume it is a prime number
# for i in range(2,num): #eg: 16 
#     if num % i==0: #16 %2=0 ,so we finds the answer we dont have to move forward
#         isPrime=False # so this will helps to show the anwerr and break helps to stop it 
#         break # used to stop the execution]

# # print(" isPrime " if  isPrime ==True else "not prime")
# if isPrime==True:
#     print("its a prime number")
# else:
#     print("its not a prime number")

# HCF -highest common factor
# (12,16) - 1, 2,4 - 4 is the hcf
# (18,24) - 1,2,3,6 -6 is hcf
# GCD - greatest common divisor
# (12,24) -  1,2,3,4,6,12 -12

# write a program to find gcd of 2 numbers
# num1=int(input("enter a number 1: ")) 
# num2=int(input("enter a number 2: "))
# gcd=1
# for i in range(1,num1+1):
#     if num1%i==0 and num2%i==0:
#         gcd=i
# print(gcd)



