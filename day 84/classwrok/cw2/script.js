// 2)შექმენი ცვლადი საცად შეინახავთ ცხოველის სახელს, შემდეგ მომხმარებელს შემოატანინეთ ცხოველის სახელი, 
// თუ მომხმარებლის შემოტანილიცხოველი არის ცვლადში შენახული ცხვოველი ან მისი შემოყვანილი ცხოველი არის 'lomi' დაუკონსოლლოგეთ --> 
// "you entered my favourite animal or king of animals"
// სხვა შემთხვევაში გამოიტანე --> "You entered the animal i hate"
let an1 = "elephant"
let an2 = prompt("Please enter your favourite animal: ").toLowerCase()
if(an1 === an2 || an2 === lion){
    console.log("you entered my favourite animal or king of animals")
}
else{
    console.log("You entered the animal i hate")
}