# read a number and extract digits from number
num=int(input("enter number:"))
while(num!=0):
    digit=num%10
    print(digit)
    num=num//10

# logic
# eg:523
# digit=num%10   #3
# print(digit)
# num=num//10 
# digit=num%10   #2
# print(digit)
# num=num//10
# digit=num%10   #5
# print(digit)
# num=num//10     #0
