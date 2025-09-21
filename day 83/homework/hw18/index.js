let userChoice = prompt("Enter rock, paper, or scissors:").toLowerCase()
let myChoice = "scissors"

if (userChoice === myChoice) {
    console.log("It's a tie!")
}
 else if (userChoice === "rock") {
    console.log("You win!")
} 
else if (userChoice === "paper") {
    console.log("You lose!")
}
 else {
    alert("Please enter rock, paper, or scissors")
}
