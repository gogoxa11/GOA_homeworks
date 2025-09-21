// მომხმარებელს შემოატანინეთ ორი რიცხვი და გამოიტანეთ მაქსიმალური რიცხვი ამ ორიდან.
let num1 = Number(prompt("enter the first number: "))
let num2 = Number(prompt("enter the second number: "))
if(num1 > num2){
    alert(num1)
}
else if(num1 < num2){
    alert(num2)
}
else if(num1 == num2){
    alert(num2)
}
else{
    alert("please enter a number")
}