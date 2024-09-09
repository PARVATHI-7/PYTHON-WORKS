# 5/7/24  (nested loop)

# print("helo")
# print("world") # oru msg kazhint thazhye aduthath vera already ath /n or newline vech set cheythath ann

# print("hello",end=",") #ivede nammal specify cheyth koduthu end ngane venam enn
# print("world") #o/p => hello,world

# 1,2,3,4,5 ingane venam nammk print cheyan
# for i in range(1,6):
#     print(i,end=" ")

# patterns
# 1 2 3 4  #3 row ,4 col
# 1 2 3 4
# 1 2 3 4

# for row in range(1,4): # row need to work for 4 times
#     for col in range(1,5): # needs to work for 
#         print(col,end=" ")
#     print()


# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

# for row in range(1,4):
#     for col in range(1,5):
#         print(row,end=" ")
#     print()

# @ @ @ @ @
# @ @ @ @ @
# @ @ @ @ @
# @ @ @ @ @

# for row in range(1,5):
#     for col in range(1,6):
#         print("@",end =" ")
#     print()

# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

# for row in range(1,5):
#     for col in range(1,7):
#         print("*",end="\t ") #\t =>tabspace,next linek veran ann or can give  just a space
#     print()

# @
# @ @
# @ @ @
# @ @ @ @

# for row in range(1,5):
#     for col in range(1,row+1): #row number ne anssarich ann koodi veruthath
#         print("@",end=" ")
#     print()

# @ @ @ @  total number-row ie,6-row=>(6-row 1)=6-1=5 so 4 thavana verum
# @ @ @ 6-row=6-2=4 so 3 thavana verum
# @ @   6-row=6-3=3 so 2 thavana work cheyum
# @     6-row = 6-4=2 so 1 thavana verum
# for row in range(1,5):
#     for col in range(1,6-row):
#         print("@",end=" ")
#     print()


# @ @ @ @ @
# @ @ @ @
# @ @ @
# @ @
# @

for row in range(1,6):
    for col in range(1,7-row):
        print("@",end = " ")
    print()