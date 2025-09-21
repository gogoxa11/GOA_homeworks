// მომხმარებელს შემოატანინეთ რიცხვი და გამოიტანე დადებითია, უარყოფითი თუ ნულის ტოლია.
let num1 = Number(prompt("enter a number: "))
if(num1 > 0){
    alert(num1 + " " + "is positive")
}
else if(num1 < 0){
    alert(num1 + " " + "is negative")
}
else if(num1 == 0){
    alert("0 is neither negative or postive")
}
else{
    alert("please enter a number")
}