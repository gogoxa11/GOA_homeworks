// მომხმარებელს შემოატანინეთ ასაკი და შეამოწმეთ, თუ რიცხვი ნაკლებია 18-ზე მაშინ კონსოლში გამოიტანეთ 
// 'ჯერ არასრულწლოვანი ხარ' სხვა დანარჩენ შემთხვევაში 'შენ ზრდასრული ხარ'
let age = Number(prompt("enter your age: "))
if(age < 18){
    console.log("You're underage")
}
else if(age >=18){
    console.log("You're an adult")
}
else{
    alert("please enter a number")
}