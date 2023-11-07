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
d_legus = df.iloc[:, -1]

# GHOSTS
df = pd.read_csv('GHOSTS_data.txt',  delimiter='\t', header=0, nrows=1000)
d_ghosts = df.iloc[:, 5]

#HALOGAS
df = pd.read_csv('halogas_data.txt',  delimiter='\t', header=0, nrows=1000)
d_ghosts = df.iloc[:, 3]

# CALIFA
df = pd.read_csv('CALIFA_dist.csv',  delimiter='\t', header=0, nrows=1000)
d_califa = df.iloc[:, -1]
# %%
# create dataframe

headers = ['THINGS', '11HUGS', 'HERACLES', 'ANGST', 'S4G', 'PINGS', 'MHONGOOSE', 'GHOSTS', 'GALEX UV Survey',
           'CALIFA', 'Chandra Survey of Nearby Galaxies', 'LVHIS', 'JINGLE', 'COMING', 'PHANGS', 'KNGS']

data = [d_things, d_11h, d_her, d_angst, d_s4g, d_pings, d_mhon, d_ghosts,
        d_galex, d_califa, d_chan, d_lvhis, d_jingle, d_com, d_phangs, d_kngs]

df_p = pd.DataFrame(np.transpose(data), columns=headers)

print(df_p)
# %%
# Create a dictionary with your data
data_dict = {
    'THINGS': d_things,
    '11HUGS': d_11h,
    'HERACLES': d_her,
    'ANGST': d_angst,
    'S4G': d_s4g,
    'PINGS': d_pings,
    'MHONGOOSE': d_mhon,
    'GHOSTS': d_ghosts,
    'GALEX UV Survey': d_galex,
    'CALIFA': d_califa,
    'Chandra Survey of Nearby Galaxies': d_chan,
    'LVHIS': d_lvhis,
    'JINGLE': d_jingle,
    'COMING': d_com,
    'PHANGS': d_phangs,
    'KNGS': d_kngs
}

df_p = pd.DataFrame(data_dict)
# %%
# make violing plot
# Create a violin plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_p, orient="v", palette='pastel',
               saturation=1, fill=True, linewidth=0.05, scale='width')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.show()

# %%
# Compute the minimum value for each column
min_dist = df_p.min(numeric_only=True)

# Compute the maximum value for each column
max_dist = df_p.max(numeric_only=True)

# Compute the median value for each column
median_dist = df_p.median(numeric_only=True)

# Combine the results into a summary DataFrame
summary_df = pd.DataFrame({
    'Minimum': min_dist,
    'Maximum': max_dist,
    'Median': median_dist
})

# Display the summary DataFrame
print(summary_df)
print()
#%%
x = np.linspace (0,1)
plt.figure(figsize=(12, 6))
sns.set_theme(style="darkgrid")
plt.plot(summary_df.index, df_p.median())

# Fill the area between the minimum and maximum lines with a transparent color
plt.fill_between(summary_df.index, df_p.min(), df_p.max(), alpha=0.3)

# Set labels and titles
plt.xlabel("Galaxy Surveys")
plt.ylabel("Distance (Mpc)")
plt.title("Distance Distribution for Galaxy Surveys")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()
# Show the plot
plt.show()