// მომხმარებელს შემოატანინე თვე (რიცხვი 1–12) და გამოიტანე რომელი თვე და სეზონია.
let m = Number(prompt("შეიყვანე თვე (1-12):"))
let month
let season

if (m === 1) {
    month = "იანვარი"
    season = "ზამთარი"
}
else if (m === 2) {
    month = "თებერვალი"
    season = "ზამთარი"
}
else if (m === 3) {
    month = "მარტი"
    season = "გაზაფხული"
}
else if (m === 4) {
    month = "აპრილი"
    season = "გაზაფხული"
}
else if (m === 5) {
    month = "მაისი"
    season = "გაზაფხული"
}
else if (m === 6) {
    month = "ივნისი"
    season = "ზაფხული"
}
else if (m === 7) {
    month = "ივლისი"
    season = "ზაფხული"
}
else if (m === 8) {
    month = "აგვისტო"
    season = "ზაფხული"
}
else if (m === 9) {
    month = "სექტემბერი"
    season = "შემოდგომა"
}
else if (m === 10) {
    month = "ოქტომბერი"
    season = "შემოდგომა"
}
else if (m === 11) {
    month = "ნოემბერი"
    season = "შემოდგომა"
}
else if (m === 12) {
    month = "დეკემბერი"
    season = "ზამთარი"
}
else {
    alert("არასწორი რიცხვი")
}
alert("სეზონი არის" + " " +  season + " " + "და თვე არის" + " " + month)