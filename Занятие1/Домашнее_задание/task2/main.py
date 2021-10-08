

MINUTES = 60

task = 10
time = int(input("Время выполнения одной задачи (минут): "))

print("~ ", round((task * time) / MINUTES, 1), " часов уходит на выполнение ", task, " задач")
