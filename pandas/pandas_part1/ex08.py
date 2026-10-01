#!/usr/bin/env python3 

import pandas as pd

scores = [
    [4, 5],
    [3, 4],
    [5, 5]
]

df = pd.DataFrame(scores, columns=['Math', 'Physics'], index=['Ivan', 'Maria', 'Oleg'])

print(df)