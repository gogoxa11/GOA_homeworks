#FOR LOOP
#1)ერთიდან ათამდე ყველა რიცხვის ჯამი
sum = 0

for i in range(1, 11):
    sum = sum + i
    
print(sum)
#2)1-15 რიცხვების კვადრატი
for i in range(1, 16):
    print(i*i)
#3)1-5 რიცხვების კვადრატის ჯამი
sum=0
for i in range(1, 6):
    sum+=i**2
    
print(sum)
#4)დავპრინტოთ ისეთი რიცხვები ერთიდან ასის ჩათვლით რომელიც 3 ზე და 5 ზე იყოფა
for i in range (1, 101):
    if i % 15== 0:
        print(i)
#5)დავპრინტოთ რიცხვები 10-1 ჩათვლით
for i in range(10, 0, -1):
    print(i)