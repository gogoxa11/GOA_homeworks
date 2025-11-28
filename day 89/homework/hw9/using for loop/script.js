// 9)შექმენი სია,სადაც მოათავსებთ მხოლოდ რიცხვებს,

// ტერმინალში გამოიტანეთ სიაში მყოფი მხოლოდ კენტი რიცხვები (შეასრულეთ ორივეთი for და while)

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
let oddNumbers = []

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 !== 0) {
        oddNumbers.push(numbers[i])
    }
}

console.log(oddNumbers)
