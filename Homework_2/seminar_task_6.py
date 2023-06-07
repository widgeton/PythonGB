"""Напишите программу банкомат.
Начальная сумма равна нулю. Допустимые действия: 'пополнить', 'снять', 'выйти'.
Сумма пополнения и снятия кратны 50 у.е. Процент за снятие — 1.5% от суммы снятия,
но не менее 30 и не более 600 у.е. После каждой третей операции пополнения или снятия
начисляются проценты - 3%. Нельзя снять больше, чем на счёте. При превышении суммы в 5 млн,
вычитать налог на богатство 10% перед каждой операцией, даже ошибочной. Любое действие
выводит сумму денег"""

DIVIDER = 50
WITHDRAW_RATE = 0.015
OPERATION_RATE = 0.03
RICH_RATE = 0.1
MIN_LIMIT = 30
MAX_LIMIT = 600
RICH_LIMIT = 5_000_000
REPLENISH = 'пополнить'
WITHDRAW = 'снять'
ESCAPE = 'выйти'
OPERATIONS = REPLENISH, WITHDRAW, ESCAPE

storage = 0
number_of_operations = 0

while True:
    print(f'Сумма на счету: {storage:_.2f}')

    if storage > RICH_LIMIT:
        storage -= round(storage * RICH_RATE, 2)

    operation = input(f'Введите слово действия: "{REPLENISH}", "{WITHDRAW}" или "{ESCAPE}": ').strip().lower()
    if operation not in OPERATIONS:
        print('Неверный ввод действия!')
        continue

    if operation == ESCAPE:
        print(f'До свидания!')
        break

    money = input(f'Сумма чтобы {operation} должна быть кратна {DIVIDER}.\nВведите сумму: ').strip()
    if not money.isdigit():
        print('Неверный ввод числа суммы!')
        continue

    money = int(money)
    if money % DIVIDER != 0:
        print(f'Сумма не кратна {DIVIDER}!')
        continue

    if operation == REPLENISH:
        storage += money
    else:
        levy = round(money * WITHDRAW_RATE, 2)
        if MIN_LIMIT <= levy <= MAX_LIMIT and money + levy <= storage:
            storage -= money + levy
        elif levy < MIN_LIMIT and money + MIN_LIMIT <= storage:
            storage -= money + MIN_LIMIT
        elif levy > MAX_LIMIT and money + MAX_LIMIT <= storage:
            storage -= money + MAX_LIMIT
        else:
            print(f'Недостаточно средств для снятия!')
            continue

    number_of_operations += 1
    if number_of_operations == 3:
        storage += round(storage * OPERATION_RATE, 2)
        number_of_operations = 0
