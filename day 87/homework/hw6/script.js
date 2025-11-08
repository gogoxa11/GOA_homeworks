let num = Number(prompt("შეიყვანე რიცხვი:"));

for (let i = 1; i <= num; i++) {
    if (i % 2 === 0) {
        console.log(i + " არის ლუწი");
    }
    else {
        console.log(i + " არის კენტი");
    }
}
