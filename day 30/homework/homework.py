#1) შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი

# def function1():
#     num1 = int(input("please enter a number: "))
#     if num1 % 2 == 0:
#         print(str(num1) + " is even")

#     else:
#         print(str(num1) + " is odd")

# function1()


# #2)შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი დადებითია თუ უარყოფითი

# def function2():
#     num3 = int(input("please enter a number: "))
#     if num3 > 0:
#         print(str(num3) + " is positive")

#     elif num3 < 0:
#         print(str(num3) + " is negative")

#     elif num3 ==0:
#         print(str(num3) + " is neutral")

# function2()


#3)შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი არის თუ არა ხუთის ჯერადი

# def function3():
#     num4 = int(input("please enter a number: "))

#     if num4 % 5 ==0:
#         print(str(num4) + " is a multiple of five")

#     else:
#         print(str(num4) + " is  not a multiple of five")

# function3()


#4)შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება ასაკს შემდეგ კი დაბეჭდავს ის არის თუ არა სრულწლოვანი
# def function4():
#     num5 = int(input("please enter your age: "))
#     if num5 > 17:
#         print("you are an adult")

#     else:
#         print("you are not an adult")

# function4()


#5)შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება რიხვს შემდეგ კი დაბეჭდავს ეს აყვანილი კვადრატში
# def function5():
#     num6 = int(input("please enter a number: "))

#     square = num6 * num6
#     print("squeare of " +  str(num6) + " is " +  str(square))

# function5()


#6)შექმნათ ფუნქცია რომელიც მომხმარებელს შეეკითხება პაროლს შემდეგ შეამოწმებს ეს პაროლი შეიცავს თუ არა 8 სიმბოლოს თუ შეიცავს დაბეჭდეთ
#  რომ რეგისტრაციამ წარმატებით ჩიარა, შხვა შემთხვევაში ხელახლა შეეკითხეთ პაროლი და უთხარი რომ აუცილებელია შეიყვანოს 8 სიმბოლო

def function6():
    password = input("Please enter a password: ")
    
    while len(password) < 8:
        print("The password must contain at least 8 characters. Please try again.")
        password = input("Please enter a password: ")
    
    print("Registration successful!")

function6()


#7)შექმენით ფუნქცია რომელიც მომხმარებელს 10ჯერ შეეკითხება რიცხვს, ამ რიცხვებს დაამატებს სიაში,
#  შემდეგ კი ამ სიიდან მიწვდება თითოეულს და დაბეჭდავს მათ კვადრატებს

#?????????