// მომხმარებელს შემოატანინეთ რიცხვი (1–12) და გამოიტანეთ შესაბამისი თვე და სეზონი
let month = Number(prompt("შეიყვანე თვის ნომერი (1-12):"));
let monthName = "";
let season = "";

if (month === 12 || month === 1 || month === 2) {
    season = "ზამთარი";
}
else if (month === 3 || month === 4 || month === 5) {
    season = "გაზაფხული";
}
else if (month === 6 || month === 7 || month === 8) {
    season = "ზაფხული";
}
else if (month === 9 || month === 10 || month === 11) {
    season = "შემოდგომა";
}
else {
    season = "არასწორი თვის ნომერი";
}

// თვის დასახელება
if (month === 1) {
    monthName = "იანვარი";
}
else if (month === 2) {
    monthName = "თებერვალი";
}
else if (month === 3) {
    monthName = "მარტი";
}
else if (month === 4) {
    monthName = "აპრილი";
}
else if (month === 5) {
    monthName = "მაისი";
}
else if (month === 6) {
    monthName = "ივნისი";
}
else if (month === 7) {
    monthName = "ივლისი";
}
else if (month === 8) {
    monthName = "აგვისტო";
}
else if (month === 9) {
    monthName = "სექტემბერი";
}
else if (month === 10) {
    monthName = "ოქტომბერი";
}
else if (month === 11) {
    monthName = "ნოემბერი";
}
else if (month === 12) {
    monthName = "დეკემბერი";
}
else {
    monthName = "არასწორი";
}

alert("თვე: " + monthName + ", " + "სეზონი: " + season);

