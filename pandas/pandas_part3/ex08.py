#!/usr/bin/env python3

import pandas as pd

data = {'user': ['user1', 'user2', 'user3', 'user4', 'user5'],
        'city': ['Moscow', 'Kazan', 'Sochi', 'Omsk', 'Ufa']}
df = pd.DataFrame(data)

target_users = df[df['city'].isin(['Kazan', 'Sochi', 'Ufa'])]

print(list(target_users.user))