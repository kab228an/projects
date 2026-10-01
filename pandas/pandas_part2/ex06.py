#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('logs.csv')

print(df.tail(3))