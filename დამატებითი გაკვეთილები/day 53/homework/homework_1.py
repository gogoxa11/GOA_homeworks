#1) შექმენით კალკულატორის ფუნქცია  რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და მოქმედების ტიპს
# (მიმატება, გამოკლება, გამრავლება, გაყოფა) შესაბამისად ფუნქცია დააბრუნებს ანუ დაბეჭდავს შედეგს იმისდამიხედვით მომხმარებელს 
# რა სურს და რა რიცხვები შემოიტანა, მაგალითად მომხმარებელმა თუ შემოიტანა 5 და 2 და ასევე მას სურს გამრავლება 
# ფუნქციამ უნდა დააბრუნოს დაბეჭდოს შედეგად 2 * 5 ანუ 10

def calculator():
    num = int(input("Please enter the first number: "))
    num1 = int(input("Please enter the second number: "))
    operation = input("Please enter one of these operators (*, /, +, -): ")

    if operation == '+':
        result = num + num1
    elif operation == '-':
        result = num - num1
    elif operation == '*':
        result = num * num1
    elif operation == '/':
        result = num / num1

    return f"The result is: {result}"

print(calculator())