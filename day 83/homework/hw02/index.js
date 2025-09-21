// შექმენით კალკულატორი, მომხმარებელს უნდა შემოატანინოთ ორი რიცხვი და მოქმედება და შედეგი გამოიტანოთ alert-ში.
let num1 = Number(prompt("შეიყვანე პირველი რიცხვი"))
let op = prompt("მოქმედება (+, -, *, /)")
let num2 = Number(prompt("შეიყვანე მეორე რიცხვი"))
let result = 0
if (op === "+") {
    result = num1 + num2
}
else if (op === "-") {
    result = num1 - num2
}
else if (op === "*") {
    result = num1 * num2
}
else if (op === "/") {
    if (num2 !== 0) {
        result = num1 / num2
    }
    else {
        result = "ნულზე გაყოფა არ შეიძლება"
    }
}
else {
    result = "არასწორი მოქმედება"
}
alert(result)