

GB = 1000000
SECONDS = 60
FREE_GB = 1

speed = int(input("Введите скорость (байт/сек): "))  # 1000 байт/сек.
time = int(input("Время (минут) на загрузку: "))  # 60 минут
coast = int(input("Стоимость 1 Гбайт (руб): "))  # 100 руб.

file_size = (time * SECONDS) * speed / GB
pay = (file_size - FREE_GB) * coast

print("Размер файла: ", file_size, " Гбайт")
print("Оплата за загрузку: ", pay, " руб")

