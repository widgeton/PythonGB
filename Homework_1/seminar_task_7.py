"""Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print"""

num = int(input('Введите число от 1 до 999: '))

digit_amount = 0
i = num
while i > 0:
    if i % 10 >= 0:
        digit_amount += 1
    i //= 10

match digit_amount:
    case 1:
        form = 'цифра'
        result = num ** 2
    case 2:
        form = 'двузначное число'
        result = (num // 10) * (num % 10)
    case 3:
        form = 'трехзначное число'
        result = (num % 10 * 100) + (num % 100 // 10 * 10) + (num // 100)

print(num, '-', form)
print(num, '-', result)
