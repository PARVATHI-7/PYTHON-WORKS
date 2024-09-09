# prime numbers = 7(1,7) [2,3,4,5,6]
# 9 is not a prime number (1,9)=>2,3,4,5,6,7,8

# n(1,n)=>2,,,,,,,n-1

num=16 #2,3,4,5,6,7,8,,,,,,,,,,15
isPrime=True
for i in range(2,num):
    if num%i==0:
        isPrime=False
        break

print("isPrime" if isPrime==True else "not prime")
# or
# print(f"{number} is prime" if isPrime==True else f"{number} not prime )

# HCD OR GCD(12,16) 1,2,4
# HCF of(18,24) #1,2,3,6........