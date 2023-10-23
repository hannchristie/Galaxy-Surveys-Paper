#import packages
import math as m
import statistics as stat
import numpy as np
import csv
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
# %%
# 11HUGS
df = pd.read_csv('dates.txt',  delimiter='\t', header=0, nrows=28)

surveys = df.iloc[:, 0]

year = df.iloc[:, 1]

num_G = df.iloc[:, 2]

max_D = df.iloc[:, -2]
print(max_D)

#%%


x_dat = np.linspace(0, len(num_G), len(num_G))
plt.scatter(surveys,num_G)
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.yscale('log')
sns.regplot(x = x_dat, y = num_G, scatter= False, fit_reg = True)

plt.ylabel('log(# galaxies)')
plt.xlabel('Surveys')

#%%

x_dat = np.linspace(0, len(max_D), len(max_D))
plt.scatter(surveys,max_D)
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
sns.regplot(x = x_dat, y = max_D, scatter= False, fit_reg = True)
plt.ylabel('Maximum Distance (Mpc)')
plt.xlabel('Surveys')
#plt.yscale('log')


