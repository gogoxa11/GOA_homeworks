# შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია. თქვენი მიზანია ამ სიის თითოეული რიცხვი გაასტრინგოთ
# და შეაერთოთ ისე რომ მათ შორის '@' იყოს.  ( join & split გამოიყენეთ )

def join_with_at(numbers):
    str_numbers = []
    for num in numbers:
        str_num = str(num)
        str_numbers.append(str_num)
    
    joined_string = '@'.join(str_numbers)
    return joined_string

print(join_with_at([167, 352, 3745, 12, 4, 135, 173]))