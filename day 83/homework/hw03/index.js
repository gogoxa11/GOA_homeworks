// მომხმარებელს შემოატანინეთ სახელი და გამოიტანეთ alert-ში 'გილოცავ' თუ ერთნაირი სახელები გაქვთ. 
// (არ აქვს დიდად დაწერთ თუ პატარა ასოებად, უნდა იმუშავოს) სხვა დანარჩენ შემთხვევაში უბრალოდ სახელი გამოიტანეთ.
let name1 = prompt("enter your name: ").toLowerCase()
name2 = "luka"
if(name1 === name2){
    alert("congratulations")
}
else{
    alert(name1)
}