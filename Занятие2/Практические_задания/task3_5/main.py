

wind = int(input("Введите скорость ветра: "))

# TODO напишите с помощью if-elif-else условие проверки скорости ветра

if 1 <= wind <= 4:
    print("Слабый")

elif 5 <= wind <= 10:
    print("Умеренный")

elif 11 <= wind <= 18:
    print("Сильный")

elif 19 <= wind:
    print("Ураганный")
