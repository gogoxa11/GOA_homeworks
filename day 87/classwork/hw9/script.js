// მომხმარებელს შემოატანინეთ რიცხვი და ამ რიცხვის ჩათვლით გამოიტანეთ ყველა ლუწი რიცხვი
let num1 = Number(prompt("Please enter a number: "))

for (let i = 0; i <= num1; i++) {
    if (i % 2 == 0) {
        console.log(i)
    }
}

