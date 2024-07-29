result = []
n = int(input('Введите число от 3 до 20 '))

for a in range(1, n):
    for b in range(a + 1, n):
        if n % (a + b) == 0:
            result.append(a)
            result.append(b)

print('Ваш пароль для числа ', n, ' - ', *result)
