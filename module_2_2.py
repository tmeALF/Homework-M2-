# first = int(input('Введите первое целое число: '))
# second = int(input('Введите второе целое число: '))
# third = int(input('Введите третье целое число: '))
# a = [first, second, third]
# b = (len(set(a))) == 1
# c = (len(set(a))) == 2
# if b:
#     print('3')
# elif c:
#     print('2')
# else:
#     print('0')
first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
numbers = [first, second, third]
unique_numbers = set(numbers)
unique_count = len(unique_numbers)
if unique_count == 1:
    print('3')
elif unique_count == 2:
    print('2')
else:
    print('0')
