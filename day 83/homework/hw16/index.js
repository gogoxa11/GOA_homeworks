let temp = Number(prompt("Enter the temperature:"))

if (temp <= 0) {
    console.log("It's cold, dress warmly")
}
 else if (temp <= 25) {
    console.log("The weather is normal")
}
 else if (temp > 25) {
    console.log("It's hot")
}
 else {
    console.log("Please enter a number")
}
