// 1)შექმენი ერთი სია,სადაც მოათავსებთ განსხვავებული ტიპის ელემენტებს,5 ზე მეტი ელემენტი იყოს სიაში

// ---გამოიტანეთ სიის თითოეული ელემენტი ცალ ცალკე

// ---გამოიტანე სიის თითოეული ელემენტი for loop ის გამოყენებით

// ---გამოიტანე სიის თითოეული ელემენტი while loop ის გამოყენებით

let myList = [10, "Hello", 3.14, true, 1, 2, 3]

// 2) თითოეული ელემენტი ცალ-ცალკე
console.log(myList[0])
console.log(myList[1])
console.log(myList[2])
console.log(myList[3])
console.log(myList[4])

// 3) for loop
console.log("for loop გამოყენებით:")
for (let i = 0; i < myList.length; i++) {
    console.log(myList[i])
}

// 4) while loop
console.log("while loop გამოყენებით:")
let i = 0;
while (i < myList.length) {
    console.log(myList[i])
    i++
}
