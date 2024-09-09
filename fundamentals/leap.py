# write a program to check whether year is leap year or not

year=int(input("enter the year:"))
if(year%4==0):
    print("it is a leap year")
else:
    print("is not leap year")



# this program will break in case of century year

year=int(input("enter year:"))
if(year%100==0 and year%400==0) or (year%100!=0 and year%400 !=0):
    print(f"{year} is leap year")

else:
    print(f"{year} not a leap year")