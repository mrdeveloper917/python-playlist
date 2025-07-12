class Employee:
    language = "Py" # This is a class attribute
    salary = 1300000


Ayush = Employee()
Ayush.name = "Ayush Thakur" # This is a Instance attribute
print(Ayush.name, Ayush.salary, Ayush.language)

Rohan = Employee()
Rohan.name = "Rohan Roro Robinson"
print(Rohan.name, Rohan.salary, Rohan.language)

# Here nsme is object attribute and salary and language are class attributes as they directly belong to the class