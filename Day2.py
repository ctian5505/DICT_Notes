#----------------------------------------
# Built in methods (if, else, islower, isupper, isdigit, isalpha)
str1 = input("Enter a string: ")
if str1.isupper():
    print("Your string is in all upper case")
elif str1.islower():
    print("Your string is in all lower case")
else:
    print("Your string is a combination of lower case, upper case and digit")


str1 = input("Enter a string: ")
if str1.isdigit():
    print("Your string are all digits")
elif str1.isalpha():
    print("Your string is in alphabet letters")
else:
    print("Your string is a combination if digits and alphabets")


text = 'Texds'

print(text.isalnum())
#----------------------------------------
#Compound Or(if, or)
n = int(input("Enter an integer: "))
if n == 5 or n == 10:
    print("The number is either 5 or 10")


g = int(input("Enter Grades: "))
if g >= 75 and g <=80:
    print("Good")
elif g >=81 and g <= 90:
    print("Very Good")
elif g >= 91 and g <= 100:
    print("Excellent")
elif g < 75:
    print("Failed")
else:
    print("Out of range")
#----------------------------------------
#For loop
str1 = "Hello"
for leter in str1:
    print(leter)


word_bank = ['Apple', 'Banana', 'Orange']
for word in word_bank:
    print(word)
#----------------------------------------
#For loop with breake
str1 = "Hello"
for o in str1:
    if o == "o":
        break
    print(o)
#----------------------------------------
#Continue
str1 = "Hello"
for l in str1:
    if l == "l":
        continue
    print(l)
#----------------------------------------
#Extend
male = ["Chris", "Tian"]
female = ["Joy", "Joan"]
male.extend(female)
print(male)

#----------------------------------------
#List
number = [1,2,3,4,5]
food = ["food1", "Food2", "Food3" ]

print(number[1])
print(food[1])

male = ["Chris", "Tian"]
#### List Sample 1 | append() - add only in the last
male = ["Chris", "Tian"]
male.append("Esp")
print(male)

#### List Sample 1 | .insert() - add in any position in the list
male = ["Chris", "Tian"]
male.insert(1,"Marco")
print(male)

######## Replace/Update the value
male = ["Chris", "Tian"]
male[1] = ("Frank")
print(male)

### pop | Remove and returns the last object by index
male = ["Chris", "Tian"]
male.pop(1)
print(male)

#### .remove() Remove via exact elements
male = ["Chris", "Tian"]
male.remove("Chris")
print(male)

#### .sort
n = [23,13,54,1,4,2,14,3,24]
n.sort(reverse=True)
print(n)


#### .reverse
nr = [23,13,54,1,4]
nr.reverse()
print(nr)

##### .count
nc = [23,13,54,1,4,2,14,3,24,1]
print(nc.count(1))


#### .index
ni = [23,13,54,1,4,2,14,3,24,1]
print(ni.index(13))


#### .append
male = ["Chris", "Tian"]
female = ["Joy", "Joan"]
male.extend(female)
print(male)
#----------------------------------------
#pass
str1 = "Hello"

for l in str1:
    if l == "l":
        pass
    print(l)
#----------------------------------------
#while
ans = "y"
while ans == "y" or ans == "Y":
    ans = input("Do you want to try again? y/Y: Yes, other characters to exit: ")
    print("Hello")
print("Thank you!")


c = 1
while c <= 20:
    print(c)
    c +=1
#----------------------------------------
#Day2_Act1
name = input("Enter your name: ")
math = float(input("Enter your math grade: "))
sci = float(input("Enter your science grade: "))
eng = float(input("Enter your english grade: "))
average =int((math + sci + eng)/3)

print(f"Your average is {average}")
if average >= 75:
    print("Congratulations! You passed the semester.")
    if math < 75:
        print("But you need to re-enroll to re-enroll Math subject")
    elif sci < 75:
        print("But you need to re-enroll to re-enroll Science subject")
    elif eng < 75:
        print("But you need to re-enroll English subject")
else:
    print("You failed the semester.")

#----------------------------------------
#Day2_Act2
office = input("Enter your office department [it, acct, hr]: ")
year_in_service = int(input("Years in service: "))

if office == "it" and year_in_service >= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your incentives for serving it department for more than 10 years is 10000")
elif office == "it" and year_in_service <= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your incentives for serving it department below 10 years is 5000")
elif office == "acct" and year_in_service >= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your Incentives for serving acct department for more than 10 years is 12000")
elif office == "acct" and year_in_service <= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your incentives for serving acct department below 10 years is 6000")
elif office == "hr" and year_in_service >= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your Incentives for serving hr department for more than 10 years is 15000")
elif office == "hr" and year_in_service <= 10:
    print(f"Office: {office}")
    print(f"Years in service: {year_in_service}")
    print("Your incentives for serving hr department below 10 years is 7500")
else:
    print("Invalid input")
#----------------------------------------
#Day2_Act3 (while loop)
msg = 1
while msg <= 20:
    print(f"Python while loop number {msg}")
    msg +=1
#----------------------------------------
#Day2_Act5
word_bank = []
yn = input("Do you want to add word? Y/y = Yes | N/n = No: ")
while yn == "y" or yn == "Y":
    word = input("Enter a word: ")
    word_bank.append(word)
    yn = input("Do you want to add more word? Y/y = Yes | N/n = No: ")
print(f"Total number of words: {len(word_bank)}")
print(word_bank)
#----------------------------------------



