

list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти суммуб количество и среднее уникальных чисел

unique = set(list_)
total = sum(unique)
count = len(unique)

print(total)
print(count)
print(total / count)
