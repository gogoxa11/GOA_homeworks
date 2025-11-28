// 1)მოცემულია სია:
// colors = ['red', 'green', 'blue', 'yellow']
// შეცვალე ისე, რომ პირველი ელემენტი შეცვალო "DarkRed" ით და ბოლო ელემენტი შეცვალო "Orange" ით
let colors = ['red', 'green', 'blue', 'yellow']
colors.shift()
colors.unshift("DarkRed")
colors.pop()
colors.push("Orange")
alert(colors)