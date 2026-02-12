student = {}

name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_subject = input("Enter your favorite subject: ")

student = {'name':name, 'age':age, 'subject':favorite_subject}

print(f'''Student Record:
Name: {student['name']}
Age: {student['age']}
Favorite Subject: {student['subject']}''')