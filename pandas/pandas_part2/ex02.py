#!/usr/bin/env  python3

import pandas as pd

df = pd.read_csv('log.csv', header=None, names=['User', 'Action'])