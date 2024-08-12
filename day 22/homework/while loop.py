#1)გამოვთვალოთ მომხმარებლის მიერ შემოტანილი რიცხვის ციფრთა ჯამი while loop ის გამოყენებით
number=input("please enter a number: ")
count = 0
sum = 0
while len(number)> count:
    sum+=int(number[count])
    count+= 1
print(sum)
#2)დაპრინტეთ რიცხვები 10-1 მდე while loop ის გამოყენებით
number1= 10
while number1 >0:
    number1 = number1 - 1
    print(number1)
#3)დაპრინტეთ ჯამი ყველა ინტეჯერისა 1-100 მდე
number2 = 0
sum2 = 0
while number2 <= 100:
    number2+= 1
    sum2+= number2

print(sum2)
#4)გამოითავლეთ 1 დან 10 მდე ყველა რიცხვის კვადრატის ჯამი while loop ის დახმარებით

sum3=0
number3=0
while number3 <= 10:
    number3+=1
    sum = number3 ** 2

print(sum)