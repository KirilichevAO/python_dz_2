# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

def posl(a):
    return (1+1/a)**a


try:
    sp = []
    for i in range(n := (int(input('Введите число: ')))):
        sp.append(posl(i+1))
    summ = sum(sp)
    print(round(summ, 2))
except:
    print('Введено некорректное значение!')
