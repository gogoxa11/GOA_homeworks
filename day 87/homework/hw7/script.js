let num1 = Number(prompt("შეიყვანე პირველი რიცხვი:"));
let num2 = Number(prompt("შეიყვანე მეორე რიცხვი:"));

let sum = 0;
let start;
let end;

if (num1 < num2) {
    start = num1;
    end = num2;
}
else {
    start = num2;
    end = num1;
}


for (let i = start; i <= end; i++) {
    sum += i;
}

console.log("ჯამი არის: " + sum);
