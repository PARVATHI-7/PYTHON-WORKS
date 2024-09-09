# read height and weight from the user and calculate bmi
# print under weight if bmi <19
# print normal weight if bmi ranges from 19-25
# print over weight if bmi in range of 25-30
# print obesity


weight=float(input("enter the weight:"))
height=float(input("enter the height:"))/100
bmi=weight/height**2
if(bmi<=19):
    print("under weight")
elif(19<=bmi<=25):
    print("normal weight")
elif(25<=bmi<=30):
    print("over weight")
else:
    print("obesity")
