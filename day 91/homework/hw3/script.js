// შექმენით 5 ელემენტიანი სია, მომხმარებლის შემოტანილი მნიშვნელობა დაამატეთ ამ სიაში იმ შემთხვევაში თუ ეს 
// ელემენტი არ არის სიაში, თუ არის მაშინ ამოშალეთ. და კონსოლში გამოიტანეთ ახალი სია.

let array1 = ["luka", "nika", "gabrieli", "erekle", "mate"]

let array2 = prompt("please enter a text: ")

if(array1.includes(array2)){
    array3 = array1.indexOf(array2)
    array1.splice(array3, 1)
}
else{
    array1.push(array2)
}
alert(array1)