vehicle_number=[
    "KL 21 B 2046",
    "KL 47 B 6969",
    "KL 91 C 7172"
]

f=open("/Users/mohammedroshan/Desktop/PaRo/python_django/PythonJune/Fileprograms/vehiclenumber.txt","w")
for number in vehicle_number:
    f.write(number+"\n")