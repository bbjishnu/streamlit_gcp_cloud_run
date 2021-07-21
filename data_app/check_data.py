import os   
import sys
import numpy as np
import pandas as pd 

data_1 = pd.DataFrame(
    
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

data_2 = pd.DataFrame(
    
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

data_3 = pd.DataFrame(
    
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)

data_1.to_csv('data_one.csv',index=False)
data_2.to_csv('data_two.csv',index=False)
data_3.to_csv('data_two.csv',index=False)