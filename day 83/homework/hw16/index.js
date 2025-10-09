// მომხმარებელს შემოატანინეთ ტემპერატურა, თუ  0-ზე ნაკლებია გამოიტანეთ  "ცივა და თბილად ჩაიცვი", 
// 0-დან 25-ის ჩათვლით თუა 'ნორმალური ამინდია;  სხვა დანარჩენ შემთხვევაში 'ცხელა'
let temp = Number(prompt("Enter the temperature:"))

if (temp <= 0) {
    console.log("It's cold, dress warmly")
}
else if (temp <= 25) {
    console.log("The weather is normal")
}
else if (temp > 25) {
    console.log("It's hot")
}
else {
    console.log("Please enter a number")
}
