class Employee:
    language = "Python" # This is a class attribute
    salary = 1300000


Ayush = Employee()
Ayush.language = "JavaScript" # This is a Instance attribute
print(Ayush.salary, Ayush.language)

