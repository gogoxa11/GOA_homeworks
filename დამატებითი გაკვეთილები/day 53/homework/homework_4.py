#4) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს და შემდეგ კი დააბრუნებს დაბეჭდავს მომხმარებლის შემოტანილი რიცხვი კენტია თუ ლუწი
def function():
    num = int(input("please enter a number: "))
    if num % 2 ==0:
        print(str(num) + " is even")

    else:
        print(str(num) + " is odd")

function()