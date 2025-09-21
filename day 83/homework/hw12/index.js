// მომხმარებელს შემოატანინე რიცხვი და შეამოწმე, იყოფა თუ არა 3-ზე.
let num1 = Number(prompt("enter a number:"))
if (num1 % 3 === 0) {
    alert(num1 + " " + "can be divided by 3")
}
if (num1 % 3 === 1) {
    alert(num1 + " " + "can't be divided by 3")
}
if (num1 % 3 === 2) {
    alert(num1 + " " + "can't be divided by 3")
}
else{
    alert("please enter a number")
}