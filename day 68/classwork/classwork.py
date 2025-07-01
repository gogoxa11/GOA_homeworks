# შექმენით ფუნქცია,რომელსაც გადაეცემა ერთ დიდი წინადადება და ამ წინადადებაში სიტყვები დაშორებულები არიან  $ ნიშნით,თქვენი დავალებაა დააბრუნოთ სია სადაც მოთავსებული იქნება თითოეული სიტყვა ამ სტრინგიდან.
def gamotvla_winadadebidan(winadadeba):
    return winadadeba.split("$")

print(gamotvla_winadadebidan("this$is$one$big$winadadeba"))
