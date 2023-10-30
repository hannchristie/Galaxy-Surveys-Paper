#import packages
import math as m
import statistics as stat
import numpy as np
import csv
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from astropy.coordinates import SkyCoord
import astropy.units as u

#%%
df = pd.read_csv('AllSkyLoc.csv')

def convert_to_skycoord(row):
    if row['Type'] == 'hms':
        coord_str = f"{row['RA']} {row['Dec']}"
        coord = SkyCoord(coord_str, unit=(u.hourangle, u.deg))
    else:
        coord = SkyCoord(row['RA'], row['Dec'], unit=(u.deg, u.deg))
    return coord

df['SkyCoord'] = df.apply(convert_to_skycoord, axis=1)


#%%
# Create a projection plot
fig, ax = plt.subplots(subplot_kw={'projection': 'mollweide'})

# Plot points
ax.scatter(df['SkyCoord'].ra.wrap_at(180 * u.deg), df['SkyCoord'].dec, s=10, label='Astronomical Coordinates')

# Customize the plot as needed
ax.set_title('Projection of Astronomical Coordinates (Equatorial ICRS)')
ax.grid()

plt.legend()
plt.show()