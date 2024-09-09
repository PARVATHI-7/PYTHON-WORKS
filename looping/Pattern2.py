#  @  @  @  @
#  @  @  @ 
#  @  @
#  @
# 
for row in range(1,5):
    for col in range(1,6-row):
        print("@",end ="\t ")
    print( ) 


#  @  @  @  @  @  @
#  @  @  @  @  @
#  @  @  @  @
#  @  @  @
#  @  @
#  @

for row in range(1,7):
    for col in range(1,8-row):
        print("@",end ="\t ")
    print( ) 



# @
# @ @
# @ @ @
# @ @ @ @
for row in range(1,5):
    for col in range(1,row+1):
        print("@",end="\t")
    print()

# @ @ @ @ #5(6-row)
# @ @ @ #4(6-2)
# @ @ #3(6-3)
# @ #2(6-4)

for row in range(1,5):
    for col in range(1,6-row):
        print("@",end="\t")
    print()