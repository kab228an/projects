#!/usr/bin/env python3

import pandas as pd

df = pd.DataFrame({
    'rooms': [1, 2, 3, 3, 4, 3, 2, 3, 1, 3],
    'price': [2500000, 3500000, 4800000, 5200000, 8000000, 4900000, 3000000, 5100000, 2000000, 4700000],
    'area': [30, 45, 65, 70, 90, 68, 42, 72, 28, 66],
    'address': ['Street A', 'Street B', 'Street C', 'Street D', 'Street E', 'Street F', 'Street G', 'Street H', 'Street I', 'Street J']
})

max_price = 5000000

# Используйте метод .query()
# Условие: rooms равно 3 И price меньше max_price
# Результат в good_flats

# Ваш код:

good_flats = df.query("rooms == 3 and price < @max_price")

print(list(good_flats.address))