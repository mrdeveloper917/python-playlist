class Employee:
    language = "Python" # This is a class attribute
    salary = 1300000

    def getInfo(self):
        print(f"The langauge is {self.language}. The salary is {self.salary}")
    

Ayush = Employee()
Ayush.language = "JavaScript" # This is a Instance attribute
Ayush.getInfo()

