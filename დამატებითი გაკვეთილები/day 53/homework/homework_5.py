# 5) შექმენით დროში მოგზაურობის ფუნქცია რომელიც მომხმარებელს შეეკითხება მის ახლანდელ ასაკს და ამჟამინდელ წელს, ასევე რამდენი ხანით 
# სურს დროშ მოგზაურობა შემდეგ კი ფუნქციამ უნდა დააბრუნოს დაბეჭდოს დროში მოგზაურობის შემდეგ რომელი წელი იქნება და რამდენი წლის 
# იქნება მომხმარებელი, ასევე დაამატეთ რომ მომხმარებელმა მიიღოს გადაწყვეტილება წარსულში სურს დრში მოგზაურობა თუ მომავალში 
def time_machine():
    
    direction = input("Do you want to go to the past or the future? (past/future): ")

    if direction == ("past" or "Past"):
       
        current_year = int(input("What year is it now? "))
        age = int(input("How old are you? "))
        years_back = int(input("How many years back do you want to go? "))

        past_year = current_year - years_back
        past_age = age - years_back
        
        print("You are now in the year " + str(past_year) + ". You are " + str(past_age) + " years old.")

    elif direction == ("future" or "Future"):
       
        current_year = int(input("What year is it now? "))
        age = int(input("How old are you? "))
        years_forward = int(input("How many years forward do you want to go? "))

        future_year = current_year + years_forward
        future_age = age + years_forward
        
        print("You are now in the year " + str(future_year) + ". You are " + str(future_age) + " years old.")

    else:
        print("Please choose past/Past or future/Future")


time_machine()
