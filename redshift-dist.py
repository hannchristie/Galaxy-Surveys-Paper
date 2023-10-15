#packages

import math as m
import numpy as np
import csv
import pandas as pd

#%%

## redshift to distance computation

## constants
global hubble
global c

hubble = 70.0 # [km/s/Mpc]
c = 3e8 #[m/c]
Om = 0.3
Oa = 0.7

#%%

# calculate distance

def distance(z):
    D = (c/hubble)*m.log(1+z)
    return D

#%%
# read csv file and create df with redshifts

df = pd.read_csv(file_name, header = 0, nrows = 100)

z = df.loc[:,'redshift']

dist = []

for i in range(0, len(z)):
    d = distance(z[i])
    dist.append(d)
    
    
    