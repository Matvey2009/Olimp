from random import randint
x = randint(1, 999)
s = 1
p = 0
for i in str(x):
	p += int(i)
	s *= int(i)
print("Случайное число: ", x)
print("Сумма цифр числа: ", p)
print("Произведение цифр числа: ", s)
