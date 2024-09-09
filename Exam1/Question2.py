# write a program to print the given number is prime or not
number=int(input("enter a number:"))
prime=True
for i in range(2,number):
    if number%i==0:
        prime=False
        break

print("the given number is prime" if prime==True else "the given number is not prime")
