#გაიმეორეთ მთლიანი მასალა რაც ისწავლეთ 


#1)python home
print("Hello, World!")

#2)python syntax
if 5 > 2:
  print("Five is greater than two!")

#3)python comments

#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment


#print("Hello, World!")
print("gamarjoba megobaro!")

#4)python variables

x = 5
y = "John"
print(x)
print(y)

x1 = 21       # x is of type int
x2 = "luka" # x is now of type str
print(x)

a = str(3)    # x will be '3' because str aka string
b = int(3)    # y will be 3 because int i used aka integer
c = float(3)  # z will be 3.0 because float is used

#5)variable names

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.

mevar = "luka"
me_var = "dato"
_me_var = "nika"
meVar = "giorgi"
MEVAR = "mari"
mevar2 = "GOA"

#6)asign multiple values
a1, b1, c1 = "Orange", "Banana", "Cherry"
print(a1)
print(b1)
print(c1)

fruits = ["apple", "pear", "dragonfruit"]
a2, b2, c2 = fruits

print(a2)
print(b2)
print(c2)


#7)output variables


a3 = "GOA is"
b3 = "better than"
c3 = "novatori"
print(a3, b3, c3)

five = 5
ten = 10
print(five + ten)

#8)global variables
#we havent learned functions yet  :( :( :( :( :( :( :( :(


#9)data types
ragaca = "GOA"
ragaca1 = 21
ragaca2 = 2.5
ragaca3 = True
ragaca4 = ["vashli", "banani", "alubali"]

print(type(ragaca))
print(type(ragaca1))
print(type(ragaca2))
print(type(ragaca3))
print(type(ragaca4))

#10)numbers
num1 = 1    # int
num2 = 2.8  # float
num3 = 1j   # complex; we havent leaned complex yet :( :( :( :( :( 

print(type(num1))
print(type(num2))
print(type(num3))


#11)casting

num4 = float(1)     # num4 will be 1.0
num5 = float(2.8)   # num5 will be 2.8
num6 = float("3")   # num6 will be 3.0
num7 = float("4.2") # num7 will be 4.2


#12)booleans

print(10 > 9)
print(10 == 9)
print(10 < 9)

booleans = ((True and False)or (False or True))
print(booleans)

#13)lists

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#14)tuples
#we havent learne tuples yet

#15)if else
novatori_is_shit = 33
GOA_is_best = 200
if GOA_is_best > novatori_is_shit:
  print("GOA is greater than novatori")

#16)while loops
i = 1
while i < 6:
  print(i)
  i += 1

#17)for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)