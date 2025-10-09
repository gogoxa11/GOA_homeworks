// მომხმარებელს შემოატანინეთ რიცხვი. და შეამოწმეთ იყოფა თუ არა 4-ზე და 3-ზე ან 5-ზე მაინც
let num1 = Number(prompt("please enter a number:"))
alert(num1 % 4 == 0 && num1 % 3 == 0 || num1 % 5 == 0)