email_ids=[
    "sam@gmail.com",
    "john@gmail.com",
    "stuart@gmail.com",
    "ram@gmail.com",
    "jam@gmail.com"
]

f=open("/Users/mohammedroshan/Desktop/PaRo/python_django/PythonJune/Fileprograms/emails.txt","w")
for email in email_ids:
    f.write(email+"\n")