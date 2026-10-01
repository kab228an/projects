#!/usr/bin/env python3 

import pandas as pd


df = pd.DataFrame({
    'total': [500, 1000, 1500, 2000, 2500, 1200, 800, 1800, 2100, 1000]
})

medium_checks = df[df['total'].between(1000, 2000, inclusive='both')]

print(list(medium_checks.total))