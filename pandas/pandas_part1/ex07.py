#!/usr/bin/env python3

import pandas as pd

l = [
    {'id': 1, 'login': 'user1', 'active': True},
    {'id': 2, 'login': 'user2'},
    {'id': 3, 'login': 'user3', 'active': False}
]

df = pd.DataFrame(l)

print(df)