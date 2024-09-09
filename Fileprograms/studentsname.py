f=open("/Users/mohammedroshan/Desktop/PaRo/python_django/PythonJune/Fileprograms/students.txt","r")
students=[]
for stud in f:
    students.append(stud.rstrip("\n"))
print(students)