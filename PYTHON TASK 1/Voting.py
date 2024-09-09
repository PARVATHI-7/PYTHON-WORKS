# write a program to check if a person is eligible for voting or not
# conditions - age greater than or equal to 18 ,the person is eligible
#            - age less than 18 not eligible for voting
age=int(input("Enter the age:"))
print("eligible" if age>=18 else "not eligible")