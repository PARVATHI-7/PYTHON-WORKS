# - both for and while loop are using for iteration
# if we know the range ie from where we have to start and we have to end ,then use for loop
# if we dont know the range then use while loop

# functions:
# print(msg)
# input(msg)=str
# len(obj)=return length of the object
# type(obj)=return type of the object
# range(start,end,step) = for calling range function,we have to call start,end,step
# eg:range(1,100,1)  = returns a sequence from 1 ...... 100 in steps of 1,2,3,.....100
# if we need range from 1 to 50,then (1,50,1)
# range(2,11) #here step will be default and consider step=1



# 1...10
# sequence for getting the above sequence:range(1,11,1)
# sequence=range(1,11,1)
# for(num in sequence):
# print(num)

# # 50,100
# sequence=range(50,101,1)
# for num in sequence:
# print(num)

# # 2,4,6,8,10
# sequence=range(2,11,2)
# for num in sequence:
# print(num)


# # 10,9,8,7,6,5,4,3,2,1
# sequence=range(10,0,-1)
# for num in sequence:
# print(num)

# print 1 to 50 using for loop
# for i in range(1,51):
#     print(i)

# print 1 to 100 using for loop
# for i in range(1,101):
#     print(i)

# print years from 1800 to 2024 using for loop
# for i in range(1800,2025):
#     print(i)

# print leap years using for loop
# for i in  range(1800,2025):
#     if i%4==0:
#         print(i)

# print centuary years using for loop
# for i in range(1800,2025):
#     if i%100==0:
#         print(i)

# 3/7/2024

# read a number and extract digits from number
# sample input num1=123
# output = #3 #2 #1
# num=int(input("enter a number:"))
# while num!=0:
#     digit=num%10
#     print(digit)
#     num=num//10

# read a number and print sum of digits
# input = 543
# o/p=5+4+3=12

# num=int(input("enter a number:"))
# sum=0
# while num!=0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10
# print(sum)

# sum of cube of each digit

# num=int(input("enter a number:"))
# cube=0
# while num!=0:
#     digit=num%10   # this step is used to extract the digit
#     exponent=digit**3
#     cube=cube+exponent
#     num=num//10
# print(cube)

#Armstrong number - eg:153:1^3+5^3+3^3=153
                    # 6134=6^4+1^4+3^4+4^4
# if 5 digits or more digits are present the we have to 
# exponent the digit using the no.of digits present in the input
# for performing this task we can use len() fuction
#,so that there will be  no error while giving any i/p
# in this function we canot give number only string is possible

# eg:
# num=2345678910
# digit_count=len(num)
# print(digit_count)    # causes type error
# just convert this int into str as
# num=234567890
# digit_count=len(str(num))
# print(digit_count)  #o/p=9

# str="hello world"
# digit_count=len(str)
# print(digit_count)    # it will print hello world=11

# wap to check a give number is armstrong

# num=int(input("enter a number:"))
# original=num
# sum=0
# digit_count=len(str(num))
# while(num!=0):
#     digit=num%10
#     exponent=digit**digit_count
#     sum=sum+exponent
#     num=num//10
# print(sum)







