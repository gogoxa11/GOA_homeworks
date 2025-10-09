// 1)შექმენით ცვლადი სადაც შეინახავთ თქვენს სახელს,მომხმარებელს შემოტანინე ასაკი და სახელი,თ მომხმარებლის მიერ შემოტანილი სახელი უდრის 
// შენს სახელს და ასაკი არის მეტი 18 ზე კონსოლში გამოიტანე---> "we have same name and you are more than 18 yo" ,შემდეგ შეამოწმეთ,
// თუ მომხმარებლის მიერ შემოტანილი ასაკი არის 18 ზე მეტი მაგრამ მომხმარებლის მიერ შემოტანილი სახელი არ უდრის თქვენს სახელს 
// დაუკონსოლლოგეთ --> "We do not have same names but you are more than 18 yo" , სხვა შემთხვევაშ დაუკონსოლლოგეთ --> "vin jandaba xar"
let name1 = "luka"
let name2 = prompt("enter your name: ").toLowerCase()
let age1 = Number(prompt("enter your age: "))
if(name1 === name2 && age1 > 18){
    console.log("we have same name and you are more than 18 yo")
}
else if(name1 !== name2 && age1 > 18){
    console.log("We do not have same names but you are more than 18 yo")
}
else{
    console.log("vin jandaba xar")
}