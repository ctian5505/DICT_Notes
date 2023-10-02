#
#--------------------------------
#Random
from random import *

i = randrange(100,1000,100)

print(i)
#--------------------------------
#ExceptionHandling
    #
try:
    a = 104
    if a <=17:
        raise Exception
except Exception:
    print("Error")
else:print("No Error")
try:
    x = 10/0
except Exception:
    print("Error")
else:
    print("No Error")
    #
try:
    x = 10/0
except ZeroDivisionError:
    print("Zero Division Error")
else:
    print("No Error")
    #
try:
    x = 10/"ds"
except ZeroDivisionError:
    print("Zero Division Error")
except TypeError:
    print("Type Error")
else:
    print("No Error")
    #
try:
    x = 10/5
except ZeroDivisionError:
    print("Zero Division Error")
except TypeError:
    print("Type Error")
except FileNotFoundError:
    print("File Not Found Error")
else:
    print("No Error")
    #
try:
    file = open('filename.txt')
except Exception:
    print("Error")
else:
    print("No Error")
finally:
    file.close()
#--------------------------------
#Inheritance
class Mother:
    eyes = "Blue"


class Father:
    hair = "Brown"


class Child(Mother, Father):  # Mother only is single Inheritance / Mother and Father are multi
    height = "170 cm"

a = Child()
print(f"Hair: {a.hair}")
print(f"Height: {a.height}")
print(f"Eyes: {a.eyes}")
#--------------------------------
#Inheritance SAmple2
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    def printname(self):
        print(self.first_name, self.last_name)
    def isStudent(self):
        return False

class Student(Person):
    def isStudent(self):
        return True

class Grades:
    def __init__(self, math, science):
        self.mymath = math
        self.myscience = science
    def printgrades(self):
        print(self.mymath, self.myscience)

person1 = Person("Chris", "Tian")
person1.printname()
print(f"Student?: {person1.isStudent()}")
student1 = Student("John", "Doe")
print(f"Student?: {student1.isStudent()}")

    # Grades di nagamit couz ubos naoras :)
#--------------------------------
# __init__
class Employee:
    def __init__(self,name,email, rate, hw): #hw = hour worked
        self.myname = name
        self.myemail = email
        self.myrate = rate
        self.myhw = hw

    def employeeInfo(self):
        print(f"Name: {self.myname}")
        print(f"Email: {self.myemail}")
    def employeeSalary(self):
        gross = self.myrate*self.myhw
        print(f"Gross Salary: {gross}")

e1 = Employee("Chris","Chan", 1000, 100)
e1.employeeInfo()
e1.employeeSalary()
#--------------------------------
#Day4_Act1
from random import *

ui = input("You want to generate a random name? (Y/y = Yes | N/n = No): ")
bank = []

while ui.lower() == "y":
    fname = ["John", "Maria", "Peter", "Grace", "Chris", "Karl", "Philip", "Lillian", "Alfred", "Mitch"]
    mname = ['Navarro', "Padilla", "Brillantes", "Espinosa", "Manalo", "Sotto", "McArthur", "Stanley", "Delacruz",
             'Hebert']
    lname = ["Beck", "Ayers", "Bowen", "Mack", "Zavala", 'Monroe', "Brock", "Mendoza", 'Harrington', "Diaz"]
    ran_no = randrange(0,9)
    gfname = fname[ran_no]
    gmname = mname[ran_no]
    glname = lname[ran_no]
    print("---------------------------------------")
    print("Congratulations! Your new name is")
    gname = gfname + " " + gmname + " " + glname
    print(gname)
    print("---------------------------------------")
    bank.append(gname)
    ui = input("You want to generate more random name? (Y/y = Yes | N/n = No): ")
    #print(ui)
print("---------------------------------------")
print(f"Thank you! \nGenerated names: {bank}")
#--------------------------------
#Day4_Act3
class Car:
    color = "Red"
    model = "Civic"
    manufacturer = 'Honda'

    def carinfo(self):
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")
        print(f"Manufacturer: {self.manufacturer}\n")

car1 = Car()
car1.carinfo()

car2 = Car()
car2.color = "White"
car2.model = "M3 Sedan"
car2.manufacturer = "BMW"
car2.carinfo()

car3 = Car()
car3.color = "Black"
car3.model = "Raptor"
car3.manufacturer = "Ford"
car3.carinfo()
#--------------------------------
#Day4_Act4
class Student:
    def __init__(self, name, math, sci, eng):
        self.sname = name
        self.gmath = math
        self.gsci = sci
        self.geng = eng
    def students_info(self):
        print(f"\nName: {self.sname}")
        print(f"Math: {self.gmath}")
        print(f"Science: {self.gsci}")
        print(f"English: {self.geng}")
    def student_grade(self):
        average = (self.gmath + self.gsci + self.geng)/3
        if average >=75 and average < 101:
            print(f"Average: {average} (Passed)")
        else:
            print(f"Average: {average} (Failed)")

s1 = Student(input("Enter your name: "), int(input("Enter your math grades: ")),int(input("Enter your science grades: ")),int(input("Enter your english grades: ")) )
s1.students_info()
s1.student_grade()
#
#Day4_Act5
class House:
    def __init__(self, floorSize, noOfFloors, noOfDoors):
        self.floorSize = floorSize
        self.noOfFloors = noOfFloors
        self.noOfDoors = noOfDoors
        self.light = False

    def switchOn(self):
        self.lightOpen()

    def lightOpen(self):
        self.light = True
        print("Lights are now on.")

    def ovenOpen(self):
        print("Oven is open.")

class TownHouse(House):
    def __init__(self, floorSize):
        self.floorSize = floorSize
        # Modify the values of noOfFloors and noOfDoors for TownHouse
        self.noOfFloors = 2
        self.noOfDoors = 4


townhouse1 = TownHouse(1500) # Instantiate the TownHouse class
print(f"Townhouse Floor Size: {townhouse1.floorSize}")
print(f"Townhouse Number of Floors: {townhouse1.noOfFloors}")
print(f"Townhouse Number of Doors: {townhouse1.noOfDoors}")
townhouse1.switchOn() # Calling switchOn() will automatically execute lightOpen()
townhouse1.ovenOpen()
