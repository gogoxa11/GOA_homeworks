# მომხმარებელს შემოატანინეთ სიტყვა. ამ სიტყვაშუ სადაც იქნება “g” ასო იმ ადგილებში გასპლიტეთ და დიდი “G”-თი გაერთიანეთ.

def function(word):
    uppercase=word.split("g")
    print("G".join(uppercase))

function("wuiyawgawiudagsr,esyfiusg")