#1)გაარკვიეთ არის თუ არა მომხმარებლის მიერ სემოტანილი წელი ნაკიანი წელი
year = int(input("Insert any year: "))  # Convert input to integer

if year % 4 == 0:
    print("That is a leap year")
else:
    print("That is not a leap year")
#2)palidrone check
word = input("what is your favourite word?: ")
if word ==word[::-1]:
    print("your word is palindrome")
else:
    print("your word is not a palindrome")
#3)გაიგეთ მომხმარებლის მიერ შემოტანილი რიცხვი ნეგატიტიურია,ნოლის ტოლია თუ პოზიტიურია.
something = int(input("insert any number you want,(positive,negative,zero): "))
if something >0:
    print("your number is positive")
elif something ==0:
    prin