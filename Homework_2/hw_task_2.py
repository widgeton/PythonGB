"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте
модуль fractions."""
import fractions as frct
import math

n1 = input('Введите первую дробь в формате "a/b": ')
num1 = [int(i.strip()) for i in n1.split('/')]
n2 = input('Введите вторую дробь в формате "a/b": ')
num2 = [int(i.strip()) for i in n2.split('/')]

s = [num1[0] * num2[1] + num2[0] * num1[1], num1[1] * num2[1]]
s = [str(i // math.gcd(*s)) for i in s]
m = [num1[0] * num2[0], num1[1] * num2[1]]
m = [str(i // math.gcd(*m)) for i in m]

fr_num1 = frct.Fraction(num1[0], num1[1])
fr_num2 = frct.Fraction(num2[0], num2[1])
print(f'{n1} + {n2} = {"/".join(s)}\nПроверка: {fr_num1 + fr_num2}')
print(f'{n1} * {n2} = {"/".join(m)}\nПроверка: {fr_num1 * fr_num2}')
