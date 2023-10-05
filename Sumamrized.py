# Casting = changing data type

# String placeholder = f"{}"

# String Formatting
  upper()
  lower()
  capitalize() = convert the first character to uppercase
  title() = convert the first character of EACH to uppercase
  split() = make the string to list
  replace() = 
  len() = count the character
    #Example
      str1 = "pyhton is Good"
      print(str1.upper())
      print(str1.lower())
      print(str1.capitalize())
      print(str1.title())
      print(str1.split())
      print(str1.replace("is", "is very"))
      print(len(str1))

# Number Formatting
  round()
    n1 = 4.6
    n2 = 4.4
    print(round(n1)) # Returns 5
    print(round(n2)) # Returns 4
  ceil()
    from math import *
    n1 = 4.6
    n2 = 4.1
    print(ceil(n1)) # Returns 5
    print(ceil(n2)) # Returns 5
  floor()
    from math import *
    n1 = 4.6
    n2 = 4.1
    print(floor(n1)) # Returns 4
    print(floor(n2)) # Returns 4
  pow()
    p1 = pow(2, 3)   # Returns 8 (2^3)
    p2 = pow(5, 2)   # Returns 25 (5^2)
    print(p1)
    print(p2)

# Built-in methods
  isupper()
  islower()
  isdigit()
  isalpha()
    #Example
      str1 = input("Enter a string: ")
      if str1.isupper():
          print("Your string is in all upper case")
      elif str1.islower():
          print("Your string is in all lower case")
      else:
          print("Your string is a combination of lower case, upper case and digit"
# Tuplw = ()  = It's immutable, meaning it cannot be changed after creation.
# Dictionary = {} = It's an unordered and mutable data structure.
# List =  [] = It's mutable, allowing you to add, remove, and modify elements.        
  #methods to control list and its object
      append() = Appends the obj to list
      count() = count how many times the obj occur in list
      extend() = Appends the obj of other lsit
      index() = return the index number of an object
      insert() = insert obj into list using index number
      pop() = removes and returns the last object
      remove() = removes obj from a list
      sort() = sort object
        #Example
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
                
