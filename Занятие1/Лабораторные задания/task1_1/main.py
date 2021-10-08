

DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input("Укажите год своего рождения: "))  # TODO запросить у пользователя год рождения
current_year = int(input("Какой сейчас год? "))  # TODO запросить у пользователя текущий год

# TODO посчитать и распечатать количество прожитых дней

days_lived = (current_year - start_year) * DAYS_OF_YEAR  # прожитые дни
years_lived = days_lived // DAYS_OF_YEAR  # года

print(days_lived, years_lived)
