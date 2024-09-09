# write a program for grade classification based on perecentage conditions
# percentage=90 ,grade A
# percentage between 80-90,grade B
# percentage between 70-80,grade C
# percentage less than 70 ,fail

percentage=int(input("enter the percentage:"))
if percentage>=90:
    print("Grade A")
elif percentage>=80 and percentage<=90:
    print("Grade B") 
elif percentage>=70 and percentage<=80:
    print("Grade C")
else:
    print("Fail")


