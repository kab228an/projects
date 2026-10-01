#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('orders.csv')

first_10 = df.head(10)