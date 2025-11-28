// 10)შექმენი სია სადაც მოათავსებ ადამიანის სახელებს

// შენი დავალებაა რომ კონსოლში გამოიტანო მხოლოდ ის სახელები რომლებიც იწყება ასო "a" ზე და მრთავდება ასო "o" ზე 
// (შეასრულეთ ორივეთი for და while)

let names = ['Luka', 'Giorgi', 'Nika', 'Gabrieli', 'Erekle', 'Mate', 'Ivane', 'andria', 'otari', 'ako']

let filteredNames = []

for (let i = 0; i < names.length; i++) {
    let name = names[i].toLowerCase()
    if (name[0] === 'a' && name[name.length - 1] === 'o') {
        filteredNames.push(names[i])
    }
}

console.log(filteredNames)
