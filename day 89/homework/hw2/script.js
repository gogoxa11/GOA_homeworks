// 2)მოცემულია სია:

// fruits = ['apple', 'banana', 'cherry', 'date', 'fig']

// შეცვალე სიის მესამე ელემენტი 'orange' ით. სიის ბოლო ელემენტი "cucumber" ით და სიის მეოთხე ელემენტი "potato" ით

let fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
fruits.splice(2, 1, 'orange')
fruits.splice(4, 1, "cucumber")
fruits.splice(3, 1, "potato")
alert(fruits)