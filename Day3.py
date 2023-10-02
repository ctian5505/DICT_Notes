#----------------------------------------
#Funtion(def)
def diff(n1, n2):
    return n1-n2
print(f"The difference is: {diff(100,99)}")
#----------------------------------------
#HaloHalo
def greet():
    print("Hi")
greet()
    ##---------------------------
def greet(name,age):
    print("Hi " + name)
    print("Age " + str(age))
name1 = "Tian"
age2 = 21

greet("Chris",22)
greet(name1,age2)
greet(name1, 99)
    #Funtions with default value
def sum(n1,n2=100):
    sum = int(n1)+int(n2)
    print(f"Sum is: {sum}")
sum(1000)
sum(50,200)

    #Funtions with default value
str = "Chan"
print(str[::-1])
    ##############
def sum(n1,n2):
    sum = int(n1)+int(n2)
    print(f"Sum is: {sum}")

sum(5,5)
#--------------------------------
#Return
def greet():
    return "Hello"

print(greet())

#-----------------------------
#Calculator
#from CalculatorOperationModules import *
import CalculatorOperationModules as op
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Sum: {op.add(num1,num2)}")
print(f"Dif: {op.sub(num1,num2)}")
print(f"Product: {op.mul(num1,num2)}")
print(f"Quotient: {op.div(num1,num2)}")

    #Modules (CalculatorOperationModules.py)
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2
#-----------------------------
#Dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(f"Name: {dict['Name']}")
print(f"Age: {dict['Age']}")
print(f"Class: {dict['Class']}")
dict['Age'] = 100 # To edit Dict
print(f"Age: {dict['Age']}")
print(dict)
dict['School'] = 'MNCHS' # to add in dict
print(dict)
del dict['Name'] # To delete specific key
print(dict)
dict.clear() # To clear the dict
print(dict)
del dict # Delete entire dictionary
print(dict)
#-----------------------------
#Delete
fruits = {'Apple', 'Banana', 'Cherry'}
fruits.remove('Banana') # Remove the value with error
print(fruits)

#-----------------------------
#discard
prog = {'C', 'C#', 'Java'} # Discard (no error)
prog.discard('Python')
print(prog)
#-----------------------------
#Sets
fruits = {'Apple', 'Banana', 'Cherry'}
print(fruits)

## Add
fruits.add('Pineapple') # add one only
print(fruits)

## Delete
fruits.remove('Banana')
print(fruits)

fruits.remove('Pineapple')
print(fruits)

prog = {'C', 'C#', 'Java'}
print(prog)
prog.update(['Python', 'SQL']) # Add two ot more data's
print(prog)

for x in prog:
    print(x)

#-----------------------------
#Tuples
tup1 = ("physics", "chemistry", 1997, 2000)
tup2 = (1,2,3,4,5,6,7)

print(f"tup1: {tup1[0]}")
print(f"Tup2 {tup2[1:5]}")
print(f"len of tup2: {len(tup2)}") #len
print(f"Max value: {max(tup2)}") #max
print(f"Min value: {min(tup2)}") #min
print(tup1+tup2) #concat

if 3 in tup2: # in
    print("3 is in tup 2")
else:
    print("3 is not in tup 2")


##### Delete UP
#del tup1
#print(tup1)

l = ["list1", "list2", "list3"]
print(tuple(l))
#-----------------------------
#Day3_Act1
def avg(name,math,sci,eng):
    gavg = float((math + eng + sci)/3)
    print(f"{name}'s grade (Math = {math}, Science = {sci}, English = {eng}) and the average is {gavg:.2f}")

avg("John", 90, 80, 80)
avg("Ana", 75, 80, 90)
avg("Frank", 76, 76, 73)
#-----------------------------
#Day3_Act2
def rev(str = input("Enter a word: ")):
    print(str)
    print(f"{str[:: -1].upper()} ({len(str)} characters)")

rev()
#-----------------------------
#Day3_Act3
data = {}
ask = input('Record Keeping App\nType "Add" if you want to Add data\nType "Del" to Delete Data\nType "End" to end the program\nType here:  ')

while ask.lower() == 'add':
    print('Adding data...')
    print(data)
    key = input("Enter Key: ")
    value = input("Enter Value: ")
    data[key] = value
    ask = input('You want to Add(Add) more, Delete(Del) or End(End)? : ')
    while ask.lower() == 'del':
        print('Deleting data...')
        print(data)
        delete = input("What key you want to delete?: ")
        del data[delete]
        print(data)
        ask = input('You want to Add(Add) more, Delete(Del) or End(End)? : ')
print(f'\nGathered data {data}')
print("Thank you")





