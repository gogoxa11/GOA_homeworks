// 10)შექმენი სია სადაც მოათავსებ ადამიანის სახელებს

// შენი დავალებაა რომ კონსოლში გამოიტანო მხოლოდ ის სახელები რომლებიც იწყება ასო "a" ზე და მრთავდება ასო "o" ზე 
// (შეასრულეთ ორივეთი for და while)

let filteredNames = []
let i = 0

while (i < names.length) {
    let name = names[i].toLowerCase();
    if (name[0] === 'a' && name[name.length - 1] === 'o') {
        filteredNames.push(names[i])
    }
    i++
}

console.log(filteredNames)
