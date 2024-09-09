# 2=>24[2+22]
# 3=>369[3+33+333]
# 4=>4936[4+44+444+4444]


number=int(input("enter a number:"))
pattern=0
for i in range(1,number+1): #1=1,2,3
    pattern= pattern*10+number #pattern = 0*10+3=3*10+3=33
    print(pattern)#3 33 333


#  write a prgm to check the number is palindrome
# 121 is a palindromic number
# 123 is not a palnindromic number