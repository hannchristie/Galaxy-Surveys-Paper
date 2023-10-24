#import packages
import math as m
import statistics as stat
import numpy as np
import csv
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from astropy.io import ascii
# %%
# 11HUGS
df = pd.read_csv('11HUGS_data.txt',  delimiter='\t', header=4, nrows=1000)
d_11h = df.iloc[:, -1]

# ANGST
df = pd.read_csv('ANGST_data.txt',  delimiter='\t', header=2, nrows=1000)
d_angst = df.iloc[:, 2]

# COMING
df = pd.read_csv('COMING_data.txt',  delimiter='\t', header=2, nrows=1000)
d_com = df.iloc[:, -1]

# Chandra
df = pd.read_csv('Chandra_data.txt', delimiter='\t', header=3 , nrows=1000)
d_chan = df.iloc[:, 2]

# GALEX UV
df = pd.read_csv('GALEX_data.txt',  delimiter='\t', header=0, nrows=1000)
d_galex = df.iloc[:, 2]

# JINGLE
df = pd.read_csv('JINGLE_data.txt',  delimiter='\t', header=0, nrows=1000)
d_jingle = df.iloc[:, -1]

#LEGUS
df = pd.read_csv('LEGUS_data.txt',  delimiter='\t', header=1, nrows=1000)
d_lvhis = df.iloc[:, -1]

# LVHIS
df = pd.read_csv('LVHIS_data.txt',  delimiter='\t', header=1, nrows=1000)
d_lvhis = df.iloc[:, 2]

# LVL
df = pd.read_csv('LVL_data.txt',  delimiter='\t', header=0, nrows=1000)
d_lvl = df.iloc[:, 4]


# PHANGS
df = pd.read_csv('PHANGS_data.txt',  delimiter='\t', header=1, nrows=1000)
d_phangs = df.iloc[:,]

# PINGS
df = pd.read_csv('PINGS_data.txt',  delimiter='\t', header=1, nrows=1000)
d_pings = df.iloc[:, 2]

# S4G
df = pd.read_csv('S4G_data.txt',  delimiter='\t', header=2, nrows=1000)
d_s4g = df.iloc[:, -1]

# THINGS
df = pd.read_csv('THINGS_data.txt',  delimiter='\t', header=0, nrows=1000)
d_things = df.iloc[:, 4]

# HERACLES
df = pd.read_csv('heracles_data.txt',  delimiter='\t', header=0, nrows=1000)
d_her = df.iloc[:, -1]

# MHONGOOSE
df = pd.read_csv('mhongoose_data.txt',  delimiter='\t', header=0, nrows=1000)
d_mhon = df.iloc[:, -2]

# KNGS
df = pd.read_csv('KNGS_data.txt',  delimiter='\t', header=0, nrows=1000)
d_kngs = df.iloc[:, 3]

# CGS
df = pd.read_csv('CGS_data.txt',  delimiter = '\t', header = 0, nrows = 1000)
d_cgs = df.iloc[:,-1]

# LEGUS
df = pd.read_csv('LEGUS_data.txt',  delimiter='\t', header=0, nrows=1000)
d_legus = df.iloc[:, 5]

# GHOSTS
df = pd.read_csv('GHOSTS_data.txt',  delimiter='\t', header=0, nrows=1000)
d_ghosts = df.iloc[:, 5]

#HALOGAS
df = pd.read_csv('halogas_data.txt',  delimiter='\t', header=0, nrows=1000)
d_ghosts = df.iloc[:, 3]

# CALIFA
df = pd.read_csv('CALIFA_dist.csv',  delimiter='\t', header=0, nrows=1000)
d_califa = df.iloc[:, -1]