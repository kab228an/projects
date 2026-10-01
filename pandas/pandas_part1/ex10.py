#!/usr/bin/env python3 

import pandas as pd

l =  {'ID' : [100, 101],
      'Paid' : [True, False],
      'Name' : ['X', 'Y']    
    }

df = pd.DataFrame(l)

print(df.dtypes)