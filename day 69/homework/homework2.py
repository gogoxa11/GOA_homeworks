# შექმენით ფუნქცია, რომელელიც არგუმენტად გადაცემულ სიტყვის შრიფტებს შეაბრუნებს (ანუ თუ რომელიმე ასო წერია პატარად ეგ ასო გადაიქცეს დიდად და პირიქით, HelLo --> hELlO

def function(before):
    after = before.swapcase()
    print(after)

function("HeLlO WoRlD")