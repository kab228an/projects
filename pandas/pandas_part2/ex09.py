#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('salaries.csv')

stats = df.describe()

print(stats)