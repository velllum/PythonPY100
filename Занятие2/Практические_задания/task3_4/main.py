mount = int(input("Ведите номер месяца: "))  # TODO запросить месяц у пользователя. Номер месяца - целочисленное значение!

if mount in [3, 4, 5]:
    print("Весна")
elif mount in [6, 7, 8]:
    print("Лето")
elif mount in [9, 10, 11]:
    print("Осень")
elif mount in [12, 1, 2]:
    print("Зима")
