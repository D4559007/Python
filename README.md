# Python

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("введите сумму вклада"))
p = (list(per_cent.values()))
import numpy as np
a = np.array(p)
b = np.array([money])
d = ((a * b / 100) + money)
print("deposit = ", d)
print("Максимальная сумма, которую вы можете заработать —", max(d))
