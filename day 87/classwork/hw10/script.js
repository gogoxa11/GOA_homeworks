// მომხმარებელს შემოატანინეთ რიცხვი და ამ რიცხვიდან 0-მდე გამოიტანეთ ყველა რიცხვი
let num1 = Number(prompt("Please enter a number: "))

for(let i = num1; i > 0; i = num1 -=1){
    console.log(num1)
}

