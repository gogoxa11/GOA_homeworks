#დავალება 1)  0-იდან 20-ის ჩათვლით გამოიტანეთ რიცხვები.
for i in range(1,21):
    print(i)



#დავალება 2) მომხმარებელს შემოატანინეთ ორი რიცხვი და მათ შორის არსებულები გამოიტანეთ.
num1 = int(input("please insert number: "))
num2 = int(input("please insert number higher than the first: "))
for i in range(num1,num2):
     print(i)



#დავალება 3) 50-იდან 100-ის ჩათვლით გამოიტანეთ რიცხვები.
for i in range(50,101):
     print(i)


#დავალება 4) დაიწყეთ 100-დან და 50-ის ჩათვლით გამოიტანეთ რიცხვები. (ჩათვალეთ დავალება 3-ის საპირისპირო)


for i in range(100,49,-1):
     print(i)





#დავალება 5) 0-იდან 50-ის ჩათვლით გამოიტანეთ რიცხვები და ბოლოს მათი ჯამი.
cvladi = 0
for i in range (0,51):
     cvladi+=i

print(cvladi)


#დავალება 6) მომხმარებელს შეეკითხეთ რომ შემოიტანოს მთელი რიცხვი. შემდეგ 0-დან ამ რიცხვამდე გამოიტანეთ ყველა მთელი რიცხვი.

num3 = int(input("please enter a number: " ))
for i in range(0,num3):
     print(i)



#დავალება 7) მომხმარებელს შეეკითხეთ ასაკი. შექმენით ცვლადი, სადაც შენახული იქნება 10 წლის შემდეგ მომხმარებლის ასაკი. 
#საბოლოოდ დაპრინტეთ მომხმარებლის ასაკსა და 10 წლის შემდეგ წლოვანებას შორის არსებული მთელი რიცხვები. 

num4 = int(input("please enter your age"))
num5 = num4 + 10
for i in range(num4,num5+1):
     print(i)


#ახალი დავალებები
#1 შექმენით პროგრამა სადაც მომხმარებელი შემოიტანს 2 რციხვს, ხოლო ამ 2 რიცხვს შორის გამოიყენეთ ყველა არითმეტიკული ოპერაცია 
# (+,-,*,/,%,//), საბოლოოდ დაბეჭდეთ შედეგები ტერმინალში + ახსენით თითოეული ნაწილი კოდის რატომ დაწერეთ კონკრეტული ხაზი 
# და რას აკეთებს.

num6 = int(input("please enter a numeber: "))
num7 = int(input("please enter a numeber: "))
print(num6-num7)
print(num6+num7)
print(num6/num7)
print(num6*num7)
print(num6%num7)

#2შემოატანინეთ მომხარებელს ასაკი და შეამოწმეთ არის თუ არა 18 წელზე მეტის და 20 წელზე ნაკლების მიღებული შედეგი დაპრინტეთ

user_age = int(input("please enter your age: "))
if user_age < 20:
    print("your age is lower then 20 years old")


elif user_age == 19:
    print("your age is higher than 18 but lower than 20")

elif user_age > 18:
    print("your age is higher than 18")


#3ჩამოწერეთ ხუთ-ხუთი მაგალითი ყველა ლოგიკურ ოპერატორზე > ,<, <=, >=, !=, == 

print(12 == 21)
print(67 <= 68)
print(70 >= 49)
print(79 != 69)
print( 898 > 1283)
print(3239837 < 3987483242389)


#4  მომხმარებელს პირველ ინფუთში მთელი რიცხვი, ხოლო მეორე ინფუთში ათწილადი შემოატანინეთ.
#  საბოლოოდ შეადარეთ ცვლადების მნიშვნელობების მონაცემთა ტიპები

num8 = int(input("please enter a full number: "))
num9 = float(input("please enter a decimal number: "))
print(type(num8))
print(type(num9))

#5შექმენით რამოდენიმე სხვადასხვა ტიპის ცვლადი და დაბეჭდეთ მათი მონაცემთა ტიპები

num10 = True
num11 = 2.4
num12 = 347
num13 = "real madrid"

#6 ) მომხმარებელს შემოატანინეთ 1 დან 7-ის ჩათვლით რომელიმე რიცხვი ამის შემდეგ კი გამოიყენეთ if elif else რომ შეუსაბამოდ კვირის დღე
#  1 ორშაბათისთვის 2 სამშაბათისთვის 3 ოთხშაბათისთვის და ასე შემდეგ

num14 = int(input("please choose number 1-7: "))

if num14 == 1:
    print("monday")
elif num14 == 2:
    print("tueasday")
elif num14 == 3:
    print("wedensday")
elif num14 == 4:
    print("thursday")
elif num14 == 5:
    print("friday")
elif num14 == 6:
    print("saturday")
elif num14 == 7:
    print("sunday")

elif num14 > 7:
    print("error")

#7 ) შექმენით ისეთი while ციკლი რომელიც 0 დან 10 ის ჩათვლ;ით დაბეჭდავს ყველა რიცხვს და if else  
# გამოყენებით გაიგეთ არის თუ არა ლუწი ან კენტი დასერჩეთ how to know if number is even or odd in python
for i in range(1, 10):
    print(i)
    if i % 2 == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")


#8 ) მომხმარებელს შემოატანინეთ თავისი ასაკი და შეამოწმეთ თუ მომხმარებლის ასაკი მეტია 5 ზე და ნაკლები 12 ზე დაუბეჭდეთ რომ არის ბავშვი ,
#  სხვა შემთხვევაში თუ მომხმარებლის ასაკი არის 12 ზე მეტი და 18 ზე ნაკლები დაუბეჭდეთ რომ არის თინეიჯერი და თუ არის 18
#  ზე მეტი დაუბეჭდეთ რომ არის ზრდასრული

num15 = int(input("how old are you?: "))
if num15 <= 5:
    print("you are either a baby or a little kid")


elif num15 > 5 and num15 >= 12:
    print("you are still a child")

elif num15 < 18:
    print("you are a teenager")

elif num15 >= 18:
    print("you are an adult")

#9)მომხმარებელს ჯერ შემოატანინეთ ბიუჯეტი, შემდეგ კი ის თანხა,
#  რომელიც სასურველი ნივთის საყიდლად სჭირდება. დაბეჭდეთ შეუძლია ყიდვა თუ არა.

thing = input("what do you want to buy?: ")
budget = int(input("what is your budget?: "))
price = int(input("how much does" + thing + "cost?"))

if budget >= price:
        print("you can buy" + thing)

else:
    print("you can not buy" + thing)
