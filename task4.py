# 4-Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).
# Пример:
# - quarter = 1 => x∈(0, ∞) u y∈(0,∞)

num_quarter = int(input('Введите номер четверти: '))
if num_quarter == 1:
    print('quarter 1 => x from 0 to + ∞, y from 0 to + ∞')
elif num_quarter == 2:
    print('quarter 2 => x from 0 to - ∞, y from 0  to + ∞')
elif num_quarter == 3:
    print('quarter 3 => x from 0 to - ∞, y from 0  to - ∞')
elif num_quarter == 4:
    print('quarter 4 => x from 0 to + ∞, y from 0  to - ∞')
else:
    print('Введите правильный номер четверти ')