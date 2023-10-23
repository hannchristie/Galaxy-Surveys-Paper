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
c = 3*10**5 #[m/c]
Om = 0.3
Oa = 0.7

#%%

# calculate distance

def distance(z):
    D = (c/hubble)*z*(1+z)
    return D

#%%
# read csv file and create df with redshifts

df = pd.read_csv('califa_data.txt',  delimiter = '\s+', header = 0, nrows = 600)

z = df.iloc[:,3]

#%%
print(z[0])
print(z)
print(max(z))

#%%
dist = []

for i in range(0, len(z)):
    d = distance(z[i])
    dist.append(d)
  
#%%
with open('komp_results.csv', 'a') as f:
    writer = csv.writer(f)
#%%


    