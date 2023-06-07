"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте
модуль fractions."""
import fractions as frct
import math

num1, denom1 = map(int, input('Введите первую дробь в формате "a/b": ').split('/'))
num2, denom2 = map(int, input('Введите вторую дробь в формате "a/b": ').split('/'))

num_s, denom_s = num1 * denom2 + num2 * denom1, denom1 * denom2
gcd_s = math.gcd(num_s, denom_s)
s = f'{num_s // gcd_s}/{denom_s // gcd_s}' if num_s % denom_s else num_s // denom_s

num_m, denom_m = num1 * num2, denom1 * denom2
gcd_m = math.gcd(num_m, denom_m)
m = f'{num_m // gcd_m}/{denom_m // gcd_m}' if num_m % denom_m else num_m // denom_m

fr_num1 = frct.Fraction(num1, denom1)
fr_num2 = frct.Fraction(num2, denom2)
print(f'{num1}/{denom1} + {num2}/{denom2} = {s}\nПроверка: {fr_num1 + fr_num2}')
print(f'{num1}/{denom1} * {num2}/{denom2} = {m}\nПроверка: {fr_num1 * fr_num2}')
