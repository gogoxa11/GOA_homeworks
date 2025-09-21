// მომხმარებელს შემოატანინეთ საყვარელი ფერი, თუ დაემთხვევა თქვენსას მაშინ ალერტში გამოიტანეთ, 
// ჩვენ ორივეს ერთნაირი ფერები მოგვწონს. სხვა დანარჩენ შემთხვევაში მომხმარებლის შემოტანილი მნიშვნელობა.
let favcol1 = "blue"
let favcol2 = prompt("what is your favourite colour?: ").toLowerCase()
if(favcol1 == favcol2){
    alert("we have the same favourite colour")
}
else{
    alert(favcol2)
}