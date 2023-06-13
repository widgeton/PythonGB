"""Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.
"""
import datetime as dt

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


def logger(act: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            with open('log.txt', 'a') as log:
                if 'storage' in kwargs:
                    log.write(f'[{dt.datetime.now()}] {act}. Состояние счета: {kwargs["storage"]}\n')
                else:
                    log.write(f'[{dt.datetime.now()}] {act}.\n')
            return res

        return wrapper

    return decorator


@logger('Вывод суммы счета на экран')
def show_storage(*, storage: list):
    print(f'Сумма на счету: {storage[1]:_.2f}')


@logger('Снятие налога на богатство')
def withdraw_rich_tax(*, storage: list):
    if storage[1] > RICH_LIMIT:
        tax = round(storage[1] * RICH_RATE, 2)
        storage[1] = storage[1] - tax
        print(f'Снят налог на богатство: {tax}')


@logger('Запрос на ввод операции')
def get_operation() -> str | None:
    operation = input(f'Введите слово действия: "{REPLENISH}", "{WITHDRAW}" или "{ESCAPE}": ').strip().lower()
    if operation in OPERATIONS:
        return operation
    print('Неверный ввод действия!')


@logger('Запрос на ввод денежной суммы')
def get_money() -> int | None:
    money = input(f'Сумма должна быть кратна {DIVIDER}.\nВведите сумму: ').strip()
    if not money.isdigit():
        print('Неверный ввод числа суммы!')
    elif int(money) % DIVIDER != 0:
        print(f'Сумма не кратна {DIVIDER}!')
    else:
        return int(money)


@logger('Пополнение счета')
def add_money(money: int, *, storage: list,):
    storage[1] = storage[1] + money


@logger('Снятие средств')
def withdraw_money(money: int, *, storage: list):
    levy = round(money * WITHDRAW_RATE, 2)
    if MIN_LIMIT <= levy <= MAX_LIMIT and money + levy <= storage[1]:
        storage[1] -= money + levy
    elif levy < MIN_LIMIT and money + MIN_LIMIT <= storage[1]:
        storage[1] -= money + MIN_LIMIT
    elif levy > MAX_LIMIT and money + MAX_LIMIT <= storage[1]:
        storage[1] -= money + MAX_LIMIT
    else:
        print(f'Недостаточно средств для снятия!')


@logger('Проведение капитализации счета')
def accrue_interest(*, storage: list):
    storage[0] += 1
    if storage[0] == 3:
        capital = round(storage[1] * OPERATION_RATE, 2)
        storage[1] += capital
        storage[0] = 0
        print(f'Капитализация счета: {capital}')


def make_transaction(operation: str, storage: list):
    money = get_money()
    if money is None:
        return

    store_before = storage[1]
    if operation == REPLENISH:
        add_money(money, storage=storage)
    elif operation == WITHDRAW:
        withdraw_money(money, storage=storage)

    if store_before != storage[1]:
        accrue_interest(storage=storage)


def main(storage: list[int, float]):
    while True:
        show_storage(storage=storage)
        withdraw_rich_tax(storage=storage)
        operation = get_operation()
        if operation is None:
            continue
        if operation == ESCAPE:
            return
        make_transaction(operation, storage)


if __name__ == '__main__':
    store = 0.0
    number_of_operations = 0

    # Это подобие объекта "счет", который хранит в себе количество операций и сумму,
    # чтобы алгоритм при желании мог работать с разными счетами и сохранять результат.
    storage = [number_of_operations, store]

    main(storage)

    # Вывод счета для проверки сохранения результата.
    print(storage)
