// 4) შექმენით ცვლადები let-ით const-ით და var-ით, თითოეული მათგანის მნიშვნელობა გაანახლეთ ბევრჯერ და კონსოლში 
// გამოიტანეთ შედეგი. რაც არ იმუშავებს განმარტეთ რატომ არ მუშაობს.


var city = "თბილისი";
let country = "საქართველო";
const year = 2025;

console.log(city);    
console.log(country); 
console.log(year); 

// 4) ცვლადების განახლება

city = "ბათუმი";
console.log(city);

country = "ინგლისი";
console.log(country); 

// const year = 2026;-error

// const-ის განახლება არ მუშაობს
// განმარტება:
// const - მუდმივი, მნიშვნელობას ვერ შევუცვლით.