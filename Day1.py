#Morning
#----------------------------------------
#input
name = input("Enter Full Name: ")
email = input("Enter Email: ")

print("Name:", name)
print("Email:",email)
#----------------------------------------
#Casting
y = "10"
z = "10"

print(float(y)+float(z))
#----------------------------------------
#Random Activities
first_name = input("Enter Name: ")
enggrade = int(input("Enter English Grade: "))
scigrade = int(input("Enter Science Grade: "))
average = (enggrade + scigrade) / 2
passed = input("Enter if Passed: True of False: ")
# - = subtraction
# * = multiplication
# % = modulus (Remaider)

print("Name:", first_name)
print("English Grade:",enggrade)
print("Science Grade:", scigrade)
print("Average:", average)
print("Passed:", passed)
#----------------------------------------
#Day1 Activity1

first_name = "Christian"
last_name = "Espinosa"
hours_worked = 8
rate_per_hour = 100
deduction = 2

print("FirstName:", first_name)
print("LastName:", last_name)
print("Hours Worked:", hours_worked)
print("Rate per hour:", rate_per_hour)
print("Deduction:", deduction)
#----------------------------------------
#Formating(Round,Ceil, Import math)
import math as m
grade1 = 88.3
grade2 = 78.46

print(round(grade1,1))
print(round(grade2,1))
print(m.ceil(grade2)) # always round up
print(m.floor(grade2)) # Always round down
print(pow(2,2))
print(2**2)
#----------------------------------------
#Placeholder example 1
item = "chocolate"
cost = 99.99

sampleText4 = "The %s cost %.2f" % (item, cost)
print(sampleText4)
#----------------------------------------
#Placeholder example 2
item = "chocolate"
cost = 99.556

sampleText5a = f"The {item} cost {cost}"
sampleText5b = f"The {item} cost {cost:.2f}"
sampleText5c = f"The {item} cost {cost*10:.2f}"

print(sampleText5a)
print(sampleText5b)
print(sampleText5c)
#----------------------------------------
#String Formatting Function (upper,lower,capitalize,title,split,replace,len)
msg1 = ("hello world")
msg2 = "HELLO WORLD"
msg3 = "Hello-world"

print(msg1.upper())
print(msg2.lower())
print(msg1.capitalize())
print(msg2.title())
print(msg1.split())
print(msg3.split("-")[0])
print(msg3.split("-")[1])
print(msg1.replace("hello","hi"))
print(len(msg1))
c = len(msg1)
print(c)
#----------------------------------------
#Day1_Activity2
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
hours_worked = int(input("Enter hours worked: "))
rate_per_hour = int(input("Enter Rate per hour: "))
deduction = int(input("Enter deduction: "))
salary = hours_worked * rate_per_hour - deduction

print("FirstName:",first_name)
print("LastName:",last_name)
print("Hours Worked:",hours_worked)
print("Rate per hour:",rate_per_hour)
print("Deduction:",deduction)
print("Salary:",float(salary))
#----------------------------------------
#Day1_Act3
noun1 = input("Enter the first noun: ").upper()  # Jhon
noun2 = input("Enter the second noun: ").upper()  # Porridge
adjectives1 = input("Enter the first adjectives: ").upper()  # Cooking
adjectives2 = input("Enter the second adjectives: ").upper()  # delicious
original_poem = "You go home one evening tired from work,\nand your mother boils you a turtle soup. \nTwelve hours hunched over the hearth"

print("\nOriginal Poem\n" + original_poem)
print("\nResult")
print(original_poem.replace("your mother", noun1).replace("boils", adjectives1).replace("turtle", adjectives2).replace(
    "soup", noun2))
#----------------------------------------


