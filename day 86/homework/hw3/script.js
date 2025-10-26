// შეიყვანე ორი სიტყვა prompt-ით.
// თუ ტოლია — "სიტყვები ემთხვევა",
// თუ მხოლოდ პირველი ასოები ემთხვევა მაშინ - “პირველი ასოები ემთხვევა”
// სხვა შემთხვევაში — "არ ემთხვევა".
let word1 = prompt("please enter the first word").toLowerCase()
let word2 = prompt("please enter the first word").toLowerCase()
if (word1 == word2) {
    alert("სიტყვები ემთხვევა")
}
else if (word1[0] == word2[0]) {
    alert("“პირველი ასოები ემთხვევა”")
}
else{
    alert("არ ემთხვევა")
}