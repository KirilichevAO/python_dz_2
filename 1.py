# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

summ = 0
if float(num := input('Введите вещественное число: ')) < 0:
    num = float(num) * (-1)
for i in str(num):
    if i != '.':
        summ += int(i)
print(f'{num} -> {summ}')
