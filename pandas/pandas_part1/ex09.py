#!/usr/bin/env python3

import pandas as pd 

l = {'A': [1, 2, 3], 'B': [4, 5, 6]}

df = pd.DataFrame(l)

print(df.shape, df.columns, sep='\n')