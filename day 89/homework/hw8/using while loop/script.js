// 8)შექმენი სია,სადაც მოათავსებთ მხოლოდ რიცხვებს,

// ტერმინალში გამოიტანეთ სიაში მყოფი მხოლოდ ლუწი რიცხვები (შეასრულეთ ორივეთი for და while)

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
let evenNumbers = []
let i = 0

while (i < numbers.length) {
    if (numbers[i] % 2 === 0) {
        evenNumbers.push(numbers[i])
    }
    i++;
}

console.log(evenNumbers)