// მომხმარებელს შემოატანინეთ რიცხვი. თუ ეს რიცხვი მეტია 20-ზე შეამოწმეთ ლუწია თუ კენტი. თუ ლუწია მაშინ გაამრავლეთ 2-ზე. 
// თუ კენტია გაამრავლეთ სამზე. თუ 20-ზე ნაკლებია ან ტოლი მაშინ შეამოწმეთ, თუ 3-ზე იყოფა სამზე გაყავით. სხვა დანარჩენ 
// შემთხვევაში რა რიცხვიცაა ის გამოიტანეთ
let num = Number(prompt("Enter a number:"))

if (num > 20) {
    if (num % 2 === 0) {
        console.log(num * 2)
    }
    else {
        console.log(num * 3)
    }
}
else if (num <= 20) {
    if (num % 3 === 0) {
        console.log(num / 3)
    }
    else {
        console.log(num)
    }
}
else {
    alert("Please enter a number")
}
