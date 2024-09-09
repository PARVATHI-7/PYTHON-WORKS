# 9/7/24

# functions-are created to do specific task
# syntax
# def function_name(para1,para2....param):
#           function defintion
#           return value

# def is_leap_year(year):
#     if year%100==0 and year%400==0 or year%100 !=0 and year%400!=0:
#         return True
#     else:
#         return False 
# print(is_leap_year(2024))

# create a function nth_digit_max with 2 parameter num1 and num2
# (123,480) => 123 ,last digit compare cheythit ann o/p verandath,bcoz 3,0 veluth 3 ann so 123

# def nth_digit(num1,num2):
#     num1_last_digit=num1%10
#     num2_last_digit=num2%10
#     if num1_last_digit>num2_last_digit:
#         return num1
#     else:
#         return num2 
# print(nth_digit(123,480)) 

# functions:
# def print()
# def input()
# def sorted()
# def sum()
# def min()
# def max()


# string-sequence of characters
# it is handled as class
# the below given are methids and which are given a class
# class str:
#      def capitalize()

# object_name=className()

# lion_obj=Lion()
# lion_obj.roar()

# duck_obj=Duck()
# duck_obj.quack()

# word="hello"
#       01234    #index
# print(word.index("e"))  #1  #always result the first occurence
# # print(word.capitalize())   #Hello
# print(word.upper())  #hello
# print(word.casefold())  #
# print(word.lower()) #hello
# print(word.isalpha()) #to check the given the alphabet or not if it is ,then result True else False
# print(word.isalpha())
# print(word.isdigit())
# print(word.isnum ())

# word="i have 2 bike and 1 car"
# print alphabets
# for ch in word:
#     if ch.isalpha():
#         print(ch ,end=" ")

# for digits
word="i have 2 bike and 1 car"
for ch in word:
    if ch.isdigit():
        print(ch,end=" ")

