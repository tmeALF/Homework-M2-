first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
a = [first, second, third]
b = (len(set(a))) == 1
c = (len(set(a))) == 2
if b:
    print('3')
elif c:
    print('2')
else:
    print('0')