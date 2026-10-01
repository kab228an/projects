#!/usr/bin/env python3

import pandas as pd

data = {'item' : ['A','B','C','D'],
        'category': ['Normal', 'Sale', 'Normal', 'Sale'],
        'discount': [10, 20, 60, 80]}
df = pd.DataFrame(data)

promo_items = df[(df.category == 'Sale') | (df.discount > 50)]

print(promo_items.shape)