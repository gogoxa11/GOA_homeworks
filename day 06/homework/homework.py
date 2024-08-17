#შედარების ოპერატორის დავალებები
#პირველი დავალება
print(5 > 6 or 11 > 21)
print(9 > 6 or 13 < 9)
print(5 > 19 or 416 < 510)
print(5 > 16 or 723 > 213)
print(555 > 444 or 666 < 777)
#მეორე დავალება
print(617 > 35 and 62 > 55)
print(513 > 34 and 52 < 45)
print(121 > 222 and 567 < 313)
print(222 < 333 and 444 > 555)
print(23 > 43 and 34364 > 123)
#მესამე დავალება
variable = (90 > 123 or 324 < 456) #True
print(variable)
second_variable = (23 > 23 and 45 > 12) #False
print(second_variable)
print(variable > second_variable)#True
#მეოთხე დავალება
variable1 = input("please insert first number:")
variable2 = input("please insert second number:")
print(variable1 > variable2 or variable1 < variable2)
print(variable1 < variable2 and variable2 < variable1)
#მეხუთე დავალება
variable_1 = (15 > 20)
variable_2 = (20 > 200)
variable_3 = (variable_1 > variable_2)
print(variable_3)
#მექანიკური გარდაქმნის დავალება
#პირველი დავალება
first = True
second = "luka"
third = 1.50
fourth = 12

print(type(first))
print(type(second))
print(type(third))
print(type(fourth))
#მეორე დავალება
Name = input(" please insert your name:")
Group = input("What number of Goa group are you in?")
print("Hello" + " " + Name+"," + " " + "Welcome to group" + " " + Group+".")
#მესამე დავალება
firstvariable = (21/7)
print(firstvariable)
print(type(firstvariable))
#მეოთხე დავალება
num1 = (20)
num2 = (24)
print(str(num1)+str(num2))
#მეხუთე დავალება
number1 = 3.7
number2 = 7.3
number3 = 2.1
number4 = 7.0
number5  = 3.0

print(str(number1))
print(str(number2))
print(str(number3))
print(str(number4))
print(str(number5))
