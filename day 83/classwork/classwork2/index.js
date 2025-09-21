// შემოატანინეთ მომხმარებელს სახელი და ასაკი, თუ სახელი და ასაკიც ემთხვევა თქვენსას მაშინ გამოიტანეთ კონსოლში შედეგი.
// სხვა დანარჩენ შემთხვევაში 'ჩვენი ასაკი ან სახელები განსხვავდება'.
let name1 = prompt("what is your name? :").toLowerCase()
let age1 = Number(prompt("how old are you? :"))
let name2 = "luka"
let age2 = 13
if( name1 === name2){
    if( age1 == age2){
        console.log("both our age and name is the same")
    }
}
else{
    console.log("either our age or our name is different")
}
