s = 0
n = int(input("Введите количество билетов " ))
for i in range(n):
    age = int(input("Введите возраст "))
    if age < 18:
        p = 0
    elif 18 <= age < 25:
        p = 990
    else:
        p = 1390
    s += p
if n > 3:
    s *= 0.9
print("Сумма к оплате", s)