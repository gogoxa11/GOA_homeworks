// მომხმარებელს შემოატანინე 3 რიცხვი. თუ ამ სამი რიცხვის ჯამი იქნება ლუწი. მაშინ მათი საშუალო არითმეტიკული დააბრუნეთ. 
// სხვა შემთხვევაში 2-ზე გაამრავლეთ
let num1 = Number(prompt("Enter the first number:"))
let num2 = Number(prompt("Enter the second number:"))
let num3 = Number(prompt("Enter the third number:"))

if ((num1 + num2 + num3) % 2 === 0) {
    alert((num1 + num2 + num3) / 3)
}
else if ((num1 + num2 + num3) % 2 === 1) {
    alert((num1 + num2 + num3) * 2)
}
else {
    alert("Please enter a number")
}
