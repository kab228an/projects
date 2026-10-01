#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('lottery.csv')

winner = df.sample(random_state=1)