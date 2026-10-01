#!/usr/bin/env python3

import pandas as pd 

l = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Salary' : [50000, 60000, 55000],
    'Job' : ['Junior', 'Senior', 'Middle']
}

df = pd.DataFrame(l)

print(df)