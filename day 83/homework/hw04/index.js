// მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ ეს რიცხვი ლუწია თუ კენტი.
let num1 = Number(prompt("enter a number: "))
if(num1 === 0){
    alert("0 is neither odd or even")
}
else if(num1%2 ===0){
    alert(num1 + " " + "is even")
}
else if(num1%2 ===1){
    alert(num1 + " " + "is odd")
}
else{
    alert("please enter a number")
}