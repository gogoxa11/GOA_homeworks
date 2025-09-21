let password = prompt("Enter the password:")

if (password === "1234") {
    let firstName = prompt("Enter your first name:").toLowerCase()
    let lastName = prompt("Enter your last name:").toLowerCase()
    let age = Number(prompt("Enter your age:"))

    if (firstName === "luka") {
        if (lastName === "gogokhia") {
            if (age === 13) {
                console.log("You have successfully registered")
            }
             else {
                console.log("There was an error during registration")
            }
        }
         else {
            console.log("There was an error during registration")
        }
    }
     else {
        console.log("There was an error during registration")
    }
}
 else {
    console.log("Incorrect password")
}
