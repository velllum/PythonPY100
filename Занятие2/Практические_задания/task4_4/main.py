list_numbers = list(range(5, 17))

# TODO заменить значение 5-го элемента средним арифметическим

for e, num in enumerate(list_numbers):
    if e == 5:
        list_numbers[e] = sum(list_numbers) / len(list_numbers)

print(list_numbers)
