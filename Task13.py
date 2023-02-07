tickets = int(input("Введите количество билетов: "))
total = 0
for i in range (tickets):    
    age = int(input("Введите свой возраст: "))
    if  18 <= age <=25:
        total = total + 990
    elif age > 25:
        total = total + 1390
if tickets > 3:
    total = total * 0.9
print(total)



