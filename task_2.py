# Задача 2: Найдите сумму цифр трехзначного числа.

i = int (input("Введите 3-х значное число: ", ))
first = i % 10
second = int (i/10)%10
three = int (i/100)%10
print (first + second + three)